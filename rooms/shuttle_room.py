from typing import List, Optional
from crew import CrewMember, CrewType
from .room import Room, RoomType
import pygame

class ShuttleRoom(Room):
    def __init__(self):
        super().__init__("Shuttle Room", RoomType.SHUTTLE)
        self.current_shuttle: Optional[str] = None
        self.attached_pods: List[str] = []
        self.fuel_level: float = 0.0
        self.max_fuel: float = 100.0
        self.is_launched: bool = False
        self.current_location: str = "Docked"
        self._icon = None
        
    @property
    def icon(self) -> pygame.Surface:
        """Get the room's icon, loading it if not already loaded"""
        if self._icon is None:
            icon_path = 'assets/graphics/gui/icons/Shuttle.png'
            self._icon = pygame.image.load(icon_path)
        return self._icon
        
    def attach_pod(self, pod_id: str) -> bool:
        """Attach a pod to the shuttle"""
        if len(self.attached_pods) < 3:  # Maximum 3 pods
            self.attached_pods.append(pod_id)
            return True
        return False
        
    def detach_pod(self, pod_id: str) -> bool:
        """Detach a pod from the shuttle"""
        if pod_id in self.attached_pods:
            self.attached_pods.remove(pod_id)
            return True
        return False
        
    def add_fuel(self, amount: float) -> float:
        """Add fuel to the shuttle. Returns amount actually added."""
        space_left = self.max_fuel - self.fuel_level
        amount_to_add = min(amount, space_left)
        self.fuel_level += amount_to_add
        return amount_to_add
        
    def launch(self) -> bool:
        """Launch the shuttle if it has enough fuel"""
        if not self.is_launched and self.fuel_level > 0:
            self.is_launched = True
            self.current_location = "In Flight"
            return True
        return False
        
    def land(self) -> bool:
        """Land the shuttle"""
        if self.is_launched:
            self.is_launched = False
            self.current_location = "Docked"
            return True
        return False
        
    def set_course(self, destination: str) -> None:
        """Set the shuttle's course to a destination"""
        if self.is_launched:
            self.current_location = f"En route to {destination}"
            
    def update(self, delta_time: float) -> None:
        if self.is_launched:
            # Consume fuel over time
            fuel_consumption = delta_time * 0.1  # 0.1 fuel per second
            self.fuel_level = max(0.0, self.fuel_level - fuel_consumption)
            
            # If fuel runs out, force landing
            if self.fuel_level <= 0:
                self.land()
                
    def can_enter(self, crew_member: CrewMember) -> bool:
        # Only marines can enter the shuttle (they are the pilots)
        return crew_member.crew_type == CrewType.MARINE
        
    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Draw the shuttle room content"""
        super().draw(screen, x, y, width, height)
        
        font = pygame.font.Font(None, 24)
        y_offset = y + 60
        
        # Draw shuttle status
        status_text = font.render(f"Status: {'Launched' if self.is_launched else 'Docked'}", True, (0, 0, 0))
        screen.blit(status_text, (x + 20, y_offset))
        y_offset += 30
        
        # Draw fuel level
        fuel_text = font.render(f"Fuel: {self.fuel_level:.1f}/{self.max_fuel:.1f}", True, (0, 0, 0))
        screen.blit(fuel_text, (x + 20, y_offset))
        y_offset += 30
        
        # Draw location
        location_text = font.render(f"Location: {self.current_location}", True, (0, 0, 0))
        screen.blit(location_text, (x + 20, y_offset))
        y_offset += 30
        
        # Draw attached pods
        pod_text = font.render("Attached Pods:", True, (0, 0, 0))
        screen.blit(pod_text, (x + 20, y_offset))
        y_offset += 30
        
        for pod in self.attached_pods:
            pod_text = font.render(f"- {pod}", True, (0, 0, 0))
            screen.blit(pod_text, (x + 40, y_offset))
            y_offset += 30 