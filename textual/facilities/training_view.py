from textual.interface import TextInterface, TextColor
from coordinators.game_coordinator import GameCoordinator
from textual.view import View
import re

class TrainingView(View):
    def __init__(self, game_coordinator: GameCoordinator, interface: TextInterface):
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
        header = self.interface.center_text("=== TRITIUM - Training Facility ===", 80)
        header = self.interface.colorize(header, TextColor.FG_WHITE)
        header = self.interface.colorize(header, TextColor.BG_MAGENTA)
        header = self.interface.colorize(header, TextColor.STYLE_BRIGHT)
        print(header)
        
        time_display = self.interface.colorize("Game Time: ", TextColor.FG_CYAN) + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", TextColor.FG_YELLOW)
        print(time_display)
        
        # Get training facility from coordinator
        training_facility = self.training_coordinator.get_training_facility()
        
        # Show training facility status
        population_display = self.interface.colorize(f"\nAvailable Population for Recruitment: ", TextColor.FG_LIGHTBLUE) 
        population_display = self.interface.colorize(population_display, TextColor.STYLE_BRIGHT)
        population_display += self.interface.colorize(f"{self.training_coordinator.get_available_population()}", TextColor.FG_YELLOW)
        print(population_display)
        
        # Show marines training status
        marines_header = self.interface.colorize("\nMarines Training:", TextColor.FG_LIGHTRED)
        marines_header = self.interface.colorize(marines_header, TextColor.STYLE_BRIGHT)
        print(marines_header)
        
        marines_in_training = self.training_coordinator.get_marines_in_training()
        if marines_in_training:
            print(self.interface.colorize("  Status: ", TextColor.FG_WHITE) + self.interface.colorize("TRAINING IN PROGRESS", TextColor.FG_YELLOW))
            print(self.interface.colorize(f"  Amount: ", TextColor.FG_WHITE) + self.interface.colorize(f"{marines_in_training.amount}", TextColor.FG_YELLOW))
            print(self.interface.colorize(f"  Days Remaining: ", TextColor.FG_WHITE) + self.interface.colorize(f"{marines_in_training.days_remaining}", TextColor.FG_YELLOW))
        else:
            marines_selector = self.training_coordinator.get_marines_selector()
            print(self.interface.colorize("  Status: ", TextColor.FG_WHITE) + self.interface.colorize("Ready for training", TextColor.FG_GREEN))
            print(self.interface.colorize(f"  Current Selection: ", TextColor.FG_WHITE) + self.interface.colorize(f"{marines_selector}", TextColor.FG_YELLOW) + self.interface.colorize(" marines", TextColor.FG_WHITE))
            if not self.training_coordinator.can_train_marines(marines_selector):
                print(self.interface.colorize("  NOTE: ", TextColor.FG_WHITE) + self.interface.colorize("Cannot train marines at the current selection level", TextColor.FG_RED))
        
        # Show researchers training status
        researchers_header = self.interface.colorize("\nResearchers Training:", TextColor.FG_LIGHTBLUE)
        researchers_header = self.interface.colorize(researchers_header, TextColor.STYLE_BRIGHT)
        print(researchers_header)
        
        researchers_in_training = self.training_coordinator.get_researchers_in_training()
        if researchers_in_training:
            print(self.interface.colorize("  Status: ", TextColor.FG_WHITE) + self.interface.colorize("TRAINING IN PROGRESS", TextColor.FG_YELLOW))
            print(self.interface.colorize(f"  Amount: ", TextColor.FG_WHITE) + self.interface.colorize(f"{researchers_in_training.amount}", TextColor.FG_YELLOW))
            print(self.interface.colorize(f"  Days Remaining: ", TextColor.FG_WHITE) + self.interface.colorize(f"{researchers_in_training.days_remaining}", TextColor.FG_YELLOW))
        else:
            researchers_selector = self.training_coordinator.get_researchers_selector()
            print(self.interface.colorize("  Status: ", TextColor.FG_WHITE) + self.interface.colorize("Ready for training", TextColor.FG_GREEN))
            print(self.interface.colorize(f"  Current Selection: ", TextColor.FG_WHITE) + self.interface.colorize(f"{researchers_selector}", TextColor.FG_YELLOW) + self.interface.colorize(" researchers", TextColor.FG_WHITE))
            if not self.training_coordinator.can_train_researchers(researchers_selector):
                print(self.interface.colorize("  NOTE: ", TextColor.FG_WHITE) + self.interface.colorize("Cannot train researchers at the current selection level", TextColor.FG_RED))
        
        # Show producers training status
        producers_header = self.interface.colorize("\nProducers Training:", TextColor.FG_LIGHTYELLOW)
        producers_header = self.interface.colorize(producers_header, TextColor.STYLE_BRIGHT)
        print(producers_header)
        
        producers_in_training = self.training_coordinator.get_producers_in_training()
        if producers_in_training:
            print(self.interface.colorize("  Status: ", TextColor.FG_WHITE) + self.interface.colorize("TRAINING IN PROGRESS", TextColor.FG_YELLOW))
            print(self.interface.colorize(f"  Amount: ", TextColor.FG_WHITE) + self.interface.colorize(f"{producers_in_training.amount}", TextColor.FG_YELLOW))
            print(self.interface.colorize(f"  Days Remaining: ", TextColor.FG_WHITE) + self.interface.colorize(f"{producers_in_training.days_remaining}", TextColor.FG_YELLOW))
        else:
            producers_selector = self.training_coordinator.get_producers_selector()
            print(self.interface.colorize("  Status: ", TextColor.FG_WHITE) + self.interface.colorize("Ready for training", TextColor.FG_GREEN))
            print(self.interface.colorize(f"  Current Selection: ", TextColor.FG_WHITE) + self.interface.colorize(f"{producers_selector}", TextColor.FG_YELLOW) + self.interface.colorize(" producers", TextColor.FG_WHITE))
            if not self.training_coordinator.can_train_producers(producers_selector):
                print(self.interface.colorize("  NOTE: ", TextColor.FG_WHITE) + self.interface.colorize("Cannot train producers at the current selection level", TextColor.FG_RED))
        
        # Show light switch status
        light_status = 'ON' if training_facility.light_switched_on else 'OFF'
        light_color = TextColor.FG_YELLOW if training_facility.light_switched_on else TextColor.FG_LIGHTBLACK
        print(self.interface.colorize(f"\nLight Switch: ", TextColor.FG_CYAN) + self.interface.colorize(f"{light_status}", light_color))
        
        # Show commands
        commands_header = self.interface.colorize("\nCommands:", TextColor.FG_GREEN)
        commands_header = self.interface.colorize(commands_header, TextColor.STYLE_BRIGHT)
        print(commands_header)
        
        cmd_advance = self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize(".        ", TextColor.FG_CYAN) + self.interface.colorize("- Advance time by one round", TextColor.FG_WHITE) + self.interface.colorize(" (Training will start automatically)", TextColor.FG_YELLOW)
        cmd_earth = self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("e        ", TextColor.FG_CYAN) + self.interface.colorize("- Return to Earth Base view", TextColor.FG_WHITE)
        cmd_light = self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("l        ", TextColor.FG_CYAN) + self.interface.colorize("- Toggle light switch", TextColor.FG_WHITE)
        cmd_quit = self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("q        ", TextColor.FG_CYAN) + self.interface.colorize("- Quit game", TextColor.FG_WHITE)
        
        print(cmd_advance)
        print(cmd_earth)
        print(cmd_light)
        print(cmd_quit)
        
        marine_header = self.interface.colorize("\nMarine Training Setup:", TextColor.FG_LIGHTRED)
        marine_header = self.interface.colorize(marine_header, TextColor.STYLE_BRIGHT)
        print(marine_header)
        
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("m+N      ", TextColor.FG_CYAN) + self.interface.colorize("- Increase marines selection by N (e.g. m+10)", TextColor.FG_WHITE))
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("m-N      ", TextColor.FG_CYAN) + self.interface.colorize("- Decrease marines selection by N (e.g. m-5)", TextColor.FG_WHITE))
        
        researcher_header = self.interface.colorize("\nResearcher Training Setup:", TextColor.FG_LIGHTBLUE)
        researcher_header = self.interface.colorize(researcher_header, TextColor.STYLE_BRIGHT)
        print(researcher_header)
        
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("r+N      ", TextColor.FG_CYAN) + self.interface.colorize("- Increase researchers selection by N (e.g. r+10)", TextColor.FG_WHITE))
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("r-N      ", TextColor.FG_CYAN) + self.interface.colorize("- Decrease researchers selection by N (e.g. r-5)", TextColor.FG_WHITE))
        
        producer_header = self.interface.colorize("\nProducer Training Setup:", TextColor.FG_LIGHTYELLOW)
        producer_header = self.interface.colorize(producer_header, TextColor.STYLE_BRIGHT)
        print(producer_header)
        
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("p+N      ", TextColor.FG_CYAN) + self.interface.colorize("- Increase producers selection by N (e.g. p+10)", TextColor.FG_WHITE))
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("p-N      ", TextColor.FG_CYAN) + self.interface.colorize("- Decrease producers selection by N (e.g. p-5)", TextColor.FG_WHITE))
    
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
        return self.interface.colorize("Training Command: ", TextColor.FG_GREEN) 