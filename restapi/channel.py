from urllib.request import Request
from restapi import _core
from restapi import url


def get_channel(channel_id):
    endpoint = url.URL(path="/channels/{cid}".format(cid=channel_id))
    request = Request(endpoint.build())
    return _core.make_request(request)


def get_messages(channel_id,
                 limit=None,
                 around_message=None,
                 before_message=None,
                 after_message=None):
    endpoint = url.URL("/channels/{cid}/messages".format(cid=channel_id))
    endpoint.add_query_params({
        "limit": str(limit),
        "around": around_message,
        "before": before_message,
        "after": after_message
    })

    request = Request(endpoint.build())
    return _core.make_request(request)