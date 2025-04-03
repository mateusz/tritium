from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.chassis.chassis import Chassis
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class SCGChassis(Chassis):
    """
    SCG chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SCG_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 250,
        Resource.TITANIUM: 600,
        Resource.ALUMINUM: 400,
        Resource.COPPER: 185,
        Resource.PALLADIUM: 100,
        Resource.SILVER: 100,
        Resource.GOLD: 50
    }, init=False)
    mass: int = field(default=1685, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 