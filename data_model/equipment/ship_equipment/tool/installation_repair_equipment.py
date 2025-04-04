from dataclasses import dataclass, field
from data_model.equipment.ship_equipment.tool.tool import Tool
from data_model.equipment.equipment import EquipmentType, RequiredLocation
from data_model.resource.resource import Resource
from typing import Dict
from data_model.rank.researcher_rank import ResearcherRank
@dataclass
class InstallationRepairEquipment(Tool):
    """
    Installation repair equipment (Bandaid) tool.
    """
    type: EquipmentType = field(default=EquipmentType.INSTALLATION_REPAIR_EQUIPMENT, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 30,
        Resource.TITANIUM: 30,
        Resource.ALUMINUM: 30,
        Resource.CARBON: 30,
        Resource.COPPER: 30
    }, init=False)
    mass: int = field(default=150, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 