from dataclasses import dataclass
from data_model.system.system import System

@dataclass
class SolarSystem(System):
    def advance_time(self):
        for location in self.locations:
            location.advance_time()