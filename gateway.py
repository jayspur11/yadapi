import asyncio
import heartbeat
import json
import opcodes
import websockets

from payload import Payload
from urllib import request as urlrequest

# Constants
_BASE_API_URL = "https://discord.com/api"
_GATEWAY_ENDPOINT = "/gateway"
_BOT_GATEWAY_ENDPOINT = "/gateway/bot"

# Singletons
_connection = None
_receiver = None
_sequence_number = None
_session_id = None


# Public methods
async def start(app_name, bot_token, intents, operating_system):
    connection = await _connect(app_name, bot_token)
    identity_data = {
        "token": bot_token,
        "intents": intents,
        "properties": {
            "$os": operating_system,
            "$browser": app_name,
            "$device": app_name
        }
    }
    identity_payload = Payload(opcodes.IDENTIFY, identity_data)
    await connection.send(identity_payload.dumps())


async def resume(app_name, bot_token, close_code=1000, close_reason=""):
    global _connection
    global _receiver
    global _sequence_number
    global _session_id

    if None in [_connection, _session_id, _sequence_number]:
        raise RuntimeError(
            "Tried resuming with missing info about prior connection.")

    await heartbeat.stop()
    await _connection.close(code=close_code, reason=close_reason)
    _receiver.cancel()

    connection = await _connect(app_name, bot_token)
    resume_data = {
        "token": bot_token,
        "session_id": _session_id,
        "seq": _sequence_number
    }
    resume_payload = Payload(opcodes.RESUME, resume_data)
    await connection.send(resume_payload.dumps())


# Private methods
def _get_gateway_information(app_name, bot_token):
    headers = {"User-Agent": app_name}
    if bot_token:
        headers["Authorization"] = "Bot " + bot_token
        endpoint = _BOT_GATEWAY_ENDPOINT
    else:
        endpoint = _GATEWAY_ENDPOINT

    gateway_request = urlrequest.Request(_BASE_API_URL + endpoint,
                                         headers=headers)
    with urlrequest.urlopen(gateway_request) as gateway_response:
        gateway_info = json.load(gateway_response)

    return gateway_info


async def _connect(app_name, bot_token):
    global _connection
    global _receiver

    gateway_info = _get_gateway_information(app_name, bot_token)
    gateway_url = gateway_info["url"] + "?v=8&encoding=json"
    _connection = await websockets.connect(gateway_url)
    _receiver = asyncio.get_event_loop().create_task(_receive())
    return _connection


async def _process_event(payload):
    # Gonna need to break this up by event title. Whee!
    pass


async def _revalidate(payload):
    if payload.data:
        # TODO: resume
        pass
    else:
        # TODO: start fresh
        pass


async def _process_greeting(payload):
    heartbeat.start(_connection, payload.data["interval"])


async def _receive():
    global _connection

    opcode_router = {
        opcodes.DISPATCH: _process_event,
        opcodes.RECONNECT: resume,
        opcodes.INVALID_SESSION: _revalidate,
        opcodes.HELLO: _process_greeting,
        opcodes.HEARTBEAT_ACK: heartbeat.ack,
        opcodes.HEARTBEAT: heartbeat.fire
    }
    while True:
        payload = await Payload.receive(_connection.recv())
        await opcode_router[payload.opcode](payload)