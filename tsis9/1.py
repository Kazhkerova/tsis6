import pygame
import sys
from pygame.locals import *
import random

def main() -> None:
    # Constants
    FPS = 60
    w = 400
    h = 600
    WHITE = (255, 255, 255)
    GOLD = (255, 215, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # Initialize Pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((w, h))
    stree = pygame.image.load("/Users/asus2/OneDrive/Рабочий стол/pp2/tsis8/Street.png")
    pygame.display.set_caption("Game")

    # Clock for controlling FPS
    FramePerSec = pygame.time.Clock()

    # Font setup
    font = pygame.font.SysFont("Verdana", 20)

    # Enemy class
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("/Users/asus2/OneDrive/Рабочий стол/pp2/tsis8/Enemy.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, w - 40), 0)
            self.speed = 5  # Initial speed

        def move(self):
            self.rect.move_ip(0, self.speed)
            if self.rect.bottom > h:
                self.rect.top = 0
                self.rect.center = (random.randint(30, 370), 0)

        def draw(self, surface):
            surface.blit(self.image, self.rect)

    # Player class
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load("/Users/asus2/OneDrive/Рабочий стол/pp2/tsis8/Player.png"), (90, 90))
            self.rect = self.image.get_rect()
            self.rect.center = (w / 2, h - 100)

        def update(self):
            pressed_keys = pygame.key.get_pressed()
            if self.rect.top > 0 and pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
            if self.rect.bottom < h and pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
            if self.rect.left > 0 and pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if self.rect.right < w and pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

        def draw(self, surface):
            surface.blit(self.image, self.rect)

    # Coin class
    class Coin(pygame.sprite.Sprite):
        def __init__(self, weight):
            super().__init__()
            self.weight = weight
            self.width = self.weight * 20
            self.height = self.weight * 20
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.rect(self.image, GOLD, (0, 0, self.width, self.height))  # Coin size based on weight
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(75, w - 75), random.randint(100, h - 100))

        def draw(self, surface):
            surface.blit(self.image, self.rect)

    # Function to display game over screen
    def game_over_screen():
        game_over_text = font.render("Game Over", True, RED)
        text_rect = game_over_text.get_rect(center=(w/ 2, w / 2))
        screen.blit(game_over_text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)

    # Game initialization
    coin_counter = 0
    coins = pygame.sprite.Group()
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group(enemy)

    # Flags to track the appearance of enemies and coins
    enemy_on_screen = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update player and enemy
        player.update()
        enemy.move()

        screen.blit(stree, (0, 0))

        # Draw player and enemy
        player.draw(screen)
        enemy.draw(screen)

        # Collision detection with enemy
        if pygame.sprite.spritecollide(player, enemies, False):
            game_over_screen()
            pygame.quit()
            sys.exit()

        # Generate coins randomly
        if not coins and random.randint(1, 100) <= 3:
            weight = random.randint(1, 3)
            coin = Coin(weight)
            coins.add(coin)

        # Draw and handle collision with coins
        for coin in coins:
            coin.draw(screen)
        coin_collisions = pygame.sprite.spritecollide(player, coins, True)
        coin_counter += len(coin_collisions)

        # Increase enemy speed when the player earns N coins
        if coin_counter % 10 == 0 and coin_counter != 0:
            enemy.speed += 1

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    main()