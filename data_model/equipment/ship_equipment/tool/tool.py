from dataclasses import dataclass
from data_model.equipment.ship_equipment.ship_equipment import ShipEquipment

@dataclass
class Tool(ShipEquipment):
    """
    Base class for all tools installable on ToolPod.
    """
    pass 