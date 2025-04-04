class Controller:
    """
    Base class for all controllers.
    Controllers sit between the data model and the views, providing business logic
    and coordination between different components.
    """
    
    def __init__(self, game_state=None):
        """
        Initialize the controller with a game state.
        
        Args:
            game_state: The current game state
        """
        self._game_state = game_state 