from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class SonicBlaster(Tool):
    """
    Sonic blaster tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SONIC_BLASTER, init=False)
    pass 