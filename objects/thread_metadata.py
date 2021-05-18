import datetime

from dataclasses import dataclass
from objects.snowflake import Snowflake


@dataclass
class ThreadMetadata:
    archived: bool
    auto_archive_duration: int
    archive_timestamp: datetime.datetime
    archiver_id: Snowflake = None
    locked: bool = None
