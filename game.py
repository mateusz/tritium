import sys
import readline
from colorama import init, Fore, Back, Style
from data_model.game_state import GameState
from cli.master_view import MasterView

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
    # Initialize game state and command history
    game_state = GameState()
    command_history = CommandHistory()
    
    # Start with master view
    current_view = MasterView(game_state)
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
            running = False
        elif action == 'switch' and new_view:
            # The view itself provides the new view instance
            current_view = new_view

    print(Fore.YELLOW + "Game ended. Goodbye!")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 