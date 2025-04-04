from textual.interface import TextInterface
from textual.master_view import MasterView
from textual.bases.earth_view import EarthView
from textual.facilities.training_view import TrainingView
from textual.facilities.research_view import ResearchView
from coordinators.game_coordinator import GameCoordinator

class GameRunner:
    """Runs the game using a specific TextInterface implementation."""
    
    def __init__(self, interface: TextInterface):
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

def start_game(interface_type='cli'):
    """Start the game with the specified interface type"""
    if interface_type == 'web':
        # Import web interface dynamically
        try:
            from web.interface import WebInterface
            interface = WebInterface()
        except ImportError:
            # Fall back to CLI if web interface isn't available
            print("Web interface not available, falling back to CLI")
            from cli.interface import CliInterface
            interface = CliInterface()
    else:
        # Use CLI interface by default
        try:
            from cli.interface import CliInterface
            interface = CliInterface()
        except ImportError:
            # This should not happen in a normal setup
            raise ImportError("CLI interface not available. Check your installation.")
    
    # Create and run the game
    runner = GameRunner(interface)
    return runner.run()

if __name__ == "__main__":
    # Create a game runner with the default CLI interface
    start_game('cli') 