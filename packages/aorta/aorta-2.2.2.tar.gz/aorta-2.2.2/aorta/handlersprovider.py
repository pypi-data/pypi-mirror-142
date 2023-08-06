"""Declares :class:`HandlersProvider`."""
import typing

from .commandhandler import CommandHandler
from .eventlistener import EventListener
from .handlermetaclass import HandlerMetaclass
from .models import Message


class HandlersProvider:
    """Provides an interface to lookup handlers for specific messages."""
    __module__ = 'aorta'

    def __init__(self):
        self._command = {}
        self._event = []

    def get(self, message: Message) -> typing.List[HandlerMetaclass]:
        """Return the list of handlers that match the given `message`."""
        handlers = []
        if message.is_command() and self._command.get(message.qualname):
            handlers.append(self._command[message.qualname])
        elif message.is_event():
            handlers.extend([x for x in self._event if x.can_handle(message)])
        return handlers

    def register(self, handler_class: HandlerMetaclass) -> None:
        """Register an concrete implementation of :class:`aorta.CommandHandler`
        or :class:`aorta.EventListener`.

        :class:`CommandHandler` implementations can only be registered once for
        a specific command, successive calls for the same command will register
        the last handler only.
        """
        if not issubclass(handler_class, (CommandHandler, EventListener)):
            raise TypeError(f"Not a valid handler: {handler_class.__name__}")
        elif issubclass(handler_class, CommandHandler):
            self._command.update(handler_class)
        elif issubclass(handler_class, EventListener):
            self._event.append(handler_class)
