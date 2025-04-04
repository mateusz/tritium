from data_model.initialise import initialize_solar_system
from data_model.base.earth_base import EarthBase
from data_model.system.solar_system import SolarSystem
from data_model.game_progression.game_progression import GameProgression
from data_model.game_progression.initial_progress import InitialProgress
import pickle

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
    