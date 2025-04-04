from coordinators.coordinator import Coordinator
from data_model.personnel.marine import Marine

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
    