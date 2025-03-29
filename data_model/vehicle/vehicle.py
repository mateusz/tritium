from dataclasses import dataclass, field
from abc import ABC
from typing import List, Optional

from data_model.system.system import System
from data_model.location.location import Location
from data_model.base.base import Base
from data_model.personnel.personnel import Personnel
from data_model.equipment.equipment import Equipment
from data_model.grapplable.artifact import Artifact

@dataclass
class Vehicle(ABC):
    """Abstract base for all vehicles"""
    system: Optional[System] = None
    location: Optional[Location] = None
    docked_at_base: Optional[Base] = None
    crew: Optional[Personnel] = None
    equipment: List[Equipment] = field(default_factory=list)
    artifacts: List[Artifact] = field(default_factory=list) 