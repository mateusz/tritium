from cli.master_view import MasterView
from data_model.game_state import GameState

class EarthView(MasterView):
    def __init__(self, game_state: GameState):
        super().__init__(game_state)
        self.earth_base = game_state.get_earth_base()
        self.view_name = "earth"
        
    def display(self):
        """Display Earth-specific game state"""
        self.clear_screen()
        print("=== TRITIUM - Earth Base View ===")
        print(f"Game Time: {self.game_state.game_time}")
        
        # Display Earth-specific information
        print("\nEarth Base Status:")
        # Access and display training facility information if available
        try:
            training = self.earth_base.get_training_facility()
            if training:
                print(f"Training Facility: Active")
        except (AttributeError, NotImplementedError):
            print("Training Facility: Not implemented yet")
        
        print("\nCommands:")
        print("  .    - Advance time by one round")
        print("  t    - Go to Training Facility")
        print("  m    - Return to main view")
        print("  q    - Quit game")
    
    def process_command(self, command: str):
        """Process Earth view specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        if command == "m":
            # Return to main view - create a new master view
            from cli.master_view import MasterView
            master_view = MasterView(self.game_state)
            return ('switch', master_view)
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            self.game_state.update()
            return ('continue', None)
        elif command == "t":
            # Switch to Training Facility view - create and hydrate the new view
            from cli.facilities.training_view import TrainingView
            training_view = TrainingView(self.game_state)
            return ('switch', training_view)
        else:
            print("Unknown command. Type '.' to continue, 't' for Training, 'm' for main view, or 'q' to quit.")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return "Earth Command: " 