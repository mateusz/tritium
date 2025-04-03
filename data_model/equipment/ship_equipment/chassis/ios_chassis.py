from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.chassis.chassis import Chassis
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class IOSChassis(Chassis):
    """
    IOS chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.IOS_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 100,
        Resource.TITANIUM: 250,
        Resource.ALUMINUM: 175,
        Resource.CARBON: 50,
        Resource.COPPER: 75
    }, init=False)
    mass: int = field(default=650, init=False)
    required_rank: int = field(default=ResearcherRank.DOCTOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 