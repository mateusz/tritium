from dataclasses import dataclass, field
from typing import Optional
from data_model.base.base import Base
from data_model.equipment.equipment import EquipmentType
from data_model.facility.mining import Mining
from data_model.facility.storage import Storage
from data_model.facility.shuttle_bay import ShuttleBay

@dataclass
class ResourceBase(Base):
    """Base on a planetary surface for resource gathering"""
    deployed_derricks: int = 0
    resource_frames: int = 0
    REQUIRED_FRAMES = 2

    def __post_init__(self):
        """Initialize with ResourceBase-specific facilities"""
        super().__post_init__()
        
        # Add Mining facility
        mining_facility = Mining()
        self.facilities.append(mining_facility)
        
        # Add Storage facility
        storage_facility = Storage()
        self.facilities.append(storage_facility)
        
        # Add ShuttleBay facility
        shuttle_bay = ShuttleBay()
        self.facilities.append(shuttle_bay)

    def deploy_derrick(self):
        self.deployed_derricks += 1
        self.storage[EquipmentType.DERRICK] -= 1
    
    def add_resource_frame(self):
        """Add a resource factory frame to the base
        
        Returns:
            bool: True if frame was added, False if base already has max frames
        """
        if self.resource_frames < self.REQUIRED_FRAMES:
            self.resource_frames += 1
            return True
        return False
    
    @property
    def is_operational(self) -> bool:
        """Check if the base has enough frames to be operational
        
        Returns:
            bool: True if base has required number of frames
        """
        return self.resource_frames >= self.REQUIRED_FRAMES
        
    def get_mining_facility(self) -> Optional[Mining]:
        """Get the Mining facility
        
        Returns:
            Mining facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Mining):
                return facility
                
        return None
        
    def get_storage_facility(self) -> Optional[Storage]:
        """Get the Storage facility
        
        Returns:
            Storage facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Storage):
                return facility
                
        return None
        
    def get_shuttle_bay(self) -> Optional[ShuttleBay]:
        """Get the ShuttleBay facility
        
        Returns:
            ShuttleBay facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, ShuttleBay):
                return facility
                
        return None
