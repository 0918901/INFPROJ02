import random
import pygame
from pygame.locals import *
from sys import exit

def main():
    #afbeeldingen locaties aangeven
    board       = 'Main/Instructions/SH.jpg'
    lp          = 'Button/GM/levenspunten.png'
    cp          = 'Button/GM/conditiepunten.png'
    ds          = 'Main/Dice/D0.png'
    sf          = 'Cards/SFC/SFC1.png'
    score       = 'Cards/SFC/SC1.png'
    speler      = 'Player/S1.png'
    pion1       = 'Player/Piece/Rood.png'

    #opstarten van pygame
    pygame.init()

    #Grootte van scherm aangeven
    screen_width        = 768
    screen_height       = 1024

    #grootte van het scherm aangeven
    screen = pygame.display.set_mode((screen_height,screen_width))

    #Laden van afbeelding
    spelbord = pygame.image.load(board).convert()
    #Hervormen van de afbeelding
    gameboard = pygame.transform.scale(spelbord, (1024, 768))

    #zolang de bovenstaande klopt
    while True:
        #ophalen van pygame event
        for event in pygame.event.get():
            #anders stop de pygame
            if event.type == QUIT:
                #detect sluitknop
                pygame.quit()
                #sluit de pygame
                exit()

            #als escape wordt ingedrukt
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                #detect sluit knop
                pygame.quit()
                #sluit de pygame
                exit()


        #locaties op het spelbord
        screen.blit(gameboard, (0,0))

        #Scherm vernieuwen bij verandering
        pygame.display.update()

main()
