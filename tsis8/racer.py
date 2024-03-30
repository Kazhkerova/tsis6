import pygame
import sys
import random

pygame.init()
# Screen
w = 900
h = 545
fps= 60
s= 5
coinv = 10
conf = 60  # Coin spawn rate (in frames)
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
# Fonts
font = pygame.font.SysFont("Times New Roman", 60)
small_font = pygame.font.SysFont("Times New Roman", 20)

# Load images
street = pygame.image.load("/Users/asus2/OneDrive/Рабочий стол/pp2/tsis8/Street.png")
player= pygame.transform.scale(pygame.image.load("/Users/asus2/OneDrive/Рабочий стол/pp2/tsis8/Player.png"), (90, 90))
enemy = pygame.image.load("/Users/asus2/OneDrive/Рабочий стол/pp2/tsis8/Enemy.png")
coin = pygame.Surface((30, 30))
coin.fill((255, 255, 0))  # Yellow color

# Create screen
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Racer Game')

# Clock
clock = pygame.time.Clock()
# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (w// 2, h - 100)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= s
        if keys[pygame.K_RIGHT]:
            self.rect.x += s
        # Boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > w:
            self.rect.right = h

# Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(w- self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > h + 10:
            self.rect.x = random.randrange(h - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
# Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(w- self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = coinv

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > h:
            self.rect.x = random.randrange(w - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = coinv

# Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game loop
running = True
score = 0
spawn_timer = 0
enemy_spawned = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn enemies and coins
    spawn_timer += 1
    if spawn_timer % conf == 0:
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Spawn enemy if none exists
    if not enemy_spawned:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        enemy_spawned = True

    # Update
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, coins, True)
    for hit in hits:
        score += 1
        hit.kill()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # If enemy goes off-screen, reset enemy_spawned flag
    if enemy.rect.top >h + 10:
        enemy_spawned = False

    # Draw / render
    screen.blit(street, (0, 0))
    all_sprites.draw(screen)

    # Draw score
    score_text = small_font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(fps)

# Game over
game_over_text = font.render("Game Over", True, red)
screen.blit(game_over_text, (w// 2 - game_over_text.get_width() // 2, h // 2 - game_over_text.get_height() // 2))
pygame.display.flip()
pygame.time.wait(2000)  # 2 seconds delay
pygame.quit()
sys.exit()