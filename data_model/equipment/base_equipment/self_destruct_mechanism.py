from dataclasses import dataclass, field
from data_model.equipment.base_equipment.base_equipment import BaseEquipment
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class SelfDestructMechanism(BaseEquipment):
    """
    Self-destruct mechanism base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SELF_DESTRUCT_MECHANISM, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.ALUMINUM: 5,
        Resource.COPPER: 1,
        Resource.PALLADIUM: 1,
        Resource.PLATINUM: 2
    }, init=False)
    mass: int = field(default=9, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 