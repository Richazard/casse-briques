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
RECT_SIZE = (100, 50)

DISPLAYSURF = pygame.display.set_mode((SCREEN_SIDE, SCREEN_SIDE))
pygame.display.set_caption("Casse-Briques")


class Brick(pygame.sprite.Sprite):

    def __init__(self, x, y, hits):
        super().__init__()
        self.size = (100, 50)
        self.hits = hits
        self.x = x
        self.y = y
        self.color = BLUE




