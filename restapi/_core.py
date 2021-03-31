import json
from urllib.request import Request, urlopen

BASE_API_URL = "https://discord.com/api/v8/"

app_name = None
bot_token = None


def endpoint(*args):
    return BASE_API_URL + "/".join(args)


def make_request(request: Request):
    request.add_header("User-Agent", app_name)
    request.add_header("Authorization", "Bot " + bot_token)
    with urlopen(request) as response:
        return json.load(response)