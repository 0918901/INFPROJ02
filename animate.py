import os
import random
from sys import exit
import pygame
import sys
import copy
from pygame.locals import *
RED = (255, 0, 0)
white = (255,255,255)

pygame.init()

screen = pygame.display.set_mode((1024, 768))
clock=pygame.time.Clock()


m1 = pygame.image.load("m1.png")
m2 = pygame.image.load("m2.png")

marioCurrentImage =1


screen.fill(white)

x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10
done = False
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 1
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 1

    # --- Game Logic
    pygame.mouse.set_visible(0)
    # Move the object according to the speed vector.

    if (marioCurrentImage==1):



        if (marioCurrentImage==2):

            screen.blit(m2, (10,10))


        if (marioCurrentImage==2):

            marioCurrentImage=1

        else:

            marioCurrentImage+=1;
            screen.blit(m1, (10,10))
        pygame.display.update()
    #zet de limite

    clock.tick(10)
#Afsluiten
pygame.quit()
quit()
