from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
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
    mass: int = field(default=5, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 