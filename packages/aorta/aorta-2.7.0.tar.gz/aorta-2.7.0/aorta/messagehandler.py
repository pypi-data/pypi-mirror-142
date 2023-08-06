"""Declares :class:`MessageHandler`."""
import asyncio
import inspect
import logging
import typing

from .command import Command
from .event import Event
from .ipublisher import IPublisher
from .models import Message


class MessageHandler:
    """The base class for all message handlers."""
    __module__: str = 'aorta'
    _is_coroutine = asyncio.coroutines._is_coroutine
    logger: logging.Logger = logging.getLogger('uvicorn')

    @property
    def __signature__(self):
        return inspect.signature(self.handle)

    def __init__(self,
        message: Message,
        publisher: IPublisher = None
    ):
        assert asyncio.iscoroutinefunction(self) # nosec
        self._message = message
        self._publisher = publisher

    async def handle(self):
        """Handle the incoming message."""
        raise NotImplementedError

    def get_parameters(self):
        """Return the parameters of the function to invoke."""
        raise NotImplementedError

    def issue(self, command: Command):
        """Issue a command using the default command issuer."""
        self._publisher.issue(command)

    async def on_exception(self, exception: Exception) -> bool:
        """Hook to perform cleanup after a fatal exception. Return a boolean
        indicating if the exception may be suppressed.
        """
        return False

    def publish(self, event: Event):
        """Publish an event using the default event publisher."""
        self._publisher.publish(event)

    async def __call__(self, *args, **kwargs):
        try:
            return await self.handle(*args, **kwargs)
        except Exception as exception:
            must_suppress = await self.on_exception(exception)
            if not must_suppress:
                self.logger.exception(
                    "Caught fatal %s",
                    type(exception).__name__
                )
                raise
