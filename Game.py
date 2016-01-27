import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)



#setDisplay = pygame.display.set_mode( (300,300) )
pygame.display.set_caption('epic game')

#img = pygame.image.load('Button/GM/conditiepunten.png')
FPS = 30
dispWidth=800
dispHeight=600
cellSize=10

UP='up'
DOWN='down'
RIGHT='right'
LEFT='left'

def runGame():
    startx=3
    starty=3
    coords=[{'x':startx, 'y':starty}]
    direction  =RIGHT
fpsTime = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
             pygame.quit()
             sys.exit()

        elif event.type == KEYDOWN:
            if event.key ==K_LEFT:
                direction= LEFT
            elif event.key ==K_RIGHT:
                direction= RIGHT
            elif event.key ==K_DOWN:
                direction= DOWN
            elif event.key ==K_UP:
                direction= UP
pygame.display.update()
fpsTime.tick(FPS)
