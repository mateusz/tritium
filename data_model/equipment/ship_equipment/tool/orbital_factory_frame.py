from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class OrbitalFactoryFrame(Tool):
    """
    Orbital factory frame tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.ORBITAL_FACTORY_FRAME, init=False)
    pass 