import asyncio
import socket
import time

from gateway import connection
from gateway import opcodes
from gateway.payload import Payload

_HEARTBEAT_PAYLOAD = Payload(opcodes.HEARTBEAT).dumps()

_last_ack = None
_next_beat = None


# Public methods
async def ack():
    """Handle HEARTBEAT_ACK event.
    """
    global _last_ack

    _last_ack = time.time()


async def fire(last_send=None):
    """Send a HEARTBEAT command to the server.

    Args:
        last_send (int, optional): Time of last scheduled send.
            Can be None if this is the first send, or if this wasn't scheduled.
            Defaults to None.
    """
    if not last_send or (_last_ack and last_send < _last_ack):
        await socket.send(_HEARTBEAT_PAYLOAD)
    else:
        await connection.restart(close_code=1001,
                                 close_reason="Missed heartbeat ack.")


def start(interval_ms):
    """Start sending HEARTBEAT commands at a regular interval.

    Args:
        interval_ms (int): Number of milliseconds the server is expecting the
            client to wait between heartbeats.
    """
    global _next_beat

    _next_beat = asyncio.get_event_loop().create_task(
        _start_heartbeat(interval_ms / 1000))


async def stop():
    """Stop sending regular HEARTBEAT commands.
    """
    _next_beat.cancel()


# Private methods
async def _start_heartbeat(interval_sec):
    """Set up an infinite loop to send regular HEARTBEAT commands.

    Args:
        interval_sec (int): Number of seconds the server is expecting the client
            to wait between heartbeats.
            
    NOTE: This is meant to be a background process. Do NOT await this.
    """
    last_send = None
    while True:
        await asyncio.sleep(interval_sec)
        await fire(last_send)
        last_send = time.time()