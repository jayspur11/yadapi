import websockets

from rate_counter import RateCounter

_RATE_LIMIT = 2

_connection = None
_counter = RateCounter(60)


async def close(code=1000, reason=""):
    _connection.close(code=code, reason=reason)


async def connect(url):
    global _connection

    _connection = await websockets.connect(url)


async def recv():
    return await _connection.recv()


async def send(payload):
    if _counter.rate() > _RATE_LIMIT:
        # TODO: rate limit
        pass
    _counter.add()
    await _connection.send(payload)