import pygame
from pygame.locals import *
from sys import exit

#afbeelding locaties
bg = 'Main/Menu/bg.jpg'
play = 'Button/SM/play.png'
quit = 'Button/SM/quit.png'

SCREEN_SIZE = (1050, 768)

#opstarten van pygame
pygame.init()

#grootte van het scherm
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
BG = pygame.image.load(bg).convert()

#laden van play_button
playbutton = pygame.image.load(play)

#laden van close_button
closebutton = pygame.image.load(quit)

while True:
    #ophalen van pygame
    for event in pygame.event.get():
        #anders stop de pygame
        if event.type == QUIT:
            #sluitknop
            pygame.quit()
            #sluit pygame
            exit()

    #venster vergroten
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resized to "+str(event.size))



    #locaties in menu
    screen.blit(BG, (0,0))
    screen.blit(playbutton, (20,300))
    screen.blit(closebutton, (20,500))

    #Scherm vernieuwen bij verandering
    pygame.display.update()