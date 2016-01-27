import pygame
from pygame.locals import *
from sys import exit

#afbeeldingen locaties aangeven
board       = 'Main/Game/board.png'
lp          = 'Button/GM/levenspunten.png'
cp          = 'Button/GM/conditiepunten.png'
ds          = 'Main/Dice/D1.png'
sf          = 'Cards/SFC/SFC1.png'
score       = 'Cards/SC/SC1.jpg'
speler      = 'Player/Faces/S1.png'
pion1       = 'Player/Piece/Rood.png'
quit        = 'Button/GM/kruis.png'
start       = 'Button/GM/help.png'
roll        = 'Button/GM/knop roll.png'
bg          = 'Main/Game/wood.jpg'
#opstarten van pygame
pygame.init()


#grootte van het scherm aangeven
screen = pygame.display.set_mode((1024, 768))
#BG = pygame.image.load(bg).convert()
#achtergrondkleur
screen.fill((80, 200, 250))

#Laden van afbeelding
spelbord = pygame.image.load(board)

#Hervormen van de afbeelding
gameboard = pygame.transform.scale(spelbord, (500, 500))

#Laden van afbeelding
levenspunt = pygame.image.load(lp)

#Hervormen van de afbeelding
lifepoints = pygame.transform.scale(levenspunt, (250, 40))

#conditiepunten afbeelding
CP = pygame.image.load(cp)
CP = pygame.transform.scale(CP, (40, 40))

#Quit button
Quit = pygame.image.load(quit)
Quit = pygame.transform.scale(Quit,(40, 40))

#Start button
Start = pygame.image.load(start)
Start = pygame.transform.scale(Start,(40, 40))

#dobbelsteen
DS  = pygame.image.load(ds)
DS = pygame.transform.scale(DS,(100, 100))

# knop roll
Roll = pygame.image.load(roll)
Roll = pygame.transform.scale(Roll,(100, 100))

#superfight kaart
SF = pygame.image.load(sf)
SF = pygame.transform.scale(SF,(200, 300))

#score
Score = pygame.image.load(score)
Score = pygame.transform.scale(Score,(300, 300))

#player
Speler = pygame.image.load(speler)
Speler = pygame.transform.scale(Speler,(100, 100))

red_Pion = pygame.image.load(pion1)
red_Pion= pygame.transform.scale(red_Pion,(50, 50))

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
    screen.blit(lifepoints, (20,15))
    screen.blit(gameboard, (20,100))
    screen.blit(CP,(300,15))
    screen.blit(Quit,(950,15))
    screen.blit(Start,(900,15))
    screen.blit(DS,(900,80))
    screen.blit(Roll,(900,200))
    screen.blit(SF,(550,100))
    screen.blit(Speler,(850,350))
    screen.blit(red_Pion,(460,530))
    screen.blit(Score,(550,440))
    #screen.blit(BG, (0,0))
    #Scherm vernieuwen bij verandering
    pygame.display.update()