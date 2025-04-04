from cli.master_view import MasterView
from colorama import Fore, Back, Style
from controllers.game_controller import GameController

class EarthView(MasterView):
    def __init__(self, game_controller: GameController = None):
        super().__init__(game_controller)
        self.view_name = "earth"
    
    def display(self):
        """Display Earth-specific game state"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
        # Header with background color
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + "=== TRITIUM - Earth Base View ===".center(80) + Style.RESET_ALL)
        print(Fore.CYAN + f"Game Time: " + Fore.YELLOW + f"{self.game_controller.get_game_time()}")
        
        # Get Earth base through the controller
        earth_base = self.game_controller.get_earth_base()
        
        # Display Earth-specific information
        print(Fore.GREEN + Style.BRIGHT + "\nEarth Base Status:" + Style.RESET_ALL)
        # Access and display training facility information if available
        try:
            training = earth_base.get_training_facility()
            if training:
                print(Fore.WHITE + "  Training Facility: " + Fore.LIGHTGREEN_EX + "Active")
        except (AttributeError, NotImplementedError):
            print(Fore.WHITE + "  Training Facility: " + Fore.RED + "Not implemented yet")
            
        # Access and display research facility information if available
        try:
            research = earth_base.get_research_facility()
            if research:
                print(Fore.WHITE + "  Research Facility: " + Fore.LIGHTGREEN_EX + "Active")
        except (AttributeError, NotImplementedError):
            print(Fore.WHITE + "  Research Facility: " + Fore.RED + "Not implemented yet")
        
        # Commands section
        print(Fore.GREEN + "\nCommands:")
        print(Fore.WHITE + "  " + Fore.CYAN + ".    " + Fore.WHITE + "- Advance time by one round")
        print(Fore.WHITE + "  " + Fore.CYAN + "t    " + Fore.WHITE + "- Go to Training Facility")
        print(Fore.WHITE + "  " + Fore.CYAN + "r    " + Fore.WHITE + "- Go to Research Facility")
        print(Fore.WHITE + "  " + Fore.CYAN + "m    " + Fore.WHITE + "- Return to main view")
        print(Fore.WHITE + "  " + Fore.CYAN + "q    " + Fore.WHITE + "- Quit game")
    
    def process_command(self, command: str):
        """Process Earth view specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        if command == "m":
            # Return to main view using the controller
            master_view = self.game_controller.create_master_view()
            return ('switch', master_view)
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            # Advance time using the controller
            self.game_controller.advance_time()
            return ('continue', None)
        elif command == "t":
            # Switch to Training Facility view using the controller
            training_view = self.game_controller.create_training_view()
            return ('switch', training_view)
        elif command == "r":
            # Switch to Research Facility view using the controller
            research_view = self.game_controller.create_research_view()
            return ('switch', research_view)
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return Fore.GREEN + "Earth Command: " + Fore.WHITE 