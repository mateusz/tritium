from data_model.game_state import GameState
from textual.interface import TextInterface
from textual.master_view import MasterView
from textual.bases.earth_view import EarthView
from textual.facilities.training_view import TrainingView
from textual.facilities.research_view import ResearchView
from coordinators.game_coordinator import GameCoordinator
from coordinators.initialisation_coordinator import InitialisationCoordinator
from textual.persistence import Persistence

class GameRunner:
    """Runs the game using a specific TextInterface implementation."""
    
    def __init__(self, interface: TextInterface, persistence: Persistence):
        self.interface = interface
        self.persistence = persistence
        self.game_state = GameState()

        initialisation = InitialisationCoordinator(self.game_state)
        initialisation.initialize_solar_system()

        self.game_coordinator = GameCoordinator(self.game_state)
    
    def run(self):
        """Run the game's main loop."""
        # Start with the master view
        current_view = MasterView(self.game_coordinator, self.interface)
        
        # Main game loop
        while current_view is not None:
            # Display the current view and get command
            current_view.display()
            command = self.interface.read_command(current_view.get_prompt())
            
            # Process the command and get the next view if needed
            action, next_view = current_view.process_command(command)
            
            if action == 'quit':
                # Exit the game
                self.interface.print_line("Thanks for playing!")
                return
            elif action == 'load':
                # Handle loading a game
                if self.persistence:
                    loaded_game = self.persistence.load_game()
                    if loaded_game:
                        # Update game state at the runner level
                        self.game_state = loaded_game
                        # Recreate the game coordinator with the new state
                        self.game_coordinator = GameCoordinator(self.game_state)
                        # Recreate the current view with the new coordinator
                        current_view = MasterView(self.game_coordinator, self.interface)
                        current_view.log_message("Game loaded successfully!", "success")
                    else:
                        current_view.log_message("No saved game found or failed to load", "error")
                else:
                    current_view.log_message("No persistence available to load game", "error")
            elif action == 'save':
                if self.persistence:
                    self.persistence.save_game(self.game_state)
                    current_view.log_message("Game saved successfully!", "success")
                else:
                    current_view.log_message("No persistence available to save game", "error")
            elif action == 'switch':
                if next_view == 'master_view':
                    current_view = MasterView(self.game_coordinator, self.interface)
                elif next_view == 'earth_view':
                    current_view = EarthView(self.game_coordinator, self.interface)
                elif next_view == 'training_view':
                    current_view = TrainingView(self.game_coordinator, self.interface)
                elif next_view == 'research_view':
                    current_view = ResearchView(self.game_coordinator, self.interface)
