from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class MassTransciever(BaseEquipment):
    """
    Mass transciever base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.MASS_TRANSCIEVER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 500,
        Resource.COPPER: 82,
        Resource.PALLADIUM: 100,
        Resource.GOLD: 40
    }, init=False)
    pass 