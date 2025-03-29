from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.pod.pod import Pod
from data_model.equipment.equipment import EquipmentType

@dataclass
class CryoPod(Pod):
    """
    Cryo pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.CRYO_POD, init=False)
    pass 