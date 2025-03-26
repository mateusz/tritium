from typing import List, Optional
from crew import CrewType, CrewMember
from base import ResearchProject, ResourceType
from .room import Room, RoomType
import pygame

class ResearchProject:
    def __init__(self, name: str, description: str, required_resources: dict[ResourceType, float], 
                 required_crew: dict[CrewType, int], duration: float):
        self.name = name
        self.description = description
        self.required_resources = required_resources
        self.required_crew = required_crew
        self.duration = duration
        self.progress: float = 0.0
        self.is_completed: bool = False

class ResearchRoom(Room):
    def __init__(self):
        super().__init__("Research Room", RoomType.RESEARCH)
        self.active_projects: List[ResearchProject] = []
        self.completed_projects: List[ResearchProject] = []
        self._icon = None
        
    @property
    def icon(self) -> pygame.Surface:
        """Get the room's icon, loading it if not already loaded"""
        if self._icon is None:
            icon_path = 'assets/graphics/gui/icons/Research.png'
            self._icon = pygame.image.load(icon_path)
        return self._icon
        
    def start_project(self, project: ResearchProject) -> bool:
        """Start a new research project"""
        if not self.is_active:
            return False
            
        # Check if we have enough crew
        for crew_type, count in project.required_crew.items():
            available = sum(1 for crew in self.occupants if crew.crew_type == crew_type)
            if available < count:
                return False
                
        self.active_projects.append(project)
        return True
        
    def update(self, delta_time: float) -> None:
        if not self.is_active:
            return
            
        # Update each active project
        for project in self.active_projects[:]:
            # Calculate progress based on crew
            crew_progress = 0.0
            for crew_type, required in project.required_crew.items():
                available = sum(1 for crew in self.occupants if crew.crew_type == crew_type)
                crew_progress += min(available / required, 1.0)
            
            # Update project progress
            if crew_progress > 0:
                project.progress += delta_time * crew_progress
                
                # Check if project is completed
                if project.progress >= project.duration:
                    project.is_completed = True
                    self.completed_projects.append(project)
                    self.active_projects.remove(project)
                    
    def can_enter(self, crew_member: CrewMember) -> bool:
        # Only researchers can enter
        return crew_member.crew_type == CrewType.RESEARCHER
        
    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Draw the research room content"""
        super().draw(screen, x, y, width, height)
        
        font = pygame.font.Font(None, 24)
        y_offset = y + 60
        
        # Draw active projects
        active_text = font.render("Active Projects:", True, (0, 0, 0))
        screen.blit(active_text, (x + 20, y_offset))
        y_offset += 30
        
        for project in self.active_projects:
            progress = project.progress / project.duration * 100
            project_text = font.render(f"- {project.name}: {progress:.1f}%", True, (0, 0, 0))
            screen.blit(project_text, (x + 40, y_offset))
            y_offset += 30
            
        # Draw completed projects
        if self.completed_projects:
            y_offset += 20
            completed_text = font.render("Completed Projects:", True, (0, 0, 0))
            screen.blit(completed_text, (x + 20, y_offset))
            y_offset += 30
            
            for project in self.completed_projects:
                project_text = font.render(f"- {project.name}", True, (0, 0, 0))
                screen.blit(project_text, (x + 40, y_offset))
                y_offset += 30 