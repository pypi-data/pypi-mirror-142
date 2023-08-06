# pylint: skip-file
import asyncio

import ioc

from .command import Command
from .commandissuer import CommandIssuer
from .commandhandler import CommandHandler
from .dispatcher import Dispatcher
from .event import Event
from .eventlistener import EventListener
from .eventpublisher import EventPublisher
from .handler import Handler
from .handlersprovider import HandlersProvider
from .messagepublisher import MessagePublisher
from .runner import BaseRunner
from .runner import FastAPIRunner
from . import models
from . import transport


__all__ = [
    'models',
    'publish',
    'transport',
    'BaseRunner',
    'Command',
    'CommandHandler',
    'CommandIssuer',
    'Dispatcher',
    'Event',
    'EventListener',
    'EventPublisher',
    'FastAPIRunner',
    'Handler',
    'HandlersProvider',
    'MessagePublisher',
]


_issuer = ioc.require('CommandIssuer')
_provider = HandlersProvider()
_publisher = ioc.require('EventPublisher')


async def issue(name: str, params: dict, version: str = 'v1') -> None:
    """Issue a command using the default command issuer."""
    await _issuer.issue({
        'apiVersion': version,
        'kind': name,
        'spec': params
    })


async def publish(name: str, params: dict, version: str = 'v1') -> None:
    """Publishes an event using the default event publisher."""
    await _publisher.publish({
        'apiVersion': version,
        'kind': name,
        'data': params
    })


def register(*args, **kwargs):
    return _provider.register(*args, **kwargs)
register.__doc__ = _provider.register.__doc__


async def run(runner: BaseRunner, message: models.Message):
    """Run handlers for all `messages` using `runner`."""
    futures = []
    for handler_class in _provider.get(message):
        async with handler_class() as handler:
            futures.append(runner.run(handler))
    await asyncio.gather(*futures)
