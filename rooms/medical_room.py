from typing import List
from crew import CrewType, CrewMember
from room import Room, RoomType

class MedicalRoom(Room):
    def __init__(self):
        super().__init__("Medical Room", RoomType.MEDICAL)
        self.healing_rate = 0.1  # Health points per second per doctor
        
    def heal_crew(self, crew_member: CrewMember) -> None:
        """Heal a crew member"""
        if crew_member.health < 100:
            doctor_count = len([o for o in self.occupants if o.type == CrewType.DOCTORS])
            healing = self.healing_rate * doctor_count
            crew_member.health = min(100, crew_member.health + healing)
    
    def update(self, delta_time: float) -> None:
        # Heal all crew members in the room
        for crew_member in self.occupants:
            self.heal_crew(crew_member)
    
    def can_enter(self, crew_member: CrewMember) -> bool:
        return crew_member.type == CrewType.DOCTORS or crew_member.health < 100 