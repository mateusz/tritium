import sys
import js
import asyncio
import pickle
import base64
from pyodide.ffi import create_proxy

# Import the modules
from data_model.game_state import GameState
from coordinators.game_coordinator import GameCoordinator
from data_model.persistence import save_game, load_game
from textual.game_runner import GameRunner
from textual.interface import TextColor
from web.web_interface import WebInterface

# Global variables to hold state
web_interface = None
game_runner = None

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
    global game_runner
    
    if not game_runner or not game_runner.game_coordinator:
        js.window.showSaveStatus("No game to save!", "error")
        return False
    
    try:
        # Get game state from the game coordinator
        game_state = game_runner.game_coordinator.game_state
        
        # Serialize the game state to a string
        serialized_data = pickle.dumps(game_state)
        # Convert to base64 for storage
        base64_data = base64.b64encode(serialized_data).decode('utf-8')
        
        # Save to browser storage
        js.window.localStorage.setItem('game_save', base64_data)
        
        # Update status
        js.window.showSaveStatus("Game saved successfully!", "success")
        return True
    except Exception as e:
        error_msg = f"Failed to save game: {str(e)}"
        print(error_msg)
        js.window.showSaveStatus(error_msg, "error")
        return False

def load_game_from_storage():
    """Load a game from browser storage if available."""
    try:
        # Check if there's a saved game in localStorage
        if hasattr(js.window, 'localStorage') and js.window.localStorage.getItem('game_save'):
            # Get the saved data
            base64_data = js.window.localStorage.getItem('game_save')
            # Convert from base64
            serialized_data = base64.b64decode(base64_data)
            # Deserialize to a GameState object
            game_state = pickle.loads(serialized_data)
            return game_state
        # If not in browser storage, try regular file storage
        return load_game()
    except Exception as e:
        error_msg = f"Failed to load game: {str(e)}"
        print(error_msg)
        return None

async def run_game_async(game_runner):
    """Run the game in an async context."""
    try:
        # Wrap the synchronous run method in a way that doesn't block the event loop
        # Use asyncio.to_thread if available (Python 3.9+) or run_in_executor otherwise
        import inspect
        if inspect.iscoroutinefunction(game_runner.run):
            # If run is already async, just call it
            return await game_runner.run()
        else:
            # If run is synchronous, run it in a separate thread/task
            loop = asyncio.get_event_loop()
            # Create a separate task that runs the synchronous function
            return await loop.run_in_executor(None, game_runner.run)
    except Exception as e:
        error_msg = f"Error running game: {str(e)}"
        print(error_msg)
        import traceback
        traceback.print_exc()
        js.window.showError(error_msg)
        return None

def start_game():
    """Initialize and start the game."""
    global web_interface, game_runner
    
    try:
        # Initialize web interface
        web_interface = WebInterface()
        
        # Set up JavaScript bindings
        setup_js_bindings()
        
        web_interface.print_line(web_interface.colorize("Initializing game...", TextColor.FG_CYAN))
        
        # Initialize game state
        game_state = GameState()
        
        # Check for a saved game after initial setup
        has_save = False
        if hasattr(js.window, 'localStorage') and js.window.localStorage.getItem('game_save'):
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
    global web_interface, game_runner
    
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
            
            web_interface.print_line(web_interface.colorize("Game loaded successfully!", TextColor.FG_GREEN))
            
            # Start the game in the background using asyncio
            # We need to use a trick to make sure this doesn't block but also doesn't
            # return the task object which could cause strip() errors
            async def run_game_wrapper():
                await run_game_async(game_runner)
                
            # Create and forget the task
            asyncio.create_task(run_game_wrapper())
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
    global web_interface, game_runner
    
    # Clear any callback
    web_interface.set_input_callback(None)
    
    # Initialize game state
    game_state = GameState()
    
    # Create game coordinator
    game_coordinator = GameCoordinator(game_state)
    
    # Create game runner
    game_runner = GameRunner(web_interface)
    game_runner.game_coordinator = game_coordinator
    
    web_interface.print_line(web_interface.colorize("Starting new game...", TextColor.FG_GREEN))
    
    # Start the game in the background using asyncio
    # We need to use a trick to make sure this doesn't block but also doesn't
    # return the task object which could cause strip() errors
    async def run_game_wrapper():
        await run_game_async(game_runner)
        
    # Create and forget the task
    asyncio.create_task(run_game_wrapper())

# Export functions to be called from JavaScript
js.window.startGame = create_proxy(start_game)
js.window.loadSavedGame = create_proxy(load_saved_game)
js.window.startNewGame = create_proxy(start_new_game) 