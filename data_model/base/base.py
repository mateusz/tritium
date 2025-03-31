from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Optional, Dict

from data_model.system.system import System
from data_model.location.location import Location
from data_model.facility.facility import Facility
from data_model.personnel.personnel import Personnel
from data_model.vehicle.vehicle import Vehicle
from data_model.equipment.equipment import Equipment, EquipmentType
from data_model.resource.resource import Resource, ResourceType
from data_model.base.resource_base import ResourceBase
from data_model.base.orbital_base import OrbitalBase

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
    storage: Dict[EquipmentType, int] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize equipment dictionary with all equipment types set to zero"""
        if not self.equipment:
            for equip_type in EquipmentType:
                self.equipment[Equipment(type=equip_type)] = 0
            
        if not self.resources:
            for resource_type in Resource:
                self.resources[resource_type] = 0
            
    def has_free_personnel_slot(self) -> bool:
        """Check if there is a free personnel slot available"""
        return len(self.personnel) < 4
    
    @property
    @abstractmethod
    def is_operational(self) -> bool:
        """
        Check if the base is operational. Derived classes must implement this.
        
        Returns:
            bool: True if the base is operational
        """
        pass
            
    def add_equipment(self, equipment_type: EquipmentType, amount: int = 1):
        """
        Add a specified amount of equipment to the base's storage
        
        Args:
            equipment_type: Type of equipment to add
            amount: Amount to add (default: 1)
        """
        current_amount = self.storage.get(equipment_type, 0)
        self.storage[equipment_type] = current_amount + amount
            
    def add_personnel(self, person: Personnel) -> bool:
        """
        Add a personnel to the base
        
        Args:
            person: The personnel to add
            
        Returns:
            bool: True if the personnel was added successfully
        """
        # Only possible to add if there is a slot left - max 4
        if len(self.personnel) >= 4:
            return False
        
        person.base = self
        self.personnel.append(person)
        return True
        
    def get_resource_base(self) -> Optional[ResourceBase]:
        """Get the resource base for this location"""
        return self.location.get_resource_base()

    def get_orbital_base(self) -> Optional[OrbitalBase]:
        """Get the orbital base for this location"""
        return self.location.get_orbital_base()
    
    def add_facility(self, facility: Facility) -> bool:
        """
        Add a facility to the base and establish bidirectional relationship
        
        Args:
            facility: The facility to add
            
        Returns:
            bool: True if the facility was added successfully
        """
        facility.base = self
        self.facilities.append(facility)
        return True

    def update(self):
        for facility in self.facilities:
            facility.update()
