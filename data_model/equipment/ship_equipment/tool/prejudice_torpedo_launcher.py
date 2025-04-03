from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict, Optional
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class PrejudiceTorpedoLauncher(Tool):
    """
    Prejudice torpedo launcher tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PREJUDICE_TORPEDO_LAUNCHER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 96,
        Resource.ALUMINUM: 45,
        Resource.COPPER: 10
    }, init=False)
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: Optional[int] = None  # Rank not specified in documentation
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation