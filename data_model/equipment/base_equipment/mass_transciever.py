from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
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
    mass: int = field(default=722, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 