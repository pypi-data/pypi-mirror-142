"""Declares :class:`NullRunner`."""
from .base import BaseRunner


class NullRunner(BaseRunner):
    """A :class:`BaseRunner` implementation that does nothing."""
    __module__: str = 'aorta.runner'

    async def run(self, handler) -> None:
        print(handler)
