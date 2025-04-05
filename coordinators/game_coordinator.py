from typing import Dict, Optional, Any, Type
from coordinators.coordinator import Coordinator
from coordinators.training_coordinator import TrainingCoordinator
from coordinators.research_coordinator import ResearchCoordinator
from coordinators.time_coordinator import TimeCoordinator
from data_model.game_state import GameState
from coordinators.equipment_coordinator import EquipmentCoordinator

class GameCoordinator(Coordinator):
    """
    Central coordinator that manages the entire game state and provides access to
    specific coordinator subsystems.
    """
    
    def __init__(self, game_state: GameState):
        """
        Initialize the game coordinator with all subsystem coordinators.
        
        Args:
            game_state: The game state to use, or create a new one if None
        """
        super().__init__(game_state)
        self._coordinators: Dict[str, Coordinator] = {}
        
        # Initialize coordinators
        self._initialize_coordinators()
 
    
    def _initialize_coordinators(self):
        """Initialize all coordinator subsystems."""
        
        # Create training coordinator
        self._coordinators['training'] = TrainingCoordinator(self._game_state)
        
        # Create research coordinator
        self._coordinators['research'] = ResearchCoordinator(self._game_state)
        
        # Create research coordinator
        self._coordinators['time'] = TimeCoordinator(self._game_state)

        self._coordinators['equipment'] = EquipmentCoordinator(self._game_state)
        # Add more coordinators as needed
    
    def get_coordinator(self, coordinator_name: str) -> Optional[Coordinator]:
        """
        Get a specific coordinator by name.
        
        Args:
            coordinator_name: The name of the coordinator to get
            
        Returns:
            The requested coordinator, or None if not found
        """
        return self._coordinators.get(coordinator_name)
    
    def get_training_coordinator(self) -> TrainingCoordinator:
        """
        Get the training coordinator.
        
        Returns:
            The training coordinator
        """
        return self._coordinators['training']
    
    def get_research_coordinator(self) -> ResearchCoordinator:
        """
        Get the research coordinator.
        
        Returns:
            The research coordinator
        """
        return self._coordinators['research']
    
    def get_time_coordinator(self) -> TimeCoordinator:
        """
        Get the time coordinator.
        
        Returns:
            The time coordinator
        """
        return self._coordinators['time']
    
    def get_equipment_coordinator(self) -> EquipmentCoordinator:
        """
        Get the equipment coordinator.
        
        Returns:
            The equipment coordinator
        """
        return self._coordinators['equipment']