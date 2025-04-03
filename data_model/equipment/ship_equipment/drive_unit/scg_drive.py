from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.drive_unit.drive_unit import DriveUnit
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class SCGDrive(DriveUnit):
    """
    SCG drive unit equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SCG_DRIVE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 50,
        Resource.TITANIUM: 100,
        Resource.COPPER: 30,
        Resource.PALLADIUM: 50,
        Resource.PLATINUM: 25,
        Resource.SILVER: 10
    }, init=False)
    mass: int = field(default=265, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 