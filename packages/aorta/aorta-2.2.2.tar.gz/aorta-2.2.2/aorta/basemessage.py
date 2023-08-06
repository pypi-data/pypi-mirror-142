"""Declares :class:`BaseMessage`."""
import uuid

from unimatrix.lib import timezone

from .models import Message
from .messagemetaclass import MessageMetaclass


class BaseMessage:
    """The base class for all message types."""
    __abstract__: bool = True

    def __init__(self, **kwargs):
        self._params = self._model(**kwargs)

    def as_message(self, correlation_id: str = None) -> Message:
        """Wrap the message in a :class:`aorta.models.Envelope` instance."""
        dto = {
            'apiVersion': self._meta.api_version,
            'kind': type(self).__name__,
            'type': self._meta.type,
            'metadata': {
                'id': uuid.uuid4(),
                'correlationId': correlation_id or uuid.uuid4(),
                'published': timezone.now()
            },
            self._meta.envelope_field: self._params.dict()
        }
        return self._envelope(**dto)
