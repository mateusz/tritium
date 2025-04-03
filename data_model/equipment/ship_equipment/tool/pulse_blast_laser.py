from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict, Optional
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class PulseBlastLaser(Tool):
    """
    Pulse blast laser tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PULSE_BLAST_LASER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.PALLADIUM: 120,
        Resource.PLATINUM: 30
    }, init=False)
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: Optional[int] = None  # Rank not specified in documentation
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation
    pass