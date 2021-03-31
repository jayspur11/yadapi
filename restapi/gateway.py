from urllib.request import Request
from restapi import _core


def _gateway_endpoint(path):
    return _core.BASE_API_URL + "/gateway/" + path


# Public methods
def get_bot():
    url = _gateway_endpoint("bot")
    request = Request(url)
    return _core.make_request(request)