import pygame
import random
from pygame.locals import *
from sys import exit
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
gameDisplay.fill((255,200,240))
gameExit = False
while not gameExit:
    # ophalen van pygame event
    for event in pygame.event.get():
        # anders stop de pygame
        if event.type == QUIT:
            # detect sluitknop
            gameExit = True
            # sluit de pygame




pygame.quit()
quit()