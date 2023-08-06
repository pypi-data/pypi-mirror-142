"""Declares :class:`Options`."""


class Options:
    """Configures an event listener or command handler."""

    def __init__(self, cls: type, meta: object):
        self.cls = cls
        self.handles = getattr(meta, 'handles', [])

    def contribute_to_class(self, cls):
        setattr(cls, '_meta', self)
