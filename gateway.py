import asyncio
import heartbeat
import json
import opcodes
import websockets

from payload import Payload
from urllib import request as urlrequest

# Constants
_BASE_API_URL = "https://discord.com/api"
_BOT_GATEWAY_ENDPOINT = "/gateway/bot"

# Singletons
_app_name = None
_bot_token = None
_connection = None
_intents = None
_operating_system = None
_receiver = None
_sequence_number = None
_session_id = None


# Public methods
async def restart(_=None, close_code=1000, close_reason=""):
    if None in [_connection, _session_id, _sequence_number]:
        raise RuntimeError(
            "Tried resuming with missing info about prior connection.")

    await heartbeat.stop()
    await _connection.close(code=close_code, reason=close_reason)
    _receiver.cancel()

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
    global _connection
    global _receiver

    gateway_info = _get_gateway_information()
    gateway_url = gateway_info["url"] + "?v=8&encoding=json"
    _connection = await websockets.connect(gateway_url)
    _receiver = asyncio.get_event_loop().create_task(_receive())


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
    await _connection.send(identity_payload.dumps())


async def _process_event(payload):
    # Gonna need to break this up by event title. Whee!
    pass


async def _process_greeting(payload):
    heartbeat.start(_connection, payload.data["interval"])


async def _receive():
    opcode_router = {
        opcodes.DISPATCH: _process_event,
        opcodes.RECONNECT: _resume,
        opcodes.INVALID_SESSION: _revalidate,
        opcodes.HELLO: _process_greeting,
        opcodes.HEARTBEAT_ACK: heartbeat.ack,
        opcodes.HEARTBEAT: heartbeat.fire
    }
    while True:
        payload = await Payload.receive(_connection.recv())
        await opcode_router[payload.opcode](payload)


async def _resume(_=None):
    await _connect()
    resume_data = {
        "token": _bot_token,
        "session_id": _session_id,
        "seq": _sequence_number
    }
    resume_payload = Payload(opcodes.RESUME, resume_data)
    await _connection.send(resume_payload.dumps())


async def _revalidate(payload):
    if payload.data:
        await _resume()
    else:
        await _identify()