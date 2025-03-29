from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class InstallationRepairEquipment(Tool):
    """
    Installation repair equipment (Bandaid).
    """
    type: EquipmentType = field(default=EquipmentType.INSTALLATION_REPAIR_EQUIPMENT, init=False)
    pass 