from textual.master_view import MasterView
from coordinators.game_coordinator import GameCoordinator
from data_model.equipment.equipment import EquipmentType, Equipment
import re
from textual.interface import TextInterface
class ResearchView(MasterView):
    def __init__(self, game_coordinator: GameCoordinator = None, interface: TextInterface = None):
        super().__init__(game_coordinator, interface)
        self.view_name = "research"
        
        # Get the research coordinator from the game coordinator
        self.research_coordinator = None
        if game_coordinator:
            self.research_coordinator = game_coordinator.get_research_coordinator()
            self.time_coordinator = game_coordinator.get_time_coordinator()
        
    def display(self):
        """Display Research Facility view"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
        # Header with background color
        print(self.interface.colorize("=== TRITIUM - Research Facility ===".center(80), fg="white", bg="blue", style="bright"))
        print(self.interface.colorize(f"Game Time: ", fg="cyan") + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", fg="yellow"))
        
        # Get research facility from coordinator
        research_facility = self.research_coordinator.get_research_facility()
        
        # Show research status
        current_research = self.research_coordinator.get_current_research()
        print(self.interface.colorize("\nResearch Status:", fg="lightblue", style="bright"))
        
        if current_research:
            equipment_data = Equipment.get_equipment(current_research)
            progress = self.research_coordinator.get_research_progress_percentage()
            print(self.interface.colorize("  Currently Researching: ", fg="white") + self.interface.colorize(f"{current_research.name}", fg="yellow"))
            print(self.interface.colorize("  Tech Level: ", fg="white") + self.interface.colorize(f"{equipment_data.required_rank}", fg="yellow"))
            print(self.interface.colorize("  Progress: ", fg="white") + self.interface.colorize(f"{progress}%", fg="yellow"))
        else:
            print(self.interface.colorize("  No research in progress. Select a project to begin.", fg="green"))
        
        # Show research options
        print(self.interface.colorize("\nResearch Projects:", fg="lightblue", style="bright"))
        
        # Fetch all equipment types and categorize them by status
        all_equipment = list(EquipmentType)
        
        researched_items = []
        in_progress_items = []
        available_items = []
        unavailable_items = []
        
        for item in all_equipment:
            equipment_data = Equipment.get_equipment(item)
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
            print(self.interface.colorize("  Completed Research:", fg="green"))
            for i, (item, equipment_data) in enumerate(researched_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", fg="green"))
        
        if in_progress_items:
            print(self.interface.colorize("  Research In Progress:", fg="yellow"))
            for i, (item, equipment_data) in enumerate(in_progress_items):
                progress = self.research_coordinator.get_research_progress_percentage()
                print(self.interface.colorize(f"    [{i+1}] {item.name} - {progress}% Complete (Tech Level: {equipment_data.required_rank})", fg="yellow"))
        
        if available_items:
            print(self.interface.colorize("  Available for Research:", fg="blue"))
            for i, (item, equipment_data) in enumerate(available_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", fg="blue"))
        
        if unavailable_items:
            print(self.interface.colorize("  Unavailable (Rank Requirements Not Met):", fg="red"))
            for i, (item, equipment_data) in enumerate(unavailable_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", fg="red"))
        
        # Show researcher information
        print(self.interface.colorize("\nResearch Team:", fg="lightblue", style="bright"))
        researcher_count = self.research_coordinator.get_researcher_count()
        max_researchers = self.research_coordinator.get_max_researcher_count()
        leader_rank = self.research_coordinator.get_leader_rank()
        
        if leader_rank:
            print(self.interface.colorize(f"  Leader Rank: ", fg="white") + self.interface.colorize(f"{leader_rank.name}", fg="yellow"))
        else:
            print(self.interface.colorize(f"  Leader Rank: ", fg="white") + self.interface.colorize("No Leader", fg="red"))
            
        print(self.interface.colorize(f"  Researchers: ", fg="white") + self.interface.colorize(f"{researcher_count}/{max_researchers}", fg="yellow"))
        
        # Show commands
        print(self.interface.colorize("\nCommands:", fg="green", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize(".        ", fg="cyan") + self.interface.colorize("- Advance time by one round", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("e        ", fg="cyan") + self.interface.colorize("- Return to Earth Base view", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("q        ", fg="cyan") + self.interface.colorize("- Quit game", fg="white"))
        
        print(self.interface.colorize("\nResearch Commands:", fg="lightblue", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("r#       ", fg="cyan") + self.interface.colorize("- Start research on available item # (e.g. r2)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("v#       ", fg="cyan") + self.interface.colorize("- View details of item # (e.g. v1)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("a#       ", fg="cyan") + self.interface.colorize("- Add # researchers (e.g. a10)", fg="white"))
    
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
                equipment_data = Equipment.get_equipment(item)
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
                equipment_data = Equipment.get_equipment(item)
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
        return self.interface.colorize("Research Command: ", fg="green") + self.interface.colorize("", fg="white") 