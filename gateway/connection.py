import asyncio
import json
import socket
import time

from gateway import heartbeat
from gateway import opcodes
from gateway.payload import Payload
from gateway.rate_counter import RateCounter
from urllib import request as urlrequest

_BASE_API_URL = "https://discord.com/api"
_BOT_GATEWAY_ENDPOINT = "/gateway/bot"

_app_name = None
_bot_token = None
_identify_counter = RateCounter(5)
_intents = None
_operating_system = None
_receiver = None
_sequence_number = None
_session_id = None


# Public methods
async def restart(close_code=1000, close_reason=""):
    """Close the connection to the gateway and reopen (resuming the session).

    Args:
        close_code (int, optional): Code to close the connection with. Defaults to 1000 (clean).
        close_reason (str, optional): Reason for closing the connection. Defaults to "".
    """
    _receiver.cancel()
    await heartbeat.stop()
    await socket.close(close_code, close_reason)

    await _resume()


async def start(app_name, bot_token, intents, operating_system):
    global _app_name
    global _bot_token
    global _intents
    global _operating_system

    _app_name = app_name
    _bot_token = bot_token
    _intents = intents
    _operating_system = operating_system

    await _identify()


# Private methods
async def _connect():
    global _receiver

    gateway_info = _get_gateway_information()
    gateway_url = gateway_info["url"] + "?v=8&encoding=json"
    socket.connect(gateway_url)
    _receiver = asyncio.get_event_loop().create_task(_start_receiver_loop())


def _get_gateway_information():
    headers = {"User-Agent": _app_name, "Authorization": "Bot " + _bot_token}
    endpoint = _BOT_GATEWAY_ENDPOINT

    gateway_request = urlrequest.Request(_BASE_API_URL + endpoint,
                                         headers=headers)
    with urlrequest.urlopen(gateway_request) as gateway_response:
        gateway_info = json.load(gateway_response)

    return gateway_info


async def _identify():
    await _connect()
    identity_data = {
        "token": _bot_token,
        "intents": _intents,
        "properties": {
            "$os": _operating_system,
            "$browser": _app_name,
            "$device": _app_name
        }
    }
    identity_payload = Payload(opcodes.IDENTIFY, identity_data)
    if len(_identify_counter) > 1:  # TODO: use max_concurrency
        # We've exceeded the rate limit. Wait for an event to drop off.
        time.sleep(_identify_counter.next_event())
    _identify_counter.add()
    await socket.send(identity_payload.dumps())


async def _process_event(payload):
    # Gonna need to break this up by event title. Whee!
    pass


async def _process_greeting(payload):
    heartbeat.start(payload.data["interval"])


async def _process_invalid_session(payload):
    if payload.data:  # Usually a dict, but this time it's boolean.
        await _resume()
    else:
        await _identify()


async def _resume():
    """Connect to the gateway and send a RESUME command.
    
    NOTE: This must be called after a prior connection that IDENTIFY'd.

    Raises:
        RuntimeError: There wasn't enough information to send a RESUME command.
    """
    if None in [_session_id, _sequence_number]:
        raise RuntimeError(
            "Tried resuming with missing info about prior connection.")

    await _connect()
    resume_data = {
        "token": _bot_token,
        "session_id": _session_id,
        "seq": _sequence_number
    }
    resume_payload = Payload(opcodes.RESUME, resume_data)
    await socket.send(resume_payload.dumps())


async def _start_receiver_loop():
    """Set up an infinite loop to receive and process gateway payloads.
    
    NOTE: This is meant to be a background process. Do NOT await this.
    """
    # Glorified switch-statement.
    # Each opcode maps to a lambda, which wraps the actual action being taken.
    # This means the receiver has a known arg list to pass.
    # NOTE: All actions must be async; the receiver will await them.
    opcode_router = {
        opcodes.DISPATCH: lambda payload: _process_event(payload),
        opcodes.RECONNECT: lambda _: restart(),
        opcodes.INVALID_SESSION:
        lambda payload: _process_invalid_session(payload),
        opcodes.HELLO: lambda payload: _process_greeting(payload),
        opcodes.HEARTBEAT_ACK: lambda _: heartbeat.ack(),
        opcodes.HEARTBEAT: lambda _: heartbeat.fire()
    }
    while True:
        payload = await Payload.receive(socket.recv())
        await opcode_router[payload.opcode](payload)