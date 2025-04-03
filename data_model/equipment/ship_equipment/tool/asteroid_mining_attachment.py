from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class AsteroidMiningAttachment(Tool):
    """
    Asteroid mining attachment tool.
    """
    type: EquipmentType = field(default=EquipmentType.ASTEROID_MINING_ATTACHMENT, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 6,
        Resource.TITANIUM: 70,
        Resource.ALUMINUM: 10,
        Resource.CARBON: 30,
        Resource.COPPER: 2,
        Resource.PLATINUM: 5,
        Resource.SILVER: 1
    }, init=False)
    mass: int = field(default=124, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 