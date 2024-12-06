# James Rogan
# gameGraphics.py
# 11/24/2024

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants: grid size and square size
GRID_SIZE = 10         # 10x10 grid
SQUARE_SIZE = 32       # Each square is 32x32 pixels
SCREEN_WIDTH = GRID_SIZE * SQUARE_SIZE
SCREEN_HEIGHT = GRID_SIZE * SQUARE_SIZE

# Display settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adventure forth!")

# Colors for fallback in case images are missing
GREY = (211, 211, 211)
RED = (255, 0, 0)        # Player square color
GREEN = (0, 255, 0)      # Monster square color

# Movement speed
playerspeed = 1  # Move by one square space each key press

# Player's initial position
x, y = 0, 0
player_square = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

# Function to check if player and monster occupy the same position
def check_encounter(player_x, player_y, monster_x, monster_y):
    if player_x == monster_x and player_y == monster_y:
        print("The beast is slain!")
        return True
    return False

# Monster class
class Monster:
    def __init__(self, x, y, monster_image):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x * SQUARE_SIZE, self.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        self.image = monster_image

    # Move the monster one square at a time in a random direction (adjacent square)
    def move(self, player_x, player_y):
        if self.x < player_x and self.x < GRID_SIZE - 1:  # Move right if the player is to the right
            self.x += 1
        elif self.x > player_x and self.x > 0:  # Move left if the player is to the left
            self.x -= 1
        elif self.y < player_y and self.y < GRID_SIZE - 1:  # Move down if the player is below
            self.y += 1
        elif self.y > player_y and self.y > 0:  # Move up if the player is above
            self.y -= 1

        # Update monster's rect after moving
        self.rect.x = self.x * SQUARE_SIZE
        self.rect.y = self.y * SQUARE_SIZE

# Function to create a monster at a random position not occupied by the player
def create_monster(player_x, player_y, monster_image):
    while True:
        monster_x = random.randint(0, GRID_SIZE - 1)
        monster_y = random.randint(0, GRID_SIZE - 1)
        if monster_x != player_x or monster_y != player_y:  # Ensure the monster doesn't spawn on the player
            return Monster(monster_x, monster_y, monster_image)

# Load images for the player and monsters
def load_image(path, default_color):
    try:
        image = pygame.image.load(path).convert_alpha()  # Load image with transparency
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))  # Scale to square size
        return image
    except pygame.error:
        print(f"Error loading image at {path}, using fallback color instead.")
        return pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)).fill(default_color)

# Load player and monster images
player_image = load_image("player.png", RED)  # Replace "player.png" with your player image path
monster_image = load_image("monster.png", GREEN)  # Replace "monster.png" with your monster image path

# Main game loop
running = True
clock = pygame.time.Clock()

# Create the first monster (only one at the start)
monsters = [create_monster(x, y, monster_image)]

player_moved = False

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Respond to keypress events 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y > 0:
                y -= 1
                player_moved = True
            elif event.key == pygame.K_DOWN and y < GRID_SIZE - 1:
                y += 1
                player_moved = True
            elif event.key == pygame.K_LEFT and x > 0:
                x -= 1
                player_moved = True
            elif event.key == pygame.K_RIGHT and x < GRID_SIZE - 1:
                x += 1
                player_moved = True
            elif event.key == pygame.K_q:  # Quit if 'q' is pressed
                running = False

    # Update the player square's rect position
    player_square.x = x * SQUARE_SIZE
    player_square.y = y * SQUARE_SIZE

    # If the player moved, move the monster one square towards the player
    if player_moved:
        # Move all monsters
        for monster in monsters:
            monster.move(x, y)

        # Check for encounters with the monsters
        monsters_to_remove = []
        for monster in monsters:
            if check_encounter(x, y, monster.x, monster.y):
                monsters_to_remove.append(monster)

        # Remove defeated monsters
        for monster in monsters_to_remove:
            monsters.remove(monster)

        # If all monsters are defeated, spawn two new monsters
        if len(monsters) == 0:
            print("Look out, there's more!")
            # Spawn two new monsters at random positions
            monsters.append(create_monster(x, y, monster_image))
            monsters.append(create_monster(x, y, monster_image))

        player_moved = False  # Reset player move flag

    # Clear the screen
    screen.fill(GREY)

    # Draw the player image
    screen.blit(player_image, (player_square.x, player_square.y))

    # Draw all monsters
    for monster in monsters:
        screen.blit(monster.image, (monster.rect.x, monster.rect.y))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)  # 60 frames per second

pygame.quit()
