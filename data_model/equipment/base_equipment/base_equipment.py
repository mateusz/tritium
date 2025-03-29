from dataclasses import dataclass
from data_model.equipment.equipment import Equipment

@dataclass
class BaseEquipment(Equipment):
    """
    Equipment installable on bases.
    """
    pass 