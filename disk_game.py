import pygame, sys
from pygame.math import Vector2
import random
pygame.init()
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 0, 0)
cell_size = 30
number_of_cells = 25
WIDTH = 750
HEIGHT = 750
GROUND_Y = HEIGHT - 50
FONT = pygame.font.SysFont(None, 48)
man_image = pygame.image.load("apple/man.png.png")
man_image = pygame.transform.scale(man_image, (60,80))
food_image = pygame.image.load("apple/apple.png")
food_image = pygame.transform.scale(food_image, (30,30))
class Food:
    def __init__(self):
        self.image = food_image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(3, 7)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    def move(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
    def reset_position(self):
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(-100, -20)
        self.rect.topleft = (self.x, self.y)
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
class Man:
    def __init__(self):
        self.image = man_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, GROUND_Y)
        self.speed = 7
    def move(self, dx):
        self.rect.x += dx
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
    def draw(self, screen):
        screen.blit(self.image, self.rect)
def draw_text(text, size, color, x, y, center = True):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x,y) if center else (x,y))
    screen.blit(text_surface, text_rect)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Man Cutting Apples")
foods = [Food() for _ in range(2)]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Disk ")
clock = pygame.time.Clock()
man = Man()
score = 0
game_over = False
food = Food()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
         man.move(-man.speed)
        if keys[pygame.K_RIGHT]:
         man.move(man.speed)
        for food in foods:
            food.move()
            if man.rect.colliderect(food.rect):
               score += 1
               food.reset_position()
            if food.y + food.height >= GROUND_Y:
                game_over = True
    screen.fill(BLACK)
    for food in foods:
        if not game_over:
         food.draw(screen)
    man.draw(screen)
    pygame.draw.rect(screen, (100, 50, 0), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    draw_text(f"Score: {score}", 36, WIDTH, 10, 10, center=False)
    if game_over:
      draw_text("GAME OVER", 72, RED, WIDTH // 2, HEIGHT // 2)
      print(" ")
      draw_text(f"Final Score: {score}", 48, WHITE, WIDTH // 2, HEIGHT // 2 + 30)
    pygame.display.update()
    clock.tick(40)
