import abc
import functools
import logging
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

from . import backends, messaging, utils


__all__ = ["EventHandler", "Handler", "handler", "event_hander"]


logger = logging.getLogger(__name__)


WrappedFunction = TypeVar("WrappedFunction", bound=Callable)


class Handler(metaclass=abc.ABCMeta):
    """Handler."""

    supports_dry_run: bool = False

    def __call__(self, function: Callable) -> WrappedFunction:
        @functools.wraps(function)
        def wrapper(body: Any, *, metadata: Optional[dict] = None) -> Any:
            parsed_body = self.parse_body(body, metadata=metadata)
            dry_run = self.is_dry_run(parsed_body, metadata=metadata)

            if dry_run and not self.supports_dry_run:
                logger.warning(
                    "Dry-run is not supported by this handler. Skipping.",
                    extra={"function": function, "handler": self},
                )
                return None

            return function(parsed_body, metadata=metadata, dry_run=dry_run)

        setattr(wrapper, "_handler", self)
        return wrapper  # type: ignore[return-value]

    def __init__(
        self,
        *,
        dispatcher: Optional["backends.base.Dispatcher"] = None,
        supports_dry_run: Optional[bool] = None,
    ) -> None:
        self.dispatcher = dispatcher or backends.Dispatcher()
        if supports_dry_run is not None:
            self.supports_dry_run = supports_dry_run

        setattr(self, "run", self(function=self.run))

    def is_dry_run(self, body: Any, **kwargs: Any) -> bool:
        raise NotImplementedError()

    def parse_body(self, body: Any, **kwargs: Any) -> Any:
        return body

    def run(
        self,
        body: Any,
        *,
        metadata: Optional[dict] = None,
        dry_run: bool = False,
    ) -> None:
        raise NotImplementedError()


class EventHandler(Handler, metaclass=abc.ABCMeta):
    """Event handler."""

    def is_dry_run(
        self, body: messaging.events.BaseEvent, **kwargs: Any
    ) -> bool:
        return body.dry_run

    def parse_body(
        self, body: Any, **kwargs: Any
    ) -> messaging.events.BaseEvent:
        metadata = kwargs.get("metadata", {})
        content_type = metadata.get("content_type")

        if not content_type == "application/cloudevents+json":
            raise ValueError(
                "Expected content type of "
                '"application/cloudevents+json", but received '
                f'"{content_type}".'
            )

        event = messaging.Event.from_json(body, metadata=metadata)
        logger.info(
            f'Received "{event.type}" event '
            f'from "{event.source}" for "{event.subject}" '
            f'[id: "{event.id}", trace_id: "{event.trace_parent.trace_id}", '
            f'parent_id: "{event.trace_parent.parent_id}"].',
            extra={"event": event},
        )
        logger.debug(event)

        return event

    def run(
        self,
        event: messaging.events.BaseEvent,
        *,
        metadata: Optional[dict] = None,
        dry_run: bool = False,
    ) -> None:
        raise NotImplementedError()


def handler(
    base: Type[Handler] = Handler,
    *,
    dispatcher: Optional["backends.base.Dispatcher"] = None,
    supports_dry_run: Optional[bool] = None,
) -> Handler:
    return base(dispatcher=dispatcher, supports_dry_run=supports_dry_run)


def event_hander(**kwargs: Any) -> Handler:
    return handler(base=EventHandler, **kwargs)


HandlerReferences = Union[
    WrappedFunction, str, Iterable[Union[WrappedFunction, str]]
]


def _parse_handler_references(
    handlers: HandlerReferences, *, context: Any
) -> List[WrappedFunction]:
    return [
        getattr(context, handler) if isinstance(handler, str) else handler
        for handler in utils.maybe_list(handlers)
    ]
