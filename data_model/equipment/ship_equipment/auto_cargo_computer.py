from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class AutoCargoComputer(ShipEquipment):
    """
    Auto cargo computer ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.AUTO_CARGO_COMPUTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 4,
        Resource.ALUMINUM: 1,
        Resource.CARBON: 2,
        Resource.SILVER: 1
    }, init=False)
    mass: int = field(default=8, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 