from concurrent.futures import Executor, Future


class SequentialExecutor(Executor):
    """This implements the concurrent.futures.Executor interface and forces sequential execution."""

    def submit(self, fn, /, *args, **kwargs):
        future = Future()
        future.set_running_or_notify_cancel()
        try:
            future.set_result(fn(*args, **kwargs))
        except BaseException as exc:
            future.set_exception(exc)
        return future

    submit.__doc__ = Executor.submit.__doc__
