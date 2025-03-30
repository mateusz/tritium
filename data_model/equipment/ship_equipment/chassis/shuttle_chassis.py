from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.chassis.chassis import Chassis
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class ShuttleChassis(Chassis):
    """
    Shuttle chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SHUTTLE_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 20,
        Resource.TITANIUM: 50,
        Resource.ALUMINUM: 35,
        Resource.CARBON: 10,
        Resource.COPPER: 15
    }, init=False)
    pass 