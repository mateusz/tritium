import sys
from data_model.game_state import GameState
from coordinators.game_coordinator import GameCoordinator
from web.web_persistence import WebPersistence
from textual.game_runner import GameRunner
from textual.interface import TextColor
from web.web_interface import WebInterface
from pyodide.ffi import create_proxy
import js

# Global interface variable to hold reference for JS callbacks
global_interface = None

def init_web_game(js_print=None, js_clear=None, js_set_prompt=None, js_set_input=None):
    """Initialize the web game by setting up the interface and binding JS functions.
    
    Args:
        js_print: JavaScript function to print text
        js_clear: JavaScript function to clear output
        js_set_prompt: JavaScript function to set input prompt
        js_set_input: JavaScript function to set input field value
        
    Returns:
        WebInterface: The configured interface
    """
    global global_interface
    
    # Initialize the web interface
    interface = WebInterface()
    global_interface = interface
    
    # Bind JavaScript functions if provided
    if js_print:
        interface.js_print = js_print
    if js_clear:
        interface.js_clear = js_clear
    if js_set_prompt:
        interface.js_set_prompt = js_set_prompt
    if js_set_input:
        interface.js_set_input = js_set_input
    
    return interface

def handle_input(input_text):
    """Handle input from the web interface.
    
    Args:
        input_text: The text input from the user
    """
    global global_interface
    if global_interface:
        global_interface.handle_input(input_text)

def handle_history_up():
    """Handle up arrow key for command history."""
    global global_interface
    if global_interface:
        global_interface.history_up()

def handle_history_down():
    """Handle down arrow key for command history."""
    global global_interface
    if global_interface:
        global_interface.history_down()

def start_game():
    """Start the game using the web interface and persistence."""
    # Get the initialized interface
    global global_interface
    if not global_interface:
        interface = init_web_game()
    else:
        interface = global_interface
    
    # Create a persistence manager
    persistence = WebPersistence()
    
    # Create and run the game
    runner = GameRunner(interface, persistence)
    
    try:
        runner.run()
        return 0
    except Exception as e:
        interface.print_line(f"<{TextColor.FG_RED}>Error: {str(e)}<{TextColor.STYLE_RESET_ALL}>")
        js.console.error(str(e))
        return 1

# For use with Pyodide in async context, when imported as a module
def main():
    """Main function for the web game."""
    return start_game()

# Export functions to JavaScript
def export_python_functions():
    """Export Python functions to JavaScript for callbacks."""
    # Create proxies for the functions
    js.window.python_handle_input = create_proxy(handle_input)
    js.window.python_history_up = create_proxy(handle_history_up)
    js.window.python_history_down = create_proxy(handle_history_down)
    js.window.python_start_game = create_proxy(start_game)
    js.window.python_init_web_game = create_proxy(init_web_game)

# If run directly (not imported)
if __name__ == "__main__":
    export_python_functions()
    sys.exit(main()) 