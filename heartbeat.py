import asyncio
import gateway
import opcodes
import time

from payload import Payload

_HEARTBEAT_PAYLOAD = Payload(opcodes.HEARTBEAT).dumps()

_websocket = None
_interval_sec = None
_next_beat = None
_last_send = None
_last_ack = None


# Public methods
def start(websocket, interval_ms):
    global _websocket
    global _interval_sec

    _websocket = websocket
    _interval_sec = interval_ms / 1000
    _schedule_next()


async def fire():
    global _websocket
    global _last_ack
    global _last_send

    if _last_send and (not _last_ack or _last_send > _last_ack):
        await gateway.resume()
    else:
        await _websocket.send(_HEARTBEAT_PAYLOAD)


async def ack():
    global _last_ack

    _last_ack = time.time()


async def stop():
    global _next_beat

    _next_beat.cancel()
    _next_beat = None


# Private methods
def _schedule_next():
    global _next_beat

    _next_beat = asyncio.get_event_loop().create_task(_delayed_fire())


async def _delayed_fire():
    global _interval_sec

    await asyncio.sleep(_interval_sec)
    await fire()
    _schedule_next()