from dataclasses import dataclass
from typing import Optional
from data_model.base.base import Base
from data_model.facility.production import Production
from data_model.facility.storage import Storage
from data_model.facility.shuttle_bay import ShuttleBay
from data_model.facility.spacedock import Spacedock

@dataclass
class OrbitalBase(Base):
    """Orbital base in space"""
    orbital_frames: int = 0
    REQUIRED_FRAMES = 8
    
    def __post_init__(self):
        """Initialize with OrbitalBase-specific facilities"""
        super().__post_init__()
        
        # Add Production facility
        production_facility = Production(base=self)
        self.facilities.append(production_facility)
        
        # Add Storage facility
        storage_facility = Storage(base=self)
        self.facilities.append(storage_facility)
        
        # Add ShuttleBay facility
        shuttle_bay = ShuttleBay(base=self)
        self.facilities.append(shuttle_bay)
        
        # Add Spacedock facility
        spacedock = Spacedock(base=self)
        self.facilities.append(spacedock)
    
    def add_orbital_frame(self):
        """Add an orbital factory frame to the base
        
        Returns:
            bool: True if frame was added, False if base already has max frames
        """
        if self.orbital_frames < self.REQUIRED_FRAMES:
            self.orbital_frames += 1
            return True
        return False
    
    @property
    def is_operational(self) -> bool:
        """Check if the base has enough frames to be operational
        
        Returns:
            bool: True if base has required number of frames
        """
        return self.orbital_frames >= self.REQUIRED_FRAMES
    
    def get_production_facility(self) -> Optional[Production]:
        """Get the Production facility
        
        Returns:
            Production facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Production):
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
        
    def get_spacedock(self) -> Optional[Spacedock]:
        """Get the Spacedock facility
        
        Returns:
            Spacedock facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Spacedock):
                return facility
                
        return None 