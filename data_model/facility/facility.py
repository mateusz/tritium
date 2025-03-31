from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

from data_model.personnel.personnel import Personnel

if TYPE_CHECKING:
    from data_model.base.base import Base

@dataclass
class Facility(ABC):
    """Abstract base for all facilities, accessed in bases, cannot be stored"""
    base: Optional['Base'] = None

    def update(self):
        pass