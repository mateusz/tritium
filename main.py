import pygame
import sys
from pygame.locals import *
from bases.earth import Earth
from room import RoomType

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
PANEL_WIDTH = 200
PANEL_HEIGHT = WINDOW_HEIGHT
ROOM_ICON_SIZE = 64
ROOM_ICON_PADDING = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tritium')

# Load room icons
room_icons = {
    RoomType.RESEARCH: pygame.image.load('assets/graphics/gui/icons/Research.png'),
    RoomType.CREW: pygame.image.load('assets/graphics/gui/icons/Training.png'),
    RoomType.PRODUCTION: pygame.image.load('assets/graphics/gui/icons/Production.png'),
    RoomType.SHUTTLE_BAY: pygame.image.load('assets/graphics/gui/icons/ShuttleBay.png'),
    RoomType.STORAGE: pygame.image.load('assets/graphics/gui/icons/Storage.png'),
    RoomType.MINING: pygame.image.load('assets/graphics/gui/icons/Mining.png'),
    RoomType.HIRE: pygame.image.load('assets/graphics/gui/icons/Mining.png')
}

# Initialize game state
current_base = Earth()
current_room = None
selected_room_type = None

def draw_base_controls_panel():
    """Draw the base controls panel on the left side"""
    # Draw panel background
    pygame.draw.rect(screen, GRAY, (0, 0, PANEL_WIDTH, PANEL_HEIGHT))
    
    # Draw room icons
    y_offset = ROOM_ICON_PADDING
    for room_type, room in current_base.rooms.items():
        if room_type in room_icons:
            icon = room_icons[room_type]
            # Scale icon to desired size
            icon = pygame.transform.scale(icon, (ROOM_ICON_SIZE, ROOM_ICON_SIZE))
            
            # Draw icon
            screen.blit(icon, (ROOM_ICON_PADDING, y_offset))
            
            # Draw selection highlight if this room is selected
            if selected_room_type == room_type:
                pygame.draw.rect(screen, BLUE, 
                               (ROOM_ICON_PADDING-2, y_offset-2, 
                                ROOM_ICON_SIZE+4, ROOM_ICON_SIZE+4), 2)
            
            y_offset += ROOM_ICON_SIZE + ROOM_ICON_PADDING

def handle_click(pos):
    """Handle mouse clicks"""
    global selected_room_type
    
    # Check if click is in the base controls panel
    if pos[0] < PANEL_WIDTH:
        # Calculate which room icon was clicked
        y_offset = ROOM_ICON_PADDING
        for room_type, room in current_base.rooms.items():
            if room_type in room_icons:
                icon_rect = pygame.Rect(ROOM_ICON_PADDING, y_offset, 
                                      ROOM_ICON_SIZE, ROOM_ICON_SIZE)
                if icon_rect.collidepoint(pos):
                    selected_room_type = room_type
                    return
                y_offset += ROOM_ICON_SIZE + ROOM_ICON_PADDING

def main():
    global current_room
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    handle_click(event.pos)
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw base controls panel
        draw_base_controls_panel()
        
        # Draw current room if selected
        if selected_room_type:
            current_room = current_base.get_room(selected_room_type)
            if current_room:
                # Draw room content in the main area
                pygame.draw.rect(screen, WHITE, 
                               (PANEL_WIDTH, 0, 
                                WINDOW_WIDTH-PANEL_WIDTH, WINDOW_HEIGHT))
                # TODO: Draw room-specific content
        
        # Update display
        pygame.display.flip()

if __name__ == '__main__':
    main() 