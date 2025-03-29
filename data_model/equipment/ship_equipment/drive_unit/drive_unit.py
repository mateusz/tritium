from dataclasses import dataclass
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment

@dataclass
class DriveUnit(ShipEquipment):
    """
    Base class for all ship drive units.
    """
    pass 