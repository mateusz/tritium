from textual.master_view import MasterView
from coordinators.game_coordinator import GameCoordinator
from data_model.equipment.equipment import EquipmentType, Equipment
import re
from textual.interface import TextInterface, TextColor
from textual.view import View

class ResearchView(View):
    def __init__(self, game_coordinator: GameCoordinator, interface: TextInterface):
        super().__init__(game_coordinator, interface)
        self.view_name = "research"
        
        # Get the research coordinator from the game coordinator
        self.research_coordinator = None
        if game_coordinator:
            self.research_coordinator = game_coordinator.get_research_coordinator()
            self.time_coordinator = game_coordinator.get_time_coordinator()
            self.equipment_coordinator = game_coordinator.get_equipment_coordinator()
        
    def display(self):
        """Display Research Facility view"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
        # Header with background color
        header = self.interface.center_text("=== TRITIUM - Research Facility ===", 80)
        header = self.interface.colorize(header, TextColor.FG_WHITE)
        header = self.interface.colorize(header, TextColor.BG_BLUE)
        header = self.interface.colorize(header, TextColor.STYLE_BRIGHT)
        print(header)
        
        time_display = self.interface.colorize("Game Time: ", TextColor.FG_CYAN) + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", TextColor.FG_YELLOW)
        print(time_display)
        
        # Get research facility from coordinator
        research_facility = self.research_coordinator.get_research_facility()
        
        # Show research status
        current_research = self.research_coordinator.get_current_research()
        research_status = self.interface.colorize("\nResearch Status:", TextColor.FG_LIGHTBLUE)
        research_status = self.interface.colorize(research_status, TextColor.STYLE_BRIGHT)
        print(research_status)
        
        if current_research:
            equipment_data = self.equipment_coordinator.get_equipment(current_research)
            progress = self.research_coordinator.get_research_progress_percentage()
            print(self.interface.colorize("  Currently Researching: ", TextColor.FG_WHITE) + self.interface.colorize(f"{current_research.name}", TextColor.FG_YELLOW))
            print(self.interface.colorize("  Tech Level: ", TextColor.FG_WHITE) + self.interface.colorize(f"{equipment_data.required_rank}", TextColor.FG_YELLOW))
            print(self.interface.colorize("  Progress: ", TextColor.FG_WHITE) + self.interface.colorize(f"{progress}%", TextColor.FG_YELLOW))
        else:
            print(self.interface.colorize("  No research in progress. Select a project to begin.", TextColor.FG_GREEN))
        
        # Show research options
        research_projects = self.interface.colorize("\nResearch Projects:", TextColor.FG_LIGHTBLUE)
        research_projects = self.interface.colorize(research_projects, TextColor.STYLE_BRIGHT)
        print(research_projects)
        
        # Fetch all equipment types and categorize them by status
        all_equipment = list(EquipmentType)
        
        researched_items = []
        in_progress_items = []
        available_items = []
        unavailable_items = []
        
        for item in all_equipment:
            equipment_data = self.equipment_coordinator.get_equipment(item)
            status = self.research_coordinator.get_research_status(item)
            
            if status == 'researched':
                researched_items.append((item, equipment_data))
            elif status == 'in_progress':
                in_progress_items.append((item, equipment_data))
            elif status == 'available':
                available_items.append((item, equipment_data))
            elif status == 'no_suitable_researchers':
                unavailable_items.append((item, equipment_data))
        
        # Display research items by category with different colors
        # Green for completed, Yellow for in-progress, Blue for available, Red for unavailable
        
        if researched_items:
            print(self.interface.colorize("  Completed Research:", TextColor.FG_GREEN))
            for i, (item, equipment_data) in enumerate(researched_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", TextColor.FG_GREEN))
        
        if in_progress_items:
            print(self.interface.colorize("  Research In Progress:", TextColor.FG_YELLOW))
            for i, (item, equipment_data) in enumerate(in_progress_items):
                progress = self.research_coordinator.get_research_progress_percentage()
                print(self.interface.colorize(f"    [{i+1}] {item.name} - {progress}% Complete (Tech Level: {equipment_data.required_rank})", TextColor.FG_YELLOW))
        
        if available_items:
            print(self.interface.colorize("  Available for Research:", TextColor.FG_BLUE))
            for i, (item, equipment_data) in enumerate(available_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", TextColor.FG_BLUE))
        
        if unavailable_items:
            print(self.interface.colorize("  Unavailable (Rank Requirements Not Met):", TextColor.FG_RED))
            for i, (item, equipment_data) in enumerate(unavailable_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", TextColor.FG_RED))
        
        # Show researcher information
        research_team = self.interface.colorize("\nResearch Team:", TextColor.FG_LIGHTBLUE)
        research_team = self.interface.colorize(research_team, TextColor.STYLE_BRIGHT)
        print(research_team)
        
        researcher_count = self.research_coordinator.get_researcher_count()
        max_researchers = self.research_coordinator.get_max_researcher_count()
        leader_rank = self.research_coordinator.get_leader_rank()
        
        if leader_rank:
            print(self.interface.colorize(f"  Leader Rank: ", TextColor.FG_WHITE) + self.interface.colorize(f"{leader_rank.name}", TextColor.FG_YELLOW))
        else:
            print(self.interface.colorize(f"  Leader Rank: ", TextColor.FG_WHITE) + self.interface.colorize("No Leader", TextColor.FG_RED))
            
        print(self.interface.colorize(f"  Researchers: ", TextColor.FG_WHITE) + self.interface.colorize(f"{researcher_count}/{max_researchers}", TextColor.FG_YELLOW))
        
        # Show commands
        commands = self.interface.colorize("\nCommands:", TextColor.FG_GREEN)
        commands = self.interface.colorize(commands, TextColor.STYLE_BRIGHT)
        print(commands)
        
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize(".        ", TextColor.FG_CYAN) + self.interface.colorize("- Advance time by one round", TextColor.FG_WHITE))
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("e        ", TextColor.FG_CYAN) + self.interface.colorize("- Return to Earth Base view", TextColor.FG_WHITE))
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("q        ", TextColor.FG_CYAN) + self.interface.colorize("- Quit game", TextColor.FG_WHITE))
        
        research_commands = self.interface.colorize("\nResearch Commands:", TextColor.FG_LIGHTBLUE)
        research_commands = self.interface.colorize(research_commands, TextColor.STYLE_BRIGHT)
        print(research_commands)
        
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("r#       ", TextColor.FG_CYAN) + self.interface.colorize("- Start research on available item # (e.g. r2)", TextColor.FG_WHITE))
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("v#       ", TextColor.FG_CYAN) + self.interface.colorize("- View details of item # (e.g. v1)", TextColor.FG_WHITE))
        print(self.interface.colorize("  ", TextColor.FG_WHITE) + self.interface.colorize("a#       ", TextColor.FG_CYAN) + self.interface.colorize("- Add # researchers (e.g. a10)", TextColor.FG_WHITE))
    
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
            return ('switch', 'earth_view')
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            # Advance time using the coordinator
            self.time_coordinator.advance_time()
            
            # Check if research completed
            current_research_before = self.research_coordinator.get_current_research()
            if current_research_before:
                current_research_after = self.research_coordinator.get_current_research()
                if current_research_after is None:
                    # Research completed
                    self.log_message(f"Research completed: {current_research_before.name}", "success")
                else:
                    # Research in progress
                    progress = self.research_coordinator.get_research_progress_percentage()
                    self.log_message(f"Research progress: {progress}% complete", "info")
            
            return ('continue', None)
        
        # Research commands
        elif research_match:
            # Start research on item #
            index = int(research_match.group(1))
            
            # Get available items 
            available_items = []
            for item in list(EquipmentType):
                equipment_data = self.equipment_coordinator.get_equipment(item)
                if self.research_coordinator.get_research_status(item) == 'available':
                    available_items.append((item, equipment_data))
            
            if 1 <= index <= len(available_items):
                equipment_type, equipment_data = available_items[index-1]
                if self.research_coordinator.start_research(equipment_type, equipment_data):
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
                equipment_data = self.equipment_coordinator.get_equipment(item)
                all_items.append((item, equipment_data))
            
            if 1 <= index <= len(all_items):
                equipment_type, equipment_data = all_items[index-1]
                status = self.research_coordinator.get_research_status(equipment_type)
                
                details = f"Item: {equipment_type.name}\n"
                details += f"Tech Level: {equipment_data.required_rank}\n"
                
                if status == 'researched':
                    details += f"Status: Researched\n"
                    details += f"Mass: {equipment_data.mass}\n"
                    details += f"Required Minerals: {equipment_data.required_minerals}\n"
                    details += f"Production Location: {'Orbit' if equipment_data.orbit_producible else 'Earth'}"
                elif status == 'in_progress':
                    progress = self.research_coordinator.get_research_progress_percentage()
                    details += f"Status: In Progress ({progress}% complete)"
                elif status == 'available':
                    details += f"Status: Available for Research"
                elif status == 'unavailable':
                    details += f"Status: Unavailable (Requires higher researcher rank)"
                
                self.log_message(details, "info")
            else:
                self.log_message(f"Invalid item number: {index}", "error")
            
            return ('continue', None)
            
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return self.interface.colorize("Research Command: ", TextColor.FG_GREEN) 