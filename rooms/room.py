from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from crew import CrewMember
import pygame

class RoomType(Enum):
    RESEARCH = "Research"
    STORAGE = "Storage"
    MINING = "Mining"
    SHUTTLE_BAY = "Shuttle Bay"
    SHUTTLE = "Shuttle"
    PRODUCTION = "Production"
    TRAINING = "Training"  # For crew recruitment

class Room(ABC):
    def __init__(self, name: str, room_type: RoomType):
        self.name = name
        self.room_type = room_type
        self.is_active: bool = True
        self.occupants: List[CrewMember] = []
        self._icon = None
        
    @property
    def icon(self) -> pygame.Surface:
        """Get the room's icon, loading it if not already loaded"""
        if self._icon is None:
            icon_path = f'assets/graphics/gui/icons/{self.room_type.value}.png'
            self._icon = pygame.image.load(icon_path)
        return self._icon
        
    @abstractmethod
    def update(self, delta_time: float) -> None:
        """Update room state based on time passed"""
        pass
    
    @abstractmethod
    def can_enter(self, crew_member: CrewMember) -> bool:
        """Check if a crew member can enter this room"""
        pass
    
    def add_occupant(self, crew_member: CrewMember) -> bool:
        """Add a crew member to the room if they can enter"""
        if self.can_enter(crew_member):
            self.occupants.append(crew_member)
            return True
        return False
    
    def remove_occupant(self, crew_member: CrewMember) -> bool:
        """Remove a crew member from the room"""
        if crew_member in self.occupants:
            self.occupants.remove(crew_member)
            return True
        return False
        
    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Draw the room's content"""
        # Common room info
        font = pygame.font.Font(None, 24)
        title = font.render(self.name, True, (0, 0, 0))
        screen.blit(title, (x + 20, y + 20)) 