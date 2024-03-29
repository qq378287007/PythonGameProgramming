import math
import sys

import pygame
from pygame.locals import *

color = 255, 0, 255
rect = 200, 150, 200, 200
start_angle = math.radians(0)
end_angle = math.radians(180)
width = 8

pygame.init()
pygame.display.set_caption("Drawing Arcs")

screen = pygame.display.set_mode((600, 500))

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    # draw the arc
    pygame.draw.arc(screen, color, rect, start_angle, end_angle, width)
    pygame.display.update()
