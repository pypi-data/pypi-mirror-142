# Copyright 2022 Katteli Inc.
# TestFlows.com Open-Source Software Testing Framework (http://testflows.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# to the end flag
import os
import sys
import codecs
import atexit
import weakref
import queue
import threading
import traceback
import itertools
import textwrap
import subprocess
import contextlib
import concurrent.futures._base as _base

import testflows.settings as settings

from .future import Future

from .thread import GlobalThreadPoolExecutor
from .asyncio import asyncio
from .asyncio import GlobalAsyncPoolExecutor
from ..asyncio import is_running_in_event_loop, wrap_future
from ..service import BaseServiceObject, ServiceObjectType, process_service, auto_expose
from .. import current, top, previous, _get_parallel_context
from ...objects import Result

_process_queues = weakref.WeakKeyDictionary()
_shutdown = False

WORKER_READY = "_tfs_worker__ready__\n"

class Process:
    """Process for asyncio.subprocess_exec.
    """
    def __init__(self, transport, protocol):
        self.transport = transport
        self.protocol = protocol

ProcessError = subprocess.SubprocessError


def async_wait_for(aw, loop):
    return asyncio.run_coroutine_threadsafe(asyncio.wait_for(aw, None), loop=loop).result()


def _python_exit():
    global _shutdown
    _shutdown = True

    items = list(_process_queues.items())
    for proc, _ in items:
        try:
            proc.transport.terminate()
        except ProcessLookupError:
            pass

    loop = process_service().loop
    for proc, _ in items:
        async_wait_for(proc.protocol.exit_future, loop=loop)

atexit.register(_python_exit)


WorkQueueType = ServiceObjectType("WorkQueue", auto_expose(queue.Queue()))

class WorkerSettings:
    """Remote service object that is used to pass settings
    to the worker process.
    """
    def __init__(self):
        self.debug = settings.debug
        self.time_resolution = settings.debug
        self.hash_length = settings.hash_length
        self.hash_func = settings.hash_func
        self.no_colors = settings.no_colors
        self.test_id = settings.test_id
        self.output_format = settings.output_format
        self.write_logfile = self._set_service_object(current().io.io.io.writer.fd)
        self.read_logfile = self._set_service_object(current().io.io.io.reader.fd)
        self.database = settings.database
        self.show_skipped = settings.show_skipped
        self.show_retries = settings.show_retries
        self.trim = settings.trim
        self.random_order = settings.random_order
        self.service_timeout = settings.service_timeout
        self.global_thread_pool = (
                settings.global_thread_pool.__class__,
                settings.global_thread_pool.initargs
            ) if settings.global_thread_pool is not None else None
        self.global_async_pool = (
                settings.global_async_pool.__class__,
                settings.global_async_pool.initargs
            ) if settings.global_async_pool is not None else None
        self.global_process_pool = self._set_service_object(settings.global_process_pool)
        self.secrets_registry = settings.secrets_registry

    def _set_service_object(self, obj):
        if obj is None:
            return obj
        if not isinstance(obj, BaseServiceObject):
            obj = process_service().register(obj, sync=True, awaited=False)
        return obj


class _WorkItem(object):
    """Work item for the remote worker.
    """
    def __init__(self, settings, current_test, previous_test, top_test, future, fn, args, kwargs):
        self.settings = settings
        self.current_test = current_test
        self.previous_test = previous_test
        self.top_test = top_test
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self, local=False):
        """This function will be run in worker process.
        """
        if not self.future.set_running_or_notify_cancel():
            return

        ctx = _get_parallel_context()

        def set_settings(work_settings):
            """Set global test settings for this work item.
            """
            settings.debug = work_settings.debug
            settings.time_resolution = work_settings.time_resolution
            settings.hash_length = work_settings.hash_length
            settings.hash_func = work_settings.hash_func
            settings.no_colors = work_settings.no_colors
            settings.test_id = work_settings.test_id
            settings.output_format = work_settings.output_format
            settings.write_logfile = work_settings.write_logfile
            settings.read_logfile = work_settings.read_logfile
            settings.database = work_settings.database
            settings.show_skipped = work_settings.show_skipped
            settings.show_retries = work_settings.show_retries
            settings.trim = work_settings.trim
            settings.random_order = work_settings.random_order
            settings.service_timeout = work_settings.service_timeout
            # set global thread pool
            settings.global_thread_pool = None
            if work_settings.global_thread_pool is not None:
                cls, initargs = work_settings.global_thread_pool
                settings.global_thread_pool = cls(*initargs)
            # set global async pool
            settings.global_async_pool = None
            if work_settings.global_async_pool is not None:
                cls, initargs = work_settings.global_async_pool
                settings.global_async_pool = cls(*initargs)
            # set shared global process pool
            settings.global_process_pool = work_settings.global_process_pool
            settings.secrets_registry = work_settings.secrets_registry

        def runner(self):
            try:
                if not local:
                    top(self.top_test)
                    previous(self.previous_test)
                    current(self.current_test)

                    set_settings(self.settings)

                    # global thread and async pool are local to each work item
                    with (settings.global_thread_pool or contextlib.nullcontext()), (
                            settings.global_async_pool or contextlib.nullcontext()):
                        result = self.fn(*self.args, **self.kwargs)
                else:
                    result = self.fn(*self.args, **self.kwargs)

            except BaseException as exc:
                if not isinstance(exc, Result):
                    exc_type, exc_value, exc_tb = sys.exc_info()
                    exc = exc_type(str(exc_value) + "\n\nWorker Traceback (most recent call last):\n" + "".join(traceback.format_tb(exc_tb)).rstrip())
                self.future.set_exception(exc)
                # Break a reference cycle with the exception 'exc'
                self = None

            else:
                try:
                    self.future.set_result(result)
                except TypeError:
                    self.future.set_result(process_service().register(result, sync=True, awaited=False))

        ctx.run(runner, self)


class WorkerProtocol(asyncio.SubprocessProtocol):
    """Worker process protocol that set exit_future
    on process exit and logs all output on stdout
    and stderr to message_io.
    """
    def __init__(self, test_io, io_prefix, loop, encoding="utf-8", errors=None):
        self.decoder = codecs.getincrementaldecoder(encoding)(errors=errors)
        self.test_io = test_io
        self.io_prefix = io_prefix
        self.exit_future = asyncio.Future(loop=loop)
        self.ready_future = asyncio.Future(loop=loop)
        self.buffer = ''
        self.transport = None
        self.stdout_io = None
        self.stderr_io = None

    def connection_made(self, transport):
        self.transport = transport
        worker_pid = self.transport.get_pid()
        self.stdout_io = self.test_io.message_io(f"{self.io_prefix}-worker-{worker_pid}:stdout")
        self.stderr_io = self.test_io.message_io(f"{self.io_prefix}-worker-{worker_pid}:stderr")

    def pipe_data_received(self, fd, data):
        if not self.ready_future.done() and data:
            self.buffer += self.decoder.decode(data)
            if WORKER_READY in self.buffer:
                data = self.buffer.split(WORKER_READY, 1)[-1]
                self.ready_future.set_result(True)

        elif data:
            data = self.decoder.decode(data)
        
        if data:
            if fd == 1:
                self.stdout_io.write(data)
            else:
                self.stderr_io.write(data)

    def process_exited(self):
        if not self.ready_future.done():
            self.ready_future.set_result(True)
        self.exit_future.set_result(True)


class ProcessPoolExecutor(_base.Executor):
    """Process pool executor.
    """
    _counter = itertools.count().__next__

    def __init__(self, max_workers=16, process_name_prefix="", _check_max_workers=True):
        if _check_max_workers and int(max_workers) <= 0:
            raise ValueError("max_workers must be greater than 0")
        self._open = False
        self._max_workers = max_workers
        self._raw_work_queue = queue.Queue()
        self._work_queue = process_service().register(self._raw_work_queue, sync=True, awaited=False)
        self._processes = set()
        self._broken = False
        self._shutdown = False
        self._shutdown_lock = threading.Lock()
        self._process_name_prefix = f"{process_name_prefix}ProcessPoolExecutor-{os.getpid()}-{self._counter()}"

    @property
    def open(self):
        """Return if pool is opened.
        """
        return bool(self._open)

    def __enter__(self):
        self._open = True
        return self

    def map(self, fn, *iterables, timeout=None, chunksize=1):
        raise NotImplementedError()

    def submit(self, fn, args=None, kwargs=None, block=True):
        if args is None:
            args = ()
        if kwargs is None:
            kwargs = {}

        with self._shutdown_lock:
            if not self._open:
                raise RuntimeError("cannot schedule new futures before pool is opened")
            if self._shutdown:
                raise RuntimeError("cannot schedule new futures after shutdown")
            if _shutdown:
                raise RuntimeError("cannot schedule new futures after "
                    "interpreter shutdown")

            service = process_service()

            _raw_future = Future()
            future = service.register(_raw_future, sync=True, awaited=False)

            current_test = service.register(current(), sync=True, awaited=False)
            previous_test = service.register(previous(), sync=True, awaited=False)
            top_test = service.register(top(), sync=True, awaited=False)

            work_item = _WorkItem(WorkerSettings(), current_test, previous_test, top_test, future, fn, args, kwargs)

            idle_workers = self._adjust_process_count()

            if (idle_workers or block) and self._max_workers > 0:
                self._raw_work_queue.put(work_item)

        if (not block and not idle_workers) or self._max_workers < 1:
            work_item.run(local=True)

        if is_running_in_event_loop():
            return wrap_future(_raw_future)

        return _raw_future

    def _adjust_process_count(self):
        """Increase worker count up to max_workers if needed.
        Return `True` if worker is immediately available to handle
        the work item or `False` otherwise.
        """
        if len(self._processes) - self._raw_work_queue.unfinished_tasks > 0:
            return True

        num_procs = len(self._processes)

        if num_procs < self._max_workers:
            command = ["tfs-worker",
                "--oid", str(self._work_queue.oid),
                "--hostname", str(self._work_queue.address.hostname),
                "--port", str(self._work_queue.address.port)
            ]

            if settings.debug:
                command.append("--debug")
            if settings.no_colors:
                command.append("--no-colors")

            loop = process_service().loop

            proc = Process(*asyncio.run_coroutine_threadsafe(
                loop.subprocess_exec(
                    lambda: WorkerProtocol(test_io=current(), io_prefix=self._process_name_prefix, loop=loop),
                    *command), loop=loop).result())

            async_wait_for(proc.protocol.ready_future, loop=loop)

            returncode = proc.transport.get_returncode()
            if returncode:
                output = textwrap.indent(proc.protocol.buffer, prefix='  ')
                raise ProcessError(f"failed to start worker process {proc.transport.get_pid()} return code {returncode}\n{output}")
            self._processes.add(proc)
            _process_queues[proc] = self._raw_work_queue
            return True

        return False

    def shutdown(self, wait=True):
        with self._shutdown_lock:
            if self._shutdown:
                return
            self._shutdown = True

            for _ in self._processes:
                self._raw_work_queue.put_nowait(None)

        if wait:
            loop = process_service().loop
            for proc in self._processes:
                async_wait_for(proc.protocol.exit_future, loop=loop)


class SharedProcessPoolExecutor(ProcessPoolExecutor):
    """Shared process pool executor.
    """
    def __init__(self, max_workers, process_name_prefix=""):
        if int(max_workers) < 0:
            raise ValueError("max_workers must be positive or 0")
        super(SharedProcessPoolExecutor, self).__init__(
            max_workers=max_workers-1, process_name_prefix=process_name_prefix, _check_max_workers=False)

    def submit(self, fn, args=None, kwargs=None, block=False):
        return super(SharedProcessPoolExecutor, self).submit(fn=fn, args=args, kwargs=kwargs, block=block)


GlobalProcessPoolExecutor = SharedProcessPoolExecutor
