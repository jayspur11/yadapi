from urllib.parse import quote
from urllib.request import Request
from restapi import _core
from restapi import url


def get_channel(channel_id):
    endpoint = url.URL("/channels/{cid}".format(cid=channel_id))
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


def get_message(channel_id, message_id):
    endpoint = url.URL("/channels/{cid}/messages/{mid}".format(cid=channel_id,
                                                               mid=message_id))
    request = Request(endpoint.build())
    return _core.make_request(request)


def get_reactions(channel_id, message_id, emoji, after=None, limit=None):
    emoji_urlsafe = quote(emoji, safe="")
    endpoint = url.URL(f"/channels/{channel_id}/messages/{message_id}/reactions"
                       f"/{emoji_urlsafe}")
    endpoint.add_query_params({
        "after": after,
        "limit": str(limit)
    })
    request = Request(endpoint.build())
    return _core.make_request(request)


def get_invites(channel_id):
    endpoint = url.URL(f"/channels/{channel_id}/invites")
    request = Request(endpoint.build())
    return _core.make_request(request)


def get_pinned_messages(channel_id):
    endpoint = url.URL(f"/channels/{channel_id}/pins")
    request = Request(endpoint.build())
    return _core.make_request(request)
