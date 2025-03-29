from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType

@dataclass
class Hyperspace(ShipEquipment):
    """
    Hyperspace (Hyperlight) ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.HYPERSPACE, init=False)
    pass 