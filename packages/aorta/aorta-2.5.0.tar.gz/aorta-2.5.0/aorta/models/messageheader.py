"""Declares :class:`Message`."""
import pydantic

from .messagemetadata import MessageMetadata


class MessageHeader(pydantic.BaseModel):
    api_version: str = pydantic.Field(..., alias='apiVersion')
    kind: str = pydantic.Field(...)
    type: str = pydantic.Field(None)
    metadata: MessageMetadata = pydantic.Field(
        default_factory=MessageMetadata
    )

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

    def log(self, logger) -> None:
        print(f"Received {self.api_version}/{self.kind} (id: {self.metadata.id}, correlationId: {self.metadata.correlation_id})")

    def __bytes__(self) -> bytes:
        return str.encode(
            self.json(by_alias=True, exclude_defaults=True),
            "utf-8"
        )
