from textual.message_system import MessageManager
from textual.interface import TextInterface, TextColor
from coordinators.game_coordinator import GameCoordinator
from data_model.persistence import save_game

class MasterView:
    def __init__(self, game_coordinator: GameCoordinator = None, interface: TextInterface = None):
        # Ensure we have a game coordinator
        if game_coordinator is None:
            # Create a game coordinator if one wasn't provided
            self.game_coordinator = GameCoordinator()
        else:
            self.game_coordinator = game_coordinator
            
        # Set up interface
        self.interface = interface
            
        self.view_name = "master"
        self.message_manager = MessageManager.get_instance()
        self.time_coordinator = game_coordinator.get_time_coordinator()
    
    def clear_screen(self):
        """Clear the screen using the interface"""
        self.interface.clear_screen()
    
    def display(self):
        """Display the current game state using the interface"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            self.interface.print_line(messages_display)
            self.interface.print_line("")
            
        # Header with background color and centered text
        header = self.interface.center_text("=== TRITIUM - Main View ===", 80)
        header = self.interface.colorize(header, TextColor.BG_BLUE)
        header = self.interface.colorize(header, TextColor.FG_WHITE)
        header = self.interface.colorize(header, TextColor.STYLE_BRIGHT)
        self.interface.print_line(header)
        
        # Game time display
        time_display = f"Game Time: {self.time_coordinator.get_game_time()}"
        time_display = self.interface.colorize("Game Time: ", TextColor.FG_CYAN) + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", TextColor.FG_YELLOW)
        self.interface.print_line(time_display)
        
        # Commands section
        commands_header = self.interface.colorize("\nCommands:", TextColor.FG_GREEN)
        self.interface.print_line(commands_header)
        
        # Command list
        cmd_1 = "  " + self.interface.colorize(".    ", TextColor.FG_CYAN) + self.interface.colorize("- Advance time by one round", TextColor.FG_WHITE)
        cmd_2 = "  " + self.interface.colorize("e    ", TextColor.FG_CYAN) + self.interface.colorize("- Switch to Earth view", TextColor.FG_WHITE)
        cmd_3 = "  " + self.interface.colorize("s    ", TextColor.FG_CYAN) + self.interface.colorize("- Save game", TextColor.FG_WHITE)
        cmd_4 = "  " + self.interface.colorize("q    ", TextColor.FG_CYAN) + self.interface.colorize("- Quit game", TextColor.FG_WHITE)
        
        self.interface.print_line(cmd_1)
        self.interface.print_line(cmd_2)
        self.interface.print_line(cmd_3)
        self.interface.print_line(cmd_4)
    
    def advance_time(self):
        """Progress the game time by one round"""
        self.time_coordinator.advance_time()
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
        elif command == "s":
            # Save the game
            if save_game(self.game_coordinator.game_state):
                self.log_message("Game saved successfully!", "success")
            else:
                self.log_message("Failed to save game", "error")
            return ('continue', None)
        elif command == ".":
            self.advance_time()
            return ('continue', None)
        elif command == "e":
            return ('switch', 'earth_view')
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return self.interface.colorize("Command: ", TextColor.FG_GREEN)
    
    def run(self):
        """Run this view's main loop"""
        while True:
            self.display()
            command = self.interface.read_command(self.get_prompt())
            action, new_view = self.process_command(command)
            
            if action == 'quit':
                return None
            elif action == 'switch':
                return new_view 