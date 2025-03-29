from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class CommunicationsAdapter(Tool):
    """
    Communications adapter (COMMSPOD) tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.COMMUNICATIONS_ADAPTER, init=False)
    pass 