from restapi import _core


# Public methods
def get_gateway():
    return _core.make_get_request("/gateway")


def get_bot():
    return _core.make_get_request("/gateway/bot")
