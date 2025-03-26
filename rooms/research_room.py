from typing import List
from crew import CrewType, CrewMember
from base import ResearchProject
from room import Room, RoomType

class ResearchRoom(Room):
    def __init__(self):
        super().__init__("Research Room", RoomType.RESEARCH)
        self.active_projects: List[ResearchProject] = []
        self.completed_projects: List[ResearchProject] = []
        
    def start_research(self, project: ResearchProject) -> bool:
        """Start a new research project"""
        if len(self.active_projects) < len(self.occupants):  # One project per researcher
            self.active_projects.append(project)
            return True
        return False
    
    def update(self, delta_time: float) -> None:
        # Update research progress based on number of researchers
        researcher_count = len([o for o in self.occupants if o.type == CrewType.RESEARCHERS])
        for project in self.active_projects:
            if not project.is_completed:
                project.progress += delta_time * researcher_count
                if project.progress >= 1.0:
                    project.is_completed = True
                    self.completed_projects.append(project)
                    self.active_projects.remove(project)
    
    def can_enter(self, crew_member: CrewMember) -> bool:
        return crew_member.type == CrewType.RESEARCHERS 