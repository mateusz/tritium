from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict, Optional

@dataclass
class SonicBlaster(Tool):
    """
    Sonic blaster tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SONIC_BLASTER, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Cost not specified in documentation
    pass 