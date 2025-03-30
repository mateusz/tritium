from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class OrbitalFactoryFrame(Tool):
    """
    Orbital factory frame tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.ORBITAL_FACTORY_FRAME, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 55,
        Resource.TITANIUM: 80,
        Resource.ALUMINUM: 50,
        Resource.CARBON: 25,
        Resource.COPPER: 40
    }, init=False)
    pass 