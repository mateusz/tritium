from dataclasses import dataclass
from abc import ABC
from typing import Optional, TYPE_CHECKING
from enum import Enum, auto
from data_model.rank.rank import Rank

if TYPE_CHECKING:
    from data_model.facility.production import Production
    from data_model.facility.research import Research
    from data_model.vehicle.vehicle import Vehicle
    from data_model.equipment.ship_equipment.pod.cryo_pod import CryoPod
    from data_model.base.base import Base

class PersonnelType(Enum):
    RESEARCHER = auto()
    PRODUCER = auto()
    MARINE = auto()

@dataclass
class Personnel(ABC):
    rank: Optional[Rank] = None
    count: int = 0

    base: Optional['Base'] = None
    production_facility: Optional['Production'] = None
    research_facility: Optional['Research'] = None
    piloting: Optional['Vehicle'] = None 
    cryo_pod: Optional['CryoPod'] = None