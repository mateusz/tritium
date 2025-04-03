from dataclasses import dataclass
from data_model.facility.facility import Facility
from data_model.personnel.researcher import Researcher
from data_model.equipment.equipment import EquipmentType, Equipment
from data_model.rank.researcher_rank import ResearcherRank
from typing import List, Optional, Dict
from dataclasses import field

@dataclass
class Research(Facility):
    """Research facility"""
    researchers: Researcher = None
    researched_equipment: List[EquipmentType] = field(default_factory=list)
    current_research: Optional[EquipmentType] = None
    current_technician_days_remaining: int = 0
    current_technician_days_total: int = 0
    
    def can_add_researchers(self, number: int) -> bool:
        """Check if the number of researchers can be added"""
        if self.researchers is None:
            return True
        if self.researchers.count + number > 250:
            return False
        return True
    
    def add_researchers(self, number: int) -> bool:
        """Add researchers to the research facility"""
        if not self.can_add_researchers(number):
            return False
        if self.researchers is None:
            self.researchers = Researcher(count=number)
        else:
            self.researchers.count += number
        return True
    
    def start_research(self, equipment_type: EquipmentType, equipment_data: Equipment) -> bool:
        """Start researching an equipment type"""
        if self.researchers is None or self.researchers.count == 0:
            return False
        
        # Check if already researched
        if equipment_type in self.researched_equipment:
            return False
            
        # Check researcher rank against required rank
        if equipment_data.required_rank and self.researchers.rank.value < equipment_data.required_rank:
            return False
            
        self.current_research = equipment_type
        self.current_technician_days_total = equipment_data.get_research_technician_days()
        self.current_technician_days_remaining = self.current_technician_days_total
        return True
    
    def advance_research(self, days: int) -> bool:
        """Advance research by a number of days"""
        if self.current_research is None or self.researchers is None:
            return False
            
        # Calculate progress based on researcher count and their rank
        rank_multiplier = 1.0
        if self.researchers.rank == ResearcherRank.DOCTOR:
            rank_multiplier = 1.5
        elif self.researchers.rank == ResearcherRank.PROFESSOR:
            rank_multiplier = 2.0
            
        daily_progress = self.researchers.count * rank_multiplier
        technician_days_completed = int(daily_progress * days)
        self.current_technician_days_remaining -= technician_days_completed
        
        # Check if research is complete
        if self.current_technician_days_remaining <= 0:
            self.researched_equipment.append(self.current_research)
            self.current_research = None
            self.current_technician_days_remaining = 0
            self.current_technician_days_total = 0
            return True
        
        return False
    
    def get_research_progress_percentage(self) -> int:
        """Get the current research progress as a percentage"""
        if self.current_research is None or self.current_technician_days_total == 0:
            return 0
        completed = self.current_technician_days_total - self.current_technician_days_remaining
        return int((completed / self.current_technician_days_total) * 100)
    
    def can_research(self, equipment_data: Equipment) -> bool:
        """Check if the equipment can be researched with current rank"""
        if self.researchers is None:
            return False
        
        if equipment_data.required_rank and self.researchers.rank.value < equipment_data.required_rank:
            return False
            
        return True
