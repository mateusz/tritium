from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType

@dataclass
class Derrick(BaseEquipment):
    """
    Derrick base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.DERRICK, init=False)
    pass 