from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class FuzLaser(BaseEquipment):
    type: EquipmentType = field(default=EquipmentType.FUZ_LASER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.COPPER: 5,
        Resource.PALLADIUM: 10,
        Resource.PLATINUM: 10
    }, init=False)
    mass: int = field(default=25, init=False)  # Mass is not specified in the docs, using an estimate
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 