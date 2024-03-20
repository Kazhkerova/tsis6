import pygame
import sys

pygame.init()

w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Moving Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball parameters
r = 25
x = w // 2
y = h // 2
v= 20

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - v >= 0:
                   y-= v
            elif event.key == pygame.K_DOWN:
                if y + v <= h:
                  y+= v
            elif event.key == pygame.K_LEFT:
                if x-v >= 0:
                    x-= v
            elif event.key == pygame.K_RIGHT:
                if x + v <= w:
                   x+= v

    # Fill the screen with white color
    screen.fill(WHITE)
    
    # Draw the ball
    pygame.draw.circle(screen, RED, (x, y), r)
    
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()