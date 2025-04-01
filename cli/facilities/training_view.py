from cli.master_view import MasterView
from data_model.game_state import GameState

class TrainingView(MasterView):
    def __init__(self, game_state: GameState):
        super().__init__(game_state)
        self.earth_base = game_state.get_earth_base()
        self.training_facility = self.earth_base.get_training_facility()
        self.view_name = "training"
        
    def display(self):
        """Display Training Facility view"""
        self.clear_screen()
        print("=== TRITIUM - Training Facility ===")
        print(f"Game Time: {self.game_state.game_time}")
        
        # Show training facility status
        print("\nAvailable Population for Recruitment:", self.training_facility.available_population)
        
        # Show marines training status
        print("\nMarines Training:")
        if self.training_facility.marines_in_training:
            print(f"  Status: TRAINING IN PROGRESS")
            print(f"  Amount: {self.training_facility.marines_in_training.amount}")
            print(f"  Days Remaining: {self.training_facility.marines_in_training.days_remaining}")
        else:
            print(f"  Status: Ready for training")
            print(f"  Current Selection: {self.training_facility.marines_selector} marines")
            if not self.training_facility.can_train_marines(self.training_facility.marines_selector):
                print("  NOTE: Cannot train marines at the current selection level")
        
        # Show researchers training status
        print("\nResearchers Training:")
        if self.training_facility.researchers_in_training:
            print(f"  Status: TRAINING IN PROGRESS")
            print(f"  Amount: {self.training_facility.researchers_in_training.amount}")
            print(f"  Days Remaining: {self.training_facility.researchers_in_training.days_remaining}")
        else:
            print(f"  Status: Ready for training")
            print(f"  Current Selection: {self.training_facility.researchers_selector} researchers")
            if not self.training_facility.can_train_researchers(self.training_facility.researchers_selector):
                print("  NOTE: Cannot train researchers at the current selection level")
        
        # Show producers training status
        print("\nProducers Training:")
        if self.training_facility.producers_in_training:
            print(f"  Status: TRAINING IN PROGRESS")
            print(f"  Amount: {self.training_facility.producers_in_training.amount}")
            print(f"  Days Remaining: {self.training_facility.producers_in_training.days_remaining}")
        else:
            print(f"  Status: Ready for training")
            print(f"  Current Selection: {self.training_facility.producers_selector} producers")
            if not self.training_facility.can_train_producers(self.training_facility.producers_selector):
                print("  NOTE: Cannot train producers at the current selection level")
        
        # Show light switch status
        print(f"\nLight Switch: {'ON' if self.training_facility.light_switched_on else 'OFF'}")
        
        # Show commands
        print("\nCommands:")
        print("  .        - Advance time by one round")
        print("  b        - Return to Earth Base view")
        print("  l        - Toggle light switch")
        print("  q        - Quit game")
        print("\nMarine Training Commands:")
        print("  m+       - Increase marines selection")
        print("  m-       - Decrease marines selection")
        print("  mt       - Begin training marines")
        print("\nResearcher Training Commands:")
        print("  r+       - Increase researchers selection")
        print("  r-       - Decrease researchers selection")
        print("  rt       - Begin training researchers")
        print("\nProducer Training Commands:")
        print("  p+       - Increase producers selection")
        print("  p-       - Decrease producers selection")
        print("  pt       - Begin training producers")
    
    def process_command(self, command: str):
        """Process Training Facility specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        if command == "b":
            # Return to Earth Base view - create a new Earth view
            from cli.bases.earth_view import EarthView
            earth_view = EarthView(self.game_state)
            return ('switch', earth_view)
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            self.game_state.update()
            return ('continue', None)
        elif command == "l":
            # Toggle light switch
            self.training_facility.toggle_light_switch()
            return ('continue', None)
        
        # Marine training commands
        elif command == "m+":
            self.training_facility.marines_selector_up()
            return ('continue', None)
        elif command == "m-":
            self.training_facility.marines_selector_down()
            return ('continue', None)
        elif command == "mt":
            success = self.training_facility.train_marines(self.training_facility.marines_selector)
            if not success:
                print("Cannot start marine training with the current selection.")
            return ('continue', None)
        
        # Researcher training commands
        elif command == "r+":
            self.training_facility.researchers_selector_up()
            return ('continue', None)
        elif command == "r-":
            self.training_facility.researchers_selector_down()
            return ('continue', None)
        elif command == "rt":
            success = self.training_facility.train_researchers(self.training_facility.researchers_selector)
            if not success:
                print("Cannot start researcher training with the current selection.")
            return ('continue', None)
        
        # Producer training commands
        elif command == "p+":
            self.training_facility.producers_selector_up()
            return ('continue', None)
        elif command == "p-":
            self.training_facility.producers_selector_down()
            return ('continue', None)
        elif command == "pt":
            success = self.training_facility.train_producers(self.training_facility.producers_selector)
            if not success:
                print("Cannot start producer training with the current selection.")
            return ('continue', None)
        
        else:
            print("Unknown command. Type '.' to continue, 'b' to return to base, or 'q' to quit.")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return "Training Command: " 