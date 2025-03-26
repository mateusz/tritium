from typing import Optional
from crew import CrewType, CrewMember
from room import Room, RoomType

class HireRoom(Room):
    def __init__(self):
        super().__init__("Hire Room", RoomType.HIRE)
        self.recruitment_in_progress: bool = False
        self.recruitment_type: Optional[CrewType] = None
        self.recruitment_progress: float = 0.0
        self.recruitment_target: int = 0
        
    def start_recruitment(self, crew_type: CrewType, target: int) -> bool:
        """Start recruiting crew members of specified type"""
        if not self.recruitment_in_progress:
            self.recruitment_type = crew_type
            self.recruitment_target = target
            self.recruitment_progress = 0.0
            self.recruitment_in_progress = True
            return True
        return False
    
    def update(self, delta_time: float) -> None:
        if self.recruitment_in_progress:
            self.recruitment_progress += delta_time
            if self.recruitment_progress >= 1.0:
                self.recruitment_in_progress = False
                self.recruitment_progress = 0.0
    
    def can_enter(self, crew_member: CrewMember) -> bool:
        return False  # Only for recruitment, not for crew to enter 