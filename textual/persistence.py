from abc import ABC, abstractmethod
from typing import Optional
from data_model.game_state import GameState

class Persistence(ABC):
    """Abstract base class for game state persistence."""
    
    @abstractmethod
    def save_game(self, game_state: GameState, **kwargs) -> bool:
        """
        Save the current game state.
        
        Args:
            game_state: The GameState object to save
            **kwargs: Implementation-specific arguments
            
        Returns:
            bool: True if the save was successful, False otherwise
        """
        pass
    
    @abstractmethod
    def load_game(self, **kwargs) -> Optional[GameState]:
        """
        Load a game state.
        
        Args:
            **kwargs: Implementation-specific arguments
            
        Returns:
            Optional[GameState]: The loaded GameState object or None if loading failed
        """
        pass 