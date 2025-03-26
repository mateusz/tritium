from typing import List
from crew import CrewMember, CrewType
from .room import Room, RoomType
import pygame

class TrainingRoom(Room):
    def __init__(self):
        super().__init__("Training Room", RoomType.TRAINING)
        self.available_crew: List[CrewMember] = []
        self._icon = None
        
    @property
    def icon(self) -> pygame.Surface:
        """Get the room's icon, loading it if not already loaded"""
        if self._icon is None:
            icon_path = 'assets/graphics/gui/icons/Training.png'
            self._icon = pygame.image.load(icon_path)
        return self._icon
        
    def update(self, delta_time: float):
        # TODO: Implement crew recruitment logic
        pass
        
    def can_enter(self, crew_member: CrewMember) -> bool:
        # Anyone can enter the training room
        return True
        
    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Draw the training room content"""
        super().draw(screen, x, y, width, height)
        
        font = pygame.font.Font(None, 24)
        y_offset = y + 60
        
        # Draw available crew count
        crew_text = font.render(f"Available Crew: {len(self.available_crew)}", True, (0, 0, 0))
        screen.blit(crew_text, (x + 20, y_offset))
        y_offset += 30
        
        # Draw available crew members
        for crew_member in self.available_crew:
            crew_info = font.render(f"- {crew_member.name} ({crew_member.crew_type.name})", True, (0, 0, 0))
            screen.blit(crew_info, (x + 40, y_offset))
            y_offset += 30 