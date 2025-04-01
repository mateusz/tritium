from dataclasses import dataclass
from typing import List, Tuple
from colorama import Fore, Style
import time

@dataclass
class Message:
    """A message to be displayed to the user"""
    text: str
    color: str
    timestamp: float
    
    def __str__(self):
        return f"{self.color}{self.text}{Style.RESET_ALL}"

class MessageManager:
    """Manages messages to be displayed to the user across screen refreshes"""
    
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """Get the singleton instance of MessageManager"""
        if cls._instance is None:
            cls._instance = MessageManager()
        return cls._instance
    
    def __init__(self):
        """Initialize the message manager"""
        self.messages: List[Message] = []
        self.max_messages = 3  # Maximum number of messages to show
        self.message_ttl = 10.0  # Time to live for messages in seconds
    
    def add_message(self, text: str, color: str = Fore.WHITE):
        """Add a message to the buffer"""
        self.messages.append(Message(text, color, time.time()))
        # Clean up old messages
        self._clean_old_messages()
    
    def add_info(self, text: str):
        """Add an info message"""
        self.add_message(text, Fore.CYAN)
    
    def add_success(self, text: str):
        """Add a success message"""
        self.add_message(text, Fore.GREEN)
    
    def add_warning(self, text: str):
        """Add a warning message"""
        self.add_message(text, Fore.YELLOW)
    
    def add_error(self, text: str):
        """Add an error message"""
        self.add_message(text, Fore.RED)
    
    def _clean_old_messages(self):
        """Remove messages that are too old"""
        current_time = time.time()
        self.messages = [msg for msg in self.messages 
                        if current_time - msg.timestamp < self.message_ttl]
        
        # Keep only the most recent messages if we have too many
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
    
    def get_messages(self) -> List[Message]:
        """Get all current messages"""
        self._clean_old_messages()
        return self.messages
    
    def get_message_display(self) -> str:
        """Get a formatted string of all messages for display"""
        if not self.messages:
            return ""
        
        result = "─" * 80 + "\n"
        for msg in self.messages:
            result += f"{msg}\n"
        result += "─" * 80
        return result
    
    def clear_messages(self):
        """Clear all messages"""
        self.messages = [] 