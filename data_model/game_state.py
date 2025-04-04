from data_model.initialise import initialize_solar_system
from data_model.base.earth_base import EarthBase
from data_model.system.solar_system import SolarSystem
from data_model.game_progression.game_progression import GameProgression
from data_model.game_progression.initial_progress import InitialProgress
class GameState:
    solar_system: SolarSystem
    game_time: int
    current_game_progression: GameProgression

    def __init__(self):
        self.current_game_progression = InitialProgress()
        self.solar_system = initialize_solar_system()
        self.game_time = 0

    def update(self):
        self.game_time += 1
        self.solar_system.update()

    def get_location_by_name(self, name: str):
        for location in self.solar_system.locations:
            if location.name == name:
                return location
        return None

    def get_earth_base(self) -> EarthBase:
        return self.get_location_by_name('Earth').get_resource_base()
    