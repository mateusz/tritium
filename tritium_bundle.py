#!/usr/bin/env python3
# Tritium Game - Bundled Version
# This file is auto-generated and contains all game code combined into a single file.

from abc import ABC
from abc import ABC, abstractmethod
from dataclasses import dataclass
from dataclasses import dataclass 
from dataclasses import dataclass, field
from dataclasses import field
from enum import Enum, auto
from enum import Enum, auto 
from typing import Dict
from typing import Dict, List, Optional, Any, TYPE_CHECKING
from typing import Dict, Optional
from typing import Dict, Optional, Any, Type
from typing import List
from typing import List, Optional, Dict
from typing import List, Optional, Dict, Callable
from typing import List, Optional, Dict, TYPE_CHECKING
from typing import List, Optional, TYPE_CHECKING
from typing import List, Tuple
from typing import Optional
from typing import Optional, TYPE_CHECKING
from typing import Set
from typing import Set, Type, Optional
import js
import os
import pickle
import re
import time
import unittest


# ========== START OF BUNDLED CODE ==========


# ===== Module: data_model/__init__.py =====
"""
Tritium Game Data Model
"""

"""Data model for Tritium game.""" 


# ===== Module: data_model/grapplable/__init__.py =====



# ===== Module: data_model/system/__init__.py =====
"""System related classes.""" 


# ===== Module: data_model/game_progression/__init__.py =====
# Game progression package 


# ===== Module: data_model/resource/__init__.py =====



# ===== Module: data_model/rank/__init__.py =====



# ===== Module: data_model/equipment/__init__.py =====
"""
Equipment module.
""" 


# ===== Module: data_model/equipment/tests/__init__.py =====
# Equipment tests package 


# ===== Module: data_model/equipment/ship_equipment/__init__.py =====
"""
Ship equipment module.
""" 


# ===== Module: data_model/equipment/ship_equipment/pod/__init__.py =====
"""
Pod module.
""" 


# ===== Module: data_model/equipment/ship_equipment/chassis/__init__.py =====
"""
Chassis module.
""" 


# ===== Module: data_model/equipment/ship_equipment/drive_unit/__init__.py =====
"""
Drive unit module.
""" 


# ===== Module: data_model/equipment/ship_equipment/tool/__init__.py =====
"""
Tool module.
"""


# ===== Module: data_model/equipment/base_equipment/__init__.py =====
"""
Base equipment module.
""" 


# ===== Module: coordinators/__init__.py =====
# Coordinator layer for game systems 


# ===== Module: textual/__init__.py =====
# Textual module for Tritium game 

__all__ = ['TextInterface', 'TextColor', 'CliInterface', 'MasterView', 'MessageManager', 'GameRunner'] 


# ===== Module: textual/facilities/__init__.py =====
# Facilities views module 


# ===== Module: data_model/game_state.py =====

class GameState:
    solar_system: SolarSystem
    game_time: int
    current_game_progression: GameProgression

    def __init__(self):
        self.current_game_progression = InitialProgress()
        self.solar_system = initialize_solar_system()
        self.game_time = 0
        
    def __getstate__(self):
        """Return state for pickling - ensures proper serialization."""
        # Return a copy of the object's __dict__
        return self.__dict__.copy()
    
    def __setstate__(self, state):
        """Set state when unpickling - ensures proper deserialization."""
        # Restore instance attributes
        self.__dict__.update(state)

    def advance_time(self):
        self.game_time += 1
        self.solar_system.advance_time()

    def get_location_by_name(self, name: str):
        for location in self.solar_system.locations:
            if location.name == name:
                return location
        return None

    def get_earth_base(self) -> EarthBase:
        return self.get_location_by_name('Earth').get_resource_base()
    


# ===== Module: data_model/persistence.py =====

# Define the default save file location
DEFAULT_SAVE_FILE = "savegame.dat"

def save_game(game_state: GameState, file_path: str = DEFAULT_SAVE_FILE) -> bool:
    """
    Save the current game state to a file.
    
    Args:
        game_state: The GameState object to save
        file_path: The path to save the game state to (default: savegame.dat)
        
    Returns:
        bool: True if the save was successful, False otherwise
    """
    try:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else '.', exist_ok=True)
        
        # Use highest protocol for better performance and to handle circular references
        with open(file_path, 'wb') as save_file:
            pickle.dump(game_state, save_file, protocol=4)
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False

def load_game(file_path: str = DEFAULT_SAVE_FILE) -> Optional[GameState]:
    """
    Load a game state from a file.
    
    Args:
        file_path: The path to load the game state from (default: savegame.dat)
        
    Returns:
        Optional[GameState]: The loaded GameState object or None if loading failed
    """
    try:
        if not os.path.exists(file_path):
            print(f"Save file not found: {file_path}")
            return None
            
        with open(file_path, 'rb') as save_file:
            return pickle.load(save_file)
    except Exception as e:
        print(f"Error loading game: {e}")
        return None 


# ===== Module: data_model/initialise.py =====


def initialize_solar_system() -> SolarSystem:
    """Initialize the Solar System with all planets, moons, and their resources."""
    solar_system = SolarSystem()
    
    # Mercury
    mercury = Planet()
    mercury.name = 'Mercury'
    mercury.resources = {
        Resource.IRON: 100.0,
        Resource.TITANIUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.COPPER: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(mercury)
    
    # Venus
    venus = Planet()
    venus.name = 'Venus'
    venus.resources = {
        Resource.ALUMINUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.METHANE: 100.0,
        Resource.PLATINUM: 100.0
    }
    solar_system.add_location(venus)
    
    # Earth
    earth = Planet()
    earth.name = 'Earth'
    earth.resources = {
        Resource.IRON: 100.0,
        Resource.TITANIUM: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.COPPER: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.METHANE: 100.0,
        Resource.PALLADIUM: 100.0
    }
    solar_system.add_location(earth)

    earth_base = EarthBase()
    earth_base.add_equipment(EquipmentType.DERRICK, 1)
    earth.set_resource_base(earth_base)
    
    # Earth's Moon
    moon = Moon()
    moon.name = 'Moon'
    moon.resources = {
        Resource.IRON: 100.0,
        Resource.TITANIUM: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(moon)

    moon_base = MoonBase()
    moon.set_resource_base(moon_base) 

    # Mars
    mars = Planet()
    mars.name = 'Mars'
    mars.resources = {
        Resource.IRON: 100.0,
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.SILVER: 100.0
    }
    solar_system.add_location(mars)
    
    # Mars' Moons
    phobos = Moon()
    phobos.name = 'Phobos'
    phobos.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(phobos)
    
    deimos = Moon()
    deimos.name = 'Deimos'
    deimos.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(deimos)
    
    # Asteroid Belt
    asteroid_belt = Asteroid()
    asteroid_belt.name = 'Asteroid Belt'
    asteroid_belt.resources = {
        Resource.TITANIUM: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.COPPER: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.SILVER: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(asteroid_belt)
    
    # Jupiter
    jupiter = Planet()
    jupiter.name = 'Jupiter'
    jupiter.resources = {
        Resource.HYDROGEN: 100.0,
        Resource.HELIUM: 100.0
    }
    solar_system.add_location(jupiter)
    
    # Jupiter's Moons
    amalthea = Moon()
    amalthea.name = 'Amalthea'
    amalthea.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(amalthea)
    
    io = Moon()
    io.name = 'Io'
    io.resources = {
        Resource.CARBON: 100.0,
        Resource.METHANE: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(io)
    
    europa = Moon()
    europa.name = 'Europa'
    europa.resources = {
        Resource.CARBON: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(europa)
    
    ganymede = Moon()
    ganymede.name = 'Ganymede'
    ganymede.resources = {
        Resource.IRON: 100.0,
        Resource.TITANIUM: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.METHANE: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(ganymede)
    
    callisto = Moon()
    callisto.name = 'Callisto'
    callisto.resources = {
        Resource.IRON: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.COPPER: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.PLATINUM: 100.0
    }
    solar_system.add_location(callisto)
    
    leda = Moon()
    leda.name = 'Leda'
    leda.resources = {
        Resource.IRON: 100.0,
        Resource.TITANIUM: 100.0,
        Resource.COPPER: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.METHANE: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(leda)
    
    himalia = Moon()
    himalia.name = 'Himalia'
    himalia.resources = {
        Resource.CARBON: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(himalia)
    
    elara = Moon()
    elara.name = 'Elara'
    elara.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(elara)
    
    pasiphae = Moon()
    pasiphae.name = 'Pasiphae'
    pasiphae.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(pasiphae)
    
    # Saturn
    saturn = Planet()
    saturn.name = 'Saturn'
    saturn.resources = {
        Resource.HYDROGEN: 100.0
    }
    solar_system.add_location(saturn)
    
    # Saturn's Moons
    mimas = Moon()
    mimas.name = 'Mimas'
    mimas.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(mimas)
    
    enceladus = Moon()
    enceladus.name = 'Enceladus'
    enceladus.resources = {
        Resource.IRON: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(enceladus)
    
    tethys = Moon()
    tethys.name = 'Tethys'
    tethys.resources = {
        Resource.TITANIUM: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.COPPER: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.METHANE: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(tethys)
    
    dione = Moon()
    dione.name = 'Dione'
    dione.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(dione)
    
    rhea = Moon()
    rhea.name = 'Rhea'
    rhea.resources = {
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.SILVER: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(rhea)
    
    titan = Moon()
    titan.name = 'Titan'
    titan.resources = {
        Resource.TITANIUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.METHANE: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.SILVER: 100.0,
        Resource.GOLD: 100.0
    }
    solar_system.add_location(titan)
    
    hyperion = Moon()
    hyperion.name = 'Hyperion'
    hyperion.resources = {
        Resource.ALUMINUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.COPPER: 100.0,
        Resource.METHANE: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(hyperion)
    
    iapet = Moon()
    iapet.name = 'Iapet'
    iapet.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(iapet)
    
    phoebe = Moon()
    phoebe.name = 'Phoebe'
    phoebe.resources = {
        Resource.IRON: 100.0,
        Resource.TITANIUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.METHANE: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(phoebe)
    
    # Uranus
    uranus = Planet()
    uranus.name = 'Uranus'
    uranus.resources = {
        Resource.IRON: 100.0,
        Resource.TITANIUM: 100.0,
        Resource.COPPER: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.HELIUM: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.METHANE: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(uranus)
    
    # Uranus' Moons
    miranda = Moon()
    miranda.name = 'Miranda'
    miranda.resources = {
        Resource.IRON: 100.0,
        Resource.CARBON: 100.0,
        Resource.COPPER: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.SILVER: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(miranda)
    
    ariel = Moon()
    ariel.name = 'Ariel'
    ariel.resources = {
        Resource.ALUMINUM: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.METHANE: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(ariel)
    
    umbriel = Moon()
    umbriel.name = 'Umbriel'
    umbriel.resources = {
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(umbriel)
    
    titania = Moon()
    titania.name = 'Titania'
    titania.resources = {
        Resource.IRON: 100.0,
        Resource.CARBON: 100.0,
        Resource.COPPER: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.METHANE: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.SILVER: 100.0,
        Resource.GOLD: 100.0
    }
    solar_system.add_location(titania)
    
    oberon = Moon()
    oberon.name = 'Oberon'
    oberon.resources = {
        Resource.IRON: 100.0,
        Resource.TITANIUM: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.METHANE: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(oberon)
    
    # Neptune
    neptune = Planet()
    neptune.name = 'Neptune'
    neptune.resources = {
        Resource.IRON: 100.0,
        Resource.ALUMINUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.COPPER: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.METHANE: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.PLATINUM: 100.0
    }
    solar_system.add_location(neptune)
    
    # Neptune's Moons
    triton = Moon()
    triton.name = 'Triton'
    triton.resources = {
        Resource.TITANIUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.DEUTERIUM: 100.0,
        Resource.METHANE: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(triton)
    
    nereid = Moon()
    nereid.name = 'Nereid'
    nereid.resources = {
        Resource.CARBON: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(nereid)
    
    n3 = Moon()
    n3.name = 'N3'
    n3.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(n3)
    
    n4 = Moon()
    n4.name = 'N4'
    n4.resources = {
        Resource.SILICA: 100.0
    }
    solar_system.add_location(n4)
    
    # Pluto
    pluto = Planet()
    pluto.name = 'Pluto'
    pluto.resources = {
        Resource.CARBON: 100.0,
        Resource.HYDROGEN: 100.0,
        Resource.METHANE: 100.0,
        Resource.PALLADIUM: 100.0,
        Resource.PLATINUM: 100.0,
        Resource.GOLD: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(pluto)
    
    # Pluto's Moons
    charon = Moon()
    charon.name = 'Charon'
    charon.resources = {
        Resource.CARBON: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(charon)
    
    decuria = Moon()
    decuria.name = 'Decuria'
    decuria.resources = {
        Resource.TITANIUM: 100.0,
        Resource.CARBON: 100.0,
        Resource.SILVER: 100.0,
        Resource.SILICA: 100.0
    }
    solar_system.add_location(decuria)
    
    return solar_system




# ===== Module: data_model/grapplable/asteroid.py =====

@dataclass
class Asteroid(Grapplable):
    pass 


# ===== Module: data_model/grapplable/grapplable.py =====

@dataclass
class Grapplable:
    """
    Base class for all grapplable entities.
    """
    pass 


# ===== Module: data_model/grapplable/commspod_design.py =====

@dataclass
class CommspodDesign(Grapplable):
    pass 


# ===== Module: data_model/grapplable/artifact_part.py =====

@dataclass
class ArtifactPart(Grapplable):
    pass 


# ===== Module: data_model/vehicle/ios.py =====

@dataclass
class IOS(Vehicle):
    """IOS vehicle"""
    pass 


# ===== Module: data_model/vehicle/vehicle.py =====


@dataclass
class Vehicle(ABC):
    crew: Optional['Personnel'] = None
    equipment: List[Equipment] = field(default_factory=list)

    def advance_time(self):
        pass


# ===== Module: data_model/vehicle/shuttle.py =====

@dataclass
class Shuttle(Vehicle):
    """Shuttle vehicle"""
    pass 


# ===== Module: data_model/vehicle/scg.py =====

@dataclass
class SCG(Vehicle):
    """SCG vehicle"""
    pass 


# ===== Module: data_model/location/asteroid.py =====

@dataclass
class Asteroid(Location):
    """An asteroid location"""
    pass 


# ===== Module: data_model/location/moon.py =====

@dataclass
class Moon(Location):
    """A moon location"""
    pass 


# ===== Module: data_model/location/location.py =====


@dataclass
class Location(ABC):
    """Abstract base for all buildable locations"""
    name: Optional[str] = None
    orbital_base: Optional[Base] = None
    resource_base: Optional[Base] = None
    resources: Dict[Resource, float] = field(default_factory=dict)
    vehicles: List[Vehicle] = field(default_factory=list)
    
    def set_resource_base(self, base: ResourceBase):
        """Set the base for this location"""
        self.resource_base = base
        base.location = self 

    def set_orbital_base(self, base: OrbitalBase):
        """Set the base for this location"""
        self.orbital_base = base
        base.location = self 

    def get_resource_base(self) -> Optional[ResourceBase]:
        """Get the resource base for this location"""
        return self.resource_base

    def get_orbital_base(self) -> Optional[OrbitalBase]:
        """Get the orbital base for this location"""
        return self.orbital_base

    def advance_time(self):
        if self.orbital_base is not None:
            self.orbital_base.advance_time()
        if self.resource_base is not None:
            self.resource_base.advance_time()
        for vehicle in self.vehicles:
            vehicle.advance_time()



# ===== Module: data_model/location/planet.py =====

@dataclass
class Planet(Location):
    """A planet location"""
    pass 


# ===== Module: data_model/facility/shuttle_bay.py =====

@dataclass
class ShuttleBay(Facility):
    """Shuttle bay facility"""
    pass 


# ===== Module: data_model/facility/mining.py =====

@dataclass
class Mining(Facility):
    """Mining facility"""
    pass 


# ===== Module: data_model/facility/research.py =====

@dataclass
class Research(Facility):
    """Research facility"""
    researchers: Researcher = None
    researched_equipment: List[EquipmentType] = field(default_factory=list)
    current_research: Optional[EquipmentType] = None
    current_technician_days_remaining: int = 0
    current_technician_days_total: int = 0
    
    def can_add_researchers(self, number: int) -> bool:
        """Check if the number of researchers can be added"""
        if self.researchers is None:
            return True
        if self.researchers.count + number > 250:
            return False
        return True
    
    def add_researchers(self, number: int) -> bool:
        """Add researchers to the research facility"""
        if not self.can_add_researchers(number):
            return False
        if self.researchers is None:
            self.researchers = Researcher(count=number)
        else:
            self.researchers.count += number
        return True
    
    def start_research(self, equipment_type: EquipmentType, equipment_data: Equipment) -> bool:
        """Start researching an equipment type"""
        
        # Check if already researched
        if equipment_type in self.researched_equipment:
            return False
            
        if not self.can_research(equipment_type):
            return False
            
        self.current_research = equipment_type
        self.current_technician_days_total = equipment_data.get_research_technician_days()
        self.current_technician_days_remaining = self.current_technician_days_total
        return True
    

    
    def get_research_progress_percentage(self) -> int:
        """Get the current research progress as a percentage"""
        if self.current_research is None or self.current_technician_days_total == 0:
            return 0
        completed = self.current_technician_days_total - self.current_technician_days_remaining
        return int((completed / self.current_technician_days_total) * 100)
    
    def can_research(self, equipment_data: EquipmentType) -> bool:
        """Check if the equipment can be researched with current rank"""
        if self.researchers is None:
            return False
        if self.researchers is None or self.researchers.count == 0:
            return False

        equipment_data = Equipment.get_equipment(equipment_data)
        if equipment_data.required_rank==ResearcherRank.DOCTOR and self.researchers.rank == ResearcherRank.TECHNICIAN:
            return False
        elif equipment_data.required_rank==ResearcherRank.PROFESSOR and self.researchers.rank == ResearcherRank.DOCTOR:
            return False
        elif equipment_data.required_rank==ResearcherRank.PROFESSOR and self.researchers.rank == ResearcherRank.TECHNICIAN:
            return False
        return True

    def get_research_status(self, equipment_type: EquipmentType) -> str:
        """Get the status of a specific research item
        Returns one of: 'researched', 'in_progress', 'available', 'unavailable'
        """
        if equipment_type in self.researched_equipment:
            return 'researched'
        if self.current_research == equipment_type:
            return 'in_progress'
        
        if self.can_research(equipment_type):
            return 'available'
        else:
            return 'no_suitable_researchers'
    
    def get_leader_rank(self) -> Optional[ResearcherRank]:
        """Get the rank of the research leader"""
        if self.researchers is None:
            return None
        return self.researchers.rank
    
    def get_researcher_count(self) -> int:
        """Get the current number of researchers"""
        if self.researchers is None:
            return 0
        return self.researchers.count
    
    def get_max_researcher_count(self) -> int:
        """Get the maximum allowed number of researchers"""
        return 250
    
    def get_current_research(self) -> Optional[EquipmentType]:
        """Get the currently researched equipment type"""
        return self.current_research
    
    def get_researched_equipment(self) -> List[EquipmentType]:
        """Get the list of researched equipment types"""
        return self.researched_equipment.copy()

    def advance_time(self):
        """Advance research by a number of days"""
        if self.current_research is None or self.researchers is None:
            return
            
        # Calculate progress based on researcher count and their rank
        rank_multiplier = 1.0
        if self.researchers.rank == ResearcherRank.DOCTOR:
            rank_multiplier = 1.5
        elif self.researchers.rank == ResearcherRank.PROFESSOR:
            rank_multiplier = 2.0
            
        daily_progress = self.researchers.count * rank_multiplier
        technician_days_completed = int(daily_progress)
        self.current_technician_days_remaining -= technician_days_completed
        
        # Check if research is complete
        if self.current_technician_days_remaining <= 0:
            self.researched_equipment.append(self.current_research)
            self.current_research = None
            self.current_technician_days_remaining = 0
            self.current_technician_days_total = 0
            return
        
        return


# ===== Module: data_model/facility/spacedock.py =====

@dataclass
class Spacedock(Facility):
    """Spacedock for IOS and SCG"""
    pass 


# ===== Module: data_model/facility/facility.py =====


if TYPE_CHECKING:
    from data_model.base.base import Base

@dataclass
class Facility(ABC):

    def advance_time(self):
        pass


# ===== Module: data_model/facility/storage.py =====

@dataclass
class Storage(Facility):
    """Storage facility"""
    pass 


# ===== Module: data_model/facility/self_destruct_mechanism.py =====

@dataclass
class SelfDestructMechanism(Facility):
    """Self-destruct mechanism facility"""
    pass 


# ===== Module: data_model/facility/production.py =====

@dataclass
class Production(Facility):
    producers: Producer = None

    def can_add_producers(self, number: int) -> bool:
        if self.producers is None:
            return True
        if self.producers.count+number>200:
            return False
        return True

    def add_producers(self, number: int) -> bool:
        if not self.can_add_producers(number):
            return False
        if self.producers is None:
            self.producers = Producer(count=number)
        else:
            self.producers.count += number
        return True


# ===== Module: data_model/facility/training.py =====

if TYPE_CHECKING:
    from data_model.base.earth_base import EarthBase

@dataclass
class TrainingBatch:
    personnel_type: PersonnelType
    amount: int
    days_remaining: int
    
    def get_amount(self) -> int:
        return self.amount

    def advance_time(self):
        self.days_remaining -= 1

    def is_training_complete(self) -> bool:
        return self.days_remaining <= 0

@dataclass
class Training(Facility):
    available_population: int = 6000  # Initial population available for recruiting
    marines_in_training: TrainingBatch = None
    researchers_in_training: TrainingBatch = None
    producers_in_training: TrainingBatch = None
    marines_selector: int = 0
    researchers_selector: int = 0
    producers_selector: int = 0
    light_switched_on: bool = False

    def can_train_marines(self, number: int) -> bool:
        # Check if already training
        if self.marines_in_training is not None:
            return False


        if number > 41 or number<0:
            return False

        if self.available_population - number < 0:
            return False

        return True
    
    def can_train_researchers(self, number: int) -> bool:
        # Check if already training
        if self.researchers_in_training is not None:
            return False


        # Maximum 100 researchers per batch as per specification
        if number > 100 or number<0:
            return False
        
        if self.available_population - number < 0:
            return False

        return True
    
    def can_train_producers(self, number: int) -> bool:
        # Check if already training
        if self.producers_in_training is not None:
            return False

            
        # Maximum 100 producers per batch as per specification
        if number > 100 or number<0:
            return False

        if self.available_population - number < 0:
            return False

        return True
    
    def train_marines(self, number: int) -> bool:
        if not self.can_train_marines(number):
            return False
        self.marines_in_training = TrainingBatch(personnel_type=PersonnelType.MARINE, amount=number, days_remaining=7)
        self.available_population -= number
        return True
    
    def train_researchers(self, number: int) -> bool:
        if not self.can_train_researchers(number):
            return False
        self.researchers_in_training = TrainingBatch(personnel_type=PersonnelType.RESEARCHER, amount=number, days_remaining=14)
        self.available_population -= number
        return True
    
    def train_producers(self, number: int) -> bool:
        if not self.can_train_producers(number):
            return False
        self.producers_in_training = TrainingBatch(personnel_type=PersonnelType.PRODUCER, amount=number, days_remaining=7)
        self.available_population -= number
        return True

    def marines_selector_up(self) -> bool:
        if self.can_train_marines(self.marines_selector + 1):
            self.marines_selector += 1
            return True
        return False

    def marines_selector_down(self) -> bool:
        if self.can_train_marines(self.marines_selector - 1):
            self.marines_selector -= 1
            return True
        return False
    
    def researchers_selector_up(self) -> bool:
        if self.can_train_researchers(self.researchers_selector + 1):
            self.researchers_selector += 1
            return True
        return False
    
    def researchers_selector_down(self) -> bool:
        if self.can_train_researchers(self.researchers_selector - 1):
            self.researchers_selector -= 1
            return True
        return False
    
    def producers_selector_up(self) -> bool:
        if self.can_train_producers(self.producers_selector + 1):
            self.producers_selector += 1
            return True
        return False
    
    def producers_selector_down(self) -> bool:
        if self.can_train_producers(self.producers_selector - 1):
            self.producers_selector -= 1
            return True
        return False
        
    
    def toggle_light_switch(self) -> bool:
        self.light_switched_on = not self.light_switched_on
        return self.light_switched_on
    
    def start_pending_trainings(self):
        if self.marines_selector > 0 and self.marines_in_training is None:
            self.train_marines(self.marines_selector)
            
        if self.researchers_selector > 0 and self.researchers_in_training is None:
            self.train_researchers(self.researchers_selector)
            
        if self.producers_selector > 0 and self.producers_in_training is None:
            self.train_producers(self.producers_selector)
    
    def advance_time(self):
        # Start any pending trainings first
        self.start_pending_trainings()

        if self.marines_in_training is not None:
            self.marines_in_training.advance_time()
        if self.researchers_in_training is not None:
            self.researchers_in_training.advance_time()
        if self.producers_in_training is not None:
            self.producers_in_training.advance_time()
            



# ===== Module: data_model/system/system.py =====


@dataclass
class System(ABC):
    """Abstract base class for all planetary systems."""
    locations: List[Location] = field(default_factory=list)
    
    def add_location(self, location: Location):
        """Add a location to this system and set up bidirectional references.
        
        Args:
            location: The location to add to this system
        """
        location.system = self
        self.locations.append(location)



# ===== Module: data_model/system/solar_system.py =====

@dataclass
class SolarSystem(System):
    def advance_time(self):
        for location in self.locations:
            location.advance_time()


# ===== Module: data_model/system/star_system.py =====

@dataclass
class StarSystem(System):
    """Non-Sun star system"""
    pass 


# ===== Module: data_model/game_progression/initial_progress.py =====


class InitialProgress(GameProgression):
    """
    Initial game progression state.
    Defines the starting set of available technologies for a new game.
    """
    
    def _initialize_technologies(self) -> None:
        """Initialize the set of available technologies for the initial game state."""
        # Add the starting set of available technologies
        self._available_technologies.add(EquipmentType.DERRICK)
        self._available_technologies.add(EquipmentType.SHUTTLE_CHASSIS)
        self._available_technologies.add(EquipmentType.SHUTTLE_DRIVE)  # SHUTTLE_ENGINE in the requirements
        self._available_technologies.add(EquipmentType.CRYO_POD)
        self._available_technologies.add(EquipmentType.RESOURCE_POD)
        self._available_technologies.add(EquipmentType.TOOL_POD)
        self._available_technologies.add(EquipmentType.ORBITAL_FACTORY_FRAME) 


# ===== Module: data_model/game_progression/game_progression.py =====


class GameProgression(ABC):
    """
    Abstract base class for game progression states.
    Manages the state machine for game progression and tracks available technologies.
    """
    
    def __init__(self):
        """Initialize the game progression state."""
        self._available_technologies: Set[EquipmentType] = set()
        self._initialize_technologies()
    
    @abstractmethod
    def _initialize_technologies(self) -> None:
        """
        Initialize the set of available technologies for this progression state.
        Must be implemented by concrete subclasses.
        """
        pass
    
    @property
    def available_technologies(self) -> Set[EquipmentType]:
        """Get the set of currently available technologies."""
        return self._available_technologies
    
    def is_technology_available(self, technology: EquipmentType) -> bool:
        """Check if a specific technology is available in the current progression state."""
        return technology in self._available_technologies 


# ===== Module: data_model/resource/resource.py =====

class Resource(Enum):
    IRON = auto()
    TITANIUM = auto()
    ALUMINUM = auto()
    COPPER = auto()
    PALLADIUM = auto()
    PLATINUM = auto()
    SILVER = auto()
    GOLD = auto()
    HYDROGEN = auto()
    HELIUM = auto()
    DEUTERIUM = auto()
    METHANE = auto()
    CARBON = auto()
    SILICA = auto()
    HYDROGEN_METHANOL_FUEL = auto()
    HELIUM_DEUTERIUM_FUEL = auto() 


# ===== Module: data_model/rank/producer_rank.py =====

class ProducerRank(Enum):
    APPRENTICE = auto()
    ENGINEER = auto()
    EXPERT = auto() 


# ===== Module: data_model/rank/researcher_rank.py =====

class ResearcherRank(Enum):
    TECHNICIAN = auto()
    DOCTOR = auto()
    PROFESSOR = auto() 


# ===== Module: data_model/rank/rank.py =====

class Rank(Enum):
    pass 


# ===== Module: data_model/rank/marine_rank.py =====

class MarineRank(Enum):
    PILOT = auto()
    CAPTAIN = auto()
    ADMIRAL = auto()
    WARLORD = auto() 


# ===== Module: data_model/equipment/equipment.py =====
class EquipmentType(Enum):
    # Base Equipment
    DERRICK = auto()
    SELF_DESTRUCT_MECHANISM = auto()
    MASS_TRANSCIEVER = auto()
    AUTO_OPERATIONS_COMPUTER = auto()
    FUZ_LASER = auto()
    
    # Ship Equipment
    AUTO_CARGO_COMPUTER = auto()
    DRONE_FLEET_CONTROL_COMPUTER = auto()
    IOS_BATTLE_DRONE = auto()
    STAR_DRONE = auto()
    HYPERSPACE = auto()  # Hyperlight
    
    # Chassis
    SHUTTLE_CHASSIS = auto()
    IOS_CHASSIS = auto()
    SCG_CHASSIS = auto()
    
    # Drive Units
    SHUTTLE_DRIVE = auto()
    IOS_DRIVE = auto()
    SCG_DRIVE = auto()
    
    # Pods
    RESOURCE_POD = auto()
    TOOL_POD = auto()
    CRYO_POD = auto()
    PRISON_POD = auto()
    
    # Tools (installable on ToolPod)
    GRAPPLE = auto()
    INSTALLATION_REPAIR_EQUIPMENT = auto()  # Bandaid
    ASTEROID_MINING_ATTACHMENT = auto()
    RESOURCE_FACTORY_FRAME = auto()
    ORBITAL_FACTORY_FRAME = auto()
    COMMUNICATIONS_ADAPTER = auto()  # COMMSPOD
    PREJUDICE_TORPEDO_LAUNCHER = auto()
    PULSE_BLAST_LASER = auto()
    SONIC_BLASTER = auto()
    COMPLETE_ARTIFACT = auto()

class RequiredLocation(Enum):
    ANY_FACTORY = auto()
    ORBIT_ONLY = auto()

@dataclass
class Equipment:
    """
    Base class for all equipment. All equipment can be built and stored in storage.
    """
    type: EquipmentType
    costs: Optional[Dict[Resource, int]] = None 
    mass: Optional[int] = None
    required_rank: Optional[ResearcherRank] = None
    required_location: Optional[RequiredLocation] = None 
    
    @staticmethod
    def get_equipment(equipment_type: EquipmentType):
        """
        Return a specific equipment instance based on its type.
        This factory method creates and returns the appropriate equipment subclass.
        """
        # Base Equipment
        if equipment_type == EquipmentType.DERRICK:
            from data_model.equipment.base_equipment.derrick import Derrick
            return Derrick()
        elif equipment_type == EquipmentType.SELF_DESTRUCT_MECHANISM:
            from data_model.equipment.base_equipment.self_destruct_mechanism import SelfDestructMechanism
            return SelfDestructMechanism()
        elif equipment_type == EquipmentType.MASS_TRANSCIEVER:
            from data_model.equipment.base_equipment.mass_transciever import MassTransciever
            return MassTransciever()
        elif equipment_type == EquipmentType.AUTO_OPERATIONS_COMPUTER:
            from data_model.equipment.base_equipment.auto_operations_computer import AutoOperationsComputer
            return AutoOperationsComputer()
        elif equipment_type == EquipmentType.FUZ_LASER:
            from data_model.equipment.base_equipment.fuz_laser import FuzLaser
            return FuzLaser()
            
        # Ship Equipment
        elif equipment_type == EquipmentType.AUTO_CARGO_COMPUTER:
            from data_model.equipment.ship_equipment.auto_cargo_computer import AutoCargoComputer
            return AutoCargoComputer()
        elif equipment_type == EquipmentType.DRONE_FLEET_CONTROL_COMPUTER:
            from data_model.equipment.ship_equipment.drone_fleet_control_computer import DroneFleetControlComputer
            return DroneFleetControlComputer()
        elif equipment_type == EquipmentType.IOS_BATTLE_DRONE:
            from data_model.equipment.ship_equipment.ios_battle_drone import IOSBattleDrone
            return IOSBattleDrone()
        elif equipment_type == EquipmentType.STAR_DRONE:
            from data_model.equipment.ship_equipment.star_drone import StarDrone
            return StarDrone()
        elif equipment_type == EquipmentType.HYPERSPACE:
            from data_model.equipment.ship_equipment.hyperspace import Hyperspace
            return Hyperspace()
            
        # Chassis
        elif equipment_type == EquipmentType.SHUTTLE_CHASSIS:
            from data_model.equipment.ship_equipment.chassis.shuttle_chassis import ShuttleChassis
            return ShuttleChassis()
        elif equipment_type == EquipmentType.IOS_CHASSIS:
            from data_model.equipment.ship_equipment.chassis.ios_chassis import IOSChassis
            return IOSChassis()
        elif equipment_type == EquipmentType.SCG_CHASSIS:
            from data_model.equipment.ship_equipment.chassis.scg_chassis import SCGChassis
            return SCGChassis()
            
        # Drive Units
        elif equipment_type == EquipmentType.SHUTTLE_DRIVE:
            from data_model.equipment.ship_equipment.drive_unit.shuttle_drive import ShuttleDrive
            return ShuttleDrive()
        elif equipment_type == EquipmentType.IOS_DRIVE:
            from data_model.equipment.ship_equipment.drive_unit.ios_drive import IOSDrive
            return IOSDrive()
        elif equipment_type == EquipmentType.SCG_DRIVE:
            from data_model.equipment.ship_equipment.drive_unit.scg_drive import SCGDrive
            return SCGDrive()
            
        # Pods
        elif equipment_type == EquipmentType.RESOURCE_POD:
            from data_model.equipment.ship_equipment.pod.resource_pod import ResourcePod
            return ResourcePod()
        elif equipment_type == EquipmentType.TOOL_POD:
            from data_model.equipment.ship_equipment.pod.tool_pod import ToolPod
            return ToolPod()
        elif equipment_type == EquipmentType.CRYO_POD:
            from data_model.equipment.ship_equipment.pod.cryo_pod import CryoPod
            return CryoPod()
        elif equipment_type == EquipmentType.PRISON_POD:
            from data_model.equipment.ship_equipment.pod.prison_pod import PrisonPod
            return PrisonPod()
            
        # Tools
        elif equipment_type == EquipmentType.GRAPPLE:
            from data_model.equipment.ship_equipment.tool.grapple import Grapple
            return Grapple()
        elif equipment_type == EquipmentType.INSTALLATION_REPAIR_EQUIPMENT:
            from data_model.equipment.ship_equipment.tool.installation_repair_equipment import InstallationRepairEquipment
            return InstallationRepairEquipment()
        elif equipment_type == EquipmentType.ASTEROID_MINING_ATTACHMENT:
            from data_model.equipment.ship_equipment.tool.asteroid_mining_attachment import AsteroidMiningAttachment
            return AsteroidMiningAttachment()
        elif equipment_type == EquipmentType.RESOURCE_FACTORY_FRAME:
            from data_model.equipment.ship_equipment.tool.resource_factory_frame import ResourceFactoryFrame
            return ResourceFactoryFrame()
        elif equipment_type == EquipmentType.ORBITAL_FACTORY_FRAME:
            from data_model.equipment.ship_equipment.tool.orbital_factory_frame import OrbitalFactoryFrame
            return OrbitalFactoryFrame()
        elif equipment_type == EquipmentType.COMMUNICATIONS_ADAPTER:
            from data_model.equipment.ship_equipment.tool.communications_adapter import CommunicationsAdapter
            return CommunicationsAdapter()
        elif equipment_type == EquipmentType.PREJUDICE_TORPEDO_LAUNCHER:
            from data_model.equipment.ship_equipment.tool.prejudice_torpedo_launcher import PrejudiceTorpedoLauncher
            return PrejudiceTorpedoLauncher()
        elif equipment_type == EquipmentType.PULSE_BLAST_LASER:
            from data_model.equipment.ship_equipment.tool.pulse_blast_laser import PulseBlastLaser
            return PulseBlastLaser()
        elif equipment_type == EquipmentType.SONIC_BLASTER:
            from data_model.equipment.ship_equipment.tool.sonic_blaster import SonicBlaster
            return SonicBlaster()
        elif equipment_type == EquipmentType.COMPLETE_ARTIFACT:
            from data_model.equipment.ship_equipment.tool.complete_artifact import CompleteArtifact
            return CompleteArtifact()
        
        raise ValueError(f"Equipment type {equipment_type} not found")
    
    def get_research_technician_days(self) -> int:
        """
        Calculate the number of technician-days required to research this equipment.
        Scales proportionally with rank and the number of rare elements required.
        
        The base value is 1400 technician-days for the simplest equipment.
        """
        # Base research time
        base_days = 1400
        
        # Rank multiplier based on ResearcherRank enum
        rank_multiplier = 1.0  # Default for no rank requirement
        if self.required_rank is not None:
            if self.required_rank == ResearcherRank.TECHNICIAN:
                rank_multiplier = 1.0
            elif self.required_rank == ResearcherRank.DOCTOR:
                rank_multiplier = 1.5
            elif self.required_rank == ResearcherRank.PROFESSOR:
                rank_multiplier = 2.0
        
        # Count rare elements in costs
        rare_elements_count = 0
        if self.costs is not None:
            # Consider these resources as rare
            rare_resources = [
                Resource.PALLADIUM, 
                Resource.PLATINUM, 
                Resource.SILVER, 
                Resource.GOLD, 
                Resource.DEUTERIUM
            ]
            
            for resource in self.costs:
                if resource in rare_resources:
                    rare_elements_count += 1
        
        # Rare elements multiplier (each rare element adds 0.2 to multiplier)
        rare_multiplier = 1 + (rare_elements_count * 0.2)
        
        # Calculate total technician-days
        total_days = int(base_days * rank_multiplier * rare_multiplier)
        
        return total_days 


# ===== Module: data_model/equipment/tests/equipment_test.py =====

class EquipmentTest(unittest.TestCase):
    
    def test_get_research_technician_days(self):
        """Test the calculation of research technician-days for different equipment configurations."""
        
        # Test case 1: Basic equipment with no rank or costs specified
        basic_equipment = Equipment(type=EquipmentType.DERRICK)
        self.assertEqual(basic_equipment.get_research_technician_days(), 700)
        
        # Test case 2: Equipment with rank but no rare resources
        ranked_equipment = Equipment(
            type=EquipmentType.AUTO_OPERATIONS_COMPUTER, 
            required_rank=2,
            costs={
                Resource.IRON: 10,
                Resource.ALUMINUM: 5,
                Resource.CARBON: 3
            }
        )
        self.assertEqual(ranked_equipment.get_research_technician_days(), 1400)  # 700 * 2 * 1
        
        # Test case 3: Equipment with one rare resource
        single_rare_equipment = Equipment(
            type=EquipmentType.FUZ_LASER, 
            required_rank=1,
            costs={
                Resource.IRON: 20,
                Resource.COPPER: 5,
                Resource.GOLD: 1  # Rare resource
            }
        )
        self.assertEqual(single_rare_equipment.get_research_technician_days(), 840)  # 700 * 1 * 1.2
        
        # Test case 4: High rank equipment with multiple rare resources
        complex_equipment = Equipment(
            type=EquipmentType.HYPERSPACE, 
            required_rank=3,
            costs={
                Resource.TITANIUM: 50,
                Resource.PALLADIUM: 10,  # Rare resource
                Resource.PLATINUM: 5,    # Rare resource
                Resource.DEUTERIUM: 20   # Rare resource
            }
        )
        self.assertEqual(complex_equipment.get_research_technician_days(), 3360)  # 700 * 3 * 1.6
        
        # Test case 5: Highest rank equipment with all rare resources
        advanced_equipment = Equipment(
            type=EquipmentType.COMPLETE_ARTIFACT, 
            required_rank=5,
            costs={
                Resource.PALLADIUM: 50,  # Rare resource
                Resource.PLATINUM: 30,   # Rare resource
                Resource.SILVER: 20,     # Rare resource
                Resource.GOLD: 10,       # Rare resource
                Resource.DEUTERIUM: 100  # Rare resource
            }
        )
        self.assertEqual(advanced_equipment.get_research_technician_days(), 7000)  # 700 * 5 * 2.0

if __name__ == '__main__':
    unittest.main() 


# ===== Module: data_model/equipment/ship_equipment/auto_cargo_computer.py =====
@dataclass
class AutoCargoComputer(ShipEquipment):
    """
    Auto cargo computer ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.AUTO_CARGO_COMPUTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 4,
        Resource.ALUMINUM: 1,
        Resource.CARBON: 2,
        Resource.SILVER: 1
    }, init=False)
    mass: int = field(default=8, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/hyperspace.py =====
@dataclass
class Hyperspace(ShipEquipment):
    """
    Hyperspace (Hyperlight) ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.HYPERSPACE, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Cost not specified in documentation
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation
    pass 


# ===== Module: data_model/equipment/ship_equipment/drone_fleet_control_computer.py =====
@dataclass
class DroneFleetControlComputer(ShipEquipment):
    """
    Drone fleet control computer ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.DRONE_FLEET_CONTROL_COMPUTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.CARBON: 1,
        Resource.COPPER: 1,
        Resource.PLATINUM: 2,
        Resource.GOLD: 1
    }, init=False)
    mass: int = field(default=8, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/star_drone.py =====
@dataclass
class StarDrone(ShipEquipment):
    """
    Star drone ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.STAR_DRONE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 300,
        Resource.TITANIUM: 300,
        Resource.COPPER: 100,
        Resource.PALLADIUM: 90,
        Resource.PLATINUM: 80,
        Resource.SILVER: 95,
        Resource.GOLD: 50
    }, init=False)
    mass: int = field(default=1015, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/ship_equipment.py =====

@dataclass
class ShipEquipment(Equipment):
    """
    Equipment installable on ship chassis.
    """
    pass 


# ===== Module: data_model/equipment/ship_equipment/ios_battle_drone.py =====
@dataclass
class IOSBattleDrone(ShipEquipment):
    """
    IOS battle drone ship equipment.
    """
    type: EquipmentType = field(default=EquipmentType.IOS_BATTLE_DRONE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 120,
        Resource.TITANIUM: 120,
        Resource.ALUMINUM: 120,
        Resource.CARBON: 15,
        Resource.COPPER: 55,
        Resource.PALLADIUM: 30,
        Resource.PLATINUM: 30
    }, init=False)
    mass: int = field(default=490, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/pod/resource_pod.py =====
@dataclass
class ResourcePod(Pod):
    """
    Resource pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.RESOURCE_POD, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.COPPER: 1
    }, init=False)
    mass: int = field(default=4, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/pod/tool_pod.py =====
@dataclass
class ToolPod(Pod):
    """
    Tool pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.TOOL_POD, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.COPPER: 1
    }, init=False)
    mass: int = field(default=4, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/pod/pod.py =====

@dataclass
class Pod(ShipEquipment):
    """
    Base class for all ship pods.
    """
    pass 


# ===== Module: data_model/equipment/ship_equipment/pod/prison_pod.py =====
@dataclass
class PrisonPod(Pod):
    """
    Prison pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PRISON_POD, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Cost not specified in documentation
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: Optional[int] = None  # Rank not specified in documentation
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation
    pass 


# ===== Module: data_model/equipment/ship_equipment/pod/cryo_pod.py =====
@dataclass
class CryoPod(Pod):
    """
    Cryo pod equipment.
    """
    type: EquipmentType = field(default=EquipmentType.CRYO_POD, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.COPPER: 1
    }, init=False)
    mass: int = field(default=4, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/chassis/scg_chassis.py =====
@dataclass
class SCGChassis(Chassis):
    """
    SCG chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SCG_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 250,
        Resource.TITANIUM: 600,
        Resource.ALUMINUM: 400,
        Resource.COPPER: 185,
        Resource.PALLADIUM: 100,
        Resource.SILVER: 100,
        Resource.GOLD: 50
    }, init=False)
    mass: int = field(default=1685, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/chassis/chassis.py =====

@dataclass
class Chassis(ShipEquipment):
    """
    Base class for all ship chassis.
    """
    pass 


# ===== Module: data_model/equipment/ship_equipment/chassis/ios_chassis.py =====
@dataclass
class IOSChassis(Chassis):
    """
    IOS chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.IOS_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 100,
        Resource.TITANIUM: 250,
        Resource.ALUMINUM: 175,
        Resource.CARBON: 50,
        Resource.COPPER: 75
    }, init=False)
    mass: int = field(default=650, init=False)
    required_rank: int = field(default=ResearcherRank.DOCTOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/chassis/shuttle_chassis.py =====
@dataclass
class ShuttleChassis(Chassis):
    """
    Shuttle chassis equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SHUTTLE_CHASSIS, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 20,
        Resource.TITANIUM: 50,
        Resource.ALUMINUM: 35,
        Resource.CARBON: 10,
        Resource.COPPER: 15
    }, init=False)
    mass: int = field(default=130, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)


# ===== Module: data_model/equipment/ship_equipment/drive_unit/ios_drive.py =====
@dataclass
class IOSDrive(DriveUnit):
    """
    IOS drive unit equipment.
    """
    type: EquipmentType = field(default=EquipmentType.IOS_DRIVE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 30,
        Resource.TITANIUM: 50,
        Resource.COPPER: 15
    }, init=False)
    mass: int = field(default=95, init=False)
    required_rank: int = field(default=ResearcherRank.DOCTOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/drive_unit/drive_unit.py =====

@dataclass
class DriveUnit(ShipEquipment):
    """
    Base class for all ship drive units.
    """
    pass 


# ===== Module: data_model/equipment/ship_equipment/drive_unit/shuttle_drive.py =====
@dataclass
class ShuttleDrive(DriveUnit):
    """
    Shuttle drive unit equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SHUTTLE_DRIVE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 6,
        Resource.TITANIUM: 10,
        Resource.ALUMINUM: 4
    }, init=False)
    mass: int = field(default=20, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/drive_unit/scg_drive.py =====
@dataclass
class SCGDrive(DriveUnit):
    """
    SCG drive unit equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SCG_DRIVE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 50,
        Resource.TITANIUM: 100,
        Resource.COPPER: 30,
        Resource.PALLADIUM: 50,
        Resource.PLATINUM: 25,
        Resource.SILVER: 10
    }, init=False)
    mass: int = field(default=265, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/tool/complete_artifact.py =====
@dataclass
class CompleteArtifact(Tool):
    """
    Complete artifact tool equipment. Assembled from 8 artifact pieces.
    When activated on an SCG, triggers the game's ending sequence.
    """
    type: EquipmentType = field(default=EquipmentType.COMPLETE_ARTIFACT, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Special item assembled from 8 artifact pieces
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: Optional[int] = None  # Rank not specified in documentation
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation
    pass 


# ===== Module: data_model/equipment/ship_equipment/tool/pulse_blast_laser.py =====
@dataclass
class PulseBlastLaser(Tool):
    """
    Pulse blast laser tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PULSE_BLAST_LASER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.PALLADIUM: 120,
        Resource.PLATINUM: 30
    }, init=False)
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: Optional[int] = None  # Rank not specified in documentation
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation
    pass


# ===== Module: data_model/equipment/ship_equipment/tool/grapple.py =====
@dataclass
class Grapple(Tool):
    """
    Grapple tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.GRAPPLE, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 2,
        Resource.TITANIUM: 2,
        Resource.COPPER: 1
    }, init=False)
    mass: int = field(default=5, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)


# ===== Module: data_model/equipment/ship_equipment/tool/asteroid_mining_attachment.py =====
@dataclass
class AsteroidMiningAttachment(Tool):
    """
    Asteroid mining attachment tool.
    """
    type: EquipmentType = field(default=EquipmentType.ASTEROID_MINING_ATTACHMENT, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 6,
        Resource.TITANIUM: 70,
        Resource.ALUMINUM: 10,
        Resource.CARBON: 30,
        Resource.COPPER: 2,
        Resource.PLATINUM: 5,
        Resource.SILVER: 1
    }, init=False)
    mass: int = field(default=124, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/tool/prejudice_torpedo_launcher.py =====
@dataclass
class PrejudiceTorpedoLauncher(Tool):
    """
    Prejudice torpedo launcher tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.PREJUDICE_TORPEDO_LAUNCHER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 96,
        Resource.ALUMINUM: 45,
        Resource.COPPER: 10
    }, init=False)
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: Optional[int] = None  # Rank not specified in documentation
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation


# ===== Module: data_model/equipment/ship_equipment/tool/sonic_blaster.py =====
@dataclass
class SonicBlaster(Tool):
    """
    Sonic blaster tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SONIC_BLASTER, init=False)
    costs: Optional[Dict[Resource, int]] = None  # Cost not specified in documentation
    mass: Optional[int] = None  # Mass not specified in documentation
    required_rank: Optional[int] = None  # Rank not specified in documentation
    required_location: Optional[RequiredLocation] = None  # Location not specified in documentation
    pass 


# ===== Module: data_model/equipment/ship_equipment/tool/installation_repair_equipment.py =====
@dataclass
class InstallationRepairEquipment(Tool):
    """
    Installation repair equipment (Bandaid) tool.
    """
    type: EquipmentType = field(default=EquipmentType.INSTALLATION_REPAIR_EQUIPMENT, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 30,
        Resource.TITANIUM: 30,
        Resource.ALUMINUM: 30,
        Resource.CARBON: 30,
        Resource.COPPER: 30
    }, init=False)
    mass: int = field(default=150, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/tool/orbital_factory_frame.py =====
@dataclass
class OrbitalFactoryFrame(Tool):
    """
    Orbital factory frame tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.ORBITAL_FACTORY_FRAME, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 55,
        Resource.TITANIUM: 80,
        Resource.ALUMINUM: 50,
        Resource.CARBON: 25,
        Resource.COPPER: 40
    }, init=False)
    mass: int = field(default=250, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 


# ===== Module: data_model/equipment/ship_equipment/tool/resource_factory_frame.py =====
@dataclass
class ResourceFactoryFrame(Tool):
    """
    Resource factory frame tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.RESOURCE_FACTORY_FRAME, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 35,
        Resource.TITANIUM: 50,
        Resource.ALUMINUM: 20,
        Resource.CARBON: 15,
        Resource.COPPER: 30,
        Resource.PALLADIUM: 25,
        Resource.PLATINUM: 10,
        Resource.SILICA: 15
    }, init=False)
    mass: int = field(default=200, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass


# ===== Module: data_model/equipment/ship_equipment/tool/tool.py =====

@dataclass
class Tool(ShipEquipment):
    """
    Base class for all tools installable on ToolPod.
    """
    pass 


# ===== Module: data_model/equipment/ship_equipment/tool/communications_adapter.py =====
@dataclass
class CommunicationsAdapter(Tool):
    """
    Communications adapter (CommsPod) tool equipment.
    """
    type: EquipmentType = field(default=EquipmentType.COMMUNICATIONS_ADAPTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.ALUMINUM: 2,
        Resource.CARBON: 1,
        Resource.COPPER: 1,
        Resource.GOLD: 1
    }, init=False)
    mass: int = field(default=5, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)


# ===== Module: data_model/equipment/base_equipment/mass_transciever.py =====
@dataclass
class MassTransciever(BaseEquipment):
    """
    Mass transciever base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.MASS_TRANSCIEVER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 500,
        Resource.COPPER: 82,
        Resource.PALLADIUM: 100,
        Resource.GOLD: 40
    }, init=False)
    mass: int = field(default=722, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/base_equipment/auto_operations_computer.py =====
@dataclass
class AutoOperationsComputer(BaseEquipment):
    """
    Auto operations computer base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.AUTO_OPERATIONS_COMPUTER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.TITANIUM: 2,
        Resource.ALUMINUM: 1,
        Resource.CARBON: 1,
        Resource.COPPER: 1
    }, init=False)
    mass: int = field(default=5, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 


# ===== Module: data_model/equipment/base_equipment/fuz_laser.py =====
@dataclass
class FuzLaser(BaseEquipment):
    type: EquipmentType = field(default=EquipmentType.FUZ_LASER, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.COPPER: 5,
        Resource.PALLADIUM: 10,
        Resource.PLATINUM: 10
    }, init=False)
    mass: int = field(default=25, init=False)  # Mass is not specified in the docs, using an estimate
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/base_equipment/self_destruct_mechanism.py =====
@dataclass
class SelfDestructMechanism(BaseEquipment):
    """
    Self-destruct mechanism base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.SELF_DESTRUCT_MECHANISM, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.ALUMINUM: 5,
        Resource.COPPER: 1,
        Resource.PALLADIUM: 1,
        Resource.PLATINUM: 2
    }, init=False)
    mass: int = field(default=9, init=False)
    required_rank: int = field(default=ResearcherRank.PROFESSOR, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ORBIT_ONLY, init=False)
    pass 


# ===== Module: data_model/equipment/base_equipment/derrick.py =====
@dataclass
class Derrick(BaseEquipment):
    """
    Derrick base equipment.
    """
    type: EquipmentType = field(default=EquipmentType.DERRICK, init=False)
    costs: Dict[Resource, int] = field(default_factory=lambda: {
        Resource.IRON: 3,
        Resource.TITANIUM: 4,
        Resource.CARBON: 1
    }, init=False)
    mass: int = field(default=8, init=False)
    required_rank: int = field(default=ResearcherRank.TECHNICIAN, init=False)
    required_location: RequiredLocation = field(default=RequiredLocation.ANY_FACTORY, init=False)
    pass 


# ===== Module: data_model/equipment/base_equipment/base_equipment.py =====

@dataclass
class BaseEquipment(Equipment):
    """
    Equipment installable on bases.
    """
    pass 


# ===== Module: data_model/personnel/producer.py =====

@dataclass
class Producer(Personnel):
    """Personnel specialized in production"""
    pass 


# ===== Module: data_model/personnel/personnel.py =====

class PersonnelType(Enum):
    RESEARCHER = auto()
    PRODUCER = auto()
    MARINE = auto()

@dataclass
class Personnel(ABC):
    rank: Optional[Rank] = None
    count: int = 0


# ===== Module: data_model/personnel/researcher.py =====

@dataclass
class Researcher(Personnel):
    """Personnel specialized in research"""
    leader_name: Optional[str] = None
    rank: ResearcherRank = ResearcherRank.TECHNICIAN 


# ===== Module: data_model/personnel/marine.py =====

@dataclass
class Marine(Personnel):
    """Combat specialized personnel"""
    pass 


# ===== Module: data_model/base/resource_base.py =====

@dataclass
class ResourceBase(Base):
    """Base on a planetary surface for resource gathering"""
    deployed_derricks: int = 0
    resource_frames: int = 0
    REQUIRED_FRAMES = 2

    def __post_init__(self):
        """Initialize with ResourceBase-specific facilities"""
        super().__post_init__()
        
        # Add Mining facility
        mining_facility = Mining()
        self.facilities.append(mining_facility)
        
        # Add Storage facility
        storage_facility = Storage()
        self.facilities.append(storage_facility)
        
        # Add ShuttleBay facility
        shuttle_bay = ShuttleBay()
        self.facilities.append(shuttle_bay)

    def deploy_derrick(self):
        self.deployed_derricks += 1
        self.storage[EquipmentType.DERRICK] -= 1
    
    def add_resource_frame(self):
        """Add a resource factory frame to the base
        
        Returns:
            bool: True if frame was added, False if base already has max frames
        """
        if self.resource_frames < self.REQUIRED_FRAMES:
            self.resource_frames += 1
            return True
        return False
    
    @property
    def is_operational(self) -> bool:
        """Check if the base has enough frames to be operational
        
        Returns:
            bool: True if base has required number of frames
        """
        return self.resource_frames >= self.REQUIRED_FRAMES
        
    def get_mining_facility(self) -> Optional[Mining]:
        """Get the Mining facility
        
        Returns:
            Mining facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Mining):
                return facility
                
        return None
        
    def get_storage_facility(self) -> Optional[Storage]:
        """Get the Storage facility
        
        Returns:
            Storage facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Storage):
                return facility
                
        return None
        
    def get_shuttle_bay(self) -> Optional[ShuttleBay]:
        """Get the ShuttleBay facility
        
        Returns:
            ShuttleBay facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, ShuttleBay):
                return facility
                
        return None



# ===== Module: data_model/base/earth_base.py =====

@dataclass
class EarthBase(ResourceBase):
    
    def __post_init__(self):
        """Initialize with all Earth-specific facilities"""
        super().__post_init__()
        
        # Add the Training facility
        training_facility = Training()
        self.facilities.append(training_facility)
        
        # Add Research facility
        research_facility = Research()
        self.facilities.append(research_facility)
        
        # Add Production facility
        production_facility = Production()
        self.facilities.append(production_facility)
        
        
    @property
    def is_operational(self) -> bool:
        """
        EarthBase is always operational
        
        Returns:
            bool: Always True for EarthBase
        """
        return True
        
    def get_training_facility(self) -> Optional[Training]:
        """Get the Training facility
        
        Returns:
            Training facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Training):
                return facility
                
        return None 
        
    def get_research_facility(self) -> Optional[Research]:
        """Get the Research facility
        
        Returns:
            Research facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Research):
                return facility
                
        return None
        
    def get_production_facility(self) -> Optional[Production]:
        """Get the Production facility
        
        Returns:
            Production facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Production):
                return facility
                
        return None
        


# ===== Module: data_model/base/orbital_base.py =====

@dataclass
class OrbitalBase(Base):
    """Orbital base in space"""
    orbital_frames: int = 0
    REQUIRED_FRAMES = 8
    
    def __post_init__(self):
        """Initialize with OrbitalBase-specific facilities"""
        super().__post_init__()
        
        # Add Production facility
        production_facility = Production(base=self)
        self.facilities.append(production_facility)
        
        # Add Storage facility
        storage_facility = Storage(base=self)
        self.facilities.append(storage_facility)
        
        # Add ShuttleBay facility
        shuttle_bay = ShuttleBay(base=self)
        self.facilities.append(shuttle_bay)
        
        # Add Spacedock facility
        spacedock = Spacedock(base=self)
        self.facilities.append(spacedock)
    
    def add_orbital_frame(self):
        """Add an orbital factory frame to the base
        
        Returns:
            bool: True if frame was added, False if base already has max frames
        """
        if self.orbital_frames < self.REQUIRED_FRAMES:
            self.orbital_frames += 1
            return True
        return False
    
    @property
    def is_operational(self) -> bool:
        """Check if the base has enough frames to be operational
        
        Returns:
            bool: True if base has required number of frames
        """
        return self.orbital_frames >= self.REQUIRED_FRAMES
    
    def get_production_facility(self) -> Optional[Production]:
        """Get the Production facility
        
        Returns:
            Production facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Production):
                return facility
                
        return None
        
    def get_storage_facility(self) -> Optional[Storage]:
        """Get the Storage facility
        
        Returns:
            Storage facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Storage):
                return facility
                
        return None
        
    def get_shuttle_bay(self) -> Optional[ShuttleBay]:
        """Get the ShuttleBay facility
        
        Returns:
            ShuttleBay facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, ShuttleBay):
                return facility
                
        return None
        
    def get_spacedock(self) -> Optional[Spacedock]:
        """Get the Spacedock facility
        
        Returns:
            Spacedock facility or None if not found
        """
        for facility in self.facilities:
            if isinstance(facility, Spacedock):
                return facility
                
        return None 


# ===== Module: data_model/base/moon_base.py =====

@dataclass
class MoonBase(ResourceBase):
    """Base specific to Moon - uses bandaid device instead of resource frames"""
    bandaid_used: bool = False
    
    def __post_init__(self):
        """Initialize MoonBase facilities"""
        super().__post_init__()
        # Override ResourceBase frame count to ensure is_operational checks the bandaid status
        self.resource_frames = 0
    
    def use_bandaid_device(self) -> bool:
        """Use the Installation Repair Equipment (Bandaid) to make the base operational
        
        Returns:
            bool: True if bandaid was successfully used, False if already used
        """
        if not self.bandaid_used:
            self.bandaid_used = True
            return True
        return False
    
    @property
    def is_operational(self) -> bool:
        """Check if the bandaid device has been used to make the base operational
        
        Returns:
            bool: True if bandaid device has been used
        """
        return self.bandaid_used
    
    def add_resource_frame(self) -> bool:
        """Override the ResourceBase add_resource_frame method
        
        Returns:
            bool: Always False as MoonBase doesn't use resource frames
        """
        # MoonBase doesn't use resource frames, it uses the bandaid device
        return False 


# ===== Module: data_model/base/base.py =====



@dataclass
class Base(ABC):
    """Abstract base for all buildable structures"""
    facilities: List[Facility] = field(default_factory=list)
    personnel: List[Personnel] = field(default_factory=list)
    shuttle_bay_vehicle: Optional[Vehicle] = None
    spacedock_vehicle: Optional[Vehicle] = None
    equipment: Dict[Equipment, int] = field(default_factory=dict)
    resources: Dict[Resource, int] = field(default_factory=dict)
    storage: Dict[EquipmentType, int] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize equipment dictionary with all equipment types set to zero"""
        if not self.equipment:
            for equip_type in EquipmentType:
                self.equipment[equip_type] = 0
            
        if not self.resources:
            for resource_type in Resource:
                self.resources[resource_type] = 0
            
    def has_free_personnel_slot(self) -> bool:
        """Check if there is a free personnel slot available"""
        return len(self.personnel) < 4
    
    @property
    @abstractmethod
    def is_operational(self) -> bool:
        """
        Check if the base is operational. Derived classes must implement this.
        
        Returns:
            bool: True if the base is operational
        """
        pass
            
    def add_equipment(self, equipment_type: EquipmentType, amount: int = 1):
        """
        Add a specified amount of equipment to the base's storage
        
        Args:
            equipment_type: Type of equipment to add
            amount: Amount to add (default: 1)
        """
        current_amount = self.storage.get(equipment_type, 0)
        self.storage[equipment_type] = current_amount + amount
            
    def add_personnel(self, person: Personnel) -> bool:
        """
        Add a personnel to the base
        
        Args:
            person: The personnel to add
            
        Returns:
            bool: True if the personnel was added successfully
        """
        # Only possible to add if there is a slot left - max 4
        if len(self.personnel) >= 4:
            return False
        
        person.base = self
        self.personnel.append(person)
        return True
        
    def add_facility(self, facility: Facility) -> bool:
        """
        Add a facility to the base and establish bidirectional relationship
        
        Args:
            facility: The facility to add
            
        Returns:
            bool: True if the facility was added successfully
        """
        self.facilities.append(facility)
        return True

    def advance_time(self):
        for facility in self.facilities:
            facility.advance_time()



# ===== Module: coordinators/coordinator.py =====
class Coordinator:
    """
    Base class for all coordinators.
    Coordinators sit between the data model and the views, providing business logic
    and coordination between different components.
    """
    
    def __init__(self, game_state: GameState):
        """
        Initialize the coordinator with a game state.
        
        Args:
            game_state: The current game state
        """
        self._game_state = game_state 
   
    @property
    def game_state(self) -> GameState:
        """
        Get the current game state.
        
        Returns:
            The current game state
        """
        return self._game_state
        
    def get_earth_base(self) -> EarthBase:
        """
        Get the Earth base.
        """
        return self._game_state.get_earth_base()
        
        



# ===== Module: coordinators/research_coordinator.py =====

class ResearchCoordinator(Coordinator):
    """
    Coordinator for managing research facilities.
    Handles research projects and facility operations.
    """
    
    def get_research_facility(self):
        """
        Get the research facility from Earth base.
        
        Returns:
            The research facility
        """
        earth_base = self._game_state.get_earth_base()
        return earth_base.get_research_facility()
    
    def get_researcher_count(self):
        """
        Get the current number of researchers.
        
        Returns:
            The number of researchers
        """
        research_facility = self.get_research_facility()
        return research_facility.get_researcher_count()
    
    def get_leader_rank(self):
        """
        Get the rank of the research leader.
        
        Returns:
            The rank of the research leader
        """
        research_facility = self.get_research_facility()
        return research_facility.get_leader_rank()
    
    def get_max_researcher_count(self):
        """
        Get the maximum allowed number of researchers.
        
        Returns:
            The maximum number of researchers
        """
        research_facility = self.get_research_facility()
        return research_facility.get_max_researcher_count()
    
    def can_add_researchers(self, number):
        """
        Check if a number of researchers can be added.
        
        Args:
            number: The number of researchers to add
            
        Returns:
            True if researchers can be added, False otherwise
        """
        research_facility = self.get_research_facility()
        return research_facility.can_add_researchers(number)
    
    def add_researchers(self, number):
        """
        Add researchers to the research facility.
        
        Args:
            number: The number of researchers to add
            
        Returns:
            True if researchers were added, False otherwise
        """
        research_facility = self.get_research_facility()
        return research_facility.add_researchers(number)
    
    def get_current_research(self):
        """
        Get the currently researched equipment type.
        
        Returns:
            The equipment type being researched, or None if no research in progress
        """
        research_facility = self.get_research_facility()
        return research_facility.get_current_research()
    
    def get_researched_equipment(self):
        """
        Get the list of researched equipment types.
        
        Returns:
            List of researched equipment types
        """
        research_facility = self.get_research_facility()
        return research_facility.get_researched_equipment()
    
    def get_research_progress_percentage(self):
        """
        Get the current research progress as a percentage.
        
        Returns:
            Percentage of research completion (0-100)
        """
        research_facility = self.get_research_facility()
        return research_facility.get_research_progress_percentage()
    
    def start_research(self, equipment_type, equipment_data):
        """
        Start researching an equipment type.
        
        Args:
            equipment_type: The equipment type to research
            equipment_data: The equipment data containing research requirements
            
        Returns:
            True if research started successfully, False otherwise
        """
        research_facility = self.get_research_facility()
        return research_facility.start_research(equipment_type, equipment_data)
    
    def can_research(self, equipment_data: EquipmentType) -> bool:
        """
        Check if the equipment can be researched with current rank.
        
        Args:
            equipment_data: The equipment data containing research requirements
            
        Returns:
            True if the equipment can be researched, False otherwise
        """
        # Check if technology is available in current game progression
        if not self._game_state.current_game_progression.is_technology_available(equipment_data):
            return False
            
        research_facility = self.get_research_facility()
        return research_facility.can_research(equipment_data)
    
    def get_research_status(self, equipment_type: EquipmentType) -> str:
        """
        Get the status of a specific research item.
        
        Args:
            equipment_type: The equipment type to check
            
        Returns:
            String indicating status: 'researched', 'in_progress', 'available', or 'unavailable'
        """
        if not self._game_state.current_game_progression.is_technology_available(equipment_type):
            return 'unavailable'

        research_facility = self.get_research_facility()
        status = research_facility.get_research_status(equipment_type)
            
        return status
    


# ===== Module: coordinators/training_coordinator.py =====

class TrainingCoordinator(Coordinator):
    """
    Coordinator for managing training facilities.
    Handles training of personnel and facility operations.
    """
    
    def get_training_facility(self):
        """
        Get the training facility from Earth base.
        
        Returns:
            The training facility
        """
        earth_base = self._game_state.get_earth_base()
        return earth_base.get_training_facility()
    
    def toggle_light_switch(self):
        """
        Toggle the light switch in the training facility.
        
        Returns:
            The new state of the light switch (True for on, False for off)
        """
        training_facility = self.get_training_facility()
        return training_facility.toggle_light_switch()
    
    def get_available_population(self):
        """
        Get the available population for recruitment.
        
        Returns:
            The available population count
        """
        training_facility = self.get_training_facility()
        return training_facility.available_population
    
    # Marines selectors
    def get_marines_selector(self):
        """
        Get the current marines selection count.
        
        Returns:
            The marines selector count
        """
        training_facility = self.get_training_facility()
        return training_facility.marines_selector
    
    def marines_selector_up(self):
        """
        Increase the marines selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        if self.can_train_marines(1):
            training_facility = self.get_training_facility()
            return training_facility.marines_selector_up()
        return False
    
    def marines_selector_down(self):
        """
        Decrease the marines selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        if self.can_train_marines(-1):
            training_facility = self.get_training_facility()
            return training_facility.marines_selector_down()
        return False
    
    def can_train_marines(self, amount):
        """
        Check if marines can be trained at the specified amount.
        
        Args:
            amount: The number of marines to train
            
        Returns:
            True if marines can be trained, False otherwise
        """
            
        if self.get_earth_base() is None:
            return False
            
        if not self.get_earth_base().has_free_personnel_slot():
            return False

        training_facility = self.get_training_facility()
        return training_facility.can_train_marines(amount)
    
    def get_marines_in_training(self):
        """
        Get the marines currently in training.
        
        Returns:
            The marines in training object or None if no marines are training
        """
        training_facility = self.get_training_facility()
        return training_facility.marines_in_training
    
    # Researchers selectors
    def get_researchers_selector(self):
        """
        Get the current researchers selection count.
        
        Returns:
            The researchers selector count
        """
        training_facility = self.get_training_facility()
        return training_facility.researchers_selector
    
    def researchers_selector_up(self):
        """
        Increase the researchers selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        if self.can_train_researchers(1):
            training_facility = self.get_training_facility()
            return training_facility.researchers_selector_up()
        return False
    
    def researchers_selector_down(self):
        """
        Decrease the researchers selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        if self.can_train_researchers(-1):
            training_facility = self.get_training_facility()
            return training_facility.researchers_selector_down()
        return False
    
    def can_train_researchers(self, amount):
        """
        Check if researchers can be trained at the specified amount.
        
        Args:
            amount: The number of researchers to train
            
        Returns:
            True if researchers can be trained, False otherwise
        """
            
        research_facility = self.get_earth_base().get_research_facility()
        if research_facility is None:
            return False
            
        if not research_facility.can_add_researchers(amount):
            return False
        
        training_facility = self.get_training_facility()
        return training_facility.can_train_researchers(amount)
    
    def get_researchers_in_training(self):
        """
        Get the researchers currently in training.
        
        Returns:
            The researchers in training object or None if no researchers are training
        """
        training_facility = self.get_training_facility()
        return training_facility.researchers_in_training
    
    # Producers selectors
    def get_producers_selector(self):
        """
        Get the current producers selection count.
        
        Returns:
            The producers selector count
        """
        training_facility = self.get_training_facility()
        return training_facility.producers_selector
    
    def producers_selector_up(self):
        """
        Increase the producers selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        if self.can_train_producers(1):
            training_facility = self.get_training_facility()
            return training_facility.producers_selector_up()
        return False
    
    def producers_selector_down(self):
        """
        Decrease the producers selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        if self.can_train_producers(-1):
            training_facility = self.get_training_facility()
            return training_facility.producers_selector_down()
        return False
    
    def can_train_producers(self, amount):
        """
        Check if producers can be trained at the specified amount.
        
        Args:
            amount: The number of producers to train
            
        Returns:
            True if producers can be trained, False otherwise
        """
            
        # Get the production facility and check if it has space
        production_facility = self.get_earth_base().get_production_facility()
        if production_facility is None:
            return False
            
        if not production_facility.can_add_producers(amount):
            return False

        training_facility = self.get_training_facility()
        return training_facility.can_train_producers(amount)
    
    def get_producers_in_training(self):
        """
        Get the producers currently in training.
        
        Returns:
            The producers in training object or None if no producers are training
        """
        training_facility = self.get_training_facility()
        return training_facility.producers_in_training 


# ===== Module: coordinators/progression_controller.py =====


class ProgressionController(Controller):
    """
    Controller for managing game progression.
    Tracks current progression state and provides an interface for views to 
    access progression-related functionality.
    """
    
    def __init__(self, game_state=None):
        """
        Initialize the progression controller.
        
        Args:
            game_state: The current game state
        """
        super().__init__(game_state)
        self._progression_state: Optional[GameProgression] = None
        self.initialize_state()
    
    def initialize_state(self):
        """Initialize the progression state with the initial state."""
        self._progression_state = InitialState()
    
    def get_progression_state(self) -> Optional[GameProgression]:
        """Get the current progression state."""
        return self._progression_state
    
    def set_progression_state(self, state_class: Type[GameProgression]):
        """
        Set the progression state to a new state.
        
        Args:
            state_class: The class of the new state to set
        """
        self._progression_state = state_class()
    
    def get_available_technologies(self) -> Set[EquipmentType]:
        """
        Get the set of technologies available in the current progression state.
        
        Returns:
            A set of available EquipmentType values
        """
        if not self._progression_state:
            return set()
        return self._progression_state.available_technologies
    
    def is_technology_available(self, technology: EquipmentType) -> bool:
        """
        Check if a technology is available in the current progression state.
        
        Args:
            technology: The EquipmentType to check
            
        Returns:
            True if the technology is available, False otherwise
        """
        if not self._progression_state:
            return False
        return self._progression_state.is_technology_available(technology) 


# ===== Module: coordinators/game_coordinator.py =====

class GameCoordinator(Coordinator):
    """
    Central coordinator that manages the entire game state and provides access to
    specific coordinator subsystems.
    """
    
    def __init__(self, game_state: Optional[GameState] = None):
        """
        Initialize the game coordinator with all subsystem coordinators.
        
        Args:
            game_state: The game state to use, or create a new one if None
        """
        self._game_state = game_state or GameState()
        self._coordinators: Dict[str, Coordinator] = {}
        
        # Initialize coordinators
        self._initialize_coordinators()
 
    
    def _initialize_coordinators(self):
        """Initialize all coordinator subsystems."""
        
        # Create training coordinator
        self._coordinators['training'] = TrainingCoordinator(self._game_state)
        
        # Create research coordinator
        self._coordinators['research'] = ResearchCoordinator(self._game_state)
        
        # Create research coordinator
        self._coordinators['time'] = TimeCoordinator(self._game_state)
        # Add more coordinators as needed
    
    def get_coordinator(self, coordinator_name: str) -> Optional[Coordinator]:
        """
        Get a specific coordinator by name.
        
        Args:
            coordinator_name: The name of the coordinator to get
            
        Returns:
            The requested coordinator, or None if not found
        """
        return self._coordinators.get(coordinator_name)
    
    def get_training_coordinator(self) -> TrainingCoordinator:
        """
        Get the training coordinator.
        
        Returns:
            The training coordinator
        """
        return self._coordinators['training']
    
    def get_research_coordinator(self) -> ResearchCoordinator:
        """
        Get the research coordinator.
        
        Returns:
            The research coordinator
        """
        return self._coordinators['research']
    
    def get_time_coordinator(self) -> TimeCoordinator:
        """
        Get the time coordinator.
        
        Returns:
            The time coordinator
        """
        return self._coordinators['time']


# ===== Module: coordinators/time_coordinator.py =====

class TimeCoordinator(Coordinator):
    def advance_time(self):
        self._game_state.advance_time()
        self.finish_training()

    def get_game_time(self):
        return self._game_state.game_time
    
    def finish_training(self):
        earth_base = self.get_earth_base()
        if earth_base is None:
            return

        training = earth_base.get_training_facility()

        # Update marines training
        if training.marines_in_training is not None:
            if training.marines_in_training.is_training_complete():
                # Marines training complete - create a new marine squad
                if earth_base.add_personnel(Marine(count=training.marines_in_training.get_amount())):
                    training.marines_in_training = None
                    training.marines_selector = 0
        
        # Update researchers training
        if training.researchers_in_training is not None:
            if training.researchers_in_training.is_training_complete():
                # Researchers training complete - add to research facility
                research_facility = earth_base.get_research_facility()
                if research_facility is not None:
                    if research_facility.add_researchers(training.researchers_in_training.get_amount()):
                        training.researchers_in_training = None
                        training.researchers_selector = 0
        
        # Update producers training
        if training.producers_in_training is not None:
            if training.producers_in_training.is_training_complete():
                # Producers training complete - add to production facility
                production_facility = earth_base.get_production_facility()
                if production_facility is not None:
                    if production_facility.add_producers(training.producers_in_training.get_amount()):
                        training.producers_in_training = None
                        training.producers_selector = 0 
    


# ===== Module: web/interface.py =====

class WebInterface(TextInterface):
    """Web implementation of the TextInterface for use with Pyodide.
    
    This interface connects to JavaScript functions to handle input/output
    operations in a web browser environment.
    """
    
    def __init__(self):
        """Initialize the web interface."""
        # Color code mapping from abstract TextColor to HTML/CSS styles
        self.color_map = {
            # Foreground colors
            TextColor.FG_BLACK: "color: black;",
            TextColor.FG_RED: "color: red;",
            TextColor.FG_GREEN: "color: green;",
            TextColor.FG_YELLOW: "color: #cccc00;",
            TextColor.FG_BLUE: "color: blue;",
            TextColor.FG_MAGENTA: "color: magenta;",
            TextColor.FG_CYAN: "color: cyan;",
            TextColor.FG_WHITE: "color: white;",
            TextColor.FG_LIGHTBLACK: "color: #505050;",
            TextColor.FG_LIGHTRED: "color: #ff5050;",
            TextColor.FG_LIGHTGREEN: "color: #50ff50;",
            TextColor.FG_LIGHTYELLOW: "color: #ffff50;",
            TextColor.FG_LIGHTBLUE: "color: #5050ff;",
            TextColor.FG_LIGHTMAGENTA: "color: #ff50ff;",
            TextColor.FG_LIGHTCYAN: "color: #50ffff;",
            TextColor.FG_LIGHTWHITE: "color: #ffffff;",
            
            # Background colors
            TextColor.BG_BLACK: "background-color: black;",
            TextColor.BG_RED: "background-color: red;",
            TextColor.BG_GREEN: "background-color: green;",
            TextColor.BG_YELLOW: "background-color: #cccc00;",
            TextColor.BG_BLUE: "background-color: blue;",
            TextColor.BG_MAGENTA: "background-color: magenta;",
            TextColor.BG_CYAN: "background-color: cyan;",
            TextColor.BG_WHITE: "background-color: white;",
            
            # Styles
            TextColor.STYLE_BRIGHT: "font-weight: bold;",
            TextColor.STYLE_DIM: "opacity: 0.7;",
            TextColor.STYLE_NORMAL: "",
            TextColor.STYLE_RESET_ALL: "",
        }
        # Command history for each view
        self.command_history = {}
        self.history_position = {}
        self.current_view = None
        self.input_callback = None
        self._waiting_for_input = False
        self._last_input = ""
        
        # JS function references (will be set by game-web.py)
        self.js_print = None
        self.js_clear = None
        self.js_set_prompt = None
        self.js_set_input = None
        
    def print_line(self, text: str) -> None:
        """Print a line of text to the web output area."""
        processed_text = self._process_color_tags(text)
        if self.js_print:
            self.js_print(processed_text)
        else:
            # Fallback if not yet bound
            js.window.printOutput(processed_text)
    
    def clear_screen(self) -> None:
        """Clear the web output area."""
        if self.js_clear:
            self.js_clear()
        else:
            # Fallback if not yet bound
            js.window.clearOutput()
    
    def read_line(self, prompt: str = "") -> str:
        """Read a line of input from the web input field.
        
        This is a blocking operation that returns when the user submits input.
        """
        processed_prompt = self._process_color_tags(prompt)
        if self.js_set_prompt:
            self.js_set_prompt(processed_prompt)
        else:
            # Fallback if not yet bound
            js.window.setPrompt(processed_prompt)
        
        # Create a Promise-like mechanism using Pyodide
        self._waiting_for_input = True
        
        # Use pyodide synchronization
        import asyncio
        self._input_event = asyncio.Event()
        
        # Schedule the event to run in the background
        async def wait_for_input():
            await self._input_event.wait()
            return self._last_input
        
        # Create a future to wait on
        future = asyncio.ensure_future(wait_for_input())
        
        # This will block until JavaScript calls handle_input
        return asyncio.get_event_loop().run_until_complete(future)
    
    def handle_input(self, input_text: str) -> None:
        """Callback function to be called from JavaScript when input is submitted."""
        if self._waiting_for_input:
            self._last_input = input_text
            self._waiting_for_input = False
            
            # Signal that we have input
            import asyncio
            if hasattr(self, '_input_event'):
                self._input_event.set()
            
            # Add to history if we have a current view
            if self.current_view and input_text.strip():
                self.add_command_to_history(self.current_view, input_text)
            
            # Call any callback
            if self.input_callback:
                self.input_callback(input_text)
    
    def set_input_callback(self, callback: Callable[[str], None]) -> None:
        """Set a callback function to be called when input is received."""
        self.input_callback = callback
    
    def read_command(self, prompt: str = "", history: Optional[str] = None) -> str:
        """Read a command with view-specific history support."""
        # If a view name is provided, set it as current
        if history:
            self.current_view = history
            
        # Display history navigation help
        js.window.enableHistoryNavigation(True)
        
        # Get user input
        return self.read_line(prompt)
    
    def add_command_to_history(self, view_name: str, command: str) -> None:
        """Add a command to the history for a specific view."""
        if view_name not in self.command_history:
            self.command_history[view_name] = []
        
        # Don't add empty commands or duplicates at the end
        if command and (not self.command_history[view_name] or 
                        command != self.command_history[view_name][-1]):
            self.command_history[view_name].append(command)
            # Reset history position
            self.history_position[view_name] = len(self.command_history[view_name])
    
    def get_history(self, view_name: str) -> List[str]:
        """Get command history for a specific view."""
        return self.command_history.get(view_name, [])
    
    def history_up(self) -> None:
        """Navigate up in the command history."""
        if not self.current_view:
            return
            
        if self.current_view not in self.history_position:
            self.history_position[self.current_view] = len(self.get_history(self.current_view))
            
        if self.history_position[self.current_view] > 0:
            self.history_position[self.current_view] -= 1
            history = self.get_history(self.current_view)
            if history and self.history_position[self.current_view] < len(history):
                if self.js_set_input:
                    self.js_set_input(history[self.history_position[self.current_view]])
                else:
                    js.window.setInputValue(history[self.history_position[self.current_view]])
    
    def history_down(self) -> None:
        """Navigate down in the command history."""
        if not self.current_view:
            return
            
        history = self.get_history(self.current_view)
        if self.current_view in self.history_position:
            if self.history_position[self.current_view] < len(history):
                self.history_position[self.current_view] += 1
                if self.history_position[self.current_view] < len(history):
                    if self.js_set_input:
                        self.js_set_input(history[self.history_position[self.current_view]])
                    else:
                        js.window.setInputValue(history[self.history_position[self.current_view]])
                else:
                    if self.js_set_input:
                        self.js_set_input("")
                    else:
                        js.window.setInputValue("")
    
    def colorize(self, text: str, color_code: str) -> str:
        """Apply HTML/CSS styling to the given text."""
        if not text:
            return ""
            
        css_style = self.color_map.get(color_code, "")
        if css_style:
            return f'<span style="{css_style}">{text}</span>'
        return text
    
    def center_text(self, text: str, width: int = 80) -> str:
        """Center text using HTML."""
        return f'<div style="text-align: center; width: {width}ch;">{text}</div>'
    
    def _process_color_tags(self, text: str) -> str:
        """Process any <color_code> tags in the text and replace with HTML styling."""
        for color_code, css_style in self.color_map.items():
            if css_style:  # Skip empty styles
                text = text.replace(f"<{color_code}>", f'<span style="{css_style}">')
                
        # Replace any remaining closing tags
        text = text.replace("<style_reset_all>", "</span>")
        
        return text 


# ===== Module: textual/message_system.py =====

@dataclass
class Message:
    """A message to be displayed to the user"""
    text: str
    color: str
    timestamp: float
    
    def __str__(self):
        return f"<{self.color}>{self.text}<{TextColor.STYLE_RESET_ALL}>"

class MessageManager:
    """Manages messages to be displayed to the user across screen refreshes"""
    
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """Get the singleton instance of MessageManager"""
        if cls._instance is None:
            cls._instance = MessageManager()
        return cls._instance
    
    def __init__(self):
        """Initialize the message manager"""
        self.messages: List[Message] = []
        self.max_messages = 3  # Maximum number of messages to show
        self.message_ttl = 10.0  # Time to live for messages in seconds
        self.fixed_height = 5  # Fixed height of the message area (1 for top border + max_messages + 1 for bottom border)
    
    def add_message(self, text: str, color: str = TextColor.FG_WHITE):
        """Add a message to the buffer"""
        self.messages.append(Message(text, color, time.time()))
        # Clean up old messages
        self._clean_old_messages()
    
    def add_info(self, text: str):
        """Add an info message"""
        self.add_message(text, TextColor.FG_CYAN)
    
    def add_success(self, text: str):
        """Add a success message"""
        self.add_message(text, TextColor.FG_GREEN)
    
    def add_warning(self, text: str):
        """Add a warning message"""
        self.add_message(text, TextColor.FG_YELLOW)
    
    def add_error(self, text: str):
        """Add an error message"""
        self.add_message(text, TextColor.FG_RED)
    
    def _clean_old_messages(self):
        """Remove messages that are too old"""
        current_time = time.time()
        self.messages = [msg for msg in self.messages 
                        if current_time - msg.timestamp < self.message_ttl]
        
        # Keep only the most recent messages if we have too many
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
    
    def get_messages(self) -> List[Message]:
        """Get all current messages"""
        self._clean_old_messages()
        return self.messages
    
    def get_message_display(self) -> str:
        """Get a formatted string of all messages for display with fixed height"""
        # Top border
        result = "─" * 80 + "\n"
        
        # Get the most recent messages
        self._clean_old_messages()
        display_messages = self.messages[-self.max_messages:] if self.messages else []
        
        # Add existing messages
        for msg in display_messages:
            result += f"{msg}\n"
        
        # Add empty lines if we don't have enough messages to fill the space
        empty_lines = self.max_messages - len(display_messages)
        for _ in range(empty_lines):
            result += " " * 80 + "\n"
        
        # Bottom border
        result += "─" * 80
        
        return result
    
    def clear_messages(self):
        """Clear all messages"""
        self.messages = [] 


# ===== Module: textual/interface.py =====

class TextColor:
    """Platform-independent text color and style constants.
    
    This class provides color and style constants that are independent of the
    actual implementation (like colorama, ANSI, HTML, etc.). Interface implementations
    will map these to the appropriate platform-specific codes.
    """
    # Foreground colors
    FG_BLACK = "fg_black"
    FG_RED = "fg_red"
    FG_GREEN = "fg_green"
    FG_YELLOW = "fg_yellow"
    FG_BLUE = "fg_blue"
    FG_MAGENTA = "fg_magenta"
    FG_CYAN = "fg_cyan"
    FG_WHITE = "fg_white"
    FG_LIGHTBLACK = "fg_lightblack"
    FG_LIGHTRED = "fg_lightred"
    FG_LIGHTGREEN = "fg_lightgreen"
    FG_LIGHTYELLOW = "fg_lightyellow"
    FG_LIGHTBLUE = "fg_lightblue"
    FG_LIGHTMAGENTA = "fg_lightmagenta"
    FG_LIGHTCYAN = "fg_lightcyan"
    FG_LIGHTWHITE = "fg_lightwhite"
    
    # Background colors
    BG_BLACK = "bg_black"
    BG_RED = "bg_red"
    BG_GREEN = "bg_green"
    BG_YELLOW = "bg_yellow"
    BG_BLUE = "bg_blue"
    BG_MAGENTA = "bg_magenta"
    BG_CYAN = "bg_cyan"
    BG_WHITE = "bg_white"
    
    # Styles
    STYLE_BRIGHT = "style_bright"
    STYLE_DIM = "style_dim"
    STYLE_NORMAL = "style_normal"
    STYLE_RESET_ALL = "style_reset_all"

class TextInterface(ABC):
    """Abstract interface for text I/O operations.
    
    This interface abstracts the input/output operations needed by text-based
    interfaces, allowing implementations for different platforms (CLI, GUI, web, etc.)
    """
    
    @abstractmethod
    def print_line(self, text: str) -> None:
        """Print a line of text to the output."""
        pass
    
    @abstractmethod
    def clear_screen(self) -> None:
        """Clear the screen or output area."""
        pass
    
    @abstractmethod
    def read_line(self, prompt: str = "") -> str:
        """Read a line of input from the user.
        
        Args:
            prompt: Optional text prompt to display before reading input
            
        Returns:
            The input string entered by the user
        """
        pass
    
    @abstractmethod
    def read_command(self, prompt: str = "", history: Optional[List[str]] = None) -> str:
        """Read a command from the user with support for command history.
        
        Args:
            prompt: Text prompt to display before reading input
            history: Optional list of previous commands for up/down navigation
            
        Returns:
            The command string entered by the user
        """
        pass
    
    @abstractmethod
    def colorize(self, text: str, color_code: str) -> str:
        """Apply a color to the given text.
        
        Args:
            text: The text to colorize
            color_code: A color code from TextColor
            
        Returns:
            The colorized text string
        """
        pass
    
    @abstractmethod
    def center_text(self, text: str, width: int = 80) -> str:
        """Center text to a specified width.
        
        Args:
            text: The text to center
            width: The width to center within
            
        Returns:
            The centered text
        """
        pass




# ===== Module: textual/master_view.py =====

class MasterView:
    def __init__(self, game_coordinator: GameCoordinator = None, interface: TextInterface = None):
        # Ensure we have a game coordinator
        if game_coordinator is None:
            # Create a game coordinator if one wasn't provided
            self.game_coordinator = GameCoordinator()
        else:
            self.game_coordinator = game_coordinator
            
        # Set up interface
        if interface is None:
            from textual.cli_interface import CliInterface
            self.interface = CliInterface()
        else:
            self.interface = interface
            
        self.view_name = "master"
        self.message_manager = MessageManager.get_instance()
        self.time_coordinator = game_coordinator.get_time_coordinator()
    
    def clear_screen(self):
        """Clear the screen using the interface"""
        self.interface.clear_screen()
    
    def display(self):
        """Display the current game state using the interface"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            self.interface.print_line(messages_display)
            self.interface.print_line("")
            
        # Header with background color and centered text
        header = self.interface.center_text("=== TRITIUM - Main View ===", 80)
        header = self.interface.colorize(header, TextColor.BG_BLUE)
        header = self.interface.colorize(header, TextColor.FG_WHITE)
        header = self.interface.colorize(header, TextColor.STYLE_BRIGHT)
        self.interface.print_line(header)
        
        # Game time display
        time_display = f"Game Time: {self.time_coordinator.get_game_time()}"
        time_display = self.interface.colorize("Game Time: ", TextColor.FG_CYAN) + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", TextColor.FG_YELLOW)
        self.interface.print_line(time_display)
        
        # Commands section
        commands_header = self.interface.colorize("\nCommands:", TextColor.FG_GREEN)
        self.interface.print_line(commands_header)
        
        # Command list
        cmd_1 = "  " + self.interface.colorize(".    ", TextColor.FG_CYAN) + self.interface.colorize("- Advance time by one round", TextColor.FG_WHITE)
        cmd_2 = "  " + self.interface.colorize("e    ", TextColor.FG_CYAN) + self.interface.colorize("- Switch to Earth view", TextColor.FG_WHITE)
        cmd_3 = "  " + self.interface.colorize("s    ", TextColor.FG_CYAN) + self.interface.colorize("- Save game", TextColor.FG_WHITE)
        cmd_4 = "  " + self.interface.colorize("q    ", TextColor.FG_CYAN) + self.interface.colorize("- Quit game", TextColor.FG_WHITE)
        
        self.interface.print_line(cmd_1)
        self.interface.print_line(cmd_2)
        self.interface.print_line(cmd_3)
        self.interface.print_line(cmd_4)
    
    def advance_time(self):
        """Progress the game time by one round"""
        self.time_coordinator.advance_time()
        self.message_manager.add_info("Advanced time by one round")
    
    def log_message(self, message: str, message_type: str = "info"):
        """Log a message to be displayed across view refreshes"""
        if message_type == "info":
            self.message_manager.add_info(message)
        elif message_type == "success":
            self.message_manager.add_success(message)
        elif message_type == "warning":
            self.message_manager.add_warning(message)
        elif message_type == "error":
            self.message_manager.add_error(message)
        else:
            self.message_manager.add_message(message)
    
    def process_command(self, command: str):
        """Process a user command
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        if command == "q":
            return ('quit', None)
        elif command == "s":
            # Save the game
            if save_game(self.game_coordinator.game_state):
                self.log_message("Game saved successfully!", "success")
            else:
                self.log_message("Failed to save game", "error")
            return ('continue', None)
        elif command == ".":
            self.advance_time()
            return ('continue', None)
        elif command == "e":
            return ('switch', 'earth_view')
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return self.interface.colorize("Command: ", TextColor.FG_GREEN)
    
    def run(self):
        """Run this view's main loop"""
        while True:
            self.display()
            command = self.interface.read_command(self.get_prompt())
            action, new_view = self.process_command(command)
            
            if action == 'quit':
                return None
            elif action == 'switch':
                return new_view 


# ===== Module: textual/game_runner.py =====

class GameRunner:
    """Runs the game using a specific TextInterface implementation."""
    
    def __init__(self, interface: TextInterface):
        self.interface = interface
        self.game_coordinator = GameCoordinator()
    
    def run(self):
        """Run the game's main loop."""
        # Start with the master view
        current_view = MasterView(self.game_coordinator, self.interface)
        
        # Main game loop
        while current_view is not None:
            # Display the current view and get command
            current_view.display()
            command = self.interface.read_command(current_view.get_prompt())
            
            # Process the command and get the next view if needed
            action, next_view = current_view.process_command(command)
            
            if action == 'quit':
                # Exit the game
                self.interface.print_line("Thanks for playing!")
                return
            elif action == 'switch':
                if next_view == 'master_view':
                    current_view = MasterView(self.game_coordinator, self.interface)
                elif next_view == 'earth_view':
                    current_view = EarthView(self.game_coordinator, self.interface)
                elif next_view == 'training_view':
                    current_view = TrainingView(self.game_coordinator, self.interface)
                elif next_view == 'research_view':
                    current_view = ResearchView(self.game_coordinator, self.interface)

def start_game(interface_type='cli'):
    """Start the game with the specified interface type"""
    if interface_type == 'web':
        # Import web interface dynamically
        try:
            from web.interface import WebInterface
            interface = WebInterface()
        except ImportError:
            # Fall back to CLI if web interface isn't available
            print("Web interface not available, falling back to CLI")
            from cli.interface import CliInterface
            interface = CliInterface()
    else:
        # Use CLI interface by default
        try:
            from cli.interface import CliInterface
            interface = CliInterface()
        except ImportError:
            # This should not happen in a normal setup
            raise ImportError("CLI interface not available. Check your installation.")
    
    # Create and run the game
    runner = GameRunner(interface)
    return runner.run()

if __name__ == "__main__":
    # Create a game runner with the default CLI interface
    start_game('cli') 


# ===== Module: textual/bases/earth_view.py =====

class EarthView(MasterView):
    def __init__(self, game_coordinator: GameCoordinator = None, interface: TextInterface = None):
        super().__init__(game_coordinator, interface)
        self.view_name = "earth"
        self.time_coordinator = game_coordinator.get_time_coordinator()
    
    def display(self):
        """Display Earth-specific game state"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            self.interface.print_line(messages_display)
            self.interface.print_line("")
            
        # Header with background color and centered text
        header = self.interface.center_text("=== TRITIUM - Earth Base View ===", 80)
        header = self.interface.colorize(header, TextColor.BG_GREEN)
        header = self.interface.colorize(header, TextColor.FG_BLACK)
        header = self.interface.colorize(header, TextColor.STYLE_BRIGHT)
        self.interface.print_line(header)
        
        # Game time display
        time_display = self.interface.colorize("Game Time: ", TextColor.FG_CYAN) + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", TextColor.FG_YELLOW)
        self.interface.print_line(time_display)
        
        # Get Earth base through the coordinator
        earth_base = self.game_coordinator.get_earth_base()
        
        # Display Earth-specific information
        earth_status = self.interface.colorize("\nEarth Base Status:", TextColor.FG_GREEN)
        earth_status = self.interface.colorize(earth_status, TextColor.STYLE_BRIGHT)
        self.interface.print_line(earth_status)
        
        # Access and display training facility information if available
        try:
            training = earth_base.get_training_facility()
            if training:
                status = self.interface.colorize("  Training Facility: ", TextColor.FG_WHITE) + self.interface.colorize("Active", TextColor.FG_LIGHTGREEN)
                self.interface.print_line(status)
        except (AttributeError, NotImplementedError):
            status = self.interface.colorize("  Training Facility: ", TextColor.FG_WHITE) + self.interface.colorize("Not implemented yet", TextColor.FG_RED)
            self.interface.print_line(status)
            
        # Access and display research facility information if available
        try:
            research = earth_base.get_research_facility()
            if research:
                status = self.interface.colorize("  Research Facility: ", TextColor.FG_WHITE) + self.interface.colorize("Active", TextColor.FG_LIGHTGREEN)
                self.interface.print_line(status)
        except (AttributeError, NotImplementedError):
            status = self.interface.colorize("  Research Facility: ", TextColor.FG_WHITE) + self.interface.colorize("Not implemented yet", TextColor.FG_RED)
            self.interface.print_line(status)
        
        # Commands section
        commands_header = self.interface.colorize("\nCommands:", TextColor.FG_GREEN)
        self.interface.print_line(commands_header)
        
        # Command list
        cmd_1 = "  " + self.interface.colorize(".    ", TextColor.FG_CYAN) + self.interface.colorize("- Advance time by one round", TextColor.FG_WHITE)
        cmd_2 = "  " + self.interface.colorize("t    ", TextColor.FG_CYAN) + self.interface.colorize("- Go to Training Facility", TextColor.FG_WHITE)
        cmd_3 = "  " + self.interface.colorize("r    ", TextColor.FG_CYAN) + self.interface.colorize("- Go to Research Facility", TextColor.FG_WHITE)
        cmd_4 = "  " + self.interface.colorize("m    ", TextColor.FG_CYAN) + self.interface.colorize("- Return to main view", TextColor.FG_WHITE)
        cmd_5 = "  " + self.interface.colorize("q    ", TextColor.FG_CYAN) + self.interface.colorize("- Quit game", TextColor.FG_WHITE)
        
        self.interface.print_line(cmd_1)
        self.interface.print_line(cmd_2)
        self.interface.print_line(cmd_3)
        self.interface.print_line(cmd_4)
        self.interface.print_line(cmd_5)
    
    def process_command(self, command: str):
        """Process Earth view specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        if command == "m":
            return ('switch', 'master_view')
        elif command == "q":
            return ('quit', None)
        elif command == ".":
            # Advance time using the coordinator
            self.time_coordinator.advance_time()
            return ('continue', None)
        elif command == "t":
            return ('switch', 'training_view')
        elif command == "r":
            return ('switch', 'research_view')
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return self.interface.colorize("Earth Command: ", TextColor.FG_GREEN) 


# ===== Module: textual/facilities/training_view.py =====

class TrainingView(MasterView):
    def __init__(self, game_coordinator: GameCoordinator = None, interface: TextInterface = None):
        super().__init__(game_coordinator, interface)
        self.view_name = "training"
        
        # Get the training coordinator from the game coordinator
        self.training_coordinator = None
        if game_coordinator:
            self.training_coordinator = game_coordinator.get_training_coordinator()
            self.time_coordinator = game_coordinator.get_time_coordinator()
        
    def display(self):
        """Display Training Facility view"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
        # Header with background color
        print(self.interface.colorize("=== TRITIUM - Training Facility ===".center(80), fg="white", bg="magenta", style="bright"))
        print(self.interface.colorize(f"Game Time: ", fg="cyan") + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", fg="yellow"))
        
        # Get training facility from coordinator
        training_facility = self.training_coordinator.get_training_facility()
        
        # Show training facility status
        print(self.interface.colorize(f"\nAvailable Population for Recruitment: ", fg="lightblue", style="bright") + 
              self.interface.colorize(f"{self.training_coordinator.get_available_population()}", fg="yellow"))
        
        # Show marines training status
        print(self.interface.colorize("\nMarines Training:", fg="lightred", style="bright"))
        marines_in_training = self.training_coordinator.get_marines_in_training()
        if marines_in_training:
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("TRAINING IN PROGRESS", fg="yellow"))
            print(self.interface.colorize(f"  Amount: ", fg="white") + self.interface.colorize(f"{marines_in_training.amount}", fg="yellow"))
            print(self.interface.colorize(f"  Days Remaining: ", fg="white") + self.interface.colorize(f"{marines_in_training.days_remaining}", fg="yellow"))
        else:
            marines_selector = self.training_coordinator.get_marines_selector()
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("Ready for training", fg="green"))
            print(self.interface.colorize(f"  Current Selection: ", fg="white") + self.interface.colorize(f"{marines_selector}", fg="yellow") + self.interface.colorize(" marines", fg="white"))
            if not self.training_coordinator.can_train_marines(marines_selector):
                print(self.interface.colorize("  NOTE: ", fg="white") + self.interface.colorize("Cannot train marines at the current selection level", fg="red"))
        
        # Show researchers training status
        print(self.interface.colorize("\nResearchers Training:", fg="lightblue", style="bright"))
        researchers_in_training = self.training_coordinator.get_researchers_in_training()
        if researchers_in_training:
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("TRAINING IN PROGRESS", fg="yellow"))
            print(self.interface.colorize(f"  Amount: ", fg="white") + self.interface.colorize(f"{researchers_in_training.amount}", fg="yellow"))
            print(self.interface.colorize(f"  Days Remaining: ", fg="white") + self.interface.colorize(f"{researchers_in_training.days_remaining}", fg="yellow"))
        else:
            researchers_selector = self.training_coordinator.get_researchers_selector()
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("Ready for training", fg="green"))
            print(self.interface.colorize(f"  Current Selection: ", fg="white") + self.interface.colorize(f"{researchers_selector}", fg="yellow") + self.interface.colorize(" researchers", fg="white"))
            if not self.training_coordinator.can_train_researchers(researchers_selector):
                print(self.interface.colorize("  NOTE: ", fg="white") + self.interface.colorize("Cannot train researchers at the current selection level", fg="red"))
        
        # Show producers training status
        print(self.interface.colorize("\nProducers Training:", fg="lightyellow", style="bright"))
        producers_in_training = self.training_coordinator.get_producers_in_training()
        if producers_in_training:
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("TRAINING IN PROGRESS", fg="yellow"))
            print(self.interface.colorize(f"  Amount: ", fg="white") + self.interface.colorize(f"{producers_in_training.amount}", fg="yellow"))
            print(self.interface.colorize(f"  Days Remaining: ", fg="white") + self.interface.colorize(f"{producers_in_training.days_remaining}", fg="yellow"))
        else:
            producers_selector = self.training_coordinator.get_producers_selector()
            print(self.interface.colorize("  Status: ", fg="white") + self.interface.colorize("Ready for training", fg="green"))
            print(self.interface.colorize(f"  Current Selection: ", fg="white") + self.interface.colorize(f"{producers_selector}", fg="yellow") + self.interface.colorize(" producers", fg="white"))
            if not self.training_coordinator.can_train_producers(producers_selector):
                print(self.interface.colorize("  NOTE: ", fg="white") + self.interface.colorize("Cannot train producers at the current selection level", fg="red"))
        
        # Show light switch status
        light_status = 'ON' if training_facility.light_switched_on else 'OFF'
        light_color = "yellow" if training_facility.light_switched_on else "lightblack"
        print(self.interface.colorize(f"\nLight Switch: ", fg="cyan") + self.interface.colorize(f"{light_status}", fg=light_color))
        
        # Show commands
        print(self.interface.colorize("\nCommands:", fg="green", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize(".        ", fg="cyan") + 
              self.interface.colorize("- Advance time by one round", fg="white") + 
              self.interface.colorize(" (Training will start automatically)", fg="yellow"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("e        ", fg="cyan") + self.interface.colorize("- Return to Earth Base view", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("l        ", fg="cyan") + self.interface.colorize("- Toggle light switch", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("q        ", fg="cyan") + self.interface.colorize("- Quit game", fg="white"))
        
        print(self.interface.colorize("\nMarine Training Setup:", fg="lightred", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("m+N      ", fg="cyan") + self.interface.colorize("- Increase marines selection by N (e.g. m+10)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("m-N      ", fg="cyan") + self.interface.colorize("- Decrease marines selection by N (e.g. m-5)", fg="white"))
        
        print(self.interface.colorize("\nResearcher Training Setup:", fg="lightblue", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("r+N      ", fg="cyan") + self.interface.colorize("- Increase researchers selection by N (e.g. r+10)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("r-N      ", fg="cyan") + self.interface.colorize("- Decrease researchers selection by N (e.g. r-5)", fg="white"))
        
        print(self.interface.colorize("\nProducer Training Setup:", fg="lightyellow", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("p+N      ", fg="cyan") + self.interface.colorize("- Increase producers selection by N (e.g. p+10)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("p-N      ", fg="cyan") + self.interface.colorize("- Decrease producers selection by N (e.g. p-5)", fg="white"))
    
    def increase_marines_by(self, amount):
        """Increase marines selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_coordinator.marines_selector_up():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Increased marines selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not increase further after {success_count} increases", "warning")
        return success_count > 0
    
    def decrease_marines_by(self, amount):
        """Decrease marines selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_coordinator.marines_selector_down():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Decreased marines selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not decrease further after {success_count} decreases", "warning")
        return success_count > 0
    
    def increase_researchers_by(self, amount):
        """Increase researchers selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_coordinator.researchers_selector_up():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Increased researchers selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not increase further after {success_count} increases", "warning")
        return success_count > 0
    
    def decrease_researchers_by(self, amount):
        """Decrease researchers selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_coordinator.researchers_selector_down():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Decreased researchers selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not decrease further after {success_count} decreases", "warning")
        return success_count > 0
    
    def increase_producers_by(self, amount):
        """Increase producers selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_coordinator.producers_selector_up():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Increased producers selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not increase further after {success_count} increases", "warning")
        return success_count > 0
    
    def decrease_producers_by(self, amount):
        """Decrease producers selection by a specific amount"""
        success_count = 0
        for _ in range(amount):
            if self.training_coordinator.producers_selector_down():
                success_count += 1
            else:
                break
        
        if success_count > 0:
            self.log_message(f"Decreased producers selection by {success_count}", "success")
        if success_count < amount:
            self.log_message(f"Could not decrease further after {success_count} decreases", "warning")
        return success_count > 0
    
    def process_command(self, command: str):
        """Process Training Facility specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        # Check for numeric increment/decrement patterns
        m_plus_match = re.match(r'^m\+(\d+)$', command)
        m_minus_match = re.match(r'^m\-(\d+)$', command)
        r_plus_match = re.match(r'^r\+(\d+)$', command)
        r_minus_match = re.match(r'^r\-(\d+)$', command)
        p_plus_match = re.match(r'^p\+(\d+)$', command)
        p_minus_match = re.match(r'^p\-(\d+)$', command)
        
        if command == "e":
            return ('switch', 'earth_view')
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            # Advance time using the coordinator
            self.time_coordinator.advance_time()
            
            # Get training status after update
            training_facility = self.training_coordinator.get_training_facility()
            
            # Inform user about any training that started automatically
            marines_in_training = self.training_coordinator.get_marines_in_training()
            if marines_in_training and marines_in_training.days_remaining == 7:
                self.log_message(f"Started training {marines_in_training.amount} marines", "success")
                
            researchers_in_training = self.training_coordinator.get_researchers_in_training()
            if researchers_in_training and researchers_in_training.days_remaining == 14:
                self.log_message(f"Started training {researchers_in_training.amount} researchers", "success")
                
            producers_in_training = self.training_coordinator.get_producers_in_training()
            if producers_in_training and producers_in_training.days_remaining == 7:
                self.log_message(f"Started training {producers_in_training.amount} producers", "success")
                
            return ('continue', None)
        elif command == "l":
            # Toggle light switch using the coordinator
            is_on = self.training_coordinator.toggle_light_switch()
            status = "ON" if is_on else "OFF"
            self.log_message(f"Light switch toggled: {status}", "info")
            return ('continue', None)
        
        # Marine training commands
        elif m_plus_match:
            # Increase marines by a specific amount
            amount = int(m_plus_match.group(1))
            self.increase_marines_by(amount)
            return ('continue', None)
        elif m_minus_match:
            # Decrease marines by a specific amount
            amount = int(m_minus_match.group(1))
            self.decrease_marines_by(amount)
            return ('continue', None)
        
        # Researcher training commands
        elif r_plus_match:
            # Increase researchers by a specific amount
            amount = int(r_plus_match.group(1))
            self.increase_researchers_by(amount)
            return ('continue', None)
        elif r_minus_match:
            # Decrease researchers by a specific amount
            amount = int(r_minus_match.group(1))
            self.decrease_researchers_by(amount)
            return ('continue', None)
        
        # Producer training commands
        elif p_plus_match:
            # Increase producers by a specific amount
            amount = int(p_plus_match.group(1))
            self.increase_producers_by(amount)
            return ('continue', None)
        elif p_minus_match:
            # Decrease producers by a specific amount
            amount = int(p_minus_match.group(1))
            self.decrease_producers_by(amount)
            return ('continue', None)
        
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return self.interface.colorize("Training Command: ", fg="green") + self.interface.colorize("", fg="white") 


# ===== Module: textual/facilities/research_view.py =====
class ResearchView(MasterView):
    def __init__(self, game_coordinator: GameCoordinator = None, interface: TextInterface = None):
        super().__init__(game_coordinator, interface)
        self.view_name = "research"
        
        # Get the research coordinator from the game coordinator
        self.research_coordinator = None
        if game_coordinator:
            self.research_coordinator = game_coordinator.get_research_coordinator()
            self.time_coordinator = game_coordinator.get_time_coordinator()
        
    def display(self):
        """Display Research Facility view"""
        self.clear_screen()
        
        # Display any pending messages at the top
        messages_display = self.message_manager.get_message_display()
        if messages_display:
            print(messages_display)
            print()
            
        # Header with background color
        print(self.interface.colorize("=== TRITIUM - Research Facility ===".center(80), fg="white", bg="blue", style="bright"))
        print(self.interface.colorize(f"Game Time: ", fg="cyan") + self.interface.colorize(f"{self.time_coordinator.get_game_time()}", fg="yellow"))
        
        # Get research facility from coordinator
        research_facility = self.research_coordinator.get_research_facility()
        
        # Show research status
        current_research = self.research_coordinator.get_current_research()
        print(self.interface.colorize("\nResearch Status:", fg="lightblue", style="bright"))
        
        if current_research:
            equipment_data = Equipment.get_equipment(current_research)
            progress = self.research_coordinator.get_research_progress_percentage()
            print(self.interface.colorize("  Currently Researching: ", fg="white") + self.interface.colorize(f"{current_research.name}", fg="yellow"))
            print(self.interface.colorize("  Tech Level: ", fg="white") + self.interface.colorize(f"{equipment_data.required_rank}", fg="yellow"))
            print(self.interface.colorize("  Progress: ", fg="white") + self.interface.colorize(f"{progress}%", fg="yellow"))
        else:
            print(self.interface.colorize("  No research in progress. Select a project to begin.", fg="green"))
        
        # Show research options
        print(self.interface.colorize("\nResearch Projects:", fg="lightblue", style="bright"))
        
        # Fetch all equipment types and categorize them by status
        all_equipment = list(EquipmentType)
        
        researched_items = []
        in_progress_items = []
        available_items = []
        unavailable_items = []
        
        for item in all_equipment:
            equipment_data = Equipment.get_equipment(item)
            status = self.research_coordinator.get_research_status(item)
            
            if status == 'researched':
                researched_items.append((item, equipment_data))
            elif status == 'in_progress':
                in_progress_items.append((item, equipment_data))
            elif status == 'available':
                available_items.append((item, equipment_data))
            elif status == 'no_suitable_researchers':
                unavailable_items.append((item, equipment_data))
        
        # Display research items by category with different colors
        # Green for completed, Yellow for in-progress, Blue for available, Red for unavailable
        
        if researched_items:
            print(self.interface.colorize("  Completed Research:", fg="green"))
            for i, (item, equipment_data) in enumerate(researched_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", fg="green"))
        
        if in_progress_items:
            print(self.interface.colorize("  Research In Progress:", fg="yellow"))
            for i, (item, equipment_data) in enumerate(in_progress_items):
                progress = self.research_coordinator.get_research_progress_percentage()
                print(self.interface.colorize(f"    [{i+1}] {item.name} - {progress}% Complete (Tech Level: {equipment_data.required_rank})", fg="yellow"))
        
        if available_items:
            print(self.interface.colorize("  Available for Research:", fg="blue"))
            for i, (item, equipment_data) in enumerate(available_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", fg="blue"))
        
        if unavailable_items:
            print(self.interface.colorize("  Unavailable (Rank Requirements Not Met):", fg="red"))
            for i, (item, equipment_data) in enumerate(unavailable_items):
                print(self.interface.colorize(f"    [{i+1}] {item.name} (Tech Level: {equipment_data.required_rank})", fg="red"))
        
        # Show researcher information
        print(self.interface.colorize("\nResearch Team:", fg="lightblue", style="bright"))
        researcher_count = self.research_coordinator.get_researcher_count()
        max_researchers = self.research_coordinator.get_max_researcher_count()
        leader_rank = self.research_coordinator.get_leader_rank()
        
        if leader_rank:
            print(self.interface.colorize(f"  Leader Rank: ", fg="white") + self.interface.colorize(f"{leader_rank.name}", fg="yellow"))
        else:
            print(self.interface.colorize(f"  Leader Rank: ", fg="white") + self.interface.colorize("No Leader", fg="red"))
            
        print(self.interface.colorize(f"  Researchers: ", fg="white") + self.interface.colorize(f"{researcher_count}/{max_researchers}", fg="yellow"))
        
        # Show commands
        print(self.interface.colorize("\nCommands:", fg="green", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize(".        ", fg="cyan") + self.interface.colorize("- Advance time by one round", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("e        ", fg="cyan") + self.interface.colorize("- Return to Earth Base view", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("q        ", fg="cyan") + self.interface.colorize("- Quit game", fg="white"))
        
        print(self.interface.colorize("\nResearch Commands:", fg="lightblue", style="bright"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("r#       ", fg="cyan") + self.interface.colorize("- Start research on available item # (e.g. r2)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("v#       ", fg="cyan") + self.interface.colorize("- View details of item # (e.g. v1)", fg="white"))
        print(self.interface.colorize("  ", fg="white") + self.interface.colorize("a#       ", fg="cyan") + self.interface.colorize("- Add # researchers (e.g. a10)", fg="white"))
    
    def process_command(self, command: str):
        """Process Research Facility specific commands
        
        Returns:
            tuple: (action, new_view)
            action: 'quit', 'continue', or 'switch'
            new_view: New view instance to switch to, or None
        """
        command = command.strip().lower()
        
        # Check for numeric patterns
        research_match = re.match(r'^r(\d+)$', command)
        view_match = re.match(r'^v(\d+)$', command)
        add_researchers_match = re.match(r'^a(\d+)$', command)
        
        if command == "e":
            return ('switch', 'earth_view')
        elif command == "q":
            # Quit the entire game
            return ('quit', None)
        elif command == ".":
            # Advance time using the coordinator
            self.time_coordinator.advance_time()
            
            # Check if research completed
            current_research_before = self.research_coordinator.get_current_research()
            if current_research_before:
                current_research_after = self.research_coordinator.get_current_research()
                if current_research_after is None:
                    # Research completed
                    self.log_message(f"Research completed: {current_research_before.name}", "success")
                else:
                    # Research in progress
                    progress = self.research_coordinator.get_research_progress_percentage()
                    self.log_message(f"Research progress: {progress}% complete", "info")
            
            return ('continue', None)
        
        # Research commands
        elif research_match:
            # Start research on item #
            index = int(research_match.group(1))
            
            # Get available items 
            available_items = []
            for item in list(EquipmentType):
                equipment_data = Equipment.get_equipment(item)
                if self.research_coordinator.get_research_status(item) == 'available':
                    available_items.append((item, equipment_data))
            
            if 1 <= index <= len(available_items):
                equipment_type, equipment_data = available_items[index-1]
                if self.research_coordinator.start_research(equipment_type, equipment_data):
                    self.log_message(f"Started research on {equipment_type.name}", "success")
                else:
                    self.log_message(f"Cannot start research on {equipment_type.name}", "error")
            else:
                self.log_message(f"Invalid research item number: {index}", "error")
            
            return ('continue', None)
        
        # View commands
        elif view_match:
            # View details of item #
            index = int(view_match.group(1))
            
            # Get all items
            all_items = []
            for item in list(EquipmentType):
                equipment_data = Equipment.get_equipment(item)
                all_items.append((item, equipment_data))
            
            if 1 <= index <= len(all_items):
                equipment_type, equipment_data = all_items[index-1]
                status = self.research_coordinator.get_research_status(equipment_type)
                
                details = f"Item: {equipment_type.name}\n"
                details += f"Tech Level: {equipment_data.required_rank}\n"
                
                if status == 'researched':
                    details += f"Status: Researched\n"
                    details += f"Mass: {equipment_data.mass}\n"
                    details += f"Required Minerals: {equipment_data.required_minerals}\n"
                    details += f"Production Location: {'Orbit' if equipment_data.orbit_producible else 'Earth'}"
                elif status == 'in_progress':
                    progress = self.research_coordinator.get_research_progress_percentage()
                    details += f"Status: In Progress ({progress}% complete)"
                elif status == 'available':
                    details += f"Status: Available for Research"
                elif status == 'unavailable':
                    details += f"Status: Unavailable (Requires higher researcher rank)"
                
                self.log_message(details, "info")
            else:
                self.log_message(f"Invalid item number: {index}", "error")
            
            return ('continue', None)
            
        else:
            self.log_message(f"Unknown command: {command}", "error")
            return ('continue', None)
    
    def get_prompt(self):
        """Return the command prompt for this view"""
        return self.interface.colorize("Research Command: ", fg="green") + self.interface.colorize("", fg="white") 


# ========== END OF BUNDLED CODE ==========

# Launcher code
if __name__ == "__main__":
    # Web mode check
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--web":
        # For web mode
        try:
            from web.interface import WebInterface
            from textual.game_runner import start_game as start_game_internal
            
            def start_game():
                return start_game_internal(interface_type='web')
                
            result = start_game()
            print(result)
        except Exception as e:
            print(f"Error starting web game: {str(e)}")
    else:
        # For CLI mode
        try:
            from cli.interface import CliInterface
            from textual.game_runner import start_game as start_game_internal
            
            def start_game():
                return start_game_internal(interface_type='cli')
                
            result = start_game()
            print(result)
        except Exception as e:
            print(f"Error starting CLI game: {str(e)}")
