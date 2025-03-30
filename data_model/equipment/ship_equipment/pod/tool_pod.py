from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.pod.pod import Pod
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class ToolPod(Pod):
    """
    Tool pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.TOOL_POD, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.COPPER: 1
    }, init=False)
    pass 