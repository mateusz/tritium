from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class AsteroidMiningAttachment(Tool):
    """
    Asteroid mining attachment tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.ASTEROID_MINING_ATTACHMENT, init=False)
    pass 