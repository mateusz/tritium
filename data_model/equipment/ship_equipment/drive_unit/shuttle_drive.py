from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.drive_unit.drive_unit import DriveUnit
from data_model.equipment.equipment import EquipmentType

@dataclass
class ShuttleDrive(DriveUnit):
    """
    Shuttle drive equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SHUTTLE_DRIVE, init=False)
    pass 