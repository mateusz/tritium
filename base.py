from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum
from rooms.room import Room, RoomType
from crew import CrewMember, CrewType

class ResourceType(Enum):
    IRON = "Iron"  # Irn
    TITANIUM = "Titanium"  # Ti
    ALUMINUM = "Aluminum"  # Al
    CARBON = "Carbon"  # Crb
    COPPER = "Copper"  # Cop
    HYDROGEN = "Hydrogen"  # Hydr
    HELIUM = "Helium"  # He
    DEUTERIUM = "Deuterium"  # Deut
    METHANE = "Methane"  # Meth
    PALLADIUM = "Palladium"  # Palad
    PLATINUM = "Platinum"  # Plat
    SILVER = "Silver"  # Slv
    GOLD = "Gold"  # Gld
    SILICA = "Silica"  # Slca

@dataclass
class ResearchProject:
    name: str
    description: str
    is_completed: bool = False
    progress: float = 0.0  # 0.0 to 1.0

@dataclass
class ProductionItem:
    name: str
    description: str
    required_resources: Dict[ResourceType, float]
    is_being_produced: bool = False
    production_progress: float = 0.0  # 0.0 to 1.0

class Base:
    def __init__(self, name: str):
        self.name = name
        self.resources: Dict[ResourceType, float] = {resource: 0.0 for resource in ResourceType}
        self.resource_abundance: Dict[ResourceType, float] = {resource: 0.0 for resource in ResourceType}  # Resource gathering rate per second
        self.crew: Dict[CrewType, List[CrewMember]] = {
            CrewType.MARINES: [],
            CrewType.RESEARCHERS: [],
            CrewType.PRODUCERS: []
        }
        self.research_projects: List[ResearchProject] = []
        self.production_queue: List[ProductionItem] = []
        self.derricks: int = 1  # Start with one derrick
        self.max_derricks: int = 8
        self.is_orbital: bool = False  # Whether this is a space station or ground base
        self.rooms: Dict[RoomType, Room] = {}  # Dictionary to store room instances
        
    def set_resource_abundance(self, resource_type: ResourceType, rate: float) -> None:
        """Set the resource gathering rate for a specific resource"""
        self.resource_abundance[resource_type] = rate
        
    def get_resource_abundance(self, resource_type: ResourceType) -> float:
        """Get the current resource gathering rate for a specific resource"""
        return self.resource_abundance[resource_type]
    
    def update_resources(self, delta_time: float) -> None:
        """Update resource amounts based on abundance rates and time passed"""
        for resource_type in ResourceType:
            if self.resource_abundance[resource_type] > 0:
                # Resource gathering rate is affected by number of derricks
                gathering_rate = self.resource_abundance[resource_type] * self.derricks
                self.resources[resource_type] += gathering_rate * delta_time
    
    def add_crew_member(self, crew_type: CrewType, rank: str = "Recruit") -> bool:
        """Add a new crew member if within limits"""
        max_crew = {
            CrewType.MARINES: 41,
            CrewType.RESEARCHERS: 100,
            CrewType.PRODUCERS: 100
        }
        
        if len(self.crew[crew_type]) < max_crew[crew_type]:
            self.crew[crew_type].append(CrewMember(crew_type, rank))
            return True
        return False
    
    def add_derrick(self) -> bool:
        """Add a new derrick if under the maximum limit"""
        if self.derricks < self.max_derricks:
            self.derricks += 1
            return True
        return False
    
    def add_research_project(self, name: str, description: str) -> None:
        """Add a new research project to the queue"""
        self.research_projects.append(ResearchProject(name, description))
    
    def add_production_item(self, name: str, description: str, required_resources: Dict[ResourceType, float]) -> None:
        """Add a new item to the production queue"""
        self.production_queue.append(ProductionItem(name, description, required_resources))
    
    def has_sufficient_resources(self, required_resources: Dict[ResourceType, float]) -> bool:
        """Check if the base has sufficient resources for production"""
        return all(self.resources[resource] >= amount 
                  for resource, amount in required_resources.items())
    
    def consume_resources(self, required_resources: Dict[ResourceType, float]) -> bool:
        """Consume resources if available"""
        if self.has_sufficient_resources(required_resources):
            for resource, amount in required_resources.items():
                self.resources[resource] -= amount
            return True
        return False
    
    def add_resources(self, resources: Dict[ResourceType, float]) -> None:
        """Add resources to the base's storage"""
        for resource, amount in resources.items():
            self.resources[resource] += amount
    
    def get_crew_count(self, crew_type: CrewType) -> int:
        """Get the current number of crew members of a specific type"""
        return len(self.crew[crew_type])
    
    def get_resource_amount(self, resource_type: ResourceType) -> float:
        """Get the current amount of a specific resource"""
        return self.resources[resource_type]
    
    def add_room(self, room: Room) -> None:
        """Add a room to the base"""
        self.rooms[room.room_type] = room
        
    def get_room(self, room_type: RoomType) -> Optional[Room]:
        """Get a room by its type"""
        return self.rooms.get(room_type)
        
    def update(self, delta_time: float) -> None:
        """Update all rooms and resources"""
        self.update_resources(delta_time)
        for room in self.rooms.values():
            room.update(delta_time) 