from typing import List, Optional
from crew import CrewMember
from .room import Room, RoomType
import pygame

class ShuttleBay(Room):
    def __init__(self):
        super().__init__("Shuttle Bay", RoomType.SHUTTLE_BAY)
        self.docked_shuttles: List[str] = []  # List of shuttle IDs
        self.max_shuttles: int = 3
        self._icon = None
        
    @property
    def icon(self) -> pygame.Surface:
        """Get the room's icon, loading it if not already loaded"""
        if self._icon is None:
            icon_path = 'assets/graphics/gui/icons/ShuttleBay.png'
            self._icon = pygame.image.load(icon_path)
        return self._icon
        
    def dock_shuttle(self, shuttle_id: str) -> bool:
        """Dock a shuttle if there's space"""
        if len(self.docked_shuttles) < self.max_shuttles:
            self.docked_shuttles.append(shuttle_id)
            return True
        return False
        
    def undock_shuttle(self, shuttle_id: str) -> bool:
        """Undock a shuttle"""
        if shuttle_id in self.docked_shuttles:
            self.docked_shuttles.remove(shuttle_id)
            return True
        return False
        
    def get_docked_shuttles(self) -> List[str]:
        """Get list of currently docked shuttles"""
        return self.docked_shuttles.copy()
        
    def update(self, delta_time: float) -> None:
        # Shuttle bay doesn't need updates
        pass
        
    def can_enter(self, crew_member: CrewMember) -> bool:
        # Anyone can enter the shuttle bay
        return True
        
    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Draw the shuttle bay content"""
        super().draw(screen, x, y, width, height)
        
        font = pygame.font.Font(None, 24)
        y_offset = y + 60
        
        # Draw docked shuttles
        shuttle_text = font.render(f"Docked Shuttles: {len(self.docked_shuttles)}/{self.max_shuttles}", True, (0, 0, 0))
        screen.blit(shuttle_text, (x + 20, y_offset))
        y_offset += 30
        
        for shuttle_id in self.docked_shuttles:
            shuttle_text = font.render(f"- Shuttle {shuttle_id}", True, (0, 0, 0))
            screen.blit(shuttle_text, (x + 40, y_offset))
            y_offset += 30 