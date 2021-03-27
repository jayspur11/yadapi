from websockets.exceptions import InvalidState
import heartbeat
import json
import opcodes
import websockets

from urllib import request as urlrequest

# Constants
_BASE_API_URL = "https://discord.com/api"
_GATEWAY_ENDPOINT = "/gateway"
_BOT_GATEWAY_ENDPOINT = "/gateway/bot"
_DATA_KEY = "d"

# Singletons
_connection = None
_heartbeat = None
_sequence_number = None
_session_id = None


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
    global _heartbeat
    global _connection

    gateway_info = _get_gateway_information(app_name, bot_token)
    gateway_url = gateway_info["url"] + "?v=8&encoding=json"
    _connection = await websockets.connect(gateway_url)
    greeting = json.loads(await _connection.recv())
    _heartbeat = heartbeat.Heartbeat(_connection,
                                     greeting[_DATA_KEY]["interval"])

    return _connection


async def start(app_name, bot_token, intents, operating_system):
    connection = await _connect(app_name, bot_token)
    identity_payload = json.dumps({
        opcodes.key: opcodes.IDENTIFY,
        _DATA_KEY: {
            "token": bot_token,
            "intents": intents,
            "properties": {
                "$os": operating_system,
                "$browser": app_name,
                "$device": app_name
            }
        }
    })
    await connection.send(identity_payload)
    ready = json.loads(await connection.recv())
    # TODO: process Ready event


async def resume(app_name, bot_token, close_code=1000, close_reason=""):
    global _connection
    global _heartbeat

    if None in [_connection, _session_id, _sequence_number]:
        raise InvalidState

    # TODO: stop heartbeat
    await _connection.close(code=close_code, reason=close_reason)
    _connection = None

    connection = await _connect(app_name, bot_token)
    resume_payload = json.dumps({
        opcodes.key: opcodes.RESUME,
        _DATA_KEY: {
            "token": bot_token,
            "session_id": _session_id,
            "seq": _sequence_number
        }
    })
    await connection.send(resume_payload)


async def _revalidate():
    pass


async def _process_greeting():
    pass


async def _receive(connection, event_callback):
    opcode_router = {
        opcodes.DISPATCH: event_callback,
        opcodes.RECONNECT: resume,
        opcodes.INVALID_SESSION: _revalidate,
        opcodes.HELLO: _process_greeting,
        opcodes.HEARTBEAT_ACK: _heartbeat.ack,
        opcodes.HEARTBEAT: _heartbeat.fire
    }
    payload = await json.loads(connection.recv())
    # TODO: pass args
    await opcode_router[payload[opcodes.key]]()