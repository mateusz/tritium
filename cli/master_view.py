from data_model.game_state import GameState
from colorama import Fore, Back, Style

class MasterView:
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.view_name = "master"
    
    def clear_screen(self):
        """Simple cross-platform clear screen"""
        print("\033[H\033[J", end="")
    
    def display(self):
        """Display the current game state in the console"""
        self.clear_screen()
        # Header with background color
        print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "=== TRITIUM - Main View ===".center(80) + Style.RESET_ALL)
        print(Fore.CYAN + f"Game Time: " + Fore.YELLOW + f"{self.game_state.game_time}")
        
        # Commands section
        print(Fore.GREEN + "\nCommands:")
        print(Fore.WHITE + "  " + Fore.CYAN + ".    " + Fore.WHITE + "- Advance time by one round")
        print(Fore.WHITE + "  " + Fore.CYAN + "e    " + Fore.WHITE + "- Switch to Earth view")
        print(Fore.WHITE + "  " + Fore.CYAN + "q    " + Fore.WHITE + "- Quit game")
    
    def advance_time(self):
        """Progress the game time by one round"""
        self.game_state.update()
    
    def process_command(self, command: str):
        """Process a user command
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        if command == "q":
            return ('quit', None)
        elif command == ".":
            self.advance_time()
            return ('continue', None)
        elif command == "e":
            # Switch to Earth view - create and hydrate the new view
            from cli.bases.earth_view import EarthView
            earth_view = EarthView(self.game_state)
            return ('switch', earth_view)
        else:
            print(Fore.RED + "Unknown command. Type '.' to continue, 'e' for Earth view, or 'q' to quit.")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return Fore.GREEN + "Command: " + Fore.WHITE 