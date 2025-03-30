from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.drive_unit.drive_unit import DriveUnit
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

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
    pass 