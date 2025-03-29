from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.chassis.chassis import Chassis
from data_model.equipment.equipment import EquipmentType

@dataclass
class ShuttleChassis(Chassis):
    """
    Shuttle chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SHUTTLE_CHASSIS, init=False)
    pass 