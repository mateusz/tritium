from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType

@dataclass
class SelfDestructMechanism(BaseEquipment):
    """
    Self-destruct mechanism base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SELF_DESTRUCT_MECHANISM, init=False)
    pass 