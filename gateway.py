import json
import websockets

from urllib import request as urlrequest

# Constants
_BASE_API_URL = "https://discord.com/api"
_GATEWAY_ENDPOINT = "/gateway"
_BOT_GATEWAY_ENDPOINT = "/gateway/bot"


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


async def connect(app_name, bot_token):
    gateway_info = _get_gateway_information(app_name, bot_token)
    gateway_url = gateway_info["url"] + "?v=8&encoding=json"
    return await websockets.connect(gateway_url)
