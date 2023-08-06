"""Declares :class:`NullTransport`."""
import logging
import typing

from ..models import MessageHeader
from .itransport import ITransport


class NullTransport(ITransport):
    """A transport implementation that does nothing."""
    logger: logging.Logger = logging.getLogger('uvicorn')

    async def send(self, objects: typing.List[MessageHeader]):
        """Log each message in `objects`."""
        for message in objects:
            self.logger.info(
                "Publishing %s/%s (id: %s, correlationId: %s)",
                message.api_version,
                message.kind,
                message.metadata.id,
                message.metadata.correlationId
            )
