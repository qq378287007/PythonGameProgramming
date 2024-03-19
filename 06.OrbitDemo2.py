import sys
import math

import pygame
from pygame.locals import *


# Point class
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # X property
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    # Y property
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"


# print_text function
def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


screen_width = 800
screen_height = 600

radius = 250
angle = 0.0
rangle = 0.0
pos = Point(0, 0)
old_pos = Point(radius, 0)

# main program begins
pygame.init()
pygame.display.set_caption("Orbit Demo")

screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font(None, 18)

# load bitmaps
space = pygame.image.load("06.space.png").convert_alpha()

planet = pygame.image.load("06.planet2.png").convert_alpha()
planet_width, planet_height = planet.get_size()
planet_x, planet_y = (screen_width-planet_width)/2, (screen_height-planet_height)/2

ship = pygame.image.load("06.freelance.png").convert_alpha()
#ship = pygame.image.load("06.military.png").convert_alpha()
ship_width, ship_height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (ship_width//2, ship_height//2))

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    # draw background
    screen.blit(space, (0, 0))

    # draw planet
    screen.blit(planet, (planet_x, planet_y))

    # move the ship
    angle += 0.1
    pos.x = math.cos(math.radians(angle)) * radius
    pos.y = math.sin(math.radians(angle)) * radius
    
    delta_x = (pos.x - old_pos.x)
    delta_y = (pos.y - old_pos.y)
    rangle = math.atan2(delta_y, delta_x)
    rangled = -math.degrees(rangle)
    scratch_ship = pygame.transform.rotate(ship, rangled)
    #scratch_ship = pygame.transform.rotate(ship, -(angle+90))
    scratch_ship_width, scratch_ship_height = scratch_ship.get_size()
    
    x = screen_width//2 + pos.x - scratch_ship_width//2
    y = screen_height//2 + pos.y - scratch_ship_height//2
    screen.blit(scratch_ship, (x, y))
    
    print_text(font, 0, 0, "Orbit: " + "{:.0f}".format(angle))
    print_text(font, 0, 20, "Rotation: " + "{:.2f}".format(rangle))
    print_text(font, 0, 40, "Position: " + str(pos))
    print_text(font, 0, 60, "Old Pos: " + str(old_pos))

    pygame.display.update()

    # remember position
    old_pos.x = pos.x
    old_pos.y = pos.y
