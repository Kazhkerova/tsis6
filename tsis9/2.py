import pygame
import sys
import random
from pygame.math import Vector2

# Инициализация Pygame
pygame.init()

# Глобальные переменные
CELL_SIZE = 40
CELL_NUMBER = 20
SCREEN_SIZE = (CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE)
SCREEN_COLOR = (255,255,255)
FPS = 10

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def grow(self):
        self.new_block = True

    def draw(self, surface):
        for block in self.body:
            pygame.draw.rect(surface, (255,0,0), (block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Класс фруктов
class Fruit:
    def __init__(self):
        self.randomize()
        self.time_to_live = 60 # 1 секунды при 60 fps


    def randomize(self):
        self.pos = Vector2(random.randint(0, CELL_NUMBER - 1), random.randint(0, CELL_NUMBER - 1))
        self.size = random.randint(1, 3)  # Случайный размер от 1 до 3
    
    def update(self):
        self.time_to_live-=1  
    
    def is_expired(self):
        return self.time_to_live<=0
    
    def draw(self, surface):
        fruit_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, self.size * CELL_SIZE, self.size * CELL_SIZE)
        pygame.draw.rect(surface, (255, 255, 0), fruit_rect)

# Класс игры
class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruits = [Fruit()]
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.score = 0
        self.game_over = False

    def update(self):
        if not self.game_over:
            self.counter += 1
            if self.counter >= 300:  # Увеличиваем счетчик на 1 каждую секунду (при 60 fps)
                self.counter = 0
                for fruit in self.fruits[:]:
                    fruit.update()
                    if fruit.is_expired:
                        self.fruits.remove(fruit)
                        self.fruits.append(Fruit())
            self.snake.move()
            self.check_collision()

    def check_collision(self):
        head = self.snake.body[0]
        # Проверка столкновения со стенами
        if not (0 <= head.x < CELL_NUMBER and 0 <= head.y < CELL_NUMBER):
            self.game_over = True

        for fruit in self.fruits[:]:
            if head == fruit.pos:
                self.snake.grow()
                self.fruits.remove(fruit)
                self.score += 10
                self.fruits.append(Fruit())

    def draw(self, surface):
        surface.fill(SCREEN_COLOR)
        for fruit in self.fruits:
            fruit.draw(surface)
        self.snake.draw(surface)

    def show_game_over(self, surface):
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Score: {self.score}", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2 + 50))
        surface.blit(game_over_text, game_over_rect)
        surface.blit(score_text, score_rect)

# Основная функция
def main():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Snake')
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обработка управления змейкой
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN:
                    game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT:
                    game.snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.snake.direction = Vector2(1, 0)

        game.update()
        game.draw(screen)
        
        if game.game_over:
            game.show_game_over(screen)
        else:
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {game.score}', True, (255, 0, 0))
            screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        game.clock.tick(FPS)

if __name__ == '__main__':
    main()