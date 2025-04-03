from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.pod.pod import Pod
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class ResourcePod(Pod):
    """
    Resource pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.RESOURCE_POD, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.COPPER: 1
    }, init=False)
    mass: int = field(default=4, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 