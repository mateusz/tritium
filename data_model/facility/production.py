from dataclasses import dataclass
from data_model.facility.facility import Facility
from data_model.personnel.producer import Producer

@dataclass
class Production(Facility):
    producers: Producer = None

    def can_add_producers(self, number: int) -> bool:
        if self.producers is None:
            return True
        if self.producers.count+number>200:
            return False
        return True

    def add_producers(self, number: int) -> bool:
        if not self.can_add_producers(number):
            return False
        if self.producers is None:
            self.producers = Producer(count=number)
        else:
            self.producers.count += number
        return True