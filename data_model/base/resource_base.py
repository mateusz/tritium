from dataclasses import dataclass, field
from data_model.base.base import Base
from data_model.equipment.equipment import EquipmentType
@dataclass
class ResourceBase(Base):
    """Base on a planetary surface for resource gathering"""
    deployed_derricks: int = 0

    def deploy_derrick(self):
        self.deployed_derricks += 1
        self.storage[EquipmentType.DERRICK] -= 1
