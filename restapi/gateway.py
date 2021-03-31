import json

from restapi import _core
from urllib.request import Request, urlopen


# Public methods
async def bot():
    url = _core.BASE_API_URL + "/gateway/bot"
    headers = {
        "User-Agent": _core.app_name,
        "Authorization": "Bot " + _core.bot_token
    }
    request = Request(url, headers=headers)
    with urlopen(request) as response:
        return json.load(response)