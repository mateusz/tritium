from data_model.initialise import initialize_solar_system
class GameState:
    def __init__(self):
        self.solar_system = initialize_solar_system()
        self.game_time = 0

    def update(self):
        self.game_time += 1
        self.solar_system.update()
