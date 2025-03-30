from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class AsteroidMiningAttachment(Tool):
    """
    Asteroid mining attachment tool.
    """
    type: EquipmentType = field(default=EquipmentType.ASTEROID_MINING_ATTACHMENT, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 6,
        Resource.TITANIUM: 70,
        Resource.ALUMINUM: 10,
        Resource.CARBON: 30,
        Resource.COPPER: 2,
        Resource.PALLADIUM: 5,
        Resource.PLATINUM: 1
    }, init=False)
    pass 