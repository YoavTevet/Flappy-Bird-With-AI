import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BIRD_SIZE = 30
PILLAR_WIDTH = 50
PILLAR_GAP = 150
PILLAR_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Bird parameters
bird_x = WIDTH // 4
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 1

# Pillar parameters
pillars = [{"x": WIDTH, "height": random.randint(50, 250)}]

# Fonts
font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, BIRD_SIZE, BIRD_SIZE])

def draw_pillars(pillars):
    for pillar in pillars:
        pygame.draw.rect(screen, WHITE, [pillar["x"], 0, PILLAR_WIDTH, pillar["height"]])
        pygame.draw.rect(screen, WHITE, [pillar["x"], pillar["height"] + PILLAR_GAP, PILLAR_WIDTH, HEIGHT])

def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

# Main game loop
score = 0


q = True
while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                q = False
                break
    

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -10

    # Update bird position and velocity
    bird_y += bird_velocity
    bird_velocity += gravity

    # Update pillar positions
    for pillar in pillars:
        pillar["x"] -= PILLAR_SPEED

    # Check for collisions with pillars
    for pillar in pillars:
        if bird_x < pillar["x"] + PILLAR_WIDTH and bird_x + BIRD_SIZE > pillar["x"]:
            if bird_y < pillar["height"] or bird_y + BIRD_SIZE > pillar["height"] + PILLAR_GAP:
                pygame.quit()
                sys.exit()

    # Check if the bird passed a pillar
    if pillars and pillars[0]["x"] + PILLAR_WIDTH < 0:
        pillars.pop(0)
        pillars.append({"x": WIDTH, "height": random.randint(50, 250)})
        score += 1

    # Check for collisions with the top and bottom of the screen
    if bird_y > HEIGHT or bird_y < 0:
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    draw_bird(bird_x, bird_y)
    draw_pillars(pillars)
    display_score(score)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(30)
