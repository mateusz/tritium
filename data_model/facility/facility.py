from dataclasses import dataclass
from abc import ABC

@dataclass
class Facility(ABC):
    """Abstract base for all facilities, accessed in bases, cannot be stored"""
    pass 