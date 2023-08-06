"""Declares :class:`EventPublisher`."""
import typing

from .models import Message
from .sender import Sender


class EventPublisher(Sender):
    """Provides an interface to published event messages."""
    __module__: str = 'aorta'

    async def publish(self,
        dto: typing.Union[dict, Message],
        correlation_id: str = None
    ):
        """Publish an event to the upstream peer."""
        if not isinstance(dto, Message):
            dto['type'] = "unimatrixone.io/event"
            dto = self.prepare(dto, correlation_id=correlation_id)
        await self.send(dto)
