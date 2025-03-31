import pygame
import sys
from data_model.game_state import GameState

# Initialize Pygame
pygame.init()

# Get the display info to set up a full-screen window
display_info = pygame.display.Info()
WINDOW_WIDTH = display_info.current_w
WINDOW_HEIGHT = display_info.current_h

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Tritium")

# Initialize font for the timer
font = pygame.font.Font(None, 36)

# Initialize game state
game_state = GameState()

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Update game state
    game_state.update()

    # Clear screen with black background
    screen.fill((0, 0, 0))

    # Render timer
    timer_text = f"Game Time: {game_state.game_time}"
    timer_surface = font.render(timer_text, True, (255, 255, 255))
    screen.blit(timer_surface, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(1)

# Quit Pygame
pygame.quit()
sys.exit() 