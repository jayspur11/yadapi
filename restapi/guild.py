from restapi import _core


def get_guild(guild_id, with_counts=None):
    return _core.make_get_request(f"/guilds/{guild_id}",
                                  query_params={"with_counts": with_counts})


def get_preview(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/preview")


def get_channels(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/channels")


def get_member(guild_id, member_id):
    return _core.make_get_request(f"/guilds/{guild_id}/members/{member_id}")


def get_member_list(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/members")


def search_members(guild_id, query, limit=None):
    return _core.make_get_request(f"/guilds/{guild_id}/members/search",
                                  query_params={
                                      "query": query,
                                      "limit": str(limit)
                                  })


def get_ban_list(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/bans")


def get_ban(guild_id, member_id):
    return _core.make_get_request(f"/guilds/{guild_id}/bans/{member_id}")


def get_roles(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/roles")


def get_prune_count(guild_id, days=None, roles=[]]: list):
    return _core.make_get_request(f"/guilds/{guild_id}/prune", query_params={
        "days": str(days),
        "include_roles": ",".join(roles)
    })


def get_voice_regions(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/regions")


def get_invites(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/invites")


def get_integrations(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/integrations")


def get_widget_settings(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/widget")


def get_widget(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/widget.json")


def get_vanity_url(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/vanity-url")


def get_widget_image(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/widget.png")


def get_welcome_screen(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/welcome-screen")


# Emojis #######################################################################
def get_emoji_list(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/emojis")


def get_emoji(guild_id, emoji_id):
    return _core.make_get_request(f"/guilds/{guild_id}/emojis/{emoji_id}")


# Templates ####################################################################
def get_template(template_code):
    return _core.make_get_request(f"/guilds/templates/{template_code}")


def get_template_list(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/templates")


# Webhooks #####################################################################
def get_webhook_list(guild_id):
    return _core.make_get_request(f"/guilds/{guild_id}/webhooks")
