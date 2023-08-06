"""Declares :class:`EventListener`."""
from .handler import Handler


class EventListener(Handler):
    """A :class:`Handler` implementation that processes messages that
    represent events.
    """
    __module__: str = 'aorta'
    kind: str = 'EventListener'
