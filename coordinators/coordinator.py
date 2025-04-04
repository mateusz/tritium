from data_model.base.earth_base import EarthBase
from data_model.game_state import GameState
class Coordinator:
    """
    Base class for all coordinators.
    Coordinators sit between the data model and the views, providing business logic
    and coordination between different components.
    """
    
    def __init__(self, game_state: GameState):
        """
        Initialize the coordinator with a game state.
        
        Args:
            game_state: The current game state
        """
        self._game_state = game_state 
   
    @property
    def game_state(self) -> GameState:
        """
        Get the current game state.
        
        Returns:
            The current game state
        """
        return self._game_state
        
    def get_earth_base(self) -> EarthBase:
        """
        Get the Earth base.
        """
        return self._game_state.get_earth_base()
        
        
