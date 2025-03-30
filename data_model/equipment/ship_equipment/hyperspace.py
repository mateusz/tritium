from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict, Optional

@dataclass
class Hyperspace(ShipEquipment):
    """
    Hyperspace (Hyperlight) ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.HYPERSPACE, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Cost not specified in documentation
    pass 