from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.pod.pod import Pod
from data_model.equipment.equipment import EquipmentType

@dataclass
class PrisonPod(Pod):
    """
    Prison pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PRISON_POD, init=False)
    pass 