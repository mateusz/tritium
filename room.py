from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from crew import CrewMember

class RoomType(Enum):
    HIRE = "Hire"  # Unique to Earth base
    STORAGE = "Storage"
    SHUTTLE_BAY = "Shuttle Bay"
    SPACE_BAY = "Space Bay"
    SPACEDOCK = "Spacedock"
    RESEARCH = "Research"
    PRODUCTION = "Production"
    MINING = "Mining"
    CREW = "Crew"

class Room(ABC):
    def __init__(self, name: str, room_type: RoomType):
        self.name = name
        self.room_type = room_type
        self.is_active: bool = True
        self.occupants: List[CrewMember] = []
        
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