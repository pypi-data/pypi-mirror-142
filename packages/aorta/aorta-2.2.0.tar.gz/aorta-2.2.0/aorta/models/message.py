"""Declares :class:`Message`."""
import pydantic

from .messageheader import MessageHeader


class Message(MessageHeader):
    data: dict = pydantic.Field({})
    spec: dict = pydantic.Field({})

    @property
    def qualname(self) -> tuple:
        """Return the qualified name of the message type."""
        return (self.api_version, self.kind)

    def is_command(self) -> bool:
        """Return a boolean indicating if the message is a command."""
        return self.type == "unimatrixone.io/command"

    def is_event(self) -> bool:
        """Return a boolean indicating if the message is an event."""
        return self.type == "unimatrixone.io/event"
