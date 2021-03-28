import asyncio
import gateway
import opcodes
import socket
import time

from payload import Payload

_HEARTBEAT_PAYLOAD = Payload(opcodes.HEARTBEAT).dumps()

_interval_sec = None
_last_ack = None
_last_send = None
_next_beat = None


# Public methods
async def ack():
    global _last_ack

    _last_ack = time.time()


async def fire(scheduled=False):
    global _last_ack
    global _last_send

    acked_after_send = not _last_send or (_last_ack and _last_send < _last_ack)
    if not scheduled:
        await socket.send(_HEARTBEAT_PAYLOAD)
    elif acked_after_send:
        await socket.send(_HEARTBEAT_PAYLOAD)
        _last_send = time.time()
    else:
        await gateway.restart(close_code=1001,
                              close_reason="Missed heartbeat ack.")


def start(interval_ms):
    global _next_beat

    _next_beat = asyncio.get_event_loop().create_task(
        _start_heartbeat(interval_ms / 1000))


async def stop():
    global _last_ack
    global _last_send
    global _next_beat

    _next_beat.cancel()
    _next_beat = None
    _last_send = None
    _last_ack = None


# Private methods
async def _start_heartbeat(interval_sec):
    while True:
        await asyncio.sleep(interval_sec)
        await fire(scheduled=True)