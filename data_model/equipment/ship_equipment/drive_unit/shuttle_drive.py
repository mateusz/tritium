from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.drive_unit.drive_unit import DriveUnit
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class ShuttleDrive(DriveUnit):
    """
    Shuttle drive unit equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SHUTTLE_DRIVE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 6,
        Resource.TITANIUM: 10,
        Resource.ALUMINUM: 4
    }, init=False)
    mass: int = field(default=20, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 