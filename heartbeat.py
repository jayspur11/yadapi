import asyncio
import gateway
import opcodes
import socket
import time

from payload import Payload

_HEARTBEAT_PAYLOAD = Payload(opcodes.HEARTBEAT).dumps()

_last_ack = None
_next_beat = None


# Public methods
async def ack():
    global _last_ack

    _last_ack = time.time()


async def fire(last_send=None):
    if not last_send or (_last_ack and last_send < _last_ack):
        await socket.send(_HEARTBEAT_PAYLOAD)
    else:
        await gateway.restart(close_code=1001,
                              close_reason="Missed heartbeat ack.")


def start(interval_ms):
    global _next_beat

    _next_beat = asyncio.get_event_loop().create_task(
        _start_heartbeat(interval_ms / 1000))


async def stop():
    global _last_ack

    _next_beat.cancel()
    _last_ack = None


# Private methods
async def _start_heartbeat(interval_sec):
    last_send = None
    while True:
        await asyncio.sleep(interval_sec)
        await fire(last_send)
        last_send = time.time()