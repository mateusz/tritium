import pickle
import os
from typing import Optional
from data_model.game_state import GameState
from textual.persistence import Persistence

class CliPersistence(Persistence):
    """Handles saving and loading game state for CLI interface."""
    
    DEFAULT_SAVE_FILE = "savegame.dat"
    
    def __init__(self, save_file: str = DEFAULT_SAVE_FILE):
        self.save_file = save_file
    
    # Implement the abstract method from Persistence
    def save_game(self, game_state: GameState, **kwargs) -> bool:
        """
        Implementation of abstract method from Persistence
        """
        file_path = kwargs.get('file_path', None)

        if file_path is None:
            file_path = self.save_file
            
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

    # Implement the abstract method from Persistence
    def load_game(self, **kwargs) -> Optional[GameState]:
        """
        Implementation of abstract method from Persistence
        """
        file_path = kwargs.get('file_path', None)

        if file_path is None:
            file_path = self.save_file
            
        try:
            if not os.path.exists(file_path):
                print(f"Save file not found: {file_path}")
                return None
                
            with open(file_path, 'rb') as save_file:
                return pickle.load(save_file)
        except Exception as e:
            print(f"Error loading game: {e}")
            return None
