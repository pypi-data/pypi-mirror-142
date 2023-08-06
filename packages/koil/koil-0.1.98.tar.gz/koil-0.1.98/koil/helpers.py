import asyncio
from asyncio.log import logger
from koil.utils import run_threaded_with_context
from koil.vars import *
from koil.task import KoilTask
import time


def unkoil_gen(iterator, *args, as_task=False, timeout=None, **kwargs):
    loop = current_loop.get()

    if as_task:
        genclass = current_genclass.get()
        assert genclass is not None, "No gen class set"
        return genclass(iterator, args, kwargs, loop=loop)

    return unkoil_gen_no_task(iterator, *args, timeout=timeout, **kwargs)


def unkoil_gen_no_task(iterator, *args, timeout=None, **kwargs):
    loop = current_loop.get()
    cancel_event = current_cancel_event.get()

    if loop.is_closed():
        raise RuntimeError("Loop is not running")
    try:
        loop0 = asyncio.events.get_running_loop()
        if loop0 is loop:
            raise NotImplementedError("Calling sync() from within a running loop")
    except RuntimeError:
        pass

    ait = iterator(*args, **kwargs).__aiter__()
    res = [False, False]

    async def next_on_ait():
        try:
            try:
                obj = await ait.__anext__()
                return [False, obj]
            except StopAsyncIteration:
                return [True, None]
        except asyncio.CancelledError as e:
            return [False, e]

    while True:
        res = run_threaded_with_context(next_on_ait(), loop=loop)
        while not res.done():
            if cancel_event and cancel_event.is_set():
                raise Exception("Task was cancelled")

            time.sleep(0.01)
        x, context = res.result()
        done, obj = x
        if done:
            if obj:
                raise obj
            break

        for ctx, value in context.items():
            ctx.set(value)

        yield obj


def unkoil(coro, *args, timeout=None, as_task=False, ensure_koiled=False, **kwargs):
    try:
        asyncio.events.get_running_loop()
        if ensure_koiled:
            raise NotImplementedError(
                "Calling sync() from within a running loop, you need to await the coroutine"
            )

        return coro(*args, **kwargs)
    except RuntimeError:
        pass

    loop = current_loop.get()
    cancel_event = current_cancel_event.get()

    if loop:
        try:
            if loop.is_closed():
                raise RuntimeError("Loop is not running")

            ctxs = contextvars.copy_context()

            async def passed_with_context():
                for ctx, value in ctxs.items():
                    ctx.set(value)

                x = await coro(*args, **kwargs)
                newcontext = contextvars.copy_context()
                return x, newcontext

            if as_task:
                taskclass = current_taskclass.get()
                assert taskclass is not None, "No task class set"
                return taskclass(
                    coro, preset_args=args, preset_kwargs=kwargs, loop=loop
                )

            co_future = asyncio.run_coroutine_threadsafe(passed_with_context(), loop)
            while not co_future.done():
                time.sleep(0.01)
                if cancel_event and cancel_event.is_set():
                    raise Exception("Task was cancelled")

            x, newcontext = co_future.result()

            for ctx, value in newcontext.items():
                ctx.set(value)

            return x

        except KeyboardInterrupt:
            print("Grace period triggered?")
            raise
    else:
        if ensure_koiled:
            raise RuntimeError("No loop set and ensure_koiled was set to True")

        if as_task:
            raise RuntimeError(
                """No loop is running. That means you cannot have this run as a task. Try providing a loop by entering a Koil() context.
                """
            )

        logger.warn(
            "You used unkoil without a governing Koil in the context, this is not recommended. We will now resort to run asyncio.run()"
        )

        future = coro(*args, **kwargs)
        asyncio.run(future)


def run_spawned(
    sync_func, *sync_args, executor=None, pass_context=False, **sync_kwargs
):
    """
    Spawn a thread with a given sync function and arguments
    """

    loop = current_loop.get()
    try:
        loop0 = asyncio.get_event_loop()
        if loop:
            assert loop0 is loop, "Loop is not the same"
        else:
            loop = loop0
            current_taskclass.set(KoilTask)
    except RuntimeError:
        loop = current_loop.get()

    assert loop, "No koiled loop found"
    assert loop.is_running(), "Loop is not running"

    def wrapper(sync_args, sync_kwargs, loop, context):
        current_loop.set(loop)
        current_taskclass.set(KoilTask)

        if context:
            for ctx, value in context.items():
                ctx.set(value)

        return sync_func(*sync_args, **sync_kwargs)

    context = contextvars.copy_context() if pass_context else None

    return loop.run_in_executor(None, wrapper, sync_args, sync_kwargs, loop, context)
