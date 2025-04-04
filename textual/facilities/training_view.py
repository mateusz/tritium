from textual.interface import TextInterface
from textual.master_view import MasterView
from coordinators.game_coordinator import GameCoordinator
import re

class TrainingView(MasterView):
    def __init__(self, game_coordinator: GameCoordinator = None, interface: TextInterface = None):
        super().__init__(game_coordinator, interface)
        self.view_name = "training"
        
        # Get the training coordinator from the game coordinator
        self.training_coordinator = None
        if game_coordinator:
            self.training_coordinator = game_coordinator.get_training_coordinator()
            self.time_coordinator = game_coordinator.get_time_coordinator()
        
    def display(self):
        """Display Training Facility view"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
        # Header with background color
        print(self.interface.colorize("=== TRITIUM - Training Facility ===".center(80), fg="white", bg="magenta", style="bright"))
        print(self.interface.colorize(f"Game Time: ", fg="cyan") + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", fg="yellow"))
        
        # Get training facility from coordinator
        training_facility = self.training_coordinator.get_training_facility()
        
        # Show training facility status
        print(self.interface.colorize(f"\nAvailable Population for Recruitment: ", fg="lightblue", style="bright") + 
              self.interface.colorize(f"{self.training_coordinator.get_available_population()}", fg="yellow"))
        
        # Show marines training status
        print(self.interface.colorize("\nMarines Training:", fg="lightred", style="bright"))
        marines_in_training = self.training_coordinator.get_marines_in_training()
        if marines_in_training:
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("TRAINING IN PROGRESS", fg="yellow"))
            print(self.interface.colorize(f"  Amount: ", fg="white") + self.interface.colorize(f"{marines_in_training.amount}", fg="yellow"))
            print(self.interface.colorize(f"  Days Remaining: ", fg="white") + self.interface.colorize(f"{marines_in_training.days_remaining}", fg="yellow"))
        else:
            marines_selector = self.training_coordinator.get_marines_selector()
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("Ready for training", fg="green"))
            print(self.interface.colorize(f"  Current Selection: ", fg="white") + self.interface.colorize(f"{marines_selector}", fg="yellow") + self.interface.colorize(" marines", fg="white"))
            if not self.training_coordinator.can_train_marines(marines_selector):
                print(self.interface.colorize("  NOTE: ", fg="white") + self.interface.colorize("Cannot train marines at the current selection level", fg="red"))
        
        # Show researchers training status
        print(self.interface.colorize("\nResearchers Training:", fg="lightblue", style="bright"))
        researchers_in_training = self.training_coordinator.get_researchers_in_training()
        if researchers_in_training:
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("TRAINING IN PROGRESS", fg="yellow"))
            print(self.interface.colorize(f"  Amount: ", fg="white") + self.interface.colorize(f"{researchers_in_training.amount}", fg="yellow"))
            print(self.interface.colorize(f"  Days Remaining: ", fg="white") + self.interface.colorize(f"{researchers_in_training.days_remaining}", fg="yellow"))
        else:
            researchers_selector = self.training_coordinator.get_researchers_selector()
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("Ready for training", fg="green"))
            print(self.interface.colorize(f"  Current Selection: ", fg="white") + self.interface.colorize(f"{researchers_selector}", fg="yellow") + self.interface.colorize(" researchers", fg="white"))
            if not self.training_coordinator.can_train_researchers(researchers_selector):
                print(self.interface.colorize("  NOTE: ", fg="white") + self.interface.colorize("Cannot train researchers at the current selection level", fg="red"))
        
        # Show producers training status
        print(self.interface.colorize("\nProducers Training:", fg="lightyellow", style="bright"))
        producers_in_training = self.training_coordinator.get_producers_in_training()
        if producers_in_training:
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("TRAINING IN PROGRESS", fg="yellow"))
            print(self.interface.colorize(f"  Amount: ", fg="white") + self.interface.colorize(f"{producers_in_training.amount}", fg="yellow"))
            print(self.interface.colorize(f"  Days Remaining: ", fg="white") + self.interface.colorize(f"{producers_in_training.days_remaining}", fg="yellow"))
        else:
            producers_selector = self.training_coordinator.get_producers_selector()
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("Ready for training", fg="green"))
            print(self.interface.colorize(f"  Current Selection: ", fg="white") + self.interface.colorize(f"{producers_selector}", fg="yellow") + self.interface.colorize(" producers", fg="white"))
            if not self.training_coordinator.can_train_producers(producers_selector):
                print(self.interface.colorize("  NOTE: ", fg="white") + self.interface.colorize("Cannot train producers at the current selection level", fg="red"))
        
        # Show light switch status
        light_status = 'ON' if training_facility.light_switched_on else 'OFF'
        light_color = "yellow" if training_facility.light_switched_on else "lightblack"
        print(self.interface.colorize(f"\nLight Switch: ", fg="cyan") + self.interface.colorize(f"{light_status}", fg=light_color))
        
        # Show commands
        print(self.interface.colorize("\nCommands:", fg="green", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize(".        ", fg="cyan") + 
              self.interface.colorize("- Advance time by one round", fg="white") + 
              self.interface.colorize(" (Training will start automatically)", fg="yellow"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("e        ", fg="cyan") + self.interface.colorize("- Return to Earth Base view", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("l        ", fg="cyan") + self.interface.colorize("- Toggle light switch", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("q        ", fg="cyan") + self.interface.colorize("- Quit game", fg="white"))
        
        print(self.interface.colorize("\nMarine Training Setup:", fg="lightred", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("m+N      ", fg="cyan") + self.interface.colorize("- Increase marines selection by N (e.g. m+10)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("m-N      ", fg="cyan") + self.interface.colorize("- Decrease marines selection by N (e.g. m-5)", fg="white"))
        
        print(self.interface.colorize("\nResearcher Training Setup:", fg="lightblue", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("r+N      ", fg="cyan") + self.interface.colorize("- Increase researchers selection by N (e.g. r+10)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("r-N      ", fg="cyan") + self.interface.colorize("- Decrease researchers selection by N (e.g. r-5)", fg="white"))
        
        print(self.interface.colorize("\nProducer Training Setup:", fg="lightyellow", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("p+N      ", fg="cyan") + self.interface.colorize("- Increase producers selection by N (e.g. p+10)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("p-N      ", fg="cyan") + self.interface.colorize("- Decrease producers selection by N (e.g. p-5)", fg="white"))
    
    def increase_marines_by(self, amount):
        """Increase marines selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_coordinator.marines_selector_up():
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
            if self.training_coordinator.marines_selector_down():
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
            if self.training_coordinator.researchers_selector_up():
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
            if self.training_coordinator.researchers_selector_down():
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
            if self.training_coordinator.producers_selector_up():
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
            if self.training_coordinator.producers_selector_down():
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
            return ('switch', 'earth_view')
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            # Advance time using the coordinator
            self.time_coordinator.advance_time()
            
            # Get training status after update
            training_facility = self.training_coordinator.get_training_facility()
            
            # Inform user about any training that started automatically
            marines_in_training = self.training_coordinator.get_marines_in_training()
            if marines_in_training and marines_in_training.days_remaining == 7:
                self.log_message(f"Started training {marines_in_training.amount} marines", "success")
                
            researchers_in_training = self.training_coordinator.get_researchers_in_training()
            if researchers_in_training and researchers_in_training.days_remaining == 14:
                self.log_message(f"Started training {researchers_in_training.amount} researchers", "success")
                
            producers_in_training = self.training_coordinator.get_producers_in_training()
            if producers_in_training and producers_in_training.days_remaining == 7:
                self.log_message(f"Started training {producers_in_training.amount} producers", "success")
                
            return ('continue', None)
        elif command == "l":
            # Toggle light switch using the coordinator
            is_on = self.training_coordinator.toggle_light_switch()
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
        
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return self.interface.colorize("Training Command: ", fg="green") + self.interface.colorize("", fg="white") 