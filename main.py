import pygame
import sys
from pygame.locals import *
from bases.earth import Earth
from rooms.room import RoomType
import os

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
PANEL_WIDTH = 200
PANEL_HEIGHT = WINDOW_HEIGHT
ROOM_ICON_SIZE = 48 * 3  # Triple the size of room icons
ROOM_ICON_PADDING = 20  # Increased padding for larger icons
ICONS_PER_COLUMN = 2  # Number of icons per column

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tritium')

# Load graphics
MAIN_BACKGROUND = pygame.image.load(os.path.join('assets', 'graphics', 'gui', 'Main.png'))
MAIN_BACKGROUND = pygame.transform.scale(MAIN_BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))

CONTROL_PANEL_ORIGINAL = pygame.image.load(os.path.join('assets', 'graphics', 'gui', 'controlpanel', 'ControlPanel.png'))
# Scale to 4x original size
CONTROL_PANEL = pygame.transform.scale(CONTROL_PANEL_ORIGINAL, 
                                     (CONTROL_PANEL_ORIGINAL.get_width() * 4,
                                      CONTROL_PANEL_ORIGINAL.get_height() * 4))
CONTROL_PANEL_HEIGHT = CONTROL_PANEL.get_height()

# Initialize game state
current_base = Earth()
current_room = None
selected_room_type = None

def scale_maintain_aspect_ratio(surface, target_size):
    """Scale surface to target_size while maintaining aspect ratio"""
    width = surface.get_width()
    height = surface.get_height()
    aspect_ratio = width / height
    
    if width > height:
        new_width = target_size
        new_height = int(target_size / aspect_ratio)
    else:
        new_height = target_size
        new_width = int(target_size * aspect_ratio)
    
    return pygame.transform.scale(surface, (new_width, new_height))

def draw_control_panel():
    """Draw the control panel and room selection area on the left side"""
    # Draw the control panel at the top left (4x original size)
    screen.blit(CONTROL_PANEL, (0, 0))
    
    # Calculate column width
    column_width = PANEL_WIDTH // 2
    
    # Sort room types to ensure production is first
    room_items = list(current_base.rooms.items())
    room_items.sort(key=lambda x: x[0] != RoomType.PRODUCTION)  # Production first
    
    # Draw room icons in two columns
    for i, (room_type, room) in enumerate(room_items):
        # Calculate column and row position
        column = i % 2
        row = i // 2
        
        # Scale icon maintaining aspect ratio
        icon = scale_maintain_aspect_ratio(room.icon, ROOM_ICON_SIZE)
        
        # Calculate position
        x_pos = column * column_width + (column_width - icon.get_width()) // 2
        y_pos = CONTROL_PANEL_HEIGHT + ROOM_ICON_PADDING + row * (ROOM_ICON_SIZE + ROOM_ICON_PADDING)
        
        # Draw icon
        screen.blit(icon, (x_pos, y_pos))
        
        # Draw selection highlight if this room is selected
        if selected_room_type == room_type:
            pygame.draw.rect(screen, BLUE, 
                           (x_pos-2, y_pos-2, 
                            icon.get_width()+4, icon.get_height()+4), 2)

def handle_click(pos):
    """Handle mouse clicks"""
    global selected_room_type
    
    # Check if click is in the room selection panel
    if pos[0] < PANEL_WIDTH and pos[1] >= CONTROL_PANEL_HEIGHT:
        # Calculate column width
        column_width = PANEL_WIDTH // 2
        
        # Sort room types to ensure production is first
        room_items = list(current_base.rooms.items())
        room_items.sort(key=lambda x: x[0] != RoomType.PRODUCTION)  # Production first
        
        # Check each room icon
        for i, (room_type, room) in enumerate(room_items):
            # Calculate column and row position
            column = i % 2
            row = i // 2
            
            # Get scaled icon size
            icon = scale_maintain_aspect_ratio(room.icon, ROOM_ICON_SIZE)
            
            # Calculate position
            x_pos = column * column_width + (column_width - icon.get_width()) // 2
            y_pos = CONTROL_PANEL_HEIGHT + ROOM_ICON_PADDING + row * (ROOM_ICON_SIZE + ROOM_ICON_PADDING)
            
            icon_rect = pygame.Rect(x_pos, y_pos, 
                                  icon.get_width(), icon.get_height())
            if icon_rect.collidepoint(pos):
                selected_room_type = room_type
                return
    # Handle control panel clicks if needed
    elif pos[0] < PANEL_WIDTH and pos[1] < CONTROL_PANEL_HEIGHT:
        # Add control panel click handling here
        pass

def draw_room_content(room):
    """Draw room-specific content based on room type"""
    # Delegate drawing to the room's implementation
    room.draw(screen, PANEL_WIDTH, 0, WINDOW_WIDTH-PANEL_WIDTH, WINDOW_HEIGHT)

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
        
        # Draw main background
        screen.blit(MAIN_BACKGROUND, (0, 0))
        
        # Draw control panel and room selection
        draw_control_panel()
        
        # Draw current room if selected
        if selected_room_type:
            current_room = current_base.get_room(selected_room_type)
            if current_room:
                draw_room_content(current_room)
        
        # Update display
        pygame.display.flip()

if __name__ == '__main__':
    main() 