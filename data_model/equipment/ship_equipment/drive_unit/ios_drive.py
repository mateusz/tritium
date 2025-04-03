from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.drive_unit.drive_unit import DriveUnit
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class IOSDrive(DriveUnit):
    """
    IOS drive unit equipment.
    """
    type: EquipmentType = field(default=EquipmentType.IOS_DRIVE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 30,
        Resource.TITANIUM: 50,
        Resource.COPPER: 15
    }, init=False)
    mass: int = field(default=95, init=False)
    required_rank: int = field(default=ResearcherRank.DOCTOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 