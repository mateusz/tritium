from dataclasses import dataclass
from abc import ABC

@dataclass
class Base(ABC):
    """Abstract base for all buildable structures"""
    pass 