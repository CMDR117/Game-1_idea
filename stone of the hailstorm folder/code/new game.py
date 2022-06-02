from pickle import FALSE
from re import X
from tkinter import EventType
from turtle import position
import pygame, sys, random
import time
from pygame.locals import *
from player import Player
from settings import *
from levels import Level


# Set up pygame.
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
mainClock = pygame.time.Clock()
level = Level(level_map_final,screen)

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)



while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            pass
    


    screen.fill('blue')
    level.run()
    

    pygame.display.update()
    mainClock.tick(60)