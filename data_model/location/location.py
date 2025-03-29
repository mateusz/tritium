from dataclasses import dataclass, field
from abc import ABC
from typing import List, Optional, Dict

from data_model.system.system import System
from data_model.base.base import Base
from data_model.resource.resource import Resource
from data_model.vehicle.vehicle import Vehicle

@dataclass
class Location(ABC):
    """Abstract base for all buildable locations"""
    system: Optional[System] = None
    base: Optional[Base] = None
    resources: Dict[Resource, float] = field(default_factory=dict)
    vehicles: List[Vehicle] = field(default_factory=list) 