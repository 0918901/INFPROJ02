import pygame
import random
from pygame.locals import *
from sys import exit

#afbeeldingen locaties aangeven
bg        = 'Main/Game/wood.jpg'
board       = 'Main/Game/board.png'
lp          = 'Button/GM/levenspunten.png'
cp          = 'Button/GM/conditiepunten.png'
ds          = 'Main/Dice/D0.png'
ds1          = 'Main/Dice/D1.png'
ds2          = 'Main/Dice/D2.png'
ds3          = 'Main/Dice/D3.png'
ds4          = 'Main/Dice/D4.png'
ds5          = 'Main/Dice/D5.png'
ds6          = 'Main/Dice/D6.png'
sf          = 'Cards/SFC/SFC1.png'
score       = 'Cards/SC/SC1.jpg'
speler      = 'Player/Faces/S1.png'
pion1       = 'Player/Piece/Rood.png'
quit        = 'Button/GM/kruis.png'
start       = 'Button/GM/help.png'
roll        = 'Button/GM/knop roll.png'

#opstarten van pygame
pygame.init()


#grootte van het scherm aangeven
screen = pygame.display.set_mode((1050, 768))
BG = pygame.image.load(bg).convert()
#achtergrondkleur
#screen.fill((80, 200, 250))

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
#DS = pygame.image.load(ds)
#DS = pygame.transform.scale(DS,(100, 100))

#DS1 = pygame.image.load(ds1)
#DS1 = pygame.transform.scale(DS1,(100, 100))

#DS2  = pygame.image.load(ds2)
#DS2  = pygame.transform.scale(DS2,(100, 100))

#DS3 = pygame.image.load(ds3)
#DS3 = pygame.transform.scale(DS3,(100, 100))

DS4  = pygame.image.load(ds4)
D4  = pygame.transform.scale(DS4,(100, 100))

DS5  = pygame.image.load(ds5)
D5 = pygame.transform.scale(DS5,(100, 100))

DS6  = pygame.image.load(ds6)
D6  = pygame.transform.scale(DS6,(100, 100))

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
        screen.blit(BG, (0,0))
        screen.blit(lifepoints, (20,15))
        screen.blit(gameboard, (20,100))
        screen.blit(CP,(300,15))
        screen.blit(Quit,(950,15))
        screen.blit(Start,(900,15))
        #screen.blit(DS,(900,80))
        screen.blit(Roll,(900,200))
        screen.blit(SF,(550,100))
        screen.blit(Speler,(850,350))
        screen.blit(red_Pion,(460,530))
        screen.blit(Score,(550,440))

        pygame.display.update()

        rolling = (random.randint(2,5))


        DS  =  pygame.transform.scale(DS,(100, 100))
        D2  = pygame.transform.scale(DS2,(100, 100))

        if rolling==1:

            DS4  = pygame.image.load(ds)
            D = pygame.transform.scale(DS,(100, 100))
            screen.blit(DS4,(900,80))
            print('rolling dice1')

        elif rolling==2:

            DS2  = pygame.image.load(ds2)
            D2  = pygame.transform.scale(DS2,(100, 100))
            screen.blit(DS2,(900,80))
            print('rolling dice2')


        elif rolling==3:

            DS3  = pygame.image.load(ds3)
            D3  = pygame.transform.scale(D3,(100, 100))
            screen.blit(DS3,(900,80))
            print('rolling dice3')



    #Scherm vernieuwen bij verandering
