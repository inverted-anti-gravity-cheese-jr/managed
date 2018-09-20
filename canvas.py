import sys, pygame
from pygame import Surface
pygame.init()

screenSize = screenWidth, screenHeight = 640, 480

canvas = Surface((screenWidth / 2, screenHeight / 2))
screen = pygame.display.set_mode(screenSize)