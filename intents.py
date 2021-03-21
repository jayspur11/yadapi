""" Discord Gateway intents that limit incoming events.

When identifying to a gateway, you can specify `intents` which allow you to
conditionally subscribe to pre-defined groups of events.

If you do not specify a certain intent, you will not receive any of the gateway
events that are batched into that group.

NOTE: Any events not defined in an intent are "passthrough," and will always be
      sent.
NOTE: GUILD_MEMBER_UPDATE is always sent for the current user, regardless of the
      GUILD_MEMBERS intent.
"""

# GUILD_CREATE, GUILD_UPDATE, GUILD_DELETE, GUILD_ROLE_CREATE,
# GUILD_ROLE_UPDATE, GUILD_ROLE_DELETE, CHANNEL_CREATE, CHANNEL_UPDATE,
# CHANNEL_DELETE, CHANNEL_PINS_UPDATE
GUILDS = 1 << 0
# GUILD_MEMBER_ADD, GUILD_MEMBER_UPDATE, GUILD_MEMBER_REMOVE
# NOTE: This is a `privileged` intent. The application must have this intent
#       enabled in the Discord Developer Portal.
GUILD_MEMBERS = 1 << 1
# GUILD_BAN_ADD, GUILD_BAN_REMOVE
GUILD_BANS = 1 << 2
# GUILD_EMOJIS_UPDATE
GUILD_EMOJIS = 1 << 3
# GUILD_INTEGRATIONS_UPDATE
GUILD_INTEGRATIONS = 1 << 4
# WEBHOOKS_UPDATE
GUILD_WEBHOOKS = 1 << 5
# INVITE_CREATE, INVITE_DELETE
GUILD_INVITES = 1 << 6
# VOICE_STATE_UPDATE
GUILD_VOICE_STATES = 1 << 7
# PRESENCE_UPDATE
# NOTE: This is a `privileged` intent. The application must have this intent
#       enabled in the Discord Developer Portal.
GUILD_PRESENCES = 1 << 8
# MESSAGE_CREATE, MESSAGE_UPDATE, MESSAGE_DELETE, MESSAGE_DELETE_BULK
GUILD_MESSAGES = 1 << 9
# MESSAGE_REACTION_ADD, MESSAGE_REACTION_REMOVE, MESSAGE_REACTION_REMOVE_ALL,
# MESSAGE_REACTION_REMOVE_EMOJI
GUILD_MESSAGE_REACTIONS = 1 << 10
# TYPING_START
GUILD_MESSAGE_TYPING = 1 << 11
# MESSAGE_CREATE, MESSAGE_UPDATE, MESSAGE_DELETE, CHANNEL_PINS_UPDATE
DIRECT_MESSAGES = 1 << 12
# MESSAGE_REACTION_ADD, MESSAGE_REACTION_REMOVE, MESSAGE_REACTION_REMOVE_ALL,
# MESSAGE_REACTION_REMOVE_EMOJI
DIRECT_MESSAGE_REACTIONS = 1 << 13
# TYPING_START
DIRECT_MESSAGE_TYPING = 1 << 14