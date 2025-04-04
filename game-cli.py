import sys
import readline
from colorama import init, Fore, Back, Style
from data_model.game_state import GameState
from coordinators.game_coordinator import GameCoordinator
from data_model.persistence import save_game, load_game
from textual.game_runner import GameRunner
from textual.interface import TextInterface

# Initialize colorama
init(autoreset=True)

class CommandHistoryCliInterface(TextInterface):
    
    def __init__(self):
        super().__init__()
        self.command_history = {}  # Dictionary to store history for each view
        
    """CLI interface implementation with command history support."""
    def print_line(self, text: str) -> None:
        """Print a line of text to the console."""
        print(text)
    
    def clear_screen(self) -> None:
        """Clear the console screen."""
        print("\033[H\033[J", end="")
    
    def read_line(self, prompt: str = "") -> str:
        """Read a line of input from the console."""
        return input(prompt)
        
    def add_command_to_history(self, view_name, command):
        """Add a command to the history for a specific view"""
        if view_name not in self.command_history:
            self.command_history[view_name] = []
        
        # Don't add empty commands or duplicates at the end
        if command and (not self.command_history[view_name] or command != self.command_history[view_name][-1]):
            self.command_history[view_name].append(command)
    
    def get_history(self, view_name):
        """Get command history for a specific view"""
        return self.command_history.get(view_name, [])
    
    def setup_readline(self, view_name):
        """Set up readline with the history for the current view"""
        # Clear existing history
        readline.clear_history()
        
        # Add view-specific history
        for cmd in self.get_history(view_name):
            readline.add_history(cmd)
    
    def read_command(self, prompt="", history=None):
        """Read a command with view-specific history support."""
        # If a view name is provided in history, set up readline
        if history and isinstance(history, str):
            self.setup_readline(history)
        
        # Get user input
        command = input(prompt)
        
        # Add to history if view name provided
        if history and isinstance(history, str) and command.strip():
            self.add_command_to_history(history, command)
            
        return command

def main():
    # Check for a saved game and offer to load it
    saved_game = load_game()
    game_state = None
    
    # Initialize our CLI interface with history support
    cli_interface = CommandHistoryCliInterface()
    
    if saved_game:
        load_choice = cli_interface.read_line(Fore.CYAN + "Saved game found. Load it? (y/n): " + Style.RESET_ALL).lower()
        if load_choice == 'y' or load_choice == 'yes':
            game_state = saved_game
            cli_interface.print_line(Fore.GREEN + "Game loaded successfully!" + Style.RESET_ALL)
    
    # Initialize game state if not loaded
    if not game_state:
        game_state = GameState()
    
    # Create game coordinator with our game state
    game_coordinator = GameCoordinator(game_state)
    
    # Create and run the game with our custom interface
    runner = GameRunner(cli_interface)
    runner.game_coordinator = game_coordinator  # Use our game coordinator with loaded state
    runner.run()
    
    # Save the game when quitting
    if save_game(game_state):
        cli_interface.print_line(Fore.GREEN + "Game saved successfully!")
    
    cli_interface.print_line(Fore.YELLOW + "Game ended. Goodbye!")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 