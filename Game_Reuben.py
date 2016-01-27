import pygame
from pygame.locals import *
from sys import exit

#afbeeldingen locaties aangeven
board       = 'Main/Game/board.jpg'
lp          = 'Button/GM/levenspunten.png'
cp          = 'Button/GM/conditiepunten.png'
ds          = 'Main/Dice/D0.png'
sf          = 'Cards/SFC/SFC1.png'
score       = 'Cards/SFC/SC1.png'
speler      = 'Player/S1.png'
pion1       = 'Player/Piece/Rood.png'

#opstarten van pygame
pygame.init()

#grootte van het scherm aangeven
screen = pygame.display.set_mode((800, 600))

#Laden van afbeelding
spelbord = pygame.image.load(board).convert()
#Hervormen van de afbeelding
gameboard = pygame.transform.scale(spelbord, (500, 500))

#Laden van afbeelding
levenspunt = pygame.image.load(lp)
#Hervormen van de afbeelding
lifepoints = pygame.transform.scale(levenspunt, (250, 40))

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
    #locaties op het spelbord
    screen.blit(gameboard, (0,50))
    screen.blit(lifepoints, (0,5))
    screen.blit(gameboard, (0,50))

    #Scherm vernieuwen bij verandering
    pygame.display.update()