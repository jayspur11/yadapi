from dataclasses import dataclass
from objects.snowflake import Snowflake


@dataclass
class User:
    id: Snowflake
    username: str
    discriminator: str
    avatar: str
    bot: bool = None
    system: bool = None
    mfa_enabled: bool = None
    locale: str = None
    verified: bool = None
    email: str = None
    flags: int = None
    premium_type: int = None
    public_flags: int = None
