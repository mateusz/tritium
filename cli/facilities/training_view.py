from cli.master_view import MasterView
from data_model.game_state import GameState
from colorama import Fore, Back, Style
import re

class TrainingView(MasterView):
    def __init__(self, game_state: GameState):
        super().__init__(game_state)
        self.earth_base = game_state.get_earth_base()
        self.training_facility = self.earth_base.get_training_facility()
        self.view_name = "training"
        
    def display(self):
        """Display Training Facility view"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
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
                print(Fore.WHITE + "  NOTE: " + Fore.RED + "Cannot train marines at the current selection level")
        
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
                print(Fore.WHITE + "  NOTE: " + Fore.RED + "Cannot train researchers at the current selection level")
        
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
                print(Fore.WHITE + "  NOTE: " + Fore.RED + "Cannot train producers at the current selection level")
        
        # Show light switch status
        light_status = 'ON' if self.training_facility.light_switched_on else 'OFF'
        light_color = Fore.YELLOW if self.training_facility.light_switched_on else Fore.LIGHTBLACK_EX
        print(Fore.CYAN + f"\nLight Switch: " + light_color + f"{light_status}")
        
        # Show commands
        print(Fore.GREEN + Style.BRIGHT + "\nCommands:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + ".        " + Fore.WHITE + "- Advance time by one round" + Fore.YELLOW + " (Training will start automatically)")
        print(Fore.WHITE + "  " + Fore.CYAN + "e        " + Fore.WHITE + "- Return to Earth Base view")
        print(Fore.WHITE + "  " + Fore.CYAN + "l        " + Fore.WHITE + "- Toggle light switch")
        print(Fore.WHITE + "  " + Fore.CYAN + "q        " + Fore.WHITE + "- Quit game")
        
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "\nMarine Training Setup:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + "m+       " + Fore.WHITE + "- Increase marines selection by 1")
        print(Fore.WHITE + "  " + Fore.CYAN + "m+N      " + Fore.WHITE + "- Increase marines selection by N (e.g. m+10)")
        print(Fore.WHITE + "  " + Fore.CYAN + "m-       " + Fore.WHITE + "- Decrease marines selection by 1")
        print(Fore.WHITE + "  " + Fore.CYAN + "m-N      " + Fore.WHITE + "- Decrease marines selection by N (e.g. m-5)")
        
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nResearcher Training Setup:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + "r+       " + Fore.WHITE + "- Increase researchers selection by 1")
        print(Fore.WHITE + "  " + Fore.CYAN + "r+N      " + Fore.WHITE + "- Increase researchers selection by N (e.g. r+10)")
        print(Fore.WHITE + "  " + Fore.CYAN + "r-       " + Fore.WHITE + "- Decrease researchers selection by 1")
        print(Fore.WHITE + "  " + Fore.CYAN + "r-N      " + Fore.WHITE + "- Decrease researchers selection by N (e.g. r-5)")
        
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nProducer Training Setup:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + "p+       " + Fore.WHITE + "- Increase producers selection by 1")
        print(Fore.WHITE + "  " + Fore.CYAN + "p+N      " + Fore.WHITE + "- Increase producers selection by N (e.g. p+10)")
        print(Fore.WHITE + "  " + Fore.CYAN + "p-       " + Fore.WHITE + "- Decrease producers selection by 1")
        print(Fore.WHITE + "  " + Fore.CYAN + "p-N      " + Fore.WHITE + "- Decrease producers selection by N (e.g. p-5)")
    
    def increase_marines_by(self, amount):
        """Increase marines selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_facility.marines_selector_up():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Increased marines selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not increase further after {success_count} increases", "warning")
        return success_count > 0
    
    def decrease_marines_by(self, amount):
        """Decrease marines selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_facility.marines_selector_down():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Decreased marines selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not decrease further after {success_count} decreases", "warning")
        return success_count > 0
    
    def increase_researchers_by(self, amount):
        """Increase researchers selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_facility.researchers_selector_up():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Increased researchers selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not increase further after {success_count} increases", "warning")
        return success_count > 0
    
    def decrease_researchers_by(self, amount):
        """Decrease researchers selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_facility.researchers_selector_down():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Decreased researchers selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not decrease further after {success_count} decreases", "warning")
        return success_count > 0
    
    def increase_producers_by(self, amount):
        """Increase producers selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_facility.producers_selector_up():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Increased producers selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not increase further after {success_count} increases", "warning")
        return success_count > 0
    
    def decrease_producers_by(self, amount):
        """Decrease producers selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_facility.producers_selector_down():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Decreased producers selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not decrease further after {success_count} decreases", "warning")
        return success_count > 0
    
    def process_command(self, command: str):
        """Process Training Facility specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        # Check for numeric increment/decrement patterns
        m_plus_match = re.match(r'^m\+(\d+)$', command)
        m_minus_match = re.match(r'^m\-(\d+)$', command)
        r_plus_match = re.match(r'^r\+(\d+)$', command)
        r_minus_match = re.match(r'^r\-(\d+)$', command)
        p_plus_match = re.match(r'^p\+(\d+)$', command)
        p_minus_match = re.match(r'^p\-(\d+)$', command)
        
        if command == "e":
            # Return to Earth Base view - create a new Earth view
            from cli.bases.earth_view import EarthView
            earth_view = EarthView(self.game_state)
            return ('switch', earth_view)
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            self.game_state.update()
            
            # Inform user about any training that started automatically
            if self.training_facility.marines_in_training and self.training_facility.marines_in_training.days_remaining == 7:
                self.log_message(f"Started training {self.training_facility.marines_in_training.amount} marines", "success")
            if self.training_facility.researchers_in_training and self.training_facility.researchers_in_training.days_remaining == 14:
                self.log_message(f"Started training {self.training_facility.researchers_in_training.amount} researchers", "success")
            if self.training_facility.producers_in_training and self.training_facility.producers_in_training.days_remaining == 7:
                self.log_message(f"Started training {self.training_facility.producers_in_training.amount} producers", "success")
                
            return ('continue', None)
        elif command == "l":
            # Toggle light switch
            is_on = self.training_facility.toggle_light_switch()
            status = "ON" if is_on else "OFF"
            self.log_message(f"Light switch toggled: {status}", "info")
            return ('continue', None)
        
        # Marine training commands
        elif m_plus_match:
            # Increase marines by a specific amount
            amount = int(m_plus_match.group(1))
            self.increase_marines_by(amount)
            return ('continue', None)
        elif m_minus_match:
            # Decrease marines by a specific amount
            amount = int(m_minus_match.group(1))
            self.decrease_marines_by(amount)
            return ('continue', None)
        elif command == "m+":
            result = self.training_facility.marines_selector_up()
            if not result:
                self.log_message("Cannot increase marines selection further", "error")
            else:
                self.log_message("Increased marines selection by 1", "success")
            return ('continue', None)
        elif command == "m-":
            result = self.training_facility.marines_selector_down()
            if not result:
                self.log_message("Cannot decrease marines selection further", "error")
            else:
                self.log_message("Decreased marines selection by 1", "success")
            return ('continue', None)
        
        # Researcher training commands
        elif r_plus_match:
            # Increase researchers by a specific amount
            amount = int(r_plus_match.group(1))
            self.increase_researchers_by(amount)
            return ('continue', None)
        elif r_minus_match:
            # Decrease researchers by a specific amount
            amount = int(r_minus_match.group(1))
            self.decrease_researchers_by(amount)
            return ('continue', None)
        elif command == "r+":
            result = self.training_facility.researchers_selector_up()
            if not result:
                self.log_message("Cannot increase researchers selection further", "error")
            else:
                self.log_message("Increased researchers selection by 1", "success")
            return ('continue', None)
        elif command == "r-":
            result = self.training_facility.researchers_selector_down()
            if not result:
                self.log_message("Cannot decrease researchers selection further", "error")
            else:
                self.log_message("Decreased researchers selection by 1", "success")
            return ('continue', None)
        
        # Producer training commands
        elif p_plus_match:
            # Increase producers by a specific amount
            amount = int(p_plus_match.group(1))
            self.increase_producers_by(amount)
            return ('continue', None)
        elif p_minus_match:
            # Decrease producers by a specific amount
            amount = int(p_minus_match.group(1))
            self.decrease_producers_by(amount)
            return ('continue', None)
        elif command == "p+":
            result = self.training_facility.producers_selector_up()
            if not result:
                self.log_message("Cannot increase producers selection further", "error")
            else:
                self.log_message("Increased producers selection by 1", "success")
            return ('continue', None)
        elif command == "p-":
            result = self.training_facility.producers_selector_down()
            if not result:
                self.log_message("Cannot decrease producers selection further", "error")
            else:
                self.log_message("Decreased producers selection by 1", "success")
            return ('continue', None)
        
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return Fore.GREEN + "Training Command: " + Fore.WHITE 