import pygame, random
from pygame.locals import *
from sys import exit

pygame.init()
WINDOWS_SIZE =[750,500]
screen = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption('bordspel')

screen.fill((255,0,200))


while True:
    # ophalen van pygame event
    for event in pygame.event.get():
        # anders stop de pygame
        if event.type == QUIT:
            # detect sluitknop

            pygame.quit()
            # sluit de pygame
            exit()

pygame.display.flip()
pygame.quit()