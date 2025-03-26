from typing import List, Any
from base import CrewMember
from room import Room, RoomType

class ShuttleBay(Room):
    def __init__(self):
        super().__init__("Shuttle Bay", RoomType.SHUTTLE_BAY)
        self.docked_shuttles: List[Any] = []  # Will be replaced with Shuttle class
        self.max_shuttles: int = 4
        
    def dock_shuttle(self, shuttle: Any) -> bool:
        """Dock a shuttle if there's space"""
        if len(self.docked_shuttles) < self.max_shuttles:
            self.docked_shuttles.append(shuttle)
            return True
        return False
    
    def undock_shuttle(self, shuttle: Any) -> bool:
        """Undock a shuttle"""
        if shuttle in self.docked_shuttles:
            self.docked_shuttles.remove(shuttle)
            return True
        return False
    
    def update(self, delta_time: float) -> None:
        # Update docked shuttles
        for shuttle in self.docked_shuttles:
            pass  # Will update shuttle states
    
    def can_enter(self, crew_member: CrewMember) -> bool:
        return True  # Anyone can enter shuttle bay 