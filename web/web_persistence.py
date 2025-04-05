import pickle
import base64
import js
from typing import Optional
from data_model.game_state import GameState
from textual.persistence import Persistence

class WebPersistence(Persistence):
    """Handles saving and loading game state for Web interface."""
    
    # Key used in localStorage
    DEFAULT_STORAGE_KEY = "game_save"
    
    def __init__(self, storage_key: str = DEFAULT_STORAGE_KEY):
        self.storage_key = storage_key
    
    def save_game_instance(self, game_state: GameState, storage_key: str = None) -> bool:
        """
        Instance method to save the current game state to browser's localStorage.
        
        Args:
            game_state: The GameState object to save
            storage_key: Optional custom storage key (defaults to self.storage_key)
            
        Returns:
            bool: True if the save was successful, False otherwise
        """
        if storage_key is None:
            storage_key = self.storage_key
            
        try:
            # Serialize the game state to a string
            serialized_data = pickle.dumps(game_state)
            
            # Convert to base64 for storage
            base64_data = base64.b64encode(serialized_data).decode('utf-8')
            
            # Save to browser storage
            js.window.localStorage.setItem(storage_key, base64_data)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False
    
    # Implement the abstract method from Persistence
    def save_game(self, game_state: GameState, **kwargs) -> bool:
        """
        Implementation of abstract method from Persistence
        """
        storage_key = kwargs.get('storage_key', None)
        return self.save_game_instance(game_state, storage_key)

    def load_game_instance(self, storage_key: str = None) -> Optional[GameState]:
        """
        Instance method to load a game state from browser's localStorage.
        
        Args:
            storage_key: Optional custom storage key (defaults to self.storage_key)
            
        Returns:
            Optional[GameState]: The loaded GameState object or None if loading failed
        """
        if storage_key is None:
            storage_key = self.storage_key
            
        try:
            # Check if there's a saved game in localStorage
            if not hasattr(js.window, 'localStorage') or not js.window.localStorage.getItem(storage_key):
                print("No saved game found in browser storage")
                return None
                
            # Get the saved data
            base64_data = js.window.localStorage.getItem(storage_key)
            
            # Convert from base64
            serialized_data = base64.b64decode(base64_data)
            
            # Deserialize to a GameState object
            return pickle.loads(serialized_data)
        except Exception as e:
            print(f"Error loading game: {e}")
            return None
    
    # Implement the abstract method from Persistence
    def load_game(self, **kwargs) -> Optional[GameState]:
        """
        Implementation of abstract method from Persistence
        """
        storage_key = kwargs.get('storage_key', None)
        return self.load_game_instance(storage_key)