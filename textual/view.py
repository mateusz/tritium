from textual.message_system import MessageManager
from textual.interface import TextInterface, TextColor
from coordinators.game_coordinator import GameCoordinator
from textual.persistence import Persistence
from abc import ABC, abstractmethod

class View(ABC):
    def __init__(self, game_coordinator: GameCoordinator, interface: TextInterface):
        self.game_coordinator = game_coordinator
        self.interface = interface
    
    @abstractmethod
    def display(self):
        pass
    
    
    @abstractmethod
    def log_message(self, message: str, message_type: str = "info"):
        pass
    
    @abstractmethod
    def process_command(self, command: str):
        pass

    @abstractmethod
    def get_prompt(self):
        pass