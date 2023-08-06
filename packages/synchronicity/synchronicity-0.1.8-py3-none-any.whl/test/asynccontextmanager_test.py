import asyncio
import pytest

from synchronicity import Synchronizer


async def noop():
    pass


async def error():
    raise Exception("problem")


class Resource:
    def __init__(self):
        self.state = "none"

    async def wrap(self):
        self.state = "entered"
        try:
            yield
        finally:
            self.state = "exited"

    async def wrap_yield_twice(self):
        yield
        yield

    async def wrap_never_yield(self):
        if False:
            yield


def test_asynccontextmanager_sync():
    r = Resource()
    s = Synchronizer()
    f = s.asynccontextmanager(r.wrap)
    assert r.state == "none"
    with f():
        assert r.state == "entered"
    assert r.state == "exited"


@pytest.mark.asyncio
async def test_asynccontextmanager_async():
    r = Resource()
    s = Synchronizer()
    f = s.asynccontextmanager(r.wrap)
    assert r.state == "none"
    async with f():
        assert r.state == "entered"
    assert r.state == "exited"


@pytest.mark.asyncio
async def test_asynccontextmanager_async_raise():
    r = Resource()
    s = Synchronizer()
    f = s.asynccontextmanager(r.wrap)
    assert r.state == "none"
    with pytest.raises(Exception):
        async with f():
            assert r.state == "entered"
            raise Exception("boom")
    assert r.state == "exited"


@pytest.mark.asyncio
async def test_asynccontextmanager_yield_twice():
    r = Resource()
    s = Synchronizer()
    f = s.asynccontextmanager(r.wrap_yield_twice)
    with pytest.raises(RuntimeError):
        async with f():
            pass


@pytest.mark.asyncio
async def test_asynccontextmanager_never_yield():
    r = Resource()
    s = Synchronizer()
    f = s.asynccontextmanager(r.wrap_never_yield)
    with pytest.raises(RuntimeError):
        async with f():
            pass


@pytest.mark.asyncio
async def test_asynccontextmanager_nested():
    s = Synchronizer()
    finally_blocks = []

    @s.asynccontextmanager
    async def a():
        try:
            yield "foo"
        finally:
            finally_blocks.append("A")

    @s.asynccontextmanager
    async def b():
        async with a() as it:
            try:
                yield it
            finally:
                finally_blocks.append("B")

    with pytest.raises(BaseException):
        async with b():
            raise BaseException("boom!")

    assert finally_blocks == ["B", "A"]


@pytest.mark.asyncio
async def test_asynccontextmanager_with_in_async():
    r = Resource()
    s = Synchronizer()
    f = s.asynccontextmanager(r.wrap)
    with pytest.raises(RuntimeError):
        with f():
            pass
