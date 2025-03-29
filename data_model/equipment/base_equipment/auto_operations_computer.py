from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType

@dataclass
class AutoOperationsComputer(BaseEquipment):
    """
    Auto operations computer base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.AUTO_OPERATIONS_COMPUTER, init=False)
    pass 