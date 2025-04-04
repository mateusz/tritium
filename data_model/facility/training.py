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
    
    def get_amount(self) -> int:
        return self.amount

    def advance_time(self):
        self.days_remaining -= 1

    def is_training_complete(self) -> bool:
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

    def can_train_marines(self, number: int) -> bool:
        # Check if already training
        if self.marines_in_training is not None:
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
        self.light_switched_on = not self.light_switched_on
        return self.light_switched_on
    
    def start_pending_trainings(self):
        if self.marines_selector > 0 and self.marines_in_training is None:
            self.train_marines(self.marines_selector)
            
        if self.researchers_selector > 0 and self.researchers_in_training is None:
            self.train_researchers(self.researchers_selector)
            
        if self.producers_selector > 0 and self.producers_in_training is None:
            self.train_producers(self.producers_selector)
    
    def advance_time(self):
        # Start any pending trainings first
        self.start_pending_trainings()

        if self.marines_in_training is not None:
            self.marines_in_training.advance_time()
        if self.researchers_in_training is not None:
            self.researchers_in_training.advance_time()
        if self.producers_in_training is not None:
            self.producers_in_training.advance_time()
            
