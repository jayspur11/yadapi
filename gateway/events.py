""" Discord Gateway DISPATCH event names.

Payloads with the DISPATCH opcode carry the name of the dispatched event.
"""

# "Passthrough" events (always sent)
APPLICATION_COMMAND_CREATE = "APPLICATION_COMMAND_CREATE"
APPLICATION_COMMAND_DELETE = "APPLICATION_COMMAND_DELETE"
APPLICATION_COMMAND_UPDATE = "APPLICATION_COMMAND_UPDATE"
INTERACTION_CREATE = "INTERACTION_CREATE"
INVITE_CREATE = "INVITE_CREATE"
INVITE_DELETE = "INVITE_DELETE"
GUILD_MEMBERS_CHUNK = "GUILD_MEMBERS_CHUNK"
READY = "READY"
RESUMED = "RESUMED"
USER_UPDATE = "USER_UPDATE"
VOICE_SERVER_UPDATE = "VOICE_SERVER_UPDATE"
VOICE_STATE_UPDATE = "VOICE_STATE_UPDATE"
WEBHOOKS_UPDATE = "WEBHOOKS_UPDATE"

# GUILDS intent
CHANNEL_CREATE = "CHANNEL_CREATE"
CHANNEL_DELETE = "CHANNEL_DELETE"
CHANNEL_PINS_UPDATE = "CHANNEL_PINS_UPDATE"
CHANNEL_UPDATE = "CHANNEL_UPDATE"
GUILD_CREATE = "GUILD_CREATE"
GUILD_DELETE = "GUILD_DELETE"
GUILD_UPDATE = "GUILD_UPDATE"
GUILD_ROLE_CREATE = "GUILD_ROLE_CREATE"
GUILD_ROLE_DELETE = "GUILD_ROLE_DELETE"
GUILD_ROLE_UPDATE = "GUILD_ROLE_UPDATE"

# GUILD_BANS intent
GUILD_BAN_ADD = "GUILD_BAN_ADD"
GUILD_BAN_REMOVE = "GUILD_BAN_REMOVE"

# GUILD_EMOJIS intent
GUILD_EMOJIS_UPDATE = "GUILD_EMOJIS_UPDATE"

# GUILD_INTEGRATIONS intent
GUILD_INTEGRATIONS_UPDATE = "GUILD_INTEGRATIONS_UPDATE"

# GUILD_MEMBERS intent ** Privileged
GUILD_MEMBER_ADD = "GUILD_MEMBER_ADD"
GUILD_MEMBER_REMOVE = "GUILD_MEMBER_REMOVE"
GUILD_MEMBER_UPDATE = "GUILD_MEMBER_UPDATE"

# DIRECT_MESSAGES intent
# GUILD_MESSAGES intent
MESSAGE_CREATE = "MESSAGE_CREATE"
MESSAGE_UPDATE = "MESSAGE_UPDATE"
MESSAGE_DELETE = "MESSAGE_DELETE"
MESSAGE_DELETE_BULK = "MESSAGE_DELETE_BULK"

# DIRECT_MESSAGE_REACTIONS intent
# GUILD_MESSAGE_REACTIONS intent
MESSAGE_REACTION_ADD = "MESSAGE_REACTION_ADD"
MESSAGE_REACTION_REMOVE = "MESSAGE_REACTION_REMOVE"
MESSAGE_REACTION_REMOVE_ALL = "MESSAGE_REACTION_REMOVE_ALL"
MESSAGE_REACTION_REMOVE_EMOJI = "MESSAGE_REACTION_REMOVE_EMOJI"

# GUILD_PRESENCES intent ** Privileged
PRESENCE_UPDATE = "PRESENCE_UPDATE"

# DIRECT_MESSAGE_TYPING intent
# GUILD_MESSAGE_TYPING intent
TYPING_START = "TYPING_START"
