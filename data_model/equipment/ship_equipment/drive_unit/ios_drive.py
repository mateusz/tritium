from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.drive_unit.drive_unit import DriveUnit
from data_model.equipment.equipment import EquipmentType

@dataclass
class IOSDrive(DriveUnit):
    """
    IOS drive equipment.
    """
    type: EquipmentType = field(default=EquipmentType.IOS_DRIVE, init=False)
    pass 