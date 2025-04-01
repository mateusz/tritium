from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, TYPE_CHECKING
from enum import Enum, auto
from data_model.personnel.researcher import Researcher
from data_model.personnel.producer import Producer
from data_model.personnel.marine import Marine
from data_model.personnel.personnel import PersonnelType
from data_model.facility.facility import Facility

if TYPE_CHECKING:
    from data_model.base.earth_base import EarthBase

@dataclass
class TrainingBatch:
    personnel_type: PersonnelType
    amount: int
    days_remaining: int
    
    def update(self) -> bool:
        self.days_remaining -= 1
        return self.days_remaining <= 0

@dataclass
class Training(Facility):
    available_population: int = 6000  # Initial population available for recruiting
    marines_in_training: TrainingBatch = None
    researchers_in_training: TrainingBatch = None
    producers_in_training: TrainingBatch = None
    marines_selector: int = 0
    researchers_selector: int = 0
    producers_selector: int = 0
    light_switched_on: bool = False

    def get_earth_base(self) -> Optional['EarthBase']:
        return self.base
    
    def can_train_marines(self, number: int) -> bool:
        # Check if already training
        if self.marines_in_training is not None:
            return False
            
        if self.get_earth_base() is None:
            return False
            
        if not self.get_earth_base().has_free_personnel_slot():
            return False

        if number > 41 or number<0:
            return False

        if self.available_population - number < 0:
            return False

        return True
    
    def can_train_researchers(self, number: int) -> bool:
        # Check if already training
        if self.researchers_in_training is not None:
            return False
            
        if self.base is None:
            return False
            
        # Get the research facility and check if it has space
        research_facility = self.get_earth_base().get_research_facility()
        if research_facility is None:
            return False
            
        if not research_facility.can_add_researchers(number):
            return False

        # Maximum 100 researchers per batch as per specification
        if number > 100 or number<0:
            return False
        
        if self.available_population - number < 0:
            return False

        return True
    
    def can_train_producers(self, number: int) -> bool:
        # Check if already training
        if self.producers_in_training is not None:
            return False
            
        # Check if base exists
        if self.base is None:
            return False
            
        # Get the production facility and check if it has space
        production_facility = self.get_earth_base().get_production_facility()
        if production_facility is None:
            return False
            
        if not production_facility.can_add_producers(number):
            return False
            
        # Maximum 100 producers per batch as per specification
        if number > 100 or number<0:
            return False

        if self.available_population - number < 0:
            return False

        return True
    
    def train_marines(self, number: int) -> bool:
        if not self.can_train_marines(number):
            return False
        self.marines_in_training = TrainingBatch(personnel_type=PersonnelType.MARINE, amount=number, days_remaining=7)
        self.available_population -= number
        return True
    
    def train_researchers(self, number: int) -> bool:
        if not self.can_train_researchers(number):
            return False
        self.researchers_in_training = TrainingBatch(personnel_type=PersonnelType.RESEARCHER, amount=number, days_remaining=14)
        self.available_population -= number
        return True
    
    def train_producers(self, number: int) -> bool:
        if not self.can_train_producers(number):
            return False
        self.producers_in_training = TrainingBatch(personnel_type=PersonnelType.PRODUCER, amount=number, days_remaining=7)
        self.available_population -= number
        return True

    def marines_selector_up(self) -> bool:
        if self.can_train_marines(self.marines_selector + 1):
            self.marines_selector += 1
            return True
        return False

    def marines_selector_down(self) -> bool:
        if self.can_train_marines(self.marines_selector - 1):
            self.marines_selector -= 1
            return True
        return False
    
    def researchers_selector_up(self) -> bool:
        if self.can_train_researchers(self.researchers_selector + 1):
            self.researchers_selector += 1
            return True
        return False
    
    def researchers_selector_down(self) -> bool:
        if self.can_train_researchers(self.researchers_selector - 1):
            self.researchers_selector -= 1
            return True
        return False
    
    def producers_selector_up(self) -> bool:
        if self.can_train_producers(self.producers_selector + 1):
            self.producers_selector += 1
            return True
        return False
    
    def producers_selector_down(self) -> bool:
        if self.can_train_producers(self.producers_selector - 1):
            self.producers_selector -= 1
            return True
        return False
        
    
    def toggle_light_switch(self) -> bool:
        """
        Toggle the light switch in the training room.
        This is purely a cosmetic feature.
        
        Returns:
            bool: The new state of the light switch (True = on, False = off)
        """
        self.light_switched_on = not self.light_switched_on
        return self.light_switched_on
    
    def start_pending_trainings(self):
        """Start any pending trainings based on current selector values"""
        # Check if there are any pending trainings to start
        if self.marines_selector > 0 and self.marines_in_training is None:
            self.train_marines(self.marines_selector)
            
        if self.researchers_selector > 0 and self.researchers_in_training is None:
            self.train_researchers(self.researchers_selector)
            
        if self.producers_selector > 0 and self.producers_in_training is None:
            self.train_producers(self.producers_selector)
    
    def update(self):
        earth_base = self.get_earth_base()
        if earth_base is None:
            return
        
        # Start any pending trainings first
        self.start_pending_trainings()
            
        # Update marines training
        if self.marines_in_training is not None:
            if self.marines_in_training.update():
                # Marines training complete - create a new marine squad
                if earth_base.add_personnel(Marine(count=self.marines_in_training.amount)):
                    self.marines_in_training = None
                    self.marines_selector = 0
        
        # Update researchers training
        if self.researchers_in_training is not None:
            if self.researchers_in_training.update():
                # Researchers training complete - add to research facility
                research_facility = earth_base.get_research_facility()
                if research_facility is not None:
                    if research_facility.add_researchers(self.researchers_in_training.amount):
                        self.researchers_in_training = None
                        self.researchers_selector = 0
        
        # Update producers training
        if self.producers_in_training is not None:
            if self.producers_in_training.update():
                # Producers training complete - add to production facility
                production_facility = earth_base.get_production_facility()
                if production_facility is not None:
                    if production_facility.add_producers(self.producers_in_training.amount):
                        self.producers_in_training = None
                        self.producers_selector = 0 
    
    def for_view(self) -> Dict[str, Any]:
        return {
            "light_switched_on": self.light_switched_on,
            "marines_selector": self.marines_selector,
            "researchers_selector": self.researchers_selector,
            "producers_selector": self.producers_selector,
            "marines_in_training": bool(self.marines_in_training),
            "researchers_in_training": bool(self.researchers_in_training),
            "producers_in_training": bool(self.producers_in_training),
        }