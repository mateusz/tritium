from abc import ABC, abstractmethod
from typing import List, Optional, Dict

class TextColor:
    """Platform-independent text color and style constants.
    
    This class provides color and style constants that are independent of the
    actual implementation (like colorama, ANSI, HTML, etc.). Interface implementations
    will map these to the appropriate platform-specific codes.
    """
    # Foreground colors
    FG_BLACK = "fg_black"
    FG_RED = "fg_red"
    FG_GREEN = "fg_green"
    FG_YELLOW = "fg_yellow"
    FG_BLUE = "fg_blue"
    FG_MAGENTA = "fg_magenta"
    FG_CYAN = "fg_cyan"
    FG_WHITE = "fg_white"
    FG_LIGHTBLACK = "fg_lightblack"
    FG_LIGHTRED = "fg_lightred"
    FG_LIGHTGREEN = "fg_lightgreen"
    FG_LIGHTYELLOW = "fg_lightyellow"
    FG_LIGHTBLUE = "fg_lightblue"
    FG_LIGHTMAGENTA = "fg_lightmagenta"
    FG_LIGHTCYAN = "fg_lightcyan"
    FG_LIGHTWHITE = "fg_lightwhite"
    
    # Background colors
    BG_BLACK = "bg_black"
    BG_RED = "bg_red"
    BG_GREEN = "bg_green"
    BG_YELLOW = "bg_yellow"
    BG_BLUE = "bg_blue"
    BG_MAGENTA = "bg_magenta"
    BG_CYAN = "bg_cyan"
    BG_WHITE = "bg_white"
    
    # Styles
    STYLE_BRIGHT = "style_bright"
    STYLE_DIM = "style_dim"
    STYLE_NORMAL = "style_normal"
    STYLE_RESET_ALL = "style_reset_all"

class TextInterface(ABC):
    """Abstract interface for text I/O operations.
    
    This interface abstracts the input/output operations needed by text-based
    interfaces, allowing implementations for different platforms (CLI, GUI, web, etc.)
    """
    
    @abstractmethod
    def print_line(self, text: str) -> None:
        """Print a line of text to the output."""
        pass
    
    @abstractmethod
    def clear_screen(self) -> None:
        """Clear the screen or output area."""
        pass
    
    @abstractmethod
    def read_line(self, prompt: str = "") -> str:
        """Read a line of input from the user.
        
        Args:
            prompt: Optional text prompt to display before reading input
            
        Returns:
            The input string entered by the user
        """
        pass
    
    @abstractmethod
    def read_command(self, prompt: str = "", history: Optional[List[str]] = None) -> str:
        """Read a command from the user with support for command history.
        
        Args:
            prompt: Text prompt to display before reading input
            history: Optional list of previous commands for up/down navigation
            
        Returns:
            The command string entered by the user
        """
        pass
    
    @abstractmethod
    def colorize(self, text: str, color_code: str) -> str:
        """Apply a color to the given text.
        
        Args:
            text: The text to colorize
            color_code: A color code from TextColor
            
        Returns:
            The colorized text string
        """
        pass
    
    @abstractmethod
    def center_text(self, text: str, width: int = 80) -> str:
        """Center text to a specified width.
        
        Args:
            text: The text to center
            width: The width to center within
            
        Returns:
            The centered text
        """
        pass

