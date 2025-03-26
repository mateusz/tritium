from typing import Dict
from crew import CrewMember
from base import ResourceType
from room import Room, RoomType

class StorageRoom(Room):
    def __init__(self):
        super().__init__("Storage Room", RoomType.STORAGE)
        self.resources: Dict[ResourceType, float] = {resource: 0.0 for resource in ResourceType}
        self.max_capacity: float = 50000.0  # Maximum storage capacity per resource
        
    def add_resource(self, resource_type: ResourceType, amount: float) -> bool:
        """Add resources to storage if there's space"""
        current = self.resources[resource_type]
        if current + amount <= self.max_capacity:
            self.resources[resource_type] += amount
            return True
        return False
    
    def remove_resource(self, resource_type: ResourceType, amount: float) -> bool:
        """Remove resources from storage if available"""
        if self.resources[resource_type] >= amount:
            self.resources[resource_type] -= amount
            return True
        return False
    
    def update(self, delta_time: float) -> None:
        pass  # Storage doesn't need updates
    
    def can_enter(self, crew_member: CrewMember) -> bool:
        return True  # Anyone can enter storage 