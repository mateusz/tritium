from dataclasses import dataclass
from enum import Enum

class CrewType(Enum):
    MARINES = "Marines"
    RESEARCHERS = "Researchers"
    PRODUCERS = "Producers"

@dataclass
class CrewMember:
    type: CrewType
    rank: str  # Will be used for promotions (e.g., Admiral, Warlord)
    experience: int = 0 