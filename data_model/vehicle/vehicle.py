from dataclasses import dataclass, field
from abc import ABC
from typing import List, Optional, TYPE_CHECKING

from data_model.equipment.equipment import Equipment
from data_model.personnel.personnel import Personnel
from data_model.equipment.equipment import Equipment

@dataclass
class Vehicle(ABC):
    crew: Optional['Personnel'] = None
    equipment: List[Equipment] = field(default_factory=list)

    def advance_time(self):
        pass