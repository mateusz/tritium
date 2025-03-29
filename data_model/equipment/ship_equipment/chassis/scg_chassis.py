from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.chassis.chassis import Chassis
from data_model.equipment.equipment import EquipmentType

@dataclass
class SCGChassis(Chassis):
    """
    SCG chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SCG_CHASSIS, init=False)
    pass 