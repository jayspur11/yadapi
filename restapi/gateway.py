from urllib.request import Request
from restapi import _core
from restapi import url


# Public methods
def get_bot():
    endpoint = url.URL("/gateway/bot")
    request = Request(endpoint.build())
    return _core.make_request(request)