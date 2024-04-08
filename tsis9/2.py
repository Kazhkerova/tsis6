import pygame
import time
import random

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)

# Определение констант
w, h = 800, 600
BLOCK_SIZE = 20
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Определение классов
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Food:
    def __init__(self):
        self.position = Point(random.randint(0, w // BLOCK_SIZE - 1) * BLOCK_SIZE, random.randint(0, h // BLOCK_SIZE - 1) * BLOCK_SIZE)
        self.size = random.randint(1, 3)

    def generate_new(self, snake_body):
        self.position = Point(random.randint(0, w // BLOCK_SIZE - 1) * BLOCK_SIZE, random.randint(0, h // BLOCK_SIZE - 1) * BLOCK_SIZE)
        self.size = random.randint(1, 3)
        while self.position in snake_body:
            self.position = Point(random.randint(0, w // BLOCK_SIZE - 1) * BLOCK_SIZE, random.randint(0, h // BLOCK_SIZE - 1) * BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.position.x, self.position.y, BLOCK_SIZE * self.size, BLOCK_SIZE * self.size))

class Snake:
    def __init__(self):
        self.body = [Point(10 * BLOCK_SIZE, 10 * BLOCK_SIZE)]
        self.dx = 1
        self.dy = 0

    def move(self, dx, dy):
        new_head = Point(self.body[0].x + dx * BLOCK_SIZE, self.body[0].y + dy * BLOCK_SIZE)
        self.body.insert(0, new_head)
        self.body.pop()

    def check_collision(self, food):
        return self.body[0].x < food.position.x + food.size * BLOCK_SIZE and \
               self.body[0].x + BLOCK_SIZE > food.position.x and \
               self.body[0].y < food.position.y + food.size * BLOCK_SIZE and \
               self.body[0].y + BLOCK_SIZE > food.position.y

    def check_boundary_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= w or head.y < 0 or head.y >= h

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment.x, segment.y, BLOCK_SIZE, BLOCK_SIZE))

# Определение функций
def draw_grid():
    for x in range(0, w, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, h))
    for y in range(0, h, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (w, y))

def main():
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    score = 0
    level = 1
    to_append = 0
    spawn_time = time.perf_counter()

    font = pygame.font.SysFont(None, 30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx, snake.dy = 0, -1
                elif event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx, snake.dy = 0, 1
                elif event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx, snake.dy = 1, 0
                elif event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx, snake.dy = -1, 0
                elif event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_p:
                    time.sleep(10)

        snake.move(snake.dx, snake.dy)

        if snake.check_boundary_collision():
            running = False

        if snake.check_collision(food):
            spawn_time = time.perf_counter()
            score += 10
            level = score // 30 + 1
            to_append += food.size
            food.generate_new(snake.body)
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            to_append -= 1
        elif to_append > 0:
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))
            to_append -= 1

        if time.perf_counter() - spawn_time > 5:
            spawn_time = time.perf_counter()
            food.generate_new(snake.body)

        score_font = font.render('Score: ' + str(score), True, (255, 255, 255))
        level_font = font.render('Level: ' + str(level), True, (255, 255, 255))
        screen.fill(WHITE)
        screen.blit(score_font, (0, h))
        screen.blit(level_font, (w // 2, h))

        snake.draw()
        food.draw()
        draw_grid()

        pygame.display.flip()
        clock.tick(2 * level + 5)

    # После выхода из цикла while (когда игра завершается)
    game_over_font = font.render('Game Over', True, (255, 0, 0))
    score_message_font = font.render('Your score is: ' + str(score), True, (255, 0, 0))
    screen.blit(game_over_font, (w // 2 - 100, h // 2))
    screen.blit(score_message_font, (w // 2 - 100, h // 2 + 50))
    pygame.display.flip()
    time.sleep(3)  # Подождать 3 секунды перед завершением игры

if __name__ == '__main__':
    main()
