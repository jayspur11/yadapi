import websockets

_connection = None


async def close(code=1000, reason=""):
    _connection.close(code=code, reason=reason)


async def connect(url):
    _connection = await websockets.connect(url)


async def recv():
    return await _connection.recv()


async def send(payload):
    # TODO: rate limit
    await _connection.send(payload)