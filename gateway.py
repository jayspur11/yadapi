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
_HEARTBEAT = None


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


async def connect(app_name, bot_token, intents, operating_system, library_name):
    global _HEARTBEAT
    gateway_info = _get_gateway_information(app_name, bot_token)
    gateway_url = gateway_info["url"] + "?v=8&encoding=json"
    websocket = await websockets.connect(gateway_url)
    greeting = json.loads(await websocket.recv())
    _HEARTBEAT = heartbeat.Heartbeat(websocket, greeting[_DATA_KEY]["interval"])
    await websocket.send(json.dumps({
        opcodes.key: opcodes.IDENTIFY,
        _DATA_KEY: {
            "token": bot_token,
            "intents": intents,
            "properties": {
                "$os": operating_system,
                "$browser": library_name,
                "$device": library_name
            }
        }
    }))
    ready = json.loads(await websocket.recv())
    return websocket
