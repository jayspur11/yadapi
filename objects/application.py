from dataclasses import dataclass
from enum import Enum
from objects.snowflake import Snowflake
from objects.team import Team
from objects.user import User
from typing import List


class ApplicationFlags(Enum):
    GATEWAY_PRESENCE = 1 << 12
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    GATEWAY_GUILD_MEMBERS = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    EMBEDDED = 1 << 17


@dataclass
class Application:
    id: Snowflake
    name: str
    icon: str
    description: str
    bot_public: bool
    bot_require_code_grant: bool
    owner: User
    summary: str
    verify_key: str
    team: Team
    flags: int  # ApplicationFlags
    rpc_origins: List[str] = None
    terms_of_service_url: str = None
    privacy_policy_url: str = None
    guild_id: Snowflake = None
    primary_sku_id: Snowflake = None
    slug: str = None
    cover_image: str = None
