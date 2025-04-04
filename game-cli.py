import sys
import readline
from colorama import init, Fore, Back, Style
from data_model.game_state import GameState
from coordinators.game_coordinator import GameCoordinator
from textual.master_view import MasterView
from data_model.persistence import save_game, load_game

# Initialize colorama
init(autoreset=True)

class CommandHistory:
    def __init__(self):
        self.history = {}  # Dictionary to store history for each view type
    
    def add_command(self, view_name, command):
        """Add a command to the history for a specific view"""
        if view_name not in self.history:
            self.history[view_name] = []
        
        # Don't add empty commands or duplicates at the end
        if command and (not self.history[view_name] or command != self.history[view_name][-1]):
            self.history[view_name].append(command)
    
    def get_history(self, view_name):
        """Get command history for a specific view"""
        return self.history.get(view_name, [])

def setup_readline(history, view_name):
    """Set up readline with the history for the current view"""
    # Clear existing history
    readline.clear_history()
    
    # Add view-specific history
    for cmd in history.get_history(view_name):
        readline.add_history(cmd)

def main():
    # Check for a saved game and offer to load it
    saved_game = load_game()
    game_state = None
    
    if saved_game:
        load_choice = input(Fore.CYAN + "Saved game found. Load it? (y/n): " + Style.RESET_ALL).lower()
        if load_choice == 'y' or load_choice == 'yes':
            game_state = saved_game
            print(Fore.GREEN + "Game loaded successfully!" + Style.RESET_ALL)
    
    # Initialize game state if not loaded
    if not game_state:
        game_state = GameState()
    
    game_coordinator = GameCoordinator(game_state)
    command_history = CommandHistory()
    
    # Start with master view, passing the game controller
    current_view = MasterView(game_coordinator)
    running = True
    
    # Main game loop
    while running:
        current_view.display()
        
        # Set up readline with the current view's history
        setup_readline(command_history, current_view.view_name)
        
        # Get user input 
        user_input = input(current_view.get_prompt())
        
        # Add command to history
        if user_input.strip():
            command_history.add_command(current_view.view_name, user_input)
        
        # Process command
        action, new_view = current_view.process_command(user_input)
        
        # Handle the action
        if action == 'quit':
            # Save the game when quitting
            if save_game(game_state):
                print(Fore.GREEN + "Game saved successfully!")
            running = False
        elif action == 'switch' and new_view:
            current_view = new_view

    print(Fore.YELLOW + "Game ended. Goodbye!")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 