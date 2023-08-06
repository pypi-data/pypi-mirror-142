"""Declares :class:`Handler`."""
import asyncio
import inspect

from .handlermetaclass import HandlerMetaclass
from .models import Message
from .node import Node


class Handler(Node, metaclass=HandlerMetaclass):
    """Handles an incoming message using the :meth:`handle()` method."""
    __module__: str = 'aorta'
    _is_coroutine = asyncio.coroutines._is_coroutine

    @property
    def __signature__(self):
        return inspect.signature(self.handle)

    @classmethod
    def can_handle(self, message: Message) -> bool:
        """Return a boolean indicating if the :class:`Handler` knows
        how to process `message`.
        """
        return (message.api_version, message.kind) in self._meta.handles

    def __init__(self):
        # Check if the asyncio.iscoroutinefunction() call returns
        # True for this object, since it depends on a private
        # symbol.
        assert asyncio.iscoroutinefunction(self) # nosec
        self.logger.debug(
            "Initializing message handler %s",
            type(self).__name__
        )

    async def handle(self, message: Message, *args, **kwargs):
        """Invoked for each incoming message that matches the handlers'
        criteria.
        """
        raise NotImplementedError

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, exception, traceback) -> bool:
        pass

    async def __call__(self, *args, **kwargs):
        await self.handle(*args, **kwargs)
