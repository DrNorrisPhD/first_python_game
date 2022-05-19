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
floor = 500

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

class Player:
    def __init__(self, coords, size):
        self.x = coords[0]
        self.y = coords[1]
        self.width, self.height = self.size = size
        # self.surface = pygame.Surface(size)
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.sprite = pygame.image.load('sprites/ball_sprite.png')
        
    def move(self, direction: int, sprint: bool, step: float):
        self.old_coords = (self.x, self.y)
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
        if self.x < 0 or self.y < 0 or self.x+self.width > width or self.y+self.height > height:
            self.x, self.y = self.old_coords
            # self.x -= self.width
            # self.y -= self.height
        if self.y+self.height > floor:
            self.y = floor-self.height
    def gravity(self, speed: float):
        if self.y+self.height < floor:
            self.move(DOWN, False, speed)
    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))
    def update(self):
        if self.y+player.height > floor:
            self.y = floor-player.height
        self.hitbox = (self.x, self.y, self.width, self.height)
    
        
            
class Enemy:
    def __init__(self, coords, type):
        self.x = coords[0]
        self.y = coords[1]
        self.type = type
            
class Platform:
    def __init__(self, coords, size):
        self.x = coords[0]
        self.y = coords[1]
        self.size = size



class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FUCHSIA = (246, 29, 102)
    YELLOW = (255, 255, 0)
    SKY_BLUE = (0, 116, 220)



player = Player((width/2, 400), (49, 49))
colors = Colors
acceleration = 0.15
velocity = 0.0
speed = 0.0

while True:
    width, height = size = pygame.display.get_surface().get_size()
    if player.y > floor:
        player.y = floor
    screen.fill(colors.SKY_BLUE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Applies gravity to the player
    
    player.gravity(speed)
    velocity += acceleration
    speed += velocity
    
    # Log the player's speed, acceleration and velocity to the console
    print(str(velocity) + ", " + str(acceleration) + ", " + str(speed))
    
    if player.y+player.height >= floor:
        speed = 0.0
        velocity = 0.0
    sprint = False
    
    # Check if movement keys are pressed
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] or pressed[pygame.K_UP] or pressed[pygame.K_SPACE] or player.y+player.height < floor:# or player.y+player.height > floor:
        player.move(UP, sprint, 20.0)
    if pressed[pygame.K_CAPSLOCK] or pressed[pygame.K_LSHIFT]:
        sprint = True
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        player.move(LEFT, sprint, 3.0)
    # if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        # player.move(DOWN, sprint, 3.0)
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        player.move(RIGHT, sprint, 3.0)
    
    # Update the scene
     
    player.update()
    player.draw()
    
    # Log the player's X and Y to the console
    print(str(player.x) + ", " + str(player.y))

    pygame.display.update()
    clock.tick(60)