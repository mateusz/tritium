from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class PrejudiceTorpedoLauncher(Tool):
    """
    Prejudice torpedo launcher tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PREJUDICE_TORPEDO_LAUNCHER, init=False)
    pass 