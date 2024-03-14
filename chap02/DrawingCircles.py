# Drawing Circles
# Python 3.2

import sys

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Drawing Circles")

screen = pygame.display.set_mode((600, 500))

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    # draw a circle
    color = 255, 255, 0
    center = 300, 250
    radius = 100
    width = 10

    pygame.draw.circle(screen, color, center, radius, width)
    pygame.display.update()
