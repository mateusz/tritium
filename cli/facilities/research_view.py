from cli.master_view import MasterView
from data_model.game_state import GameState
from data_model.equipment.equipment import EquipmentType, Equipment
from colorama import Fore, Back, Style
import re

class ResearchView(MasterView):
    def __init__(self, game_state: GameState):
        super().__init__(game_state)
        self.earth_base = game_state.get_earth_base()
        self.research_facility = self.earth_base.get_research_facility()
        self.view_name = "research"
        
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
        print(Fore.CYAN + f"Game Time: " + Fore.YELLOW + f"{self.game_state.game_time}")
        
        # Show research facility status
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f"\nResearch Staff:" + Style.RESET_ALL)
        if self.research_facility.researchers:
            print(Fore.WHITE + f"  Number of Researchers: " + Fore.YELLOW + f"{self.research_facility.researchers.count}/250")
            print(Fore.WHITE + f"  Rank: " + Fore.YELLOW + f"{self.research_facility.researchers.rank.name}")
        else:
            print(Fore.RED + "  No researchers assigned" + Style.RESET_ALL)
            
        # Show current research status
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nCurrent Research:" + Style.RESET_ALL)
        if self.research_facility.current_research:
            equipment_type = self.research_facility.current_research
            equipment_data = Equipment.get_equipment(equipment_type)
            progress = self.research_facility.get_research_progress_percentage()
            
            print(Fore.WHITE + f"  Researching: " + Fore.YELLOW + f"{equipment_type.name}")
            print(Fore.WHITE + f"  Progress: " + Fore.YELLOW + f"{progress}%")
            print(Fore.WHITE + f"  Days Remaining: " + Fore.YELLOW + 
                  f"{self.research_facility.current_technician_days_remaining}")
            if equipment_data.required_rank:
                print(Fore.WHITE + f"  Required Rank: " + Fore.YELLOW + f"{equipment_data.required_rank.name}")
        else:
            print(Fore.WHITE + "  Status: " + Fore.GREEN + "Ready for new research")
            
        # Show available research projects
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\nResearch Projects:" + Style.RESET_ALL)
        
        # Group items by research status
        completed_items = []
        in_progress_items = []
        available_items = []
        unavailable_items = []
        
        for eq_type in EquipmentType:
            equipment = Equipment.get_equipment(eq_type)
            
            if eq_type in self.research_facility.researched_equipment:
                completed_items.append((eq_type, equipment))
            elif eq_type == self.research_facility.current_research:
                in_progress_items.append((eq_type, equipment))
            elif self.research_facility.researchers and self.research_facility.can_research(equipment):
                available_items.append((eq_type, equipment))
            else:
                unavailable_items.append((eq_type, equipment))
        
        # Display completed research
        if completed_items:
            print(Fore.GREEN + "  Completed Research:")
            for i, (eq_type, equipment) in enumerate(completed_items):
                print(Fore.WHITE + f"    {i+1}. " + Fore.GREEN + f"{eq_type.name}")
        
        # Display in-progress research
        if in_progress_items:
            print(Fore.YELLOW + "  Research In Progress:")
            for i, (eq_type, equipment) in enumerate(in_progress_items):
                progress = self.research_facility.get_research_progress_percentage()
                print(Fore.WHITE + f"    {i+1}. " + Fore.YELLOW + f"{eq_type.name} ({progress}%)")
        
        # Display available research
        if available_items:
            print(Fore.BLUE + "  Available Research:")
            for i, (eq_type, equipment) in enumerate(available_items):
                tech_level = getattr(equipment, 'tech_level', 'N/A')
                print(Fore.WHITE + f"    {i+1}. " + Fore.BLUE + f"{eq_type.name} (Tech: {tech_level})")
        
        # Display unavailable research
        if unavailable_items:
            print(Fore.RED + "  Unavailable Research:")
            for i, (eq_type, equipment) in enumerate(unavailable_items):
                if hasattr(equipment, 'required_rank') and equipment.required_rank:
                    rank_name = equipment.required_rank.name
                    print(Fore.WHITE + f"    {i+1}. " + Fore.RED + f"{eq_type.name} (Requires: {rank_name})")
                else:
                    print(Fore.WHITE + f"    {i+1}. " + Fore.RED + f"{eq_type.name}")
        
        # Show commands
        print(Fore.GREEN + Style.BRIGHT + "\nCommands:" + Style.RESET_ALL)
        print(Fore.WHITE + "  " + Fore.CYAN + ".        " + Fore.WHITE + "- Advance time by one round")
        print(Fore.WHITE + "  " + Fore.CYAN + "e        " + Fore.WHITE + "- Return to Earth Base view")
        print(Fore.WHITE + "  " + Fore.CYAN + "q        " + Fore.WHITE + "- Quit game")
        print(Fore.WHITE + "  " + Fore.CYAN + "r<num>   " + Fore.WHITE + "- Start researching item from available list (e.g. r2)")
        print(Fore.WHITE + "  " + Fore.CYAN + "i<num>   " + Fore.WHITE + "- Show info about completed/available research (e.g. i3)")
    
    def start_research(self, item_number):
        """Start researching an equipment type from available list"""
        available_items = []
        
        for eq_type in EquipmentType:
            equipment = Equipment.get_equipment(eq_type)
            if eq_type not in self.research_facility.researched_equipment and \
               eq_type != self.research_facility.current_research and \
               self.research_facility.researchers and \
               self.research_facility.can_research(equipment):
                available_items.append((eq_type, equipment))
                
        if not available_items:
            self.log_message("No research available to start", "error")
            return False
        
        if item_number < 1 or item_number > len(available_items):
            self.log_message(f"Invalid item number: {item_number}", "error")
            return False
            
        eq_type, equipment = available_items[item_number - 1]
        
        if self.research_facility.current_research:
            self.log_message("Research already in progress", "error")
            return False
            
        if self.research_facility.start_research(eq_type, equipment):
            self.log_message(f"Started research: {eq_type.name}", "success")
            return True
        else:
            self.log_message(f"Failed to start research on {eq_type.name}", "error")
            return False
    
    def show_item_info(self, item_number):
        """Show detailed information about a research item"""
        all_items = []
        
        # Add completed items
        for eq_type in self.research_facility.researched_equipment:
            equipment = Equipment.get_equipment(eq_type)
            all_items.append((eq_type, equipment, "completed"))
        
        # Add in-progress items
        if self.research_facility.current_research:
            eq_type = self.research_facility.current_research
            equipment = Equipment.get_equipment(eq_type)
            all_items.append((eq_type, equipment, "in_progress"))
        
        # Add available and unavailable items
        for eq_type in EquipmentType:
            if eq_type not in self.research_facility.researched_equipment and eq_type != self.research_facility.current_research:
                equipment = Equipment.get_equipment(eq_type)
                if self.research_facility.researchers and self.research_facility.can_research(equipment):
                    all_items.append((eq_type, equipment, "available"))
                else:
                    all_items.append((eq_type, equipment, "unavailable"))
        
        if item_number < 1 or item_number > len(all_items):
            self.log_message(f"Invalid item number: {item_number}", "error")
            return False
            
        eq_type, equipment, status = all_items[item_number - 1]
        
        # Display item information
        info = f"Item: {eq_type.name}\n"
        
        if hasattr(equipment, 'tech_level'):
            info += f"Tech Level: {equipment.tech_level}\n"
            
        if hasattr(equipment, 'mass'):
            info += f"Mass: {equipment.mass}\n"
            
        if hasattr(equipment, 'required_resources'):
            info += f"Required Resources: {equipment.required_resources}\n"
            
        if hasattr(equipment, 'required_rank') and equipment.required_rank:
            info += f"Required Rank: {equipment.required_rank.name}\n"
            
        if status == "in_progress":
            progress = self.research_facility.get_research_progress_percentage()
            info += f"Research Progress: {progress}%\n"
            
        if status == "completed":
            info += "Status: RESEARCH COMPLETE\n"
        elif status == "in_progress":
            info += "Status: RESEARCH IN PROGRESS\n"
        elif status == "available":
            info += "Status: AVAILABLE FOR RESEARCH\n"
        else:
            info += "Status: UNAVAILABLE (Rank requirements not met)\n"
            
        self.log_message(info, "info")
        return True
    
    def process_command(self, command: str):
        """Process Research Facility specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        # Check for research and info commands
        research_match = re.match(r'^r(\d+)$', command)
        info_match = re.match(r'^i(\d+)$', command)
        
        if command == "e":
            # Return to Earth Base view
            from cli.bases.earth_view import EarthView
            earth_view = EarthView(self.game_state)
            return ('switch', earth_view)
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            # Advance time - will also advance research
            self.game_state.update()
            
            # Check if research completed this round
            if self.research_facility.current_research is None and len(self.research_facility.researched_equipment) > 0:
                # Get the most recently completed research
                latest_research = self.research_facility.researched_equipment[-1]
                equipment_name = latest_research.name
                self.log_message(f"Research completed: {equipment_name}", "success")
                
            return ('continue', None)
        elif research_match:
            # Start research on an item
            item_number = int(research_match.group(1))
            self.start_research(item_number)
            return ('continue', None)
        elif info_match:
            # Show info about research item
            item_number = int(info_match.group(1))
            self.show_item_info(item_number)
            return ('continue', None)
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return Fore.GREEN + "Research Command: " + Fore.WHITE 