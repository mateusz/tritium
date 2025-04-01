import sys
from data_model.game_state import GameState
from cli.master_view import MasterView
from cli.bases.earth_view import EarthView
from cli.facilities.training_view import TrainingView

def get_view_by_name(name, game_state):
    """Return a view instance based on its name"""
    if name == 'master':
        return MasterView(game_state)
    elif name == 'earth':
        return EarthView(game_state)
    elif name == 'training':
        return TrainingView(game_state)
    else:
        raise ValueError(f"Invalid view name: {name}")

def main():
    # Initialize game state
    game_state = GameState()
    
    # Start with master view
    current_view = MasterView(game_state)
    running = True
    
    # Main game loop
    while running:
        current_view.display()
        
        # Get user input 
        user_input = input(current_view.get_prompt())
        
        # Process command
        action, new_view = current_view.process_command(user_input)
        
        # Handle the action
        if action == 'quit':
            running = False
        elif action == 'switch' and new_view:
            # The view itself provides the new view instance
            current_view = new_view

    print("Game ended. Goodbye!")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 