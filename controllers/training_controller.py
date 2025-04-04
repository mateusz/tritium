from controllers.controller import Controller
from data_model.facility.training import Training

class TrainingController(Controller):
    """
    Controller for managing training facilities.
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
        training_facility = self.get_training_facility()
        return training_facility.marines_selector_up()
    
    def marines_selector_down(self):
        """
        Decrease the marines selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        training_facility = self.get_training_facility()
        return training_facility.marines_selector_down()
    
    def can_train_marines(self, amount):
        """
        Check if marines can be trained at the specified amount.
        
        Args:
            amount: The number of marines to train
            
        Returns:
            True if marines can be trained, False otherwise
        """
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
        training_facility = self.get_training_facility()
        return training_facility.researchers_selector_up()
    
    def researchers_selector_down(self):
        """
        Decrease the researchers selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        training_facility = self.get_training_facility()
        return training_facility.researchers_selector_down()
    
    def can_train_researchers(self, amount):
        """
        Check if researchers can be trained at the specified amount.
        
        Args:
            amount: The number of researchers to train
            
        Returns:
            True if researchers can be trained, False otherwise
        """
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
        training_facility = self.get_training_facility()
        return training_facility.producers_selector_up()
    
    def producers_selector_down(self):
        """
        Decrease the producers selector by 1.
        
        Returns:
            True if successful, False otherwise
        """
        training_facility = self.get_training_facility()
        return training_facility.producers_selector_down()
    
    def can_train_producers(self, amount):
        """
        Check if producers can be trained at the specified amount.
        
        Args:
            amount: The number of producers to train
            
        Returns:
            True if producers can be trained, False otherwise
        """
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