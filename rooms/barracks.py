from typing import List
from crew import CrewMember
from room import Room, RoomType

class Barracks(Room):
    def __init__(self):
        super().__init__("Barracks", RoomType.BARRACKS)
        self.rest_rate = 0.05  # Energy points per second per bed
        
    def rest_crew(self, crew_member: CrewMember) -> None:
        """Allow a crew member to rest"""
        if crew_member.energy < 100:
            crew_member.energy = min(100, crew_member.energy + self.rest_rate)
    
    def update(self, delta_time: float) -> None:
        # Allow all crew members to rest
        for crew_member in self.occupants:
            self.rest_crew(crew_member)
    
    def can_enter(self, crew_member: CrewMember) -> bool:
        return crew_member.energy < 100 