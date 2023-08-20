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

BLUE = (0, 0, 255)
RED = (255, 0, 0)
RECT_SIZE = (100, 50)

DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_SIDE, SCREEN_SIDE))
pygame.display.set_caption("Casse-Briques")



class Brick(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.size = (100, 50)
        self.image = pygame.image.load("RedRectangle.png")
        self.rect = pygame.Rect((x, y), self.size)
        self.x = x
        self.y = y
        self.color = RED

blocks = pygame.sprite.Group()

for i in range(10, 891, 110):
    for j in range(25, 475, 55):
        blocks.add(Brick(i,j))

while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY_SURFACE.fill(BLUE)
    for block in blocks:
        DISPLAY_SURFACE.blit(block.image, block.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)