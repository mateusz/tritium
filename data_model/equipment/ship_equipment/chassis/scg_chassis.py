from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.chassis.chassis import Chassis
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class SCGChassis(Chassis):
    """
    SCG chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SCG_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 250,
        Resource.TITANIUM: 600,
        Resource.ALUMINUM: 400,
        Resource.COPPER: 185,
        Resource.PALLADIUM: 100,
        Resource.PLATINUM: 100,
        Resource.SILVER: 50
    }, init=False)
    pass 