# James Rogan
# gameGraphics.py
# 11/17/2024

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants: grid size and square size
GRID_SIZE = 10         # 10x10 grid
SQUARE_SIZE = 32       # Each square is 32x32 pixels
SCREEN_WIDTH = GRID_SIZE * SQUARE_SIZE
SCREEN_HEIGHT = GRID_SIZE * SQUARE_SIZE

# display settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Move the Square")

# Defines the starting position of the square
x, y = 0, 0  # top left corner
square = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

# Colors
GREY = (211, 211, 211)
RED = (255, 0, 0)

# Movement speed
playerspeed = 1  # Move by one square space each key press

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Respond to keypress events 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y > 0:
                y -= 1
            elif event.key == pygame.K_DOWN and y < GRID_SIZE - 1:
                y += 1
            elif event.key == pygame.K_LEFT and x > 0:
                x -= 1
            elif event.key == pygame.K_RIGHT and x < GRID_SIZE - 1:
                x += 1
            elif event.key == pygame.K_q:  # Quit if 'q' is pressed
                running = False

    # Update the square's rect position
    square.x = x * SQUARE_SIZE
    square.y = y * SQUARE_SIZE

    # Clear the screen
    screen.fill(GREY)

    # Draw the square
    pygame.draw.rect(screen, RED, square)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)  # 60 frames per second

pygame.quit()
