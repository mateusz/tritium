import sys
import os
import readline

# Now import the modules
from data_model.game_state import GameState
from coordinators.game_coordinator import GameCoordinator
from data_model.persistence import save_game, load_game
from textual.game_runner import GameRunner
from textual.interface import TextColor
from textual.cli_interface import CliInterface

def main():
    # Check for a saved game and offer to load it
    saved_game = load_game()
    game_state = None
    
    # Initialize our CLI interface with history support
    cli_interface = CliInterface()
    
    if saved_game:
        load_choice = cli_interface.read_line(cli_interface.colorize("Saved game found. Load it? (y/n): ", TextColor.FG_CYAN))
        if load_choice.lower() == 'y' or load_choice.lower() == 'yes':
            game_state = saved_game
            cli_interface.print_line(cli_interface.colorize("Game loaded successfully!", TextColor.FG_GREEN))
    
    # Initialize game state if not loaded
    if not game_state:
        game_state = GameState()
    
    # Create game coordinator with our game state
    game_coordinator = GameCoordinator(game_state)
    
    # Create and run the game with our custom interface
    runner = GameRunner(cli_interface)
    runner.game_coordinator = game_coordinator  # Use our game coordinator with loaded state
    runner.run()
    
    # Save the game when quitting
    if save_game(game_state):
        cli_interface.print_line(cli_interface.colorize("Game saved successfully!", TextColor.FG_GREEN))
    
    cli_interface.print_line(cli_interface.colorize("Game ended. Goodbye!", TextColor.FG_YELLOW))
    return 0

if __name__ == "__main__":
    sys.exit(main()) 