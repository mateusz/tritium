from textual.master_view import MasterView
from textual.interface import TextInterface, TextColor
from coordinators.game_coordinator import GameCoordinator
from textual.persistence import Persistence

class EarthView(MasterView):
    def __init__(self, game_coordinator: GameCoordinator, interface: TextInterface):
        super().__init__(game_coordinator, interface)
        self.view_name = "earth"
        self.time_coordinator = game_coordinator.get_time_coordinator()
    
    def display(self):
        """Display Earth-specific game state"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            self.interface.print_line(messages_display)
            self.interface.print_line("")
            
        # Header with background color and centered text
        header = self.interface.center_text("=== TRITIUM - Earth Base View ===", 80)
        header = self.interface.colorize(header, TextColor.BG_GREEN)
        header = self.interface.colorize(header, TextColor.FG_BLACK)
        header = self.interface.colorize(header, TextColor.STYLE_BRIGHT)
        self.interface.print_line(header)
        
        # Game time display
        time_display = self.interface.colorize("Game Time: ", TextColor.FG_CYAN) + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", TextColor.FG_YELLOW)
        self.interface.print_line(time_display)
        
        # Get Earth base through the coordinator
        earth_base = self.game_coordinator.get_earth_base()
        
        # Display Earth-specific information
        earth_status = self.interface.colorize("\nEarth Base Status:", TextColor.FG_GREEN)
        earth_status = self.interface.colorize(earth_status, TextColor.STYLE_BRIGHT)
        self.interface.print_line(earth_status)
        
        # Access and display training facility information if available
        try:
            training = earth_base.get_training_facility()
            if training:
                status = self.interface.colorize("  Training Facility: ", TextColor.FG_WHITE) + self.interface.colorize("Active", TextColor.FG_LIGHTGREEN)
                self.interface.print_line(status)
        except (AttributeError, NotImplementedError):
            status = self.interface.colorize("  Training Facility: ", TextColor.FG_WHITE) + self.interface.colorize("Not implemented yet", TextColor.FG_RED)
            self.interface.print_line(status)
            
        # Access and display research facility information if available
        try:
            research = earth_base.get_research_facility()
            if research:
                status = self.interface.colorize("  Research Facility: ", TextColor.FG_WHITE) + self.interface.colorize("Active", TextColor.FG_LIGHTGREEN)
                self.interface.print_line(status)
        except (AttributeError, NotImplementedError):
            status = self.interface.colorize("  Research Facility: ", TextColor.FG_WHITE) + self.interface.colorize("Not implemented yet", TextColor.FG_RED)
            self.interface.print_line(status)
        
        # Commands section
        commands_header = self.interface.colorize("\nCommands:", TextColor.FG_GREEN)
        self.interface.print_line(commands_header)
        
        # Command list
        cmd_1 = "  " + self.interface.colorize(".    ", TextColor.FG_CYAN) + self.interface.colorize("- Advance time by one round", TextColor.FG_WHITE)
        cmd_2 = "  " + self.interface.colorize("t    ", TextColor.FG_CYAN) + self.interface.colorize("- Go to Training Facility", TextColor.FG_WHITE)
        cmd_3 = "  " + self.interface.colorize("r    ", TextColor.FG_CYAN) + self.interface.colorize("- Go to Research Facility", TextColor.FG_WHITE)
        cmd_4 = "  " + self.interface.colorize("m    ", TextColor.FG_CYAN) + self.interface.colorize("- Return to main view", TextColor.FG_WHITE)
        cmd_5 = "  " + self.interface.colorize("q    ", TextColor.FG_CYAN) + self.interface.colorize("- Quit game", TextColor.FG_WHITE)
        
        self.interface.print_line(cmd_1)
        self.interface.print_line(cmd_2)
        self.interface.print_line(cmd_3)
        self.interface.print_line(cmd_4)
        self.interface.print_line(cmd_5)
    
    def process_command(self, command: str):
        """Process Earth view specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        if command == "m":
            return ('switch', 'master_view')
        elif command == "q":
            return ('quit', None)
        elif command == ".":
            # Advance time using the coordinator
            self.time_coordinator.advance_time()
            return ('continue', None)
        elif command == "t":
            return ('switch', 'training_view')
        elif command == "r":
            return ('switch', 'research_view')
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return self.interface.colorize("Earth Command: ", TextColor.FG_GREEN) 