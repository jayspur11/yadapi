import datetime

from dataclasses import dataclass
from objects.snowflake import Snowflake


@dataclass
class ThreadMember:
    id: Snowflake
    user_id: Snowflake
    join_timestamp: datetime.datetime
    flags: int
