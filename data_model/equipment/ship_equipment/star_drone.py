from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment
from data_model.equipment.equipment import EquipmentType

@dataclass
class StarDrone(ShipEquipment):
    """
    Star drone ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.STAR_DRONE, init=False)
    pass 