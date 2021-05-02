from urllib.request import Request
from restapi import _core
from restapi import url


# Public methods
def get_gateway():
    return _core.make_get_request("/gateway")


def get_bot():
    return _core.make_get_request("/gateway/bot")
