from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class DroneFleetControlComputer(ShipEquipment):
    """
    Drone fleet control computer ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.DRONE_FLEET_CONTROL_COMPUTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.CARBON: 1,
        Resource.COPPER: 1,
        Resource.PLATINUM: 2,
        Resource.GOLD: 1
    }, init=False)
    pass 