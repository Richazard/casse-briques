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
SPEED = 8
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Creation of the surface
DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_SIDE, SCREEN_SIDE))
pygame.display.set_caption("Casse-Briques")


def calculate_coefficient(n1, n2, coeff):
    return (n1-n2)/coeff


# Declaration of ball class
class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Yellow_ball2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 600)
        self.up_down = SPEED
        self.right_left = 0

    def move(self):
        self.rect.move_ip(self.right_left, self.up_down)

    def bounce_wall(self):
        if self.rect.top < 0:
            self.up_down *= -1

        if self.rect.left < 0 or self.rect.right > SCREEN_SIDE:
            self.right_left *= -1

    def bounce_plate(self, plate):

        self.right_left = SPEED * calculate_coefficient(self.rect.centerx, plate.rect.center[0], plate.rect.size[0])
        self.up_down = abs(self.right_left) - SPEED

    def touch_ground(self):
        if self.rect.bottom > SCREEN_SIDE:
            return True
        return False


class Plate(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Plate.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 990)

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
        self.image = pygame.image.load("images/RedRectangle.png")
        self.rect = pygame.Rect((x, y), self.size)

# Initiating plate and ball
plate = Plate()
ball = Ball()

# Creating sprite groups and adding everything to it
bricks = pygame.sprite.Group()

forms = pygame.sprite.Group()
forms.add(plate)
forms.add(ball)

for i in range(10, 891, 110):
    for j in range(25, 475, 55):
        brick = Brick(i,j)
        forms.add(brick)
        bricks.add(brick)




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
    if pygame.sprite.collide_rect(ball, plate):
        ball.bounce_plate(plate)
    ball.bounce_wall()
    ball.move()

    if pygame.sprite.spritecollideany(ball, bricks):

    if ball.touch_ground():
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)