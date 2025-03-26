from typing import Dict, List
from crew import CrewMember
from base import ResourceType
from .room import Room, RoomType
import pygame

class MiningRoom(Room):
    def __init__(self):
        super().__init__("Mining Room", RoomType.MINING)
        self.deployed_derricks: int = 0
        self.max_derricks: int = 8
        self.mining_rates: Dict[ResourceType, float] = {}
        self._icon = None
        
    @property
    def icon(self) -> pygame.Surface:
        """Get the room's icon, loading it if not already loaded"""
        if self._icon is None:
            icon_path = 'assets/graphics/gui/icons/Mining.png'
            self._icon = pygame.image.load(icon_path)
        return self._icon
        
    def deploy_derrick(self) -> bool:
        """Deploy a new derrick if under the maximum limit"""
        if self.deployed_derricks < self.max_derricks:
            self.deployed_derricks += 1
            return True
        return False
    
    def remove_derrick(self) -> bool:
        """Remove a deployed derrick"""
        if self.deployed_derricks > 0:
            self.deployed_derricks -= 1
            return True
        return False
    
    def set_mining_rate(self, resource_type: ResourceType, rate: float) -> None:
        """Set the mining rate for a specific resource"""
        self.mining_rates[resource_type] = rate
    
    def get_mining_rate(self, resource_type: ResourceType) -> float:
        """Get the current mining rate for a specific resource"""
        return self.mining_rates.get(resource_type, 0.0)
    
    def update(self, delta_time: float) -> None:
        # Mining room doesn't need updates as mining is handled by the base
        pass
    
    def can_enter(self, crew_member: CrewMember) -> bool:
        return True  # Anyone can enter mining room
        
    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Draw the mining room content"""
        super().draw(screen, x, y, width, height)
        
        font = pygame.font.Font(None, 24)
        y_offset = y + 60
        
        # Draw derrick status
        derrick_text = font.render(f"Deployed Derricks: {self.deployed_derricks}/{self.max_derricks}", True, (0, 0, 0))
        screen.blit(derrick_text, (x + 20, y_offset))
        y_offset += 30
        
        # Draw mining rates
        for resource_type, rate in self.mining_rates.items():
            rate_text = font.render(f"{resource_type.name}: {rate:.2f}/s", True, (0, 0, 0))
            screen.blit(rate_text, (x + 20, y_offset))
            y_offset += 30 