"""Declares :class:`CommandHandler`."""
from .messagehandler import MessageHandler


class CommandHandler(MessageHandler):
    """Handles command messages."""
    __module__: str = 'aorta'

    def get_parameters(self):
        """Return the command arguments."""
        return self._message.spec
