from dataclasses import dataclass
from data_model.facility.facility import Facility
from data_model.personnel.researcher import Researcher

@dataclass
class Research(Facility):
    """Research facility"""
    researchers: Researcher = None

    def can_add_researchers(self, number: int) -> bool:
        """Check if the number of researchers can be added"""
        if self.researchers is None:
            return True
        if self.researchers.count>250:
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
