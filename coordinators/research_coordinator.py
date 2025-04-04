from coordinators.coordinator import Coordinator
from coordinators.equipment_coordinator import EquipmentCoordinator
from data_model.equipment.equipment import EquipmentType
from data_model.rank.researcher_rank import ResearcherRank

class ResearchCoordinator(Coordinator):
    """
    Coordinator for managing research facilities.
    Handles research projects and facility operations.
    """
    
    def get_research_facility(self):
        """
        Get the research facility from Earth base.
        
        Returns:
            The research facility
        """
        earth_base = self._game_state.get_earth_base()
        return earth_base.get_research_facility()
    
    def get_researcher_count(self):
        """
        Get the current number of researchers.
        
        Returns:
            The number of researchers
        """
        research_facility = self.get_research_facility()
        return research_facility.get_researcher_count()
    
    def get_leader_rank(self):
        """
        Get the rank of the research leader.
        
        Returns:
            The rank of the research leader
        """
        research_facility = self.get_research_facility()
        return research_facility.get_leader_rank()
    
    def get_max_researcher_count(self):
        """
        Get the maximum allowed number of researchers.
        
        Returns:
            The maximum number of researchers
        """
        research_facility = self.get_research_facility()
        return research_facility.get_max_researcher_count()
    
    def can_add_researchers(self, number):
        """
        Check if a number of researchers can be added.
        
        Args:
            number: The number of researchers to add
            
        Returns:
            True if researchers can be added, False otherwise
        """
        research_facility = self.get_research_facility()
        return research_facility.can_add_researchers(number)
    
    def add_researchers(self, number):
        """
        Add researchers to the research facility.
        
        Args:
            number: The number of researchers to add
            
        Returns:
            True if researchers were added, False otherwise
        """
        research_facility = self.get_research_facility()
        return research_facility.add_researchers(number)
    
    def get_current_research(self):
        """
        Get the currently researched equipment type.
        
        Returns:
            The equipment type being researched, or None if no research in progress
        """
        research_facility = self.get_research_facility()
        return research_facility.get_current_research()
    
    def get_researched_equipment(self):
        """
        Get the list of researched equipment types.
        
        Returns:
            List of researched equipment types
        """
        research_facility = self.get_research_facility()
        return research_facility.get_researched_equipment()
    
    def get_research_progress_percentage(self):
        """
        Get the current research progress as a percentage.
        
        Returns:
            Percentage of research completion (0-100)
        """
        research_facility = self.get_research_facility()
        return research_facility.get_research_progress_percentage()
    
    def start_research(self, equipment_type, equipment_data):
        """
        Start researching an equipment type.
        
        Args:
            equipment_type: The equipment type to research
            equipment_data: The equipment data containing research requirements
            
        Returns:
            True if research started successfully, False otherwise
        """
        research_facility = self.get_research_facility()
        return research_facility.start_research(equipment_type, equipment_data)
    
    def can_research(self, equipment_data: EquipmentType) -> bool:
        """
        Check if the equipment can be researched with current rank.
        
        Args:
            equipment_data: The equipment data containing research requirements
            
        Returns:
            True if the equipment can be researched, False otherwise
        """
        # Check if technology is available in current game progression
        if not self._game_state.current_game_progression.is_technology_available(equipment_data):
            return False
            
        equipment_coordinator = EquipmentCoordinator(self._game_state)
        equipment_data = equipment_coordinator.get_equipment(equipment_data)
        if equipment_data.required_rank==ResearcherRank.DOCTOR and self.researchers.rank == ResearcherRank.TECHNICIAN:
            return False
        elif equipment_data.required_rank==ResearcherRank.PROFESSOR and self.researchers.rank == ResearcherRank.DOCTOR:
            return False
        elif equipment_data.required_rank==ResearcherRank.PROFESSOR and self.researchers.rank == ResearcherRank.TECHNICIAN:
            return False

        research_facility = self.get_research_facility()
        return research_facility.can_research(equipment_data)
    
    def get_research_status(self, equipment_type: EquipmentType) -> str:
        """
        Get the status of a specific research item.
        
        Args:
            equipment_type: The equipment type to check
            
        Returns:
            String indicating status: 'researched', 'in_progress', 'available', or 'unavailable'
        """
        if not self._game_state.current_game_progression.is_technology_available(equipment_type):
            return 'unavailable'

        research_facility = self.get_research_facility()
        status = research_facility.get_research_status(equipment_type)
            
        return status
    