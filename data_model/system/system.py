from dataclasses import dataclass, field
from abc import ABC
from typing import List

from data_model.location.location import Location
from data_model.base.base import Base
from data_model.vehicle.vehicle import Vehicle

@dataclass
class System(ABC):
    """Abstract base class for all planetary systems."""
    locations: List[Location] = field(default_factory=list)
    bases: List[Base] = field(default_factory=list)
    vehicles: List[Vehicle] = field(default_factory=list)
    pass 