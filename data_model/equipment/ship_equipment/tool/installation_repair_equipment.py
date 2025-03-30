from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class InstallationRepairEquipment(Tool):
    """
    Installation repair equipment (Bandaid) tool.
    """
    type: EquipmentType = field(default=EquipmentType.INSTALLATION_REPAIR_EQUIPMENT, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 30,
        Resource.TITANIUM: 30,
        Resource.ALUMINUM: 30,
        Resource.CARBON: 30,
        Resource.COPPER: 30
    }, init=False)
    pass 