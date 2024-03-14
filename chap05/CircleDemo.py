# Circle Demo
# Chapter 5

import random
import math
import sys

import pygame
from pygame.locals import *

# main program begins
pygame.init()
pygame.display.set_caption("Circle Demo")

screen = pygame.display.set_mode((600, 500))
screen.fill((0, 0, 100))

center_x = 300
center_y = 250
radius = 200
angle = 360

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    # increment angle
    angle += 1
    if angle >= 360:
        angle = 0
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = r, g, b

    # calculate coordinates
    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius

    # draw one step around the circle
    center = (int(center_x + x), int(center_y + y))
    pygame.draw.circle(screen, color, center, 10, 0)

    pygame.display.update()
