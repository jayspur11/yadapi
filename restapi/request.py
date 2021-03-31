import json

from urllib.request import Request, urlopen

_BASE_API_URL = "https://discord.com/api/v8"


# Public methods
async def gateway_bot(app_name, bot_token):
    url = _BASE_API_URL + "/gateway/bot"
    headers = {"User-Agent": app_name, "Authorization": "Bot " + bot_token}
    request = Request(url, headers=headers)
    with urlopen(request) as response:
        return json.load(response)