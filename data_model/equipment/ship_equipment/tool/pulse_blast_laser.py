from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class PulseBlastLaser(Tool):
    """
    Pulse blast laser tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PULSE_BLAST_LASER, init=False)