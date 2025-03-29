from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType

@dataclass
class DroneFleetControlComputer(ShipEquipment):
    """
    Drone fleet control computer ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.DRONE_FLEET_CONTROL_COMPUTER, init=False)
    pass 