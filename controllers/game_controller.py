from typing import Dict, Optional, Any, Type
from controllers.controller import Controller
from controllers.training_controller import TrainingController
from controllers.research_controller import ResearchController
from data_model.game_state import GameState


class GameController(Controller):
    """
    Central controller that manages the entire game state and provides access to
    specific controller subsystems.
    """
    
    def __init__(self, game_state: Optional[GameState] = None):
        """
        Initialize the game controller with all subsystem controllers.
        
        Args:
            game_state: The game state to use, or create a new one if None
        """
        self._game_state = game_state or GameState()
        self._controllers: Dict[str, Controller] = {}
        
        # Initialize controllers
        self._initialize_controllers()
    
    def _initialize_controllers(self):
        """Initialize all controller subsystems."""
        
        # Create training controller
        self._controllers['training'] = TrainingController(self._game_state)
        
        # Create research controller
        self._controllers['research'] = ResearchController(self._game_state)
        
        # Add more controllers as needed
    
    def get_controller(self, controller_name: str) -> Optional[Controller]:
        """
        Get a specific controller by name.
        
        Args:
            controller_name: The name of the controller to get
            
        Returns:
            The requested controller, or None if not found
        """
        return self._controllers.get(controller_name)
    
    def get_training_controller(self) -> TrainingController:
        """
        Get the training controller.
        
        Returns:
            The training controller
        """
        return self._controllers['training']
    
    def get_research_controller(self) -> ResearchController:
        """
        Get the research controller.
        
        Returns:
            The research controller
        """
        return self._controllers['research']
    
    def get_game_time(self) -> str:
        """
        Get the current game time as a formatted string.
        
        Returns:
            The current game time string
        """
        return self._game_state.game_time
    
    def advance_time(self) -> None:
        """
        Advance the game state by one time unit.
        This updates all game state components.
        """
        self._game_state.update()
    
    def get_earth_base(self):
        """
        Get the Earth base from the game state.
        
        Returns:
            The Earth base object
        """
        return self._game_state.get_earth_base()
    
    def create_master_view(self):
        """
        Create a new MasterView instance.
        
        Returns:
            A new MasterView instance
        """
        from cli.master_view import MasterView
        return MasterView(self)
    
    def create_earth_view(self):
        """
        Create a new Earth view instance.
        
        Returns:
            A new Earth view instance
        """
        from cli.bases.earth_view import EarthView
        return EarthView(self)
    
    def create_research_view(self):
        """
        Create a new Research view instance.
        
        Returns:
            A new ResearchView instance
        """
        from cli.facilities.research_view import ResearchView
        return ResearchView(self)
    
    def create_training_view(self):
        """
        Create a new Training view instance.
        
        Returns:
            A new TrainingView instance
        """
        from cli.facilities.training_view import TrainingView
        return TrainingView(self) 