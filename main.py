import pygame
import sys
import random
from pygame.locals import *
import time

# Initialization of the game
pygame.init()

# Choice of the FPS value
FPS = 60
FramePerSec = pygame.time.Clock()

# Screen information
SCREEN_SIDE = 1000
SPEED = 5
BLUE = (0, 0, 255)
RED = (255, 0, 0)
RECT_SIZE = (100, 50)

# Creation of the surface
DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_SIDE, SCREEN_SIDE))
pygame.display.set_caption("Casse-Briques")

# Declaration of ball class
class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Yellow_Ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 600)
        self.up_down = 5
        self.right_left = 0

    def move(self):
        self.rect.move_ip(self.right_left, self.up_down)

    def bounce_wall(self):
        if self.rect.top < 0:
            self.up_down *= -1

        if self.rect.left < 0 or self.rect.right > SCREEN_SIDE:
            self.right_left *= -1

    def touch_ground(self):
        if self.rect.bottom > SCREEN_SIDE:
            return True
        return False

class Plate(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Plate.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 980)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(SPEED * -1, 0)

        if self.rect.right < SCREEN_SIDE:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(SPEED, 0)

# Declaration of brick class
class Brick(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.size = (100, 50)
        self.image = pygame.image.load("RedRectangle.png")
        self.rect = pygame.Rect((x, y), self.size)

# Initiating plate and ball

plate = Plate()
ball = Ball()

# Creating sprite group and adding everything to it

forms = pygame.sprite.Group()
forms.add(plate)
forms.add(ball)

for i in range(10, 891, 110):
    for j in range(25, 475, 55):
        forms.add(Brick(i,j))

# Game loop

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY_SURFACE.fill(BLUE)
    for block in forms:
        DISPLAY_SURFACE.blit(block.image, block.rect)

    plate.move()
    ball.bounce_wall()
    ball.move()

    if ball.touch_ground():
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)