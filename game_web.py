import sys
import js
import asyncio
import pickle
import base64
from pyodide.ffi import create_proxy

# Import the modules
from data_model.game_state import GameState
from coordinators.game_coordinator import GameCoordinator
from web.web_persistence import WebPersistence
from textual.game_runner import GameRunner
from textual.interface import TextColor
from web.web_interface import WebInterface

# Global variables to hold state
web_interface = None
game_runner = None
web_persistence = None

def setup_js_bindings():
    """Setup the JavaScript bindings for the interface."""
    global web_interface
    
    # Expose Python functions to JavaScript
    js.window.handleUserInput = create_proxy(handle_user_input)
    js.window.historyUp = create_proxy(history_up)
    js.window.historyDown = create_proxy(history_down)
    js.window.saveGame = create_proxy(save_game_wrapper)
    
    # Bind WebInterface methods to JavaScript functions
    if hasattr(js.window, 'printOutput'):
        web_interface.js_print = js.window.printOutput
    if hasattr(js.window, 'clearOutput'):
        web_interface.js_clear = js.window.clearOutput
    if hasattr(js.window, 'setPrompt'):
        web_interface.js_set_prompt = js.window.setPrompt
    if hasattr(js.window, 'setInputValue'):
        web_interface.js_set_input = js.window.setInputValue

def handle_user_input(input_text):
    """Handle user input from the web interface."""
    global web_interface
    # Pass the input to the web interface
    web_interface.handle_input(input_text)

def history_up():
    """Navigate up in command history."""
    global web_interface
    web_interface.history_up()

def history_down():
    """Navigate down in command history."""
    global web_interface
    web_interface.history_down()

def save_game_wrapper():
    """Wrapper for saving the game to browser storage."""
    global game_runner, web_persistence
    
    if not game_runner or not game_runner.game_coordinator:
        js.window.showSaveStatus("No game to save!", "error")
        return False
    
    try:
        # Get game state from the game coordinator
        game_state = game_runner.game_coordinator.game_state
        
        # Use WebPersistence to save the game
        success = web_persistence.save_game_instance(game_state)
        
        if success:
            # Update status
            js.window.showSaveStatus("Game saved successfully!", "success")
        else:
            js.window.showSaveStatus("Failed to save game", "error")
        
        return success
    except Exception as e:
        error_msg = f"Failed to save game: {str(e)}"
        print(error_msg)
        js.window.showSaveStatus(error_msg, "error")
        return False

def load_game_from_storage():
    """Load a game from browser storage if available."""
    global web_persistence
    
    try:
        # Use WebPersistence to load the game
        return web_persistence.load_game_instance()
    except Exception as e:
        error_msg = f"Failed to load game: {str(e)}"
        print(error_msg)
        return None

async def run_game_async(game_runner):
    """Run the game in an async context."""
    try:
        # Instead of running the game in a separate thread, we'll call the run method directly
        # but first check if we need to modify the run method to avoid tasks being returned
        from types import MethodType
        
        # Save the original run method
        original_run = game_runner.run
        
        # Define a wrapper that ensures we don't return Task objects
        def safe_run(self):
            try:
                result = original_run()
                # If the result is a Task, we'll just return None instead
                if hasattr(result, '__class__') and result.__class__.__name__ == '_asyncio.Task':
                    return None
                return result
            except Exception as e:
                print(f"Error in game runner: {str(e)}")
                import traceback
                traceback.print_exc()
                return None
        
        # Replace the run method with our safe version
        game_runner.run = MethodType(safe_run, game_runner)
        
        # Now call the run method directly
        return game_runner.run()
    except Exception as e:
        error_msg = f"Error running game: {str(e)}"
        print(error_msg)
        import traceback
        traceback.print_exc()
        js.window.showError(error_msg)
        return None

def start_game():
    """Initialize and start the game."""
    global web_interface, game_runner, web_persistence
    
    try:
        # Initialize web interface
        web_interface = WebInterface()
        
        # Initialize persistence
        web_persistence = WebPersistence()
        
        # Set up JavaScript bindings
        setup_js_bindings()
        
        web_interface.print_line(web_interface.colorize("Initializing game...", TextColor.FG_CYAN))
        
        # Initialize game state
        game_state = GameState()
        
        # Check for a saved game after initial setup
        has_save = False
        if hasattr(js.window, 'localStorage') and js.window.localStorage.getItem(web_persistence.storage_key):
            has_save = True
            
        if has_save:
            web_interface.print_line(web_interface.colorize("Saved game found!", TextColor.FG_GREEN))
            
            # Ask if the user wants to load it
            def on_load_response(response):
                if response.lower() in ('y', 'yes'):
                    load_saved_game()
                else:
                    start_new_game()
                    
            # Set up a callback for the load question
            web_interface.set_input_callback(on_load_response)
            web_interface.print_line(web_interface.colorize("Would you like to load it? (y/n): ", TextColor.FG_CYAN))
        else:
            # No save, start a new game
            start_new_game()
            
        return "Game initialized successfully!"
        
    except Exception as e:
        error_msg = f"Error starting game: {str(e)}"
        print(error_msg)
        js.window.showError(error_msg)
        return error_msg

def load_saved_game():
    """Load a saved game from storage."""
    global web_interface, game_runner, web_persistence
    
    # Clear any callback
    web_interface.set_input_callback(None)
    
    try:
        # Load the game
        saved_game = load_game_from_storage()
        if saved_game:
            # Create game coordinator with loaded state
            game_coordinator = GameCoordinator(saved_game)
            
            # Create game runner
            game_runner = GameRunner(web_interface)
            game_runner.game_coordinator = game_coordinator
            game_runner.persistence = web_persistence  # Pass persistence to the runner
            
            web_interface.print_line(web_interface.colorize("Game loaded successfully!", TextColor.FG_GREEN))
            
            # Run the game directly, don't try to use async here
            try:
                run_game_async(game_runner)
            except Exception as e:
                error_msg = f"Error starting game: {str(e)}"
                print(error_msg)
                web_interface.print_line(web_interface.colorize(error_msg, TextColor.FG_RED))
        else:
            web_interface.print_line(web_interface.colorize("Failed to load saved game. Starting new game...", TextColor.FG_RED))
            start_new_game()
    except Exception as e:
        error_msg = f"Error loading game: {str(e)}"
        print(error_msg)
        web_interface.print_line(web_interface.colorize(f"Error: {error_msg}", TextColor.FG_RED))
        start_new_game()

def start_new_game():
    """Start a new game."""
    global web_interface, game_runner, web_persistence
    
    # Clear any callback
    web_interface.set_input_callback(None)
    
    # Initialize game state
    game_state = GameState()
    
    # Create game coordinator
    game_coordinator = GameCoordinator(game_state)
    
    # Create game runner
    game_runner = GameRunner(web_interface)
    game_runner.game_coordinator = game_coordinator
    game_runner.persistence = web_persistence  # Pass persistence to the runner
    
    web_interface.print_line(web_interface.colorize("Starting new game...", TextColor.FG_GREEN))
    
    # Run the game directly, don't try to use async here
    try:
        run_game_async(game_runner)
    except Exception as e:
        error_msg = f"Error starting game: {str(e)}"
        print(error_msg)
        web_interface.print_line(web_interface.colorize(error_msg, TextColor.FG_RED))

# Export functions to be called from JavaScript
js.window.startGame = create_proxy(start_game)
js.window.loadSavedGame = create_proxy(load_saved_game)
js.window.startNewGame = create_proxy(start_new_game) 