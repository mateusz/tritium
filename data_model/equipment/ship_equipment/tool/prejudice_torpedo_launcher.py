from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class PrejudiceTorpedoLauncher(Tool):
    """
    Prejudice torpedo launcher tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PREJUDICE_TORPEDO_LAUNCHER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 96,
        Resource.TITANIUM: 45,
        Resource.CARBON: 10
    }, init=False)
    pass 