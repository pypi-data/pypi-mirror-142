import asyncio

from . import decorators, functional


__all__ = ["maybe_list", "method_decorator"]


maybe_list = functional.maybe_list

method_decorator = decorators.method_decorator


def get_running_loop() -> asyncio.AbstractEventLoop:  # pragma: no cover
    if hasattr(asyncio, "get_running_loop"):
        return asyncio.get_running_loop()  # type: ignore[attr-defined]
    else:  # Python 3.6
        return asyncio.get_event_loop()
