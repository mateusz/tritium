from data_model.initialise import initialize_solar_system
from data_model.base.earth_base import EarthBase

class GameState:
    def __init__(self):
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
    