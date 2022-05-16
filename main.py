import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode(
    (800, 600), pygame.DOUBLEBUF | pygame.RESIZABLE # | pygame.OPENGL
)
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
width = 800
height = 600

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

class Player:
    def __init__(self, coords, size):
        self.x = coords[0]
        self.y = coords[1]
        self.width, self.height = self.size = size
        surface = pygame.Surface(size)
        
    def move(self, direction: int, sprint: bool, step: float):
        if sprint == True:
            step *= 2
        if direction == UP:
            self.y -= step
        elif direction == LEFT:
            self.x -= step
        elif direction == DOWN:
            self.y += step
        elif direction == RIGHT:
            self.x += step
    def gravity(self, speed: float):
        if self.y < 500:
            self.move(DOWN, False, speed)
    def draw(self):
        pygame.draw.circle(screen, colors.BLUE, (self.x, self.y), 20)
    
        
            
class Enemy:
    def __init__(self, coords, type):
        self.x = coords[0]
        self.y = coords[1]
        self.type = type
            
class Platform:
    def __init__(self, coords, size):
        self.x = coords[0]



class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FUCHSIA = (246, 29, 102)
    YELLOW = (255, 255, 0)



player = Player((0, 0))
colors = Colors
acceleration = 2.0
velocity = 0.0
speed = 0.0

while True:
    width, height = size = pygame.display.get_surface().get_size()
    if player.y > 500:
        player.y = 500
    screen.fill(colors.FUCHSIA)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Applies gravity to the player
    
    player.gravity(speed)
    velocity += acceleration
    speed += velocity
    if player.y >= 500:
        speed = 0.0
        velocity = 0.0
    sprint = False
    
    # Check if movement keys are pressed
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_CAPSLOCK] or pressed[pygame.K_LSHIFT]:
        sprint = True
    if pressed[pygame.K_w] or pressed[pygame.K_UP] or pressed[pygame.K_SPACE] or player.y < 500:
        player.move(UP, sprint, 10.0)
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        player.move(LEFT, sprint, 1.0)
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        player.move(DOWN, sprint, 1.0)
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        player.move(RIGHT, sprint, 1.0)
    
    player.draw()

    pygame.display.update()
    clock.tick(60)