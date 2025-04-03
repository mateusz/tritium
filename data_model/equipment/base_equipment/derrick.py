from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
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
    mass: int = field(default=8, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 