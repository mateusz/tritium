from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Optional

from data_model.base.base import Base
from data_model.personnel.personnel import Personnel

@dataclass
class Facility(ABC):
    """Abstract base for all facilities, accessed in bases, cannot be stored"""
    base: Optional[Base] = None

    def update(self):
        pass