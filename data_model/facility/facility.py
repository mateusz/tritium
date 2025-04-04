from dataclasses import dataclass
from abc import ABC


@dataclass
class Facility(ABC):

    def advance_time(self):
        pass