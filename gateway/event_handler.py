import asyncio

from gateway import connection
from gateway import heartbeat
from gateway import opcodes
from gateway import socket
from gateway.payload import Payload

_receiver = None


# Public methods
def start_receiving():
    global _receiver

    _receiver = asyncio.get_event_loop().create_task(_start_receiving_loop())


def stop_receiving():
    _receiver.cancel()


# Private methods
async def _process_event(payload):
    # Gonna need to break this up by event title. Whee!
    pass


async def _process_greeting(payload):
    heartbeat.start(payload.data["interval"])


async def _process_invalid_session(payload):
    if payload.data:  # Usually a dict, but this time it's boolean.
        await connection._resume()
    else:
        await connection._identify()


async def _start_receiving_loop():
    """Set up an infinite loop to receive and process gateway payloads.
    
    NOTE: This is meant to be a background process. Do NOT await this.
    """
    # Glorified switch-statement.
    # Each opcode maps to a lambda, which wraps the actual action being taken.
    # This means the receiver has a known arg list to pass.
    # NOTE: All actions must be async; the receiver will await them.
    opcode_router = {
        opcodes.DISPATCH: lambda payload: _process_event(payload),
        opcodes.RECONNECT: lambda _: connection.restart(),
        opcodes.INVALID_SESSION:
        lambda payload: _process_invalid_session(payload),
        opcodes.HELLO: lambda payload: _process_greeting(payload),
        opcodes.HEARTBEAT_ACK: lambda _: heartbeat.ack(),
        opcodes.HEARTBEAT: lambda _: heartbeat.fire()
    }
    while True:
        payload = await Payload.receive(socket.recv())
        await opcode_router[payload.opcode](payload)