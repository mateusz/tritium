from dataclasses import dataclass
from typing import Optional
from data_model.base.resource_base import ResourceBase

@dataclass
class MoonBase(ResourceBase):
    """Base specific to Moon - uses bandaid device instead of resource frames"""
    bandaid_used: bool = False
    
    def __post_init__(self):
        """Initialize MoonBase facilities"""
        super().__post_init__()
        # Override ResourceBase frame count to ensure is_operational checks the bandaid status
        self.resource_frames = 0
    
    def use_bandaid_device(self) -> bool:
        """Use the Installation Repair Equipment (Bandaid) to make the base operational
        
        Returns:
            bool: True if bandaid was successfully used, False if already used
        """
        if not self.bandaid_used:
            self.bandaid_used = True
            return True
        return False
    
    @property
    def is_operational(self) -> bool:
        """Check if the bandaid device has been used to make the base operational
        
        Returns:
            bool: True if bandaid device has been used
        """
        return self.bandaid_used
    
    def add_resource_frame(self) -> bool:
        """Override the ResourceBase add_resource_frame method
        
        Returns:
            bool: Always False as MoonBase doesn't use resource frames
        """
        # MoonBase doesn't use resource frames, it uses the bandaid device
        return False 