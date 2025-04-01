from cli.master_view import MasterView
from data_model.game_state import GameState
from colorama import Fore, Back, Style

class TrainingView(MasterView):
    def __init__(self, game_state: GameState):
        super().__init__(game_state)
        self.earth_base = game_state.get_earth_base()
        self.training_facility = self.earth_base.get_training_facility()
        self.view_name = "training"
        
    def display(self):
        """Display Training Facility view"""
        self.clear_screen()
        # Header with background color
        print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "=== TRITIUM - Training Facility ===".center(80) + Style.RESET_ALL)
        print(Fore.CYAN + f"Game Time: " + Fore.YELLOW + f"{self.game_state.game_time}")
        
        # Show training facility status
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f"\nAvailable Population for Recruitment: " + 
              Fore.YELLOW + f"{self.training_facility.available_population}" + Style.RESET_ALL)
        
        # Show marines training status
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "\nMarines Training:" + Style.RESET_ALL)
        if self.training_facility.marines_in_training:
            print(Fore.WHITE + "  Status: " + Fore.YELLOW + "TRAINING IN PROGRESS")
            print(Fore.WHITE + f"  Amount: " + Fore.YELLOW + f"{self.training_facility.marines_in_training.amount}")
            print(Fore.WHITE + f"  Days Remaining: " + Fore.YELLOW + f"{self.training_facility.marines_in_training.days_remaining}")
        else:
            print(Fore.WHITE + "  Status: " + Fore.GREEN + "Ready for training")
            print(Fore.WHITE + f"  Current Selection: " + Fore.YELLOW + f"{self.training_facility.marines_selector}" + Fore.WHITE + " marines")
            if not self.training_facility.can_train_marines(self.training_facility.marines_selector):
                print(Fore.RED + "  NOTE: Cannot train marines at the current selection level")
        
        # Show researchers training status
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nResearchers Training:" + Style.RESET_ALL)
        if self.training_facility.researchers_in_training:
            print(Fore.WHITE + "  Status: " + Fore.YELLOW + "TRAINING IN PROGRESS")
            print(Fore.WHITE + f"  Amount: " + Fore.YELLOW + f"{self.training_facility.researchers_in_training.amount}")
            print(Fore.WHITE + f"  Days Remaining: " + Fore.YELLOW + f"{self.training_facility.researchers_in_training.days_remaining}")
        else:
            print(Fore.WHITE + "  Status: " + Fore.GREEN + "Ready for training")
            print(Fore.WHITE + f"  Current Selection: " + Fore.YELLOW + f"{self.training_facility.researchers_selector}" + Fore.WHITE + " researchers")
            if not self.training_facility.can_train_researchers(self.training_facility.researchers_selector):
                print(Fore.RED + "  NOTE: Cannot train researchers at the current selection level")
        
        # Show producers training status
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nProducers Training:" + Style.RESET_ALL)
        if self.training_facility.producers_in_training:
            print(Fore.WHITE + "  Status: " + Fore.YELLOW + "TRAINING IN PROGRESS")
            print(Fore.WHITE + f"  Amount: " + Fore.YELLOW + f"{self.training_facility.producers_in_training.amount}")
            print(Fore.WHITE + f"  Days Remaining: " + Fore.YELLOW + f"{self.training_facility.producers_in_training.days_remaining}")
        else:
            print(Fore.WHITE + "  Status: " + Fore.GREEN + "Ready for training")
            print(Fore.WHITE + f"  Current Selection: " + Fore.YELLOW + f"{self.training_facility.producers_selector}" + Fore.WHITE + " producers")
            if not self.training_facility.can_train_producers(self.training_facility.producers_selector):
                print(Fore.RED + "  NOTE: Cannot train producers at the current selection level")
        
        # Show light switch status
        light_status = 'ON' if self.training_facility.light_switched_on else 'OFF'
        light_color = Fore.YELLOW if self.training_facility.light_switched_on else Fore.LIGHTBLACK_EX
        print(Fore.CYAN + f"\nLight Switch: " + light_color + f"{light_status}")
        
        # Show commands
        print(Fore.GREEN + Style.BRIGHT + "\nCommands:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + ".        " + Fore.WHITE + "- Advance time by one round")
        print(Fore.WHITE + "  " + Fore.CYAN + "b        " + Fore.WHITE + "- Return to Earth Base view")
        print(Fore.WHITE + "  " + Fore.CYAN + "l        " + Fore.WHITE + "- Toggle light switch")
        print(Fore.WHITE + "  " + Fore.CYAN + "q        " + Fore.WHITE + "- Quit game")
        
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "\nMarine Training Commands:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + "m+       " + Fore.WHITE + "- Increase marines selection")
        print(Fore.WHITE + "  " + Fore.CYAN + "m-       " + Fore.WHITE + "- Decrease marines selection")
        print(Fore.WHITE + "  " + Fore.CYAN + "mt       " + Fore.WHITE + "- Begin training marines")
        
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nResearcher Training Commands:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + "r+       " + Fore.WHITE + "- Increase researchers selection")
        print(Fore.WHITE + "  " + Fore.CYAN + "r-       " + Fore.WHITE + "- Decrease researchers selection")
        print(Fore.WHITE + "  " + Fore.CYAN + "rt       " + Fore.WHITE + "- Begin training researchers")
        
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nProducer Training Commands:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + "p+       " + Fore.WHITE + "- Increase producers selection")
        print(Fore.WHITE + "  " + Fore.CYAN + "p-       " + Fore.WHITE + "- Decrease producers selection")
        print(Fore.WHITE + "  " + Fore.CYAN + "pt       " + Fore.WHITE + "- Begin training producers")
    
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
            is_on = self.training_facility.toggle_light_switch()
            status = "ON" if is_on else "OFF"
            print(Fore.CYAN + f"Light switch toggled: " + 
                  (Fore.YELLOW if is_on else Fore.LIGHTBLACK_EX) + f"{status}")
            return ('continue', None)
        
        # Marine training commands
        elif command == "m+":
            result = self.training_facility.marines_selector_up()
            if not result:
                print(Fore.RED + "Cannot increase marines selection further.")
            return ('continue', None)
        elif command == "m-":
            result = self.training_facility.marines_selector_down()
            if not result:
                print(Fore.RED + "Cannot decrease marines selection further.")
            return ('continue', None)
        elif command == "mt":
            success = self.training_facility.train_marines(self.training_facility.marines_selector)
            if not success:
                print(Fore.RED + "Cannot start marine training with the current selection.")
            else:
                print(Fore.GREEN + f"Started training {self.training_facility.marines_in_training.amount} marines.")
            return ('continue', None)
        
        # Researcher training commands
        elif command == "r+":
            result = self.training_facility.researchers_selector_up()
            if not result:
                print(Fore.RED + "Cannot increase researchers selection further.")
            return ('continue', None)
        elif command == "r-":
            result = self.training_facility.researchers_selector_down()
            if not result:
                print(Fore.RED + "Cannot decrease researchers selection further.")
            return ('continue', None)
        elif command == "rt":
            success = self.training_facility.train_researchers(self.training_facility.researchers_selector)
            if not success:
                print(Fore.RED + "Cannot start researcher training with the current selection.")
            else:
                print(Fore.GREEN + f"Started training {self.training_facility.researchers_in_training.amount} researchers.")
            return ('continue', None)
        
        # Producer training commands
        elif command == "p+":
            result = self.training_facility.producers_selector_up()
            if not result:
                print(Fore.RED + "Cannot increase producers selection further.")
            return ('continue', None)
        elif command == "p-":
            result = self.training_facility.producers_selector_down()
            if not result:
                print(Fore.RED + "Cannot decrease producers selection further.")
            return ('continue', None)
        elif command == "pt":
            success = self.training_facility.train_producers(self.training_facility.producers_selector)
            if not success:
                print(Fore.RED + "Cannot start producer training with the current selection.")
            else:
                print(Fore.GREEN + f"Started training {self.training_facility.producers_in_training.amount} producers.")
            return ('continue', None)
        
        else:
            print(Fore.RED + "Unknown command. Type '.' to continue, 'b' to return to base, or 'q' to quit.")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return Fore.GREEN + "Training Command: " + Fore.WHITE 