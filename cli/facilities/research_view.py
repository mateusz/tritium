from cli.master_view import MasterView
from controllers.game_controller import GameController
from colorama import Fore, Back, Style
from data_model.equipment.equipment import EquipmentType, Equipment
import re

class ResearchView(MasterView):
    def __init__(self, game_controller: GameController = None):
        super().__init__(game_controller)
        self.view_name = "research"
        
        # Get the research controller from the game controller
        self.research_controller = None
        if game_controller:
            self.research_controller = game_controller.get_research_controller()
        
    def display(self):
        """Display Research Facility view"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
        # Header with background color
        print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "=== TRITIUM - Research Facility ===".center(80) + Style.RESET_ALL)
        print(Fore.CYAN + f"Game Time: " + Fore.YELLOW + f"{self.game_controller.get_game_time()}")
        
        # Get research facility from controller
        research_facility = self.research_controller.get_research_facility()
        
        # Show research status
        current_research = self.research_controller.get_current_research()
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nResearch Status:" + Style.RESET_ALL)
        
        if current_research:
            equipment_data = Equipment.get_equipment(current_research)
            progress = self.research_controller.get_research_progress_percentage()
            print(Fore.WHITE + "  Currently Researching: " + Fore.YELLOW + f"{current_research.name}")
            print(Fore.WHITE + "  Tech Level: " + Fore.YELLOW + f"{equipment_data.required_rank}")
            print(Fore.WHITE + "  Progress: " + Fore.YELLOW + f"{progress}%")
        else:
            print(Fore.GREEN + "  No research in progress. Select a project to begin.")
        
        # Show research options
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nResearch Projects:" + Style.RESET_ALL)
        
        # Fetch all equipment types and categorize them by status
        all_equipment = list(EquipmentType)
        
        researched_items = []
        in_progress_items = []
        available_items = []
        unavailable_items = []
        
        for item in all_equipment:
            equipment_data = Equipment.get_equipment(item)
            status = self.research_controller.get_research_status(item)
            
            if status == 'researched':
                researched_items.append((item, equipment_data))
            elif status == 'in_progress':
                in_progress_items.append((item, equipment_data))
            elif status == 'available':
                available_items.append((item, equipment_data))
            elif status == 'unavailable':
                unavailable_items.append((item, equipment_data))
        
        # Display research items by category with different colors
        # Green for completed, Yellow for in-progress, Blue for available, Red for unavailable
        
        if researched_items:
            print(Fore.GREEN + "  Completed Research:")
            for i, (item, equipment_data) in enumerate(researched_items):
                print(Fore.GREEN + f"    [{i+1}] {item.name} (Tech Level: {equipment_data.terequired_rankch_level})")
        
        if in_progress_items:
            print(Fore.YELLOW + "  Research In Progress:")
            for i, (item, equipment_data) in enumerate(in_progress_items):
                progress = self.research_controller.get_research_progress_percentage()
                print(Fore.YELLOW + f"    [{i+1}] {item.name} - {progress}% Complete (Tech Level: {equipment_data.required_rank})")
        
        if available_items:
            print(Fore.BLUE + "  Available for Research:")
            for i, (item, equipment_data) in enumerate(available_items):
                print(Fore.BLUE + f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})")
        
        if unavailable_items:
            print(Fore.RED + "  Unavailable (Rank Requirements Not Met):")
            for i, (item, equipment_data) in enumerate(unavailable_items):
                print(Fore.RED + f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})")
        
        # Show researcher information
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nResearch Team:" + Style.RESET_ALL)
        researcher_count = self.research_controller.get_researcher_count()
        max_researchers = self.research_controller.get_max_researcher_count()
        leader_rank = self.research_controller.get_leader_rank()
        
        if leader_rank:
            print(Fore.WHITE + f"  Leader Rank: " + Fore.YELLOW + f"{leader_rank.name}")
        else:
            print(Fore.WHITE + f"  Leader Rank: " + Fore.RED + "No Leader")
            
        print(Fore.WHITE + f"  Researchers: " + Fore.YELLOW + f"{researcher_count}/{max_researchers}")
        
        # Show commands
        print(Fore.GREEN + Style.BRIGHT + "\nCommands:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + ".        " + Fore.WHITE + "- Advance time by one round")
        print(Fore.WHITE + "  " + Fore.CYAN + "e        " + Fore.WHITE + "- Return to Earth Base view")
        print(Fore.WHITE + "  " + Fore.CYAN + "q        " + Fore.WHITE + "- Quit game")
        
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\nResearch Commands:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + "r#       " + Fore.WHITE + "- Start research on available item # (e.g. r2)")
        print(Fore.WHITE + "  " + Fore.CYAN + "v#       " + Fore.WHITE + "- View details of item # (e.g. v1)")
        print(Fore.WHITE + "  " + Fore.CYAN + "a#       " + Fore.WHITE + "- Add # researchers (e.g. a10)")
    
    def process_command(self, command: str):
        """Process Research Facility specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        # Check for numeric patterns
        research_match = re.match(r'^r(\d+)$', command)
        view_match = re.match(r'^v(\d+)$', command)
        add_researchers_match = re.match(r'^a(\d+)$', command)
        
        if command == "e":
            # Return to Earth Base view using the controller
            earth_view = self.game_controller.create_earth_view()
            return ('switch', earth_view)
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            # Advance time using the controller
            self.game_controller.advance_time()
            
            # Check if research completed
            current_research_before = self.research_controller.get_current_research()
            if current_research_before:
                current_research_after = self.research_controller.get_current_research()
                if current_research_after is None:
                    # Research completed
                    self.log_message(f"Research completed: {current_research_before.name}", "success")
                else:
                    # Research in progress
                    progress = self.research_controller.get_research_progress_percentage()
                    self.log_message(f"Research progress: {progress}% complete", "info")
            
            return ('continue', None)
        
        # Research commands
        elif research_match:
            # Start research on item #
            index = int(research_match.group(1))
            
            # Get available items 
            available_items = []
            for item in list(EquipmentType):
                equipment_data = Equipment.get_equipment(item)
                if self.research_controller.get_research_status(item) == 'available':
                    available_items.append((item, equipment_data))
            
            if 1 <= index <= len(available_items):
                equipment_type, equipment_data = available_items[index-1]
                if self.research_controller.start_research(equipment_type, equipment_data):
                    self.log_message(f"Started research on {equipment_type.name}", "success")
                else:
                    self.log_message(f"Cannot start research on {equipment_type.name}", "error")
            else:
                self.log_message(f"Invalid research item number: {index}", "error")
            
            return ('continue', None)
        
        # View commands
        elif view_match:
            # View details of item #
            index = int(view_match.group(1))
            
            # Get all items
            all_items = []
            for item in list(EquipmentType):
                equipment_data = Equipment.get_equipment(item)
                all_items.append((item, equipment_data))
            
            if 1 <= index <= len(all_items):
                equipment_type, equipment_data = all_items[index-1]
                status = self.research_controller.get_research_status(equipment_type)
                
                details = f"Item: {equipment_type.name}\n"
                details += f"Tech Level: {equipment_data.required_rank}\n"
                
                if status == 'researched':
                    details += f"Status: Researched\n"
                    details += f"Mass: {equipment_data.mass}\n"
                    details += f"Required Minerals: {equipment_data.required_minerals}\n"
                    details += f"Production Location: {'Orbit' if equipment_data.orbit_producible else 'Earth'}"
                elif status == 'in_progress':
                    progress = self.research_controller.get_research_progress_percentage()
                    details += f"Status: In Progress ({progress}% complete)"
                elif status == 'available':
                    details += f"Status: Available for Research"
                elif status == 'unavailable':
                    details += f"Status: Unavailable (Requires higher researcher rank)"
                
                self.log_message(details, "info")
            else:
                self.log_message(f"Invalid item number: {index}", "error")
            
            return ('continue', None)
            
        # Add researchers
        elif add_researchers_match:
            # Add researchers
            amount = int(add_researchers_match.group(1))
            
            if amount <= 0:
                self.log_message("Amount must be positive", "error")
            else:
                if self.research_controller.can_add_researchers(amount):
                    if self.research_controller.add_researchers(amount):
                        self.log_message(f"Added {amount} researchers", "success")
                    else:
                        self.log_message("Failed to add researchers", "error")
                else:
                    self.log_message(f"Cannot add {amount} researchers - exceeds maximum", "error")
            
            return ('continue', None)
        
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return Fore.GREEN + "Research Command: " + Fore.WHITE 