import random
import pygame
from pygame.locals import *
from sys import exit

def dobbelsteen():
    D0    = 'Main/Dice/D0.png'
    D1    = 'Main/Dice/D1.png'
    D2    = 'Main/Dice/D2.png'
    D3    = 'Main/Dice/D3.png'
    D4    = 'Main/Dice/D4.png'
    D5    = 'Main/Dice/D5.png'
    D6    = 'Main/Dice/D6.png'
    dob   = 'Button/GM/knop_roll.png'

    screen_width   = 768
    screen_height  = 1024

    dice_width  =   200
    dice_height =   200
    dice_x      =   10
    dice_y      =   10

    dob_width  =   200
    dob_height =   200
    dob_x      =   10
    dob_y      =   200

    screen = pygame.display.set_mode((screen_height,screen_width),FULLSCREEN, 32)

    dob = pygame.image.load(dob)
    dob = pygame.transform.scale(dob, (dob_width, dob_height))

    player1_dice = 0

    if player1_dice == 0:
        D0 = pygame.image.load(D0).convert_alpha()
        D = pygame.transform.scale(D0, (dice_width, dice_height))


    print("---------------------------------------------------------------")
    #Naam opdracht
    print("Dobbelsteen dobbelen")
    print("---------------------------------------------------------------")

    while True:
        for event in pygame.event.get():
            #anders stop de pygame
            if event.type == QUIT:
                #detect sluitknop
                pygame.quit()
                #sluit de pygame
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print ("X =",mouseX, "Y =",mouseY)
                if mouseX >= dob_x and mouseY >= dob_y and mouseX <= (dob_x+100) and mouseY <= (dob_y+100):
                    print("je hebt de roll knop gevonden")
                player1_dice = random.randint(1,6)
                if player1_dice == 1:
                    D1 = pygame.image.load(D1)
                    D = pygame.transform.scale(D1, (dice_width, dice_height))
                    print ("je hebt 1 gegooid")

                elif player1_dice == 2:
                    D2 = pygame.image.load(D2)
                    D = pygame.transform.scale(D2, (dice_width, dice_height))
                    print ("je hebt 2 gegooid")

                elif player1_dice == 3:
                    D3 = pygame.image.load(D3)
                    D = pygame.transform.scale(D3, (dice_width, dice_height))
                    print ("je hebt 3 gegooid")

                elif player1_dice == 4:
                    D4 = pygame.image.load(D4)
                    D = pygame.transform.scale(D4, (dice_width, dice_height))
                    print ("je hebt 4 gegooid")

                elif player1_dice == 5:
                    D5 = pygame.image.load(D5)
                    D = pygame.transform.scale(D5, (dice_width, dice_height))
                    print ("je hebt 5 gegooid")

                elif player1_dice == 6:
                    D6 = pygame.image.load(D6)
                    D = pygame.transform.scale(D6, (dice_width, dice_height))
                    print ("je hebt 6 gegooid")

                    #als escape wordt ingedrukt
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                #detect sluit knop
                pygame.quit()
                #sluit de pygame
                exit()


        screen.blit(D,(dice_x, dice_y))
        screen.blit(dob,(dob_x, dob_y))



        pygame.display.update()
dobbelsteen()

def main():
    #afbeeldingen locaties aangeven
    board       = 'Main/Game/Spelbord.jpg'
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
    screen = pygame.display.set_mode((screen_height,screen_width),FULLSCREEN, 32)

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
