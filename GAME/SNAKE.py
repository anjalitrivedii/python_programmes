import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 127)
RED = (255, 69, 58)
BLACK = (20, 20, 20)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Background
def draw_background():
    screen.fill(BLACK)
    for y in range(0, HEIGHT, 2):
        color = (0, int(150 * (y / HEIGHT)), 100)
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

# Snake class
class Snake:
    def __init__(self):
        self.body = [[10, 10]]
        self.direction = [1, 0]
        self.growing = False

    def move(self):
        head = self.body[-1]
        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]
        self.body.append(new_head)

        if self.growing:
            self.growing = False  # One-time grow
        else:
            self.body.pop(0)

    def grow(self):
        self.growing = True  # Trigger grow on next move

    def draw(self):
        for segment in self.body:
            x, y = segment[0] * CELL_SIZE, segment[1] * CELL_SIZE
            pygame.draw.rect(screen, GREEN, (x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4))

    def change_direction(self, new_dir):
        if new_dir[0] != -self.direction[0] or new_dir[1] != -self.direction[1]:
            self.direction = new_dir

    def check_collision(self):
        head = self.body[-1]
        return (
            head in self.body[:-1] or
            head[0] < 0 or head[0] >= WIDTH // CELL_SIZE or
            head[1] < 0 or head[1] >= HEIGHT // CELL_SIZE
        )

# Food class
class Food:
    def __init__(self):
        self.respawn([])

    def draw(self):
        x, y = self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE
        pygame.draw.circle(screen, RED, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 2)

    def respawn(self, snake_body):
        while True:
            pos = [random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1)]
            if pos not in snake_body:
                self.position = pos
                break

# Game Over
def game_over(score):
    screen.fill(BLACK)
    text = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

# Game loop
def game_loop():
    snake = Snake()
    food = Food()
    score = 0

    while True:
        draw_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.change_direction([0, -1])
        elif keys[pygame.K_DOWN]:
            snake.change_direction([0, 1])
        elif keys[pygame.K_LEFT]:
            snake.change_direction([-1, 0])
        elif keys[pygame.K_RIGHT]:
            snake.change_direction([1, 0])

        snake.move()

        # Check food collision
        if snake.body[-1] == food.position:
            score += 1
            snake.grow()
            food.respawn(snake.body)

        # Check collision
        if snake.check_collision():
            game_over(score)
            return

        # Draw everything
        snake.draw()
        food.draw()
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10 + score // 5)

# Start game
try:
    game_loop()
except Exception as e:
    print("Error:", e)
    pygame.quit()
    sys.exit()

