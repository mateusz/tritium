from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType

@dataclass
class CompleteArtifact(Tool):
    """
    Complete artifact tool equipment. Assembled from 8 artifact pieces.
    When activated on an SCG, triggers the game's ending sequence.
    """
    type: EquipmentType = field(default=EquipmentType.COMPLETE_ARTIFACT, init=False) 