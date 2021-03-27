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


async def fire(_=None, scheduled=False):
    global _websocket
    global _last_ack
    global _last_send

    acked_after_send = not _last_send or (_last_ack and _last_send < _last_ack)
    if not scheduled or acked_after_send:
        await _websocket.send(_HEARTBEAT_PAYLOAD)
        _last_send = time.time()
    else:
        await gateway.resume(close_code=1001,
                             close_reason="Missed heartbeat ack.")


async def ack():
    global _last_ack

    _last_ack = time.time()


async def stop():
    global _last_ack
    global _last_send
    global _next_beat

    _next_beat.cancel()
    _next_beat = None
    _last_send = None
    _last_ack = None


# Private methods
def _schedule_next():
    global _next_beat

    _next_beat = asyncio.get_event_loop().create_task(_delayed_fire())


async def _delayed_fire():
    global _interval_sec

    await asyncio.sleep(_interval_sec)
    await fire(scheduled=True)
    _schedule_next()