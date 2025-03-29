from dataclasses import dataclass
from abc import ABC

@dataclass
class Location(ABC):
    """Abstract base for all buildable locations"""
    pass 