from typing import List, Optional, Dict, Callable
from textual.interface import TextInterface, TextColor
import js
from pyodide.ffi import create_proxy

class WebInterface(TextInterface):
    """Web implementation of the TextInterface for use with Pyodide.
    
    This interface connects to JavaScript functions to handle input/output
    operations in a web browser environment.
    """
    
    def __init__(self):
        """Initialize the web interface."""
        # Color code mapping from abstract TextColor to HTML/CSS styles
        self.color_map = {
            # Foreground colors
            TextColor.FG_BLACK: "color: black;",
            TextColor.FG_RED: "color: red;",
            TextColor.FG_GREEN: "color: green;",
            TextColor.FG_YELLOW: "color: #cccc00;",
            TextColor.FG_BLUE: "color: blue;",
            TextColor.FG_MAGENTA: "color: magenta;",
            TextColor.FG_CYAN: "color: cyan;",
            TextColor.FG_WHITE: "color: white;",
            TextColor.FG_LIGHTBLACK: "color: #505050;",
            TextColor.FG_LIGHTRED: "color: #ff5050;",
            TextColor.FG_LIGHTGREEN: "color: #50ff50;",
            TextColor.FG_LIGHTYELLOW: "color: #ffff50;",
            TextColor.FG_LIGHTBLUE: "color: #5050ff;",
            TextColor.FG_LIGHTMAGENTA: "color: #ff50ff;",
            TextColor.FG_LIGHTCYAN: "color: #50ffff;",
            TextColor.FG_LIGHTWHITE: "color: #ffffff;",
            
            # Background colors
            TextColor.BG_BLACK: "background-color: black;",
            TextColor.BG_RED: "background-color: red;",
            TextColor.BG_GREEN: "background-color: green;",
            TextColor.BG_YELLOW: "background-color: #cccc00;",
            TextColor.BG_BLUE: "background-color: blue;",
            TextColor.BG_MAGENTA: "background-color: magenta;",
            TextColor.BG_CYAN: "background-color: cyan;",
            TextColor.BG_WHITE: "background-color: white;",
            
            # Styles
            TextColor.STYLE_BRIGHT: "font-weight: bold;",
            TextColor.STYLE_DIM: "opacity: 0.7;",
            TextColor.STYLE_NORMAL: "",
            TextColor.STYLE_RESET_ALL: "",
        }
        # Command history for each view
        self.command_history = {}
        self.history_position = {}
        self.current_view = None
        self.input_callback = None
        self._waiting_for_input = False
        self._last_input = ""
        
        # JS function references (will be set by game-web.py)
        self.js_print = None
        self.js_clear = None
        self.js_set_prompt = None
        self.js_set_input = None
        
    def print_line(self, text: str) -> None:
        """Print a line of text to the web output area."""
        processed_text = self._process_color_tags(text)
        if self.js_print:
            self.js_print(processed_text)
        else:
            # Fallback if not yet bound
            js.window.printOutput(processed_text)
    
    def clear_screen(self) -> None:
        """Clear the web output area."""
        if self.js_clear:
            self.js_clear()
        else:
            # Fallback if not yet bound
            js.window.clearOutput()
    
    def read_line(self, prompt: str = "") -> str:
        """Read a line of input from the web input field.
        
        This is a blocking operation that returns when the user submits input.
        """
        processed_prompt = self._process_color_tags(prompt)
        if self.js_set_prompt:
            self.js_set_prompt(processed_prompt)
        else:
            # Fallback if not yet bound
            js.window.setPrompt(processed_prompt)
        
        # Create a Promise-like mechanism using Pyodide
        self._waiting_for_input = True
        
        # Use pyodide synchronization
        import asyncio
        self._input_event = asyncio.Event()
        
        # Schedule the event to run in the background
        async def wait_for_input():
            await self._input_event.wait()
            return self._last_input
        
        # Create a future to wait on
        future = asyncio.ensure_future(wait_for_input())
        
        # This will block until JavaScript calls handle_input
        return asyncio.get_event_loop().run_until_complete(future)
    
    def handle_input(self, input_text: str) -> None:
        """Callback function to be called from JavaScript when input is submitted."""
        if self._waiting_for_input:
            self._last_input = input_text
            self._waiting_for_input = False
            
            # Signal that we have input
            import asyncio
            if hasattr(self, '_input_event'):
                self._input_event.set()
            
            # Add to history if we have a current view
            if self.current_view and input_text.strip():
                self.add_command_to_history(self.current_view, input_text)
            
            # Call any callback
            if self.input_callback:
                self.input_callback(input_text)
    
    def set_input_callback(self, callback: Callable[[str], None]) -> None:
        """Set a callback function to be called when input is received."""
        self.input_callback = callback
    
    def read_command(self, prompt: str = "", history: Optional[str] = None) -> str:
        """Read a command with view-specific history support."""
        # If a view name is provided, set it as current
        if history:
            self.current_view = history
            
        # Display history navigation help
        js.window.enableHistoryNavigation(True)
        
        # Get user input
        return self.read_line(prompt)
    
    def add_command_to_history(self, view_name: str, command: str) -> None:
        """Add a command to the history for a specific view."""
        if view_name not in self.command_history:
            self.command_history[view_name] = []
        
        # Don't add empty commands or duplicates at the end
        if command and (not self.command_history[view_name] or 
                        command != self.command_history[view_name][-1]):
            self.command_history[view_name].append(command)
            # Reset history position
            self.history_position[view_name] = len(self.command_history[view_name])
    
    def get_history(self, view_name: str) -> List[str]:
        """Get command history for a specific view."""
        return self.command_history.get(view_name, [])
    
    def history_up(self) -> None:
        """Navigate up in the command history."""
        if not self.current_view:
            return
            
        if self.current_view not in self.history_position:
            self.history_position[self.current_view] = len(self.get_history(self.current_view))
            
        if self.history_position[self.current_view] > 0:
            self.history_position[self.current_view] -= 1
            history = self.get_history(self.current_view)
            if history and self.history_position[self.current_view] < len(history):
                if self.js_set_input:
                    self.js_set_input(history[self.history_position[self.current_view]])
                else:
                    js.window.setInputValue(history[self.history_position[self.current_view]])
    
    def history_down(self) -> None:
        """Navigate down in the command history."""
        if not self.current_view:
            return
            
        history = self.get_history(self.current_view)
        if self.current_view in self.history_position:
            if self.history_position[self.current_view] < len(history):
                self.history_position[self.current_view] += 1
                if self.history_position[self.current_view] < len(history):
                    if self.js_set_input:
                        self.js_set_input(history[self.history_position[self.current_view]])
                    else:
                        js.window.setInputValue(history[self.history_position[self.current_view]])
                else:
                    if self.js_set_input:
                        self.js_set_input("")
                    else:
                        js.window.setInputValue("")
    
    def colorize(self, text: str, color_code: str) -> str:
        """Apply HTML/CSS styling to the given text."""
        if not text:
            return ""
            
        css_style = self.color_map.get(color_code, "")
        if css_style:
            return f'<span style="{css_style}">{text}</span>'
        return text
    
    def center_text(self, text: str, width: int = 80) -> str:
        """Center text using HTML."""
        return f'<div style="text-align: center; width: {width}ch;">{text}</div>'
    
    def _process_color_tags(self, text: str) -> str:
        """Process any <color_code> tags in the text and replace with HTML styling."""
        for color_code, css_style in self.color_map.items():
            if css_style:  # Skip empty styles
                text = text.replace(f"<{color_code}>", f'<span style="{css_style}">')
                
        # Replace any remaining closing tags
        text = text.replace("<style_reset_all>", "</span>")
        
        return text 