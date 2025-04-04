from abc import ABC, abstractmethod
from typing import Set
from data_model.equipment.equipment import EquipmentType


class GameProgression(ABC):
    """
    Abstract base class for game progression states.
    Manages the state machine for game progression and tracks available technologies.
    """
    
    def __init__(self):
        """Initialize the game progression state."""
        self._available_technologies: Set[EquipmentType] = set()
        self._initialize_technologies()
    
    @abstractmethod
    def _initialize_technologies(self) -> None:
        """
        Initialize the set of available technologies for this progression state.
        Must be implemented by concrete subclasses.
        """
        pass
    
    @property
    def available_technologies(self) -> Set[EquipmentType]:
        """Get the set of currently available technologies."""
        return self._available_technologies
    
    def is_technology_available(self, technology: EquipmentType) -> bool:
        """Check if a specific technology is available in the current progression state."""
        return technology in self._available_technologies 