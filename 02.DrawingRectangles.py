import sys

import pygame
from pygame.locals import *

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1

pygame.init()
pygame.display.set_caption("Drawing Rectangles")

screen = pygame.display.set_mode((600, 500))

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    # move the rectangle
    pos_x += vel_x
    pos_y += vel_y

    # keep rectangle on the screen
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y

    # draw the rectangle
    color = 255, 255, 0
    width = 0  # solid fill
    rect = pos_x, pos_y, 100, 100

    pygame.draw.rect(screen, color, rect, width)
    pygame.display.update()
