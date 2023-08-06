"""Declares :class:`EventListener`."""
from .messagehandler import MessageHandler


class EventListener(MessageHandler):
    """Handles event messages."""
    __module__: str = 'aorta'

    def get_parameters(self):
        """Return the event data."""
        return self._message.data
