from dataclasses import dataclass
from data_model.facility.facility import Facility
from data_model.personnel.personnel import Researcher
@dataclass
class Research(Facility):
    """Research facility"""
    researchers: Researcher = None

    def can_add_researchers(self, number: int) -> bool:
        """Check if the number of researchers can be added"""
        if self.researchers is not None:
            return False
        if self.researchers.count>250:
            return False
        return True
    