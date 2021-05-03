from restapi import _core


def get_current_user():
    return _core.make_get_request("/users/@me")


def get_user(user_id):
    return _core.make_get_request(f"/users/{user_id}")


def get_current_user_guild_list(before=None, after=None, limit=None):
    return _core.make_get_request("/users/@me/guilds", query_params={
        "before": before,
        "after": after,
        "limit": str(limit)
    })


def get_current_user_connections():
    return _core.make_get_request("/users/@me/connections")
