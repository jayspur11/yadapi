from urllib.parse import quote
from urllib.request import Request
from restapi import _core
from restapi import url


def get_channel(channel_id):
    endpoint = url.URL(f"/channels/{channel_id}")
    return _core.make_get_request(endpoint)


def get_messages(channel_id,
                 limit=None,
                 around_message=None,
                 before_message=None,
                 after_message=None):
    endpoint = url.URL(f"/channels/{channel_id}/messages")
    endpoint.add_query_params({
        "limit": str(limit),
        "around": around_message,
        "before": before_message,
        "after": after_message
    })

    return _core.make_get_request(endpoint)


def get_message(channel_id, message_id):
    endpoint = url.URL(f"/channels/{channel_id}/messages/{message_id}")
    return _core.make_get_request(endpoint)


def get_reactions(channel_id, message_id, emoji, after=None, limit=None):
    emoji_urlsafe = quote(emoji, safe="")
    endpoint = url.URL(f"/channels/{channel_id}/messages/{message_id}/reactions"
                       f"/{emoji_urlsafe}")
    endpoint.add_query_params({
        "after": after,
        "limit": str(limit)
    })
    return _core.make_get_request(endpoint)


def get_invites(channel_id):
    endpoint = url.URL(f"/channels/{channel_id}/invites")
    return _core.make_get_request(endpoint)


def get_pinned_messages(channel_id):
    endpoint = url.URL(f"/channels/{channel_id}/pins")
    return _core.make_get_request(endpoint)


def get_thread_members(channel_id):
    endpoint = url.URL(f"/channels/{channel_id}/threads-members")
    return _core.make_get_request(endpoint)


def get_active_threads(channel_id):
    endpoint = url.URL(f"/channels/{channel_id}/threads/active")
    return _core.make_get_request(endpoint)


def get_public_archived_threads(channel_id, before=None, limit=None):
    endpoint = url.URL(f"/channels/{channel_id}/threads/archived/public")
    endpoint.add_query_params({
        "before": before,
        "limit": str(limit)
    })
    return _core.make_get_request(endpoint)


def get_private_archived_threads(channel_id, before=None, limit=None):
    endpoint = url.URL(f"/channels/{channel_id}/threads/archived/private")
    endpoint.add_query_params({
        "before": before,
        "limit": str(limit)
    })
    return _core.make_get_request(endpoint)


def get_joined_private_archived_threads(channel_id, before=None, limit=None):
    endpoint = url.URL(f"/channels/{channel_id}/users/@me/threads/archived/"
                       f"private")
    endpoint.add_query_params({
        "before": before,
        "limit": str(limit)
    })
    return _core.make_get_request(endpoint)
