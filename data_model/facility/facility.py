from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

from data_model.personnel.personnel import Personnel

if TYPE_CHECKING:
    from data_model.base.base import Base

@dataclass
class Facility(ABC):

    def advance_time(self):
        pass