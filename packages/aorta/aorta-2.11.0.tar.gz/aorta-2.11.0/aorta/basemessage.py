"""Declares :class:`BaseMessage`."""
import logging
import uuid

from unimatrix.lib import timezone

from .models import Message
from .messagemetaclass import MessageMetaclass


class BaseMessage:
    """The base class for all message types."""
    __abstract__: bool = True

    def __init__(self, **kwargs):
        self._params = self._model(**kwargs)

    def as_message(self,
        correlation_id: str = None,
        ttl: int = None
    ) -> Message:
        """Wrap the message in a :class:`aorta.models.Envelope` instance.

        The `correlation_id` specifies a correlation identifier that may be
        used to find relationships between various messages.

        A message time-to-live can be specified with the `ttl` argument, which
        indicates the time-to-live in milliseconds.
        """
        dto = {
            'apiVersion': self._meta.api_version,
            'kind': type(self).__name__,
            'type': self._meta.type,
            'metadata': {
                'id': uuid.uuid4(),
                'correlationId': correlation_id or uuid.uuid4(),
                'published': timezone.now(),
                'ttl': ttl
            },
            self._meta.envelope_field: self._params.dict()
        }
        return self._envelope(**dto)
