from dataclasses import dataclass
from data_model.system.system import System

@dataclass
class SolarSystem(System):
    def update(self):
        for location in self.locations:
            location.update()