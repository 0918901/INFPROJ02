import pygame
import random
from pygame.locals import *
from sys import exit

# afbeeldingen locaties aangeven
bg = 'Main/Game/wood.jpg'
board = 'Main/Game/board.png'
lp = 'Button/GM/levenspunten.png'
cp = 'Button/GM/conditiepunten.png'

#dobbelsteen
ds = 'Main/Dice/D1.png'
ds2 = 'Main/Dice/D2.png'
ds3 = 'Main/Dice/D3.png'
ds4 = 'Main/Dice/D4.png'
ds5 = 'Main/Dice/D5.png'
ds6 = 'Main/Dice/D6.png'

sf = 'Cards/SFC/SFC1.jpg'
score = 'Cards/SC/SC1.jpg'
speler = 'Player/Faces/S1.png'
pion1 = 'Player/Piece/Rood.png'
pion2 = 'Player/Piece/Blauw.png'
quit = 'Button/GM/Kruis.png'
start = 'Button/GM/help.png'
roll = 'Button/GM/knop_roll.png'
knop1 = 'Button/GM/kies_1.png'
knop2 = 'Button/GM/kies_2.png'
knop3 = 'Button/GM/kies_3.png'

#knop1
button_width        = 100
button_height       = 100
button_x            = 900
button_y            = 200

#dice
dice_width      =  100
dice_height     =  100

# opstarten van pygame
pygame.init()

# grootte van het scherm aangeven
screen = pygame.display.set_mode((1024, 768))
BG = pygame.image.load(bg).convert()
# achtergrondkleur
# screen.fill((80, 200, 250))

# Laden van afbeelding
spelbord = pygame.image.load(board)

# Hervormen van de afbeelding
gameboard = pygame.transform.scale(spelbord, (500, 500))

# Laden van afbeelding
levenspunt = pygame.image.load(lp)

# Hervormen van de afbeelding
lifepoints = pygame.transform.scale(levenspunt, (250, 50))

# conditiepunten afbeelding
CP = pygame.image.load(cp)
CP = pygame.transform.scale(CP, (40, 40))

# Quit button
Quit = pygame.image.load(quit)
Quit = pygame.transform.scale(Quit, (40, 40))

# Start button
Start = pygame.image.load(start)
Start = pygame.transform.scale(Start, (40, 40))

# dobbelsteen
DS = pygame.image.load(ds)
DS = pygame.transform.scale(DS, (dice_width,dice_height ))

# knop roll
Roll = pygame.image.load(roll)
Roll = pygame.transform.scale(Roll, (button_width, button_height))

# superfight kaart
SF = pygame.image.load(sf).convert_alpha()
SF = pygame.transform.scale(SF, (200, 300))

# score
Score = pygame.image.load(score)
Score = pygame.transform.scale(Score, (300, 300))

# player
Speler = pygame.image.load(speler)
Speler = pygame.transform.scale(Speler, (100, 100))

red_Pion = pygame.image.load(pion1)
red_Pion = pygame.transform.scale(red_Pion, (50, 50))

blue_Pion = pygame.image.load(pion2)
blue_Pion = pygame.transform.scale(blue_Pion, (50, 50))

# knop1
Knop1 = pygame.image.load(knop1)
Knop1 = pygame.transform.scale(Knop1, (60, 60))

# knop2
Knop2 = pygame.image.load(knop2)
Knop2 = pygame.transform.scale(Knop2, (60, 60))

# knop3
Knop3 = pygame.image.load(knop3)
Knop3 = pygame.transform.scale(Knop3, (60, 60))

# zolang de bovenstaande kloptKnop3 = pygame.transform.scale(Knop3, (60, 60))

D1 = pygame.image.load(ds)
D = pygame.transform.scale(D1, (dice_width, dice_height))

# Coördinaten vakken
vakjes = [[470, 105], [470, 152], [470, 188], [470, 225], [470, 263], [470, 320], [470, 377], [470, 415], [470, 450], [470, 490], [470, 542],
         [418, 472], [380, 472], [343, 472], [306, 472], [250, 472], [192, 472], [154, 472], [118, 472], [80, 472], [30, 472], [30, 419], [30, 380],
         [30, 344], [30, 306], [30, 249], [30, 193], [30, 156], [30, 119], [30, 81], [30, 30], [80, 32], [120, 32], [155, 32], [193, 32], [250, 32],
         [306, 32], [343, 32], [381, 32], [418, 32]]

# pion positie
vak = 0
print(vakjes[vak] [0], vakjes [vak] [1])

red_Pion_x = vakjes[vak] [0]
red_Pion_y = vakjes[vak] [1]


while True:
    # ophalen van pygame event
    for event in pygame.event.get():
        # anders stop de pygame
        if event.type == QUIT:
            # detect sluitknop
            pygame.quit()
            # sluit de pygame
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()

            if mouseX >=(button_x+900) and mouseY>= (button_y+200):
                print("je hebt de roll knop gevonden")
            player1_choice = random.randint(1,6)
            vak = vak + player1_choice
            red_Pion_x = vakjes[vak] [0]
            red_Pion_y = vakjes[vak] [1]
            if player1_choice == 1:

                D1 = pygame.image.load(ds)
                D = pygame.transform.scale(D1, (dice_width, dice_height))
                print ("je hebt 1 gegooid")

            elif player1_choice == 2:
                D2 = pygame.image.load(ds2)
                D = pygame.transform.scale(D2, (dice_width, dice_height))
                print ("je hebt 2 gegooid")

            elif player1_choice == 3:
                D3 = pygame.image.load(ds3)
                D = pygame.transform.scale(D3, (dice_width, dice_height))
                print ("je hebt 3 gegooid")

            elif player1_choice == 4:
                D4 = pygame.image.load(ds4)
                D = pygame.transform.scale(D4, (dice_width, dice_height))
                print ("je hebt 4 gegooid")

            elif player1_choice == 5:
                D5 = pygame.image.load(ds5)
                D = pygame.transform.scale(D5, (dice_width, dice_height))
                print ("je hebt 5 gegooid")

            elif player1_choice == 6:
                D6 = pygame.image.load(ds6)
                D = pygame.transform.scale(D6, (dice_width, dice_height))
                print ("je hebt 6 gegooid")


    # locaties op het spelbord
    screen.blit(BG, (0, 0))
    screen.blit(lifepoints, (20, 15))
    screen.blit(gameboard, (20, 100))
    screen.blit(CP, (300, 15))
    screen.blit(Quit, (950, 15))
    screen.blit(Start, (900, 15))
    screen.blit(D, (900, 80))
    screen.blit(Roll, (900, 200))
    screen.blit(SF, (550, 20))
    screen.blit(Speler, (850, 450))
    screen.blit(Score, (550, 350))
    screen.blit(Knop1, (550, 650))
    screen.blit(Knop2, (650, 650))
    screen.blit(Knop3, (750, 650))
    screen.blit(red_Pion, (red_Pion_x, red_Pion_y))
    # Scherm vernieuwen bij verandering
    pygame.display.update()
