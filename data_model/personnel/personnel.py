from dataclasses import dataclass
from abc import ABC
from typing import Optional, TYPE_CHECKING
from enum import Enum, auto
from data_model.rank.rank import Rank

class PersonnelType(Enum):
    RESEARCHER = auto()
    PRODUCER = auto()
    MARINE = auto()

@dataclass
class Personnel(ABC):
    rank: Optional[Rank] = None
    count: int = 0