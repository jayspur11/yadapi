from dataclasses import dataclass


@dataclass
class Overwrite:
    id: str
    type: int
    allow: str
    deny: str
