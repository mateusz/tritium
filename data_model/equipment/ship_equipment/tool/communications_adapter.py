from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class CommunicationsAdapter(Tool):
    """
    Communications adapter (CommsPod) tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.COMMUNICATIONS_ADAPTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.ALUMINUM: 2,
        Resource.CARBON: 1,
        Resource.COPPER: 1,
        Resource.GOLD: 1
    }, init=False)
    pass 