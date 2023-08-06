# pylint: skip-file
import pytest

import aorta


class TestCommand(aorta.Command):
    foo: int


class TestEvent(aorta.Event):
    foo: int


@pytest.fixture
def command():
    return TestCommand(foo=1)


@pytest.fixture
def event():
    return TestEvent(foo=1)


@pytest.fixture
def publisher():
    return aorta.MessagePublisher(
        transport=aorta.transport.NullTransport()
    )
