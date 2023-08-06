"""Declares :class:`ITransport`."""
import logging

from ..models import Message


class ITransport:
    """Declares the interface for all transport implementations."""
    logger: logging.Logger = logging.getLogger('uvicorn')

    async def send(self, message: Message):
        raise NotImplementedError

    async def publish(self, objects: typing.List[MessageHeader]):
        """Perform last-minute operations prior to serializing the message
        and transmitting it to the upstream peer.
        """
        for message in objects:
            self.logger.info(
                "Publishing %s/%s (id: %s, correlationId: %s)",
                message.api_version,
                message.kind,
                message.metadata.id,
                message.metadata.correlation_id
            )
        return await self.send(objects)
