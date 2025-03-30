from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType
from data_model.resource.resource import Resource
from typing import Dict

@dataclass
class PulseBlastLaser(Tool):
    """
    Pulse blast laser tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PULSE_BLAST_LASER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.PALLADIUM: 120,
        Resource.PLATINUM: 30
    }, init=False)
    pass