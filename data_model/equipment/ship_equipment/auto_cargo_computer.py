from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType

@dataclass
class AutoCargoComputer(ShipEquipment):
    """
    Auto cargo computer ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.AUTO_CARGO_COMPUTER, init=False)
    pass 