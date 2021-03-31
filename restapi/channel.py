from urllib.request import Request
from restapi import _core


def get_channel(channel_id):
    url = _core.endpoint("channels", channel_id)
    request = Request(url)
    return _core.make_request(request)


def get_messages(channel_id,
                 limit=None,
                 around_message=None,
                 before_message=None,
                 after_message=None):
    query = []
    if limit:
        query.append("limit=" + str(limit))
    # Mutually exclusive
    if around_message:
        query.append("around=" + around_message)
    elif before_message:
        query.append("before=" + before_message)
    elif after_message:
        query.append("after=" + after_message)
    query = "?" + "&".join(query) if query else ""

    url = _core.endpoint("channels", channel_id, "messages") + query
    request = Request(url)
    return _core.make_request(request)