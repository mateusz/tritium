from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class AutoOperationsComputer(BaseEquipment):
    """
    Auto operations computer base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.AUTO_OPERATIONS_COMPUTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.CARBON: 1,
        Resource.COPPER: 1
    }, init=False)
    pass 