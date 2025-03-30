from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.drive_unit.drive_unit import DriveUnit
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

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
    pass 