from urllib.request import Request
from restapi import _core


# Public methods
def get_bot():
    url = _core.BASE_API_URL + "/gateway/bot"
    request = Request(url)
    return _core.make_request(request)