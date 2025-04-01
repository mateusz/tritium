from data_model.game_state import GameState
from colorama import Fore, Back, Style
from cli.message_system import MessageManager

class MasterView:
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.view_name = "master"
        self.message_manager = MessageManager.get_instance()
    
    def clear_screen(self):
        """Simple cross-platform clear screen"""
        print("\033[H\033[J", end="")
    
    def display(self):
        """Display the current game state in the console"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
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
        self.message_manager.add_info("Advanced time by one round")
    
    def log_message(self, message: str, message_type: str = "info"):
        """Log a message to be displayed across view refreshes"""
        if message_type == "info":
            self.message_manager.add_info(message)
        elif message_type == "success":
            self.message_manager.add_success(message)
        elif message_type == "warning":
            self.message_manager.add_warning(message)
        elif message_type == "error":
            self.message_manager.add_error(message)
        else:
            self.message_manager.add_message(message)
    
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
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return Fore.GREEN + "Command: " + Fore.WHITE 