from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class AutoCargoComputer(ShipEquipment):
    """
    Auto cargo computer ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.AUTO_CARGO_COMPUTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 4,
        Resource.ALUMINUM: 1,
        Resource.CARBON: 2,
        Resource.SILVER: 1
    }, init=False)
    pass 