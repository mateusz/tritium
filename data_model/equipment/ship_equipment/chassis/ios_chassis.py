from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.chassis.chassis import Chassis
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class IOSChassis(Chassis):
    """
    IOS chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.IOS_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 100,
        Resource.TITANIUM: 250,
        Resource.ALUMINUM: 175,
        Resource.CARBON: 50,
        Resource.COPPER: 75
    }, init=False)
    pass 