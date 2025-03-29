from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class ResourceFactoryFrame(Tool):
    """
    Resource factory frame tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.RESOURCE_FACTORY_FRAME, init=False)