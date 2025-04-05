import sys
import os
import readline

# Now import the modules
from data_model.game_state import GameState
from coordinators.game_coordinator import GameCoordinator
from cli.cli_persistence import CliPersistence
from textual.game_runner import GameRunner
from textual.interface import TextColor
from cli.cli_interface import CliInterface

def main():
    game_state = None
    cli_interface = CliInterface()
    persistence = CliPersistence()

    runner = GameRunner(cli_interface, persistence)
    runner.run()
    return 0

if __name__ == "__main__":
    sys.exit(main()) 