from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class Grapple(Tool):
    """
    Grapple tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.GRAPPLE, init=False)
    pass 