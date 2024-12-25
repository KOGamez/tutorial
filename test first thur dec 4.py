import pygame
from sys import exit

# Initialize Pygame (needed before any other code)
pygame.init()

# Set up the main display surface with dimensions 800x400
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('runner')  # Set the window title
clock = pygame.time.Clock()  # Create a clock object to manage frame rate

# Load game assets
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)  # Load custom font for text

# Load images for background and ground, using convert_alpha for transparency
sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render('my game', False, 'Black')  # Render text surface

# Load snail image and set initial position
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600  # Starting position of the snail

# Load player image and set its rectangle for positioning
player_surface = pygame.image.load('graphics/Player/player_walk_1.png')
player_rect = player_surface.get_rect(midbottom=(80, 300))  # Position the player

# Main game loop
while True:
    for event in pygame.event.get():  # Check for user inputs/events
        if event.type == pygame.QUIT:  # Check if the user closed the window
            pygame.quit()  # Uninitialize all Pygame modules
            exit()  # Exit the program

    # Reset snail position if it goes off-screen
    if snail_x_pos <= -100: 
        snail_x_pos = 800  # Reset to starting position

    # Draw all game elements on the screen
    screen.blit(sky_surface, (0, 0))  # Draw the sky background
    screen.blit(ground_surface, (0, 300))  # Draw the ground
    screen.blit(text_surface, (300, 50))  # Draw the text on screen
    snail_x_pos -= 4  # Move the snail left across the screen
    screen.blit(snail_surface, (snail_x_pos, 250))  # Draw the snail at its current position
    
    player_rect.left += 1  # Move the player to the right
    screen.blit(player_surface, player_rect)  # Draw the player on the screen    

    # Update the display and control frame rate
    pygame.display.update()  # Refresh the display with new drawings
    clock.tick(60)  # Limit to 60 frames per second

#this is a test print