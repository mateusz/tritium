from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.pod.pod import Pod
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict, Optional

@dataclass
class PrisonPod(Pod):
    """
    Prison pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PRISON_POD, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Cost not specified in documentation
    pass 