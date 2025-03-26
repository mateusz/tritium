from typing import List, Dict
from crew import CrewMember, CrewType
from base import ResourceType, ProductionItem
from .room import Room, RoomType
import pygame

class ProductionItem:
    def __init__(self, name: str, required_resources: Dict[ResourceType, float], 
                 required_crew: Dict[CrewType, int], duration: float):
        self.name = name
        self.required_resources = required_resources
        self.required_crew = required_crew
        self.duration = duration
        self.production_progress: float = 0.0
        self.is_completed: bool = False

class ProductionRoom(Room):
    def __init__(self):
        super().__init__("Production Room", RoomType.PRODUCTION)
        self.active_productions: List[ProductionItem] = []
        self.automated_productions: List[ProductionItem] = []
        self.has_aoc: bool = False  # Auto Operations Computer
        self._icon = None
        
    @property
    def icon(self) -> pygame.Surface:
        """Get the room's icon, loading it if not already loaded"""
        if self._icon is None:
            icon_path = 'assets/graphics/gui/icons/Production.png'
            self._icon = pygame.image.load(icon_path)
        return self._icon
        
    def start_production(self, item: ProductionItem, automated: bool = False) -> bool:
        """Start production of an item"""
        if automated and not self.has_aoc:
            return False
            
        if automated:
            self.automated_productions.append(item)
        else:
            self.active_productions.append(item)
        return True
        
    def stop_production(self, item: ProductionItem) -> bool:
        """Stop production of an item"""
        if item in self.active_productions:
            self.active_productions.remove(item)
            return True
        if item in self.automated_productions:
            self.automated_productions.remove(item)
            return True
        return False
        
    def install_aoc(self) -> bool:
        """Install Auto Operations Computer"""
        if not self.has_aoc:
            self.has_aoc = True
            return True
        return False
        
    def remove_aoc(self) -> bool:
        """Remove Auto Operations Computer"""
        if self.has_aoc:
            self.has_aoc = False
            # Stop all automated productions
            self.automated_productions.clear()
            return True
        return False
        
    def update(self, delta_time: float) -> None:
        # Update active productions
        for item in self.active_productions[:]:
            # Calculate progress based on number of producers
            producer_count = len([o for o in self.occupants if o.crew_type == CrewType.PRODUCER])
            if producer_count > 0:
                item.production_progress += delta_time * producer_count
                if item.production_progress >= item.duration:
                    item.is_completed = True
                    self.active_productions.remove(item)
                    
        # Update automated productions (faster with AOC)
        if self.has_aoc:
            for item in self.automated_productions[:]:
                item.production_progress += delta_time * 1.5  # 50% faster with AOC
                if item.production_progress >= item.duration:
                    item.is_completed = True
                    self.automated_productions.remove(item)
                    
    def can_enter(self, crew_member: CrewMember) -> bool:
        # Only producers can enter the production room
        return crew_member.crew_type == CrewType.PRODUCER
        
    def draw(self, screen: pygame.Surface, x: int, y: int, width: int, height: int) -> None:
        """Draw the production room content"""
        super().draw(screen, x, y, width, height)
        
        font = pygame.font.Font(None, 24)
        y_offset = y + 60
        
        # Draw AOC status
        aoc_text = font.render(f"AOC Installed: {'Yes' if self.has_aoc else 'No'}", True, (0, 0, 0))
        screen.blit(aoc_text, (x + 20, y_offset))
        y_offset += 30
        
        # Draw active productions
        active_text = font.render("Active Productions:", True, (0, 0, 0))
        screen.blit(active_text, (x + 20, y_offset))
        y_offset += 30
        
        for item in self.active_productions:
            progress = item.production_progress / item.duration * 100
            item_text = font.render(f"- {item.name}: {progress:.1f}%", True, (0, 0, 0))
            screen.blit(item_text, (x + 40, y_offset))
            y_offset += 30
            
        # Draw automated productions
        if self.has_aoc:
            y_offset += 20
            auto_text = font.render("Automated Productions:", True, (0, 0, 0))
            screen.blit(auto_text, (x + 20, y_offset))
            y_offset += 30
            
            for item in self.automated_productions:
                progress = item.production_progress / item.duration * 100
                item_text = font.render(f"- {item.name}: {progress:.1f}%", True, (0, 0, 0))
                screen.blit(item_text, (x + 40, y_offset))
                y_offset += 30 