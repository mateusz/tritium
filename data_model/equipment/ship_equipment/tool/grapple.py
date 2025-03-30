from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class Grapple(Tool):
    """
    Grapple tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.GRAPPLE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 2,
        Resource.TITANIUM: 2,
        Resource.COPPER: 1
    }, init=False)
    pass 