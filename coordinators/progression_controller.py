from typing import Set, Type, Optional
from coordinators.coordinator import Controller
from data_model.game_progression.game_progression import GameProgression
from data_model.equipment.equipment import EquipmentType


class ProgressionController(Controller):
    """
    Controller for managing game progression.
    Tracks current progression state and provides an interface for views to 
    access progression-related functionality.
    """
    
    def __init__(self, game_state=None):
        """
        Initialize the progression controller.
        
        Args:
            game_state: The current game state
        """
        super().__init__(game_state)
        self._progression_state: Optional[GameProgression] = None
        self.initialize_state()
    
    def initialize_state(self):
        """Initialize the progression state with the initial state."""
        self._progression_state = InitialState()
    
    def get_progression_state(self) -> Optional[GameProgression]:
        """Get the current progression state."""
        return self._progression_state
    
    def set_progression_state(self, state_class: Type[GameProgression]):
        """
        Set the progression state to a new state.
        
        Args:
            state_class: The class of the new state to set
        """
        self._progression_state = state_class()
    
    def get_available_technologies(self) -> Set[EquipmentType]:
        """
        Get the set of technologies available in the current progression state.
        
        Returns:
            A set of available EquipmentType values
        """
        if not self._progression_state:
            return set()
        return self._progression_state.available_technologies
    
    def is_technology_available(self, technology: EquipmentType) -> bool:
        """
        Check if a technology is available in the current progression state.
        
        Args:
            technology: The EquipmentType to check
            
        Returns:
            True if the technology is available, False otherwise
        """
        if not self._progression_state:
            return False
        return self._progression_state.is_technology_available(technology) 