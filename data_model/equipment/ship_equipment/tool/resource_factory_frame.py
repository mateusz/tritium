from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class ResourceFactoryFrame(Tool):
    """
    Resource factory frame tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.RESOURCE_FACTORY_FRAME, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 35,
        Resource.TITANIUM: 50,
        Resource.ALUMINUM: 20,
        Resource.CARBON: 15,
        Resource.COPPER: 30,
        Resource.PALLADIUM: 25,
        Resource.PLATINUM: 10,
        Resource.SILICA: 15
    }, init=False)
    pass