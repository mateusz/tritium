from dataclasses import dataclass, field
from abc import ABC
from typing import List, Optional, Dict, TYPE_CHECKING

from data_model.base.base import Base
from data_model.base.orbital_base import OrbitalBase
from data_model.base.resource_base import ResourceBase
from data_model.resource.resource import Resource
from data_model.vehicle.vehicle import Vehicle

if TYPE_CHECKING:
    from data_model.system.system import System

@dataclass
class Location(ABC):
    """Abstract base for all buildable locations"""
    name: Optional[str] = None
    system: Optional['System'] = None
    orbital_base: Optional[Base] = None
    resource_base: Optional[Base] = None
    resources: Dict[Resource, float] = field(default_factory=dict)
    vehicles: List[Vehicle] = field(default_factory=list)
    
    def set_resource_base(self, base: ResourceBase):
        """Set the base for this location"""
        self.resource_base = base
        base.location = self 

    def set_orbital_base(self, base: OrbitalBase):
        """Set the base for this location"""
        self.orbital_base = base
        base.location = self 

    def get_resource_base(self) -> Optional[ResourceBase]:
        """Get the resource base for this location"""
        return self.resource_base

    def get_orbital_base(self) -> Optional[OrbitalBase]:
        """Get the orbital base for this location"""
        return self.orbital_base

    def update(self):
        if self.orbital_base is not None:
            self.orbital_base.update()
        if self.resource_base is not None:
            self.resource_base.update()
        for vehicle in self.vehicles:
            vehicle.update()
