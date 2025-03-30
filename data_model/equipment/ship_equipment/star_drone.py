from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class StarDrone(ShipEquipment):
    """
    Star drone ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.STAR_DRONE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 300,
        Resource.TITANIUM: 300,
        Resource.COPPER: 100,
        Resource.PALLADIUM: 90,
        Resource.PLATINUM: 80,
        Resource.SILVER: 95,
        Resource.GOLD: 50
    }, init=False)
    pass 