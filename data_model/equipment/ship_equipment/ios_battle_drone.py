from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class IOSBattleDrone(ShipEquipment):
    """
    IOS battle drone ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.IOS_BATTLE_DRONE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 120,
        Resource.TITANIUM: 120,
        Resource.ALUMINUM: 120,
        Resource.CARBON: 15,
        Resource.COPPER: 55,
        Resource.PALLADIUM: 30,
        Resource.PLATINUM: 30
    }, init=False)
    mass: int = field(default=490, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 