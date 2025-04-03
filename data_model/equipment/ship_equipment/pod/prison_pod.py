from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.pod.pod import Pod
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict, Optional
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class PrisonPod(Pod):
    """
    Prison pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PRISON_POD, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Cost not specified in documentation
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: Optional[int] = None  # Rank not specified in documentation
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation
    pass 