import pickle
import os
from typing import Optional
from data_model.game_state import GameState

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