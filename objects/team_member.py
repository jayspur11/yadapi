from dataclasses import dataclass
from enum import Enum
from typing import List
from objects.snowflake import Snowflake
from objects.user import User


class MembershipState(Enum):
    INVITED = 1
    ACCEPTED = 2


@dataclass
class TeamMember:
    membership_state: MembershipState
    permissions: List[str]
    team_id: Snowflake
    user: User
