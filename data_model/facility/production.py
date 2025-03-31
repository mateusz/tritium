from dataclasses import dataclass
from data_model.facility.facility import Facility
from data_model.personnel.personnel import Personnel

@dataclass
class Production(Facility):
    producers: Personnel = None

    def can_add_producers(self, number: int) -> bool:
        if self.producers is None:
            return True
        if self.producers.count+number>200:
            return False
        return True
    