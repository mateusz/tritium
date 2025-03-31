from data_model.initialise import initialize_solar_system
class GameState:
    def __init__(self):
        self.solar_system = initialize_solar_system()
        self.game_time = 0
        self.game_state = GameState.GAME_STATE_PLAYING

    def update(self):
        self.game_time += 1
        self.solar_system.update()
