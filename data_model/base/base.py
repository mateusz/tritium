from dataclasses import dataclass, field
from abc import ABC
from typing import List, Optional, Dict

from data_model.system.system import System
from data_model.location.location import Location
from data_model.facility.facility import Facility
from data_model.personnel.personnel import Personnel
from data_model.vehicle.vehicle import Vehicle
from data_model.equipment.equipment import Equipment, EquipmentType
from data_model.resource.resource import Resource, ResourceType

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
            
    def add_equipment(self, equipment_type: EquipmentType, amount: int = 1):
        """
        Add a specified amount of equipment to the base's storage
        
        Args:
            equipment_type: Type of equipment to add
            amount: Amount to add (default: 1)
        """
        current_amount = self.storage.get(equipment_type, 0)
        self.storage[equipment_type] = current_amount + amount
            