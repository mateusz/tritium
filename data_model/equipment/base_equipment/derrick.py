from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class Derrick(BaseEquipment):
    """
    Derrick base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.DERRICK, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 3,
        Resource.TITANIUM: 4,
        Resource.CARBON: 1
    }, init=False)
    pass 