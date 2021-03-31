from urllib.request import Request
from restapi import _core


def _channel_endpoint(path):
    return _core.BASE_API_URL + "/channels/" + path


def get_channel(channel_id):
    url = _channel_endpoint + channel_id
    request = Request(url)
    return _core.make_request(request)