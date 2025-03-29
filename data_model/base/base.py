from dataclasses import dataclass, field
from abc import ABC
from typing import List, Optional, Dict

from data_model.system.system import System
from data_model.location.location import Location
from data_model.facility.facility import Facility
from data_model.personnel.personnel import Personnel
from data_model.vehicle.vehicle import Vehicle
from data_model.equipment.equipment import Equipment
from data_model.resource.resource import Resource

@dataclass
class Base(ABC):
    """Abstract base for all buildable structures"""
    system: Optional[System] = None
    location: Optional[Location] = None
    facilities: List[Facility] = field(default_factory=list)
    personnel: List[Personnel] = field(default_factory=list)
    shuttle_bay_vehicle: Optional[Vehicle] = None
    spacedock_vehicle: Optional[Vehicle] = None
    equipment: Dict[Equipment, int] = field(default_factory=dict)
    resources: Dict[Resource, int] = field(default_factory=dict)
    pass 