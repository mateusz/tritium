from base import Base, ResourceType
from rooms.research_room import ResearchRoom
from rooms.training_room import TrainingRoom
from rooms.shuttle_bay import ShuttleBay
from rooms.storage_room import StorageRoom
from rooms.mining_room import MiningRoom
from rooms.shuttle_room import ShuttleRoom
from rooms.production_room import ProductionRoom

class Earth(Base):
    def __init__(self):
        super().__init__("Earth")
        
        # Set resource abundances based on real-world knowledge
        # Values are in tons per second
        self.set_resource_abundance(ResourceType.IRON, 0.5)  # Earth has abundant iron
        self.set_resource_abundance(ResourceType.TITANIUM, 0.2)  # Less common than iron
        self.set_resource_abundance(ResourceType.ALUMINUM, 0.4)  # Very abundant in Earth's crust
        self.set_resource_abundance(ResourceType.CARBON, 0.3)  # Abundant in various forms
        self.set_resource_abundance(ResourceType.COPPER, 0.25)  # Moderately abundant
        self.set_resource_abundance(ResourceType.HYDROGEN, 0.1)  # Available from water
        self.set_resource_abundance(ResourceType.DEUTERIUM, 0.05)  # Rare isotope of hydrogen
        self.set_resource_abundance(ResourceType.METHANE, 0.15)  # Available from natural gas
        self.set_resource_abundance(ResourceType.PALLADIUM, 0.08)  # Rare platinum group metal
        self.set_resource_abundance(ResourceType.PLATINUM, 0.06)  # Very rare precious metal
        self.set_resource_abundance(ResourceType.SILVER, 0.12)  # Moderately rare precious metal
        self.set_resource_abundance(ResourceType.SILICA, 0.0)  # Not available on Earth according to docs

        # Initialize rooms
        self.add_room(ResearchRoom())      # For research projects
        self.add_room(TrainingRoom())      # For crew recruitment
        self.add_room(ShuttleBay())        # For shuttle operations
        self.add_room(StorageRoom())       # For resource storage
        self.add_room(MiningRoom())        # For derrick deployment and mining
        self.add_room(ShuttleRoom())       # For shuttle interior controls
        self.add_room(ProductionRoom())    # For item production 