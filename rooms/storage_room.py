from typing import Dict
from crew import CrewMember
from base import ResourceType
from .room import Room, RoomType
import pygame

class StorageRoom(Room):
    def __init__(self):
        super().__init__("Storage Room", RoomType.STORAGE)
        self.storage_capacity: Dict[ResourceType, float] = {}
        self.stored_resources: Dict[ResourceType, float] = {}
        self._icon = None
        
    @property
    def icon(self) -> pygame.Surface:
        """Get the room's icon, loading it if not already loaded"""
        if self._icon is None:
            icon_path = 'assets/graphics/gui/icons/Storage.png'
            self._icon = pygame.image.load(icon_path)
        return self._icon
        
    def set_capacity(self, resource_type: ResourceType, capacity: float) -> None:
        """Set storage capacity for a resource type"""
        self.storage_capacity[resource_type] = capacity
        if resource_type not in self.stored_resources:
            self.stored_resources[resource_type] = 0.0
            
    def add_resource(self, resource_type: ResourceType, amount: float) -> float:
        """Add resources to storage. Returns amount actually added."""
        if resource_type not in self.storage_capacity:
            return 0.0
            
        current = self.stored_resources.get(resource_type, 0.0)
        capacity = self.storage_capacity[resource_type]
        space_left = capacity - current
        
        amount_to_add = min(amount, space_left)
        self.stored_resources[resource_type] = current + amount_to_add
        
        return amount_to_add
        
    def remove_resource(self, resource_type: ResourceType, amount: float) -> float:
        """Remove resources from storage. Returns amount actually removed."""
        if resource_type not in self.stored_resources:
            return 0.0
            
        current = self.stored_resources[resource_type]
        amount_to_remove = min(amount, current)
        self.stored_resources[resource_type] = current - amount_to_remove
        
        return amount_to_remove
        
    def get_stored_amount(self, resource_type: ResourceType) -> float:
        """Get amount of a resource currently stored"""
        return self.stored_resources.get(resource_type, 0.0)
        
    def get_capacity(self, resource_type: ResourceType) -> float:
        """Get storage capacity for a resource type"""
        return self.storage_capacity.get(resource_type, 0.0)
        
    def update(self, delta_time: float) -> None:
        # Storage room doesn't need updates
        pass
        
    def can_enter(self, crew_member: CrewMember) -> bool:
        # Anyone can enter the storage room
        return True
        
    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Draw the storage room content"""
        super().draw(screen, x, y, width, height)
        
        font = pygame.font.Font(None, 24)
        y_offset = y + 60
        
        # Draw stored resources
        for resource_type in ResourceType:
            stored = self.get_stored_amount(resource_type)
            capacity = self.get_capacity(resource_type)
            if capacity > 0:  # Only show resources that have capacity set
                resource_text = font.render(f"{resource_type.name}: {stored:.1f}/{capacity:.1f}", True, (0, 0, 0))
                screen.blit(resource_text, (x + 20, y_offset))
                y_offset += 30 