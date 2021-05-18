from dataclasses import dataclass
from objects.snowflake import Snowflake
from objects.team_member import TeamMember
from typing import List


@dataclass
class Team:
    icon: str
    id: Snowflake
    members: List[TeamMember]
    name: str
    owner_user_id: Snowflake
