from abc import ABC, abstractmethod
from typing import List, Optional

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

