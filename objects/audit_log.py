from _typeshed import StrPath
import enum
import json
import objects

from dataclasses import dataclass
from typing import List, Union


class Keys(enum.Enum):
    WEBHOOKS = "webhooks"
    USERS = "users"
    AUDIT_LOG_ENTRIES = "audit_log_entries"
    INTEGRATIONS = "integrations"


class AuditLogEvent(enum.Enum):
    GUILD_UPDATE = 1
    CHANNEL_CREATE = 10
    CHANNEL_UPDATE = 11
    CHANNEL_DELETE = 12
    CHANNEL_OVERWRITE_CREATE = 13
    CHANNEL_OVERWRITE_UPDATE = 14
    CHANNEL_OVERWRITE_DELETE = 15
    MEMBER_KICK = 20
    MEMBER_PRUNE = 21
    MEMBER_BAN_ADD = 22
    MEMBER_BAN_REMOVE = 23
    MEMBER_UPDATE = 24
    MEMBER_ROLE_UPDATE = 25
    MEMBER_MOVE = 26
    MEMBER_DISCONNECT = 27
    BOT_ADD = 28
    ROLE_CREATE = 30
    ROLE_UPDATE = 31
    ROLE_DELETE = 32
    INVITE_CREATE = 40
    INVITE_UPDATE = 41
    INVITE_DELETE = 42
    WEBHOOK_CREATE = 50
    WEBHOOK_UPDATE = 51
    WEBHOOK_DELETE = 52
    EMOJI_CREATE = 60
    EMOJI_UPDATE = 61
    EMOJI_DELETE = 62
    MESSAGE_DELETE = 72
    MESSAGE_BULK_DELETE = 73
    MESSAGE_PIN = 74
    MESSAGE_UNPIN = 75
    INTEGRATION_CREATE = 80
    INTEGRATION_UPDATE = 81
    INTEGRATION_DELETE = 82


@dataclass
class _BaseAuditLogChangeKey:
    id: objects.snowflake.Snowflake
    type: Union(str, objects.channel.Type)


@dataclass
class GuildChangeKey(_BaseAuditLogChangeKey):
    name: str
    description: str
    icon_hash: str
    splash_hash: str
    discovery_splash_hash: str
    banner_hash: str
    owner_id: objects.snowflake.Snowflake
    region: str
    preferred_locale: str
    afk_channel_id: objects.snowflake.Snowflake
    afk_timeout: int
    rules_channel_id: objects.snowflake.Snowflake
    public_updates_channel_id: objects.snowflake.Snowflake
    mfa_level: int
    verification_level: int
    explicit_content_filter: int
    default_message_notifications: int
    vanity_url_code: str
    add: List[objects.permissions.Role]
    remove: List[objects.permissions.Role]
    prune_delete_days: int
    widget_enabled: bool
    widget_channel_id: objects.snowflake.Snowflake
    system_channel_id: objects.snowflake.Snowflake


@dataclass
class ChannelChangeKey(_BaseAuditLogChangeKey):
    position: int
    topic: str
    bitrate: int
    permission_overwrites: List[objects.overwrite.Overwrite]
    nsfw: bool
    application_id: objects.snowflake.Snowflake
    rate_limit_per_user: int


@dataclass
class RoleChangeKey(_BaseAuditLogChangeKey):
    permissions: str
    color: int
    hoist: bool
    mentionable: bool
    allow: str
    deny: str


@dataclass
class InviteChangeKey(_BaseAuditLogChangeKey):
    code: str
    channel_id: objects.snowflake.Snowflake
    inviter_id: objects.snowflake.Snowflake
    max_uses: int
    uses: int
    max_age: int
    temporary: bool


@dataclass
class UserChangeKey(_BaseAuditLogChangeKey):
    deaf: bool
    mute: bool
    nick: str
    avatar_hash: str


@dataclass
class IntegrationChangeKey(_BaseAuditLogChangeKey):
    enable_emoticons: bool
    expire_behavior: int
    expire_grace_period: int


@dataclass
class VoiceChannelChangeKey(ChannelChangeKey):
    user_limit: int


@dataclass
class AuditLogChange:
    value_type = Union[GuildChangeKey, ChannelChangeKey, RoleChangeKey,
                       InviteChangeKey, UserChangeKey, IntegrationChangeKey,
                       VoiceChannelChangeKey]

    key: str
    new_value: value_type = None
    old_value: value_type = None


@dataclass
class AuditEntryInfo:  # TODO: break this up -- different fields for different events
    delete_member_days: str
    members_removed: str
    channel_id: objects.snowflake.Snowflake
    message_id: objects.snowflake.Snowflake
    count: str
    id: objects.snowflake.Snowflake
    type: str
    role_name: str


@dataclass
class AuditLogEntry:
    target_id: str
    user_id: objects.snowflake.Snowflake
    id: objects.snowflake.Snowflake
    action_type: AuditLogEvent
    changes: AuditLogChange = None
    options: AuditEntryInfo = None
    reason: str = None


@dataclass
class AuditLog:
    webhooks: List[objects.webhook.Webhook]
    users: List[objects.user.User]
    audit_log_entries: List[AuditLogEntry]
    integrations: List[objects.guild.Integration]


# class AuditLog:
#     @classmethod
#     def receive(cls, audit_log_string):
#         audit_log = json.loads(audit_log_string)
#         # TODO process these into their respective objects -- should be arrays!
#         return cls(audit_log.get(Keys.WEBHOOKS), audit_log.get(Keys.USERS),
#                    audit_log.get(Keys.AUDIT_LOG_ENTRIES),
#                    audit_log.get(Keys.INTEGRATIONS))

#     def __init__(self, webhooks, users, audit_log_entries, integrations):
#         self.webhooks = webhooks
#         self.users = users
#         self.audit_log_entries = audit_log_entries
#         self.integrations = integrations
