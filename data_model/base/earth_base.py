from dataclasses import dataclass, field
from typing import Optional
from data_model.base.resource_base import ResourceBase
from data_model.facility.training import Training
from data_model.facility.research import Research
from data_model.facility.production import Production
from data_model.facility.mining import Mining
from data_model.facility.storage import Storage
from data_model.facility.shuttle_bay import ShuttleBay

@dataclass
class EarthBase(ResourceBase):
    
    def __post_init__(self):
        """Initialize with all Earth-specific facilities"""
        super().__post_init__()
        
        # Add the Training facility
        training_facility = Training()
        self.facilities.append(training_facility)
        
        # Add Research facility
        research_facility = Research()
        self.facilities.append(research_facility)
        
        # Add Production facility
        production_facility = Production()
        self.facilities.append(production_facility)
        
        
    @property
    def is_operational(self) -> bool:
        """
        EarthBase is always operational
        
        Returns:
            bool: Always True for EarthBase
        """
        return True
        
    def get_training_facility(self) -> Optional[Training]:
        """Get the Training facility
        
        Returns:
            Training facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Training):
                return facility
                
        return None 
        
    def get_research_facility(self) -> Optional[Research]:
        """Get the Research facility
        
        Returns:
            Research facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Research):
                return facility
                
        return None
        
    def get_production_facility(self) -> Optional[Production]:
        """Get the Production facility
        
        Returns:
            Production facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Production):
                return facility
                
        return None
        