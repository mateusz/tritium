from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class Grapple(Tool):
    """
    Grapple tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.GRAPPLE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 2,
        Resource.TITANIUM: 2,
        Resource.COPPER: 1
    }, init=False)
    mass: int = field(default=5, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)