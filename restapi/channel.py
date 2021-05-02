from urllib.parse import quote
from restapi import _core


def get_channel(channel_id):
    return _core.make_get_request(f"/channels/{channel_id}")


def get_messages(channel_id,
                 limit=None,
                 around_message=None,
                 before_message=None,
                 after_message=None):
    return _core.make_get_request(f"/channels/{channel_id}/messages",
                                  query_params={
                                      "limit": str(limit),
                                      "around": around_message,
                                      "before": before_message,
                                      "after": after_message
                                  })


def get_message(channel_id, message_id):
    return _core.make_get_request(
        f"/channels/{channel_id}/messages/{message_id}")


def get_reactions(channel_id, message_id, emoji, after=None, limit=None):
    emoji_urlsafe = quote(emoji, safe="")
    return _core.make_get_request(
        f"/channels/{channel_id}/messages/{message_id}/"
        f"reactions/{emoji_urlsafe}",
        query_params={
            "after": after,
            "limit": str(limit)
        })


def get_invites(channel_id):
    return _core.make_get_request(f"/channels/{channel_id}/invites")


def get_pinned_messages(channel_id):
    return _core.make_get_request(f"/channels/{channel_id}/pins")


def get_thread_members(channel_id):
    return _core.make_get_request(f"/channels/{channel_id}/threads-members")


def get_active_threads(channel_id):
    return _core.make_get_request(f"/channels/{channel_id}/threads/active")


def get_public_archived_threads(channel_id, before=None, limit=None):
    return _core.make_get_request(
        f"/channels/{channel_id}/threads/archived/public",
        query_params={
            "before": before,
            "limit": str(limit)
        })


def get_private_archived_threads(channel_id, before=None, limit=None):
    return _core.make_get_request(
        f"/channels/{channel_id}/threads/archived/private",
        query_params={
            "before": before,
            "limit": str(limit)
        })


def get_joined_private_archived_threads(channel_id, before=None, limit=None):
    return _core.make_get_request(
        f"/channels/{channel_id}/users/@me/threads/archived/private",
        query_params={
            "before": before,
            "limit": str(limit)
        })
