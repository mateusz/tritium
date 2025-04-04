from textual.interface import TextInterface
from textual.master_view import MasterView
from textual.bases.earth_view import EarthView
from textual.facilities.training_view import TrainingView
from textual.facilities.research_view import ResearchView
from coordinators.game_coordinator import GameCoordinator

class GameRunner:
    """Runs the game using a specific TextInterface implementation."""
    
    def __init__(self, interface: TextInterface = None):
        """Initialize the game runner with an interface.
        
        Args:
            interface: The TextInterface implementation to use. Defaults to CliInterface.
        """
        if interface is None:
            self.interface = CliInterface()
        else:
            self.interface = interface
            
        self.game_coordinator = GameCoordinator()
    
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
            elif action == 'switch':
                if next_view == 'master_view':
                    current_view = MasterView(self.game_coordinator, self.interface)
                elif next_view == 'earth_view':
                    current_view = EarthView(self.game_coordinator, self.interface)
                elif next_view == 'training_view':
                    current_view = TrainingView(self.game_coordinator, self.interface)
                elif next_view == 'research_view':
                    current_view = ResearchView(self.game_coordinator, self.interface)

if __name__ == "__main__":
    # Create a game runner with the default CLI interface
    runner = GameRunner()
    runner.run() 