from typing import List, Optional, Dict
from textual.interface import TextInterface, TextColor
import readline
# Import colorama conditionally, so it's only needed for CLI interface
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)  # Initialize colorama
    COLORAMA_AVAILABLE = True
except ImportError:
    # Fallback if colorama isn't available
    COLORAMA_AVAILABLE = False
    
    # Define empty placeholder classes
    class ForeStub:
        BLACK = ""
        RED = ""
        GREEN = ""
        YELLOW = ""
        BLUE = ""
        MAGENTA = ""
        CYAN = ""
        WHITE = ""
        LIGHTBLACK_EX = ""
        LIGHTRED_EX = ""
        LIGHTGREEN_EX = ""
        LIGHTYELLOW_EX = ""
        LIGHTBLUE_EX = ""
        LIGHTMAGENTA_EX = ""
        LIGHTCYAN_EX = ""
        LIGHTWHITE_EX = ""
        
    class BackStub:
        BLACK = ""
        RED = ""
        GREEN = ""
        YELLOW = ""
        BLUE = ""
        MAGENTA = ""
        CYAN = ""
        WHITE = ""
        
    class StyleStub:
        BRIGHT = ""
        DIM = ""
        NORMAL = ""
        RESET_ALL = ""
    
    # Assign stub classes
    Fore = ForeStub()
    Back = BackStub()
    Style = StyleStub()

class CliInterface(TextInterface):
    """CLI implementation of the TextInterface using colorama for colors."""
    
    def __init__(self):
        """Initialize the CLI interface."""
        # Color code mapping from abstract TextColor to colorama
        self.color_map = {
            # Foreground colors
            TextColor.FG_BLACK: Fore.BLACK,
            TextColor.FG_RED: Fore.RED,
            TextColor.FG_GREEN: Fore.GREEN,
            TextColor.FG_YELLOW: Fore.YELLOW,
            TextColor.FG_BLUE: Fore.BLUE,
            TextColor.FG_MAGENTA: Fore.MAGENTA,
            TextColor.FG_CYAN: Fore.CYAN,
            TextColor.FG_WHITE: Fore.WHITE,
            TextColor.FG_LIGHTBLACK: Fore.LIGHTBLACK_EX,
            TextColor.FG_LIGHTRED: Fore.LIGHTRED_EX,
            TextColor.FG_LIGHTGREEN: Fore.LIGHTGREEN_EX,
            TextColor.FG_LIGHTYELLOW: Fore.LIGHTYELLOW_EX,
            TextColor.FG_LIGHTBLUE: Fore.LIGHTBLUE_EX,
            TextColor.FG_LIGHTMAGENTA: Fore.LIGHTMAGENTA_EX,
            TextColor.FG_LIGHTCYAN: Fore.LIGHTCYAN_EX,
            TextColor.FG_LIGHTWHITE: Fore.LIGHTWHITE_EX,
            
            # Background colors
            TextColor.BG_BLACK: Back.BLACK,
            TextColor.BG_RED: Back.RED,
            TextColor.BG_GREEN: Back.GREEN,
            TextColor.BG_YELLOW: Back.YELLOW,
            TextColor.BG_BLUE: Back.BLUE,
            TextColor.BG_MAGENTA: Back.MAGENTA,
            TextColor.BG_CYAN: Back.CYAN,
            TextColor.BG_WHITE: Back.WHITE,
            
            # Styles
            TextColor.STYLE_BRIGHT: Style.BRIGHT,
            TextColor.STYLE_DIM: Style.DIM,
            TextColor.STYLE_NORMAL: Style.NORMAL,
            TextColor.STYLE_RESET_ALL: Style.RESET_ALL,
        }
        self.command_history = {}  # Dictionary to store history for each view
        
    def add_command_to_history(self, view_name, command):
        """Add a command to the history for a specific view"""
        if view_name not in self.command_history:
            self.command_history[view_name] = []
        
        # Don't add empty commands or duplicates at the end
        if command and (not self.command_history[view_name] or command != self.command_history[view_name][-1]):
            self.command_history[view_name].append(command)
    
    def get_history(self, view_name):
        """Get command history for a specific view"""
        return self.command_history.get(view_name, [])
    
    def setup_readline(self, view_name):
        """Set up readline with the history for the current view"""
        # Clear existing history
        readline.clear_history()
        
        # Add view-specific history
        for cmd in self.get_history(view_name):
            readline.add_history(cmd)
    
    def read_command(self, prompt="", history=None):
        """Read a command with view-specific history support."""
        # If a view name is provided in history, set up readline
        if history and isinstance(history, str):
            self.setup_readline(history)
        
        # Get user input
        processed_prompt = self._process_color_tags(prompt)
        command = input(processed_prompt)
        
        # Add to history if view name provided
        if history and isinstance(history, str) and command.strip():
            self.add_command_to_history(history, command)
            
        return command 

    def print_line(self, text: str) -> None:
        """Print a line of text to the console."""
        # Process any color tags before printing
        processed_text = self._process_color_tags(text)
        print(processed_text)
    
    def clear_screen(self) -> None:
        """Clear the console screen."""
        print("\033[H\033[J", end="")
    
    def read_line(self, prompt: str = "") -> str:
        """Read a line of input from the console."""
        processed_prompt = self._process_color_tags(prompt)
        return input(processed_prompt)
    
    def colorize(self, text: str, color_code: str) -> str:
        """Apply a color to the given text using colorama codes."""
        if not text:
            return ""
            
        colorama_code = self.color_map.get(color_code, "")
        if colorama_code:
            return f"{colorama_code}{text}{Style.RESET_ALL}"
        return text
    
    def center_text(self, text: str, width: int = 80) -> str:
        """Center text to a specified width."""
        return text.center(width)
    
    def _process_color_tags(self, text: str) -> str:
        """Process any <color_code> tags in the text and replace with actual color codes."""
        # This is a simple implementation to handle the format from MessageManager
        # For a more robust solution, consider using a proper template engine or regex
        for color_code, colorama_code in self.color_map.items():
            text = text.replace(f"<{color_code}>", colorama_code)
        return text 