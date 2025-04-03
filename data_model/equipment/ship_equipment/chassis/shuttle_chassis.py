from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.chassis.chassis import Chassis
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class ShuttleChassis(Chassis):
    """
    Shuttle chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SHUTTLE_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 20,
        Resource.TITANIUM: 50,
        Resource.ALUMINUM: 35,
        Resource.CARBON: 10,
        Resource.COPPER: 15
    }, init=False)
    mass: int = field(default=130, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)