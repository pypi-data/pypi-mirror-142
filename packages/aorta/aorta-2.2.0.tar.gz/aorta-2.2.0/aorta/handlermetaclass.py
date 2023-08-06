"""Declares :class:`HandlerMetaclass`."""
from .options import Options


class HandlerMetaclass(type):

    def __new__(cls, name, bases, attrs):
        new = super().__new__
        if name in ('Handler', 'CommandHandler', 'EventListener'):
            return new(cls, name, bases, attrs)
        meta = attrs.pop('Meta', None)
        if meta is None:
            raise AttributeError(
                f"Declare an inner Meta class for {name}"
            )
        new_class = new(cls, name, bases, attrs)
        opts = Options(new_class, meta)
        opts.contribute_to_class(new_class)
        return new_class

    def __iter__(self):
        return iter((x, self) for x in self._meta.handles)

    def __repr__(self) -> str:
        return f"<{self.kind}: {self.__name__}>"
