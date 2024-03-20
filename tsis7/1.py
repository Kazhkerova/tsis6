import pygame
import sys
from datetime import datetime
import os

# Initialize Pygame
pygame.init()

# Set up the screen
width =1000
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

# Load Mickey's image
mp=os.path.join('OneDrive','Рабочий стол','pp2','tsis7','mickey.png')
mi= pygame.image.load(mp)
l=os.path.join('OneDrive','Рабочий стол','pp2','tsis7','leftarm.png')
ml=pygame.image.load(l)
r=os.path.join('OneDrive','Рабочий стол','pp2','tsis7','rightarm.png')
mr=pygame.image.load(r)
def draw_clock():
    screen.fill((255, 255, 255))  # Fill the screen with white color
    
    # Get current time
    current_time = datetime.now().time()
    hour_angle = (current_time.hour % 12) * 30 + current_time.minute * 0.5
    minute_angle = current_time.minute * 6
    mk=mi.get_rect(center=(width//2,height//2))
    screen.blit(mi,mk)
    # Rotate Mickey's hands
    hour = pygame.transform.rotate(mr, -hour_angle)
    h=hour.get_rect(center=mk.center)
    screen.blit(hour,h)
    minute = pygame.transform.rotate(ml, -minute_angle)
    m=minute.get_rect(center=mk.center)
    screen.blit(minute,m)
    
    
    
    pygame.display.update()

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_clock()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
sys.exit()