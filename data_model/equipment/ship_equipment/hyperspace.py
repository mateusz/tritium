from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict, Optional
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class Hyperspace(ShipEquipment):
    """
    Hyperspace (Hyperlight) ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.HYPERSPACE, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Cost not specified in documentation
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation
    pass 