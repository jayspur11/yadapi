import datetime
import enum

from dataclasses import dataclass
from objects.overwrite import Overwrite
from objects.snowflake import Snowflake
from objects.thread_member import ThreadMember
from objects.thread_metadata import ThreadMetadata
from objects.user import User
from typing import List


class Type(enum.Enum):
    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_NEWS = 5
    GUILD_STORE = 6
    GUILD_NEWS_THREAD = 10
    GUILD_PUBLIC_THREAD = 11
    GUILD_PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13


class VideoQualityMode(enum.Enum):
    AUTO = 1
    FULL = 2


@dataclass
class Channel:
    id: Snowflake
    type: Type
    guild_id: Snowflake = None
    position: int = None
    permission_overwrites: List[Overwrite] = None
    name: str = None
    topic: str = None
    nsfw: bool = None
    last_message_id: Snowflake = None
    bitrate: int = None
    user_limit: int = None
    rate_limit_per_user: int = None
    recipients: List[User] = None
    icon: str = None
    owner_id: Snowflake = None
    application_id: Snowflake = None
    parent_id: Snowflake = None
    last_pin_timestamp: datetime.datetime = None
    rtc_region: str = None
    video_quality_mode: VideoQualityMode = VideoQualityMode.AUTO
    message_count: int = None
    member_count: int = None
    thread_metadata: ThreadMetadata = None
    member: ThreadMember = None
