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
    
    def add_location(self, location: Location):
        """Add a location to this system and set up bidirectional references.
        
        Args:
            location: The location to add to this system
        """
        location.system = self
        self.locations.append(location)
