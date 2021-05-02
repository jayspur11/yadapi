import json
from restapi import url
from urllib.request import Request, urlopen

app_name = None
bot_token = None


def make_get_request(endpoint_path: str, query_params={}: dict):
    endpoint = url.URL(endpoint_path)
    endpoint.add_query_params(query_params)
    request = Request(endpoint.build())
    return make_request(request)


def make_request(request: Request):
    request.add_header("User-Agent", app_name)
    request.add_header("Authorization", "Bot " + bot_token)
    with urlopen(request) as response:
        return json.load(response)