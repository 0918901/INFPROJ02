import random
import pygame
from pygame.locals import *
from sys import exit


D0    = 'Main/Dice/D0.png'
D1    = 'Main/Dice/D1.png'
D2    = 'Main/Dice/D2.png'
D3    = 'Main/Dice/D3.png'
D4    = 'Main/Dice/D4.png'
D5    = 'Main/Dice/D5.png'
D6    = 'Main/Dice/D6.png'
dob   = 'Button/GM/knop roll.png'

screen_width   = 768
screen_height  = 1024

dice_width  =   200
dice_height =   200
dice_x      =   300
dice_y      =   200

dob_width  =   200
dob_height =   200
dob_x      =   500
dob_y      =   200

screen = pygame.display.set_mode((screen_height,screen_width), DOUBLEBUF, 32)

dob = pygame.image.load(dob)
dob = pygame.transform.scale(dob, (dob_width, dob_height))

player1_choice = 0

if player1_choice == 0:
    D0 = pygame.image.load(D0).convert_alpha()
    D = pygame.transform.scale(D0, (dice_width, dice_height))

if player1_choice == 1:
    D1 = pygame.image.load(D1).convert_alpha()
    D = pygame.transform.scale(D1, (dice_width, dice_height))

if player1_choice == 2:
    D2 = pygame.image.load(D2).convert_alpha()
    D = pygame.transform.scale(D2, (dice_width, dice_height))

if player1_choice == 3:
    D3 = pygame.image.load(D3).convert_alpha()
    D = pygame.transform.scale(D3, (dice_width, dice_height))

if player1_choice == 4:
    D4 = pygame.image.load(D4).convert_alpha()
    D = pygame.transform.scale(D4, (dice_width, dice_height))

if player1_choice == 5:
    D5 = pygame.image.load(D5).convert_alpha()
    D = pygame.transform.scale(D5, (dice_width, dice_height))

if player1_choice == 6:
    D6 = pygame.image.load(D6).convert_alpha()
    D = pygame.transform.scale(D6, (dice_width, dice_height))


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
            player1_choice = random.randint(1,6)
            if player1_choice == 0:
                D0 = pygame.image.load(D0)
                D = pygame.transform.scale(D0, (dice_width, dice_height))
                print ("je hebt 0 gegooid")

            elif player1_choice == 1:
                D1 = pygame.image.load(D1)
                D = pygame.transform.scale(D1, (dice_width, dice_height))
                print ("je hebt 1 gegooid")

            elif player1_choice == 2:
                D2 = pygame.image.load(D2)
                D = pygame.transform.scale(D2, (dice_width, dice_height))
                print ("je hebt 2 gegooid")

            elif player1_choice == 3:
                D3 = pygame.image.load(D3)
                D = pygame.transform.scale(D3, (dice_width, dice_height))
                print ("je hebt 3 gegooid")

            elif player1_choice == 4:
                D4 = pygame.image.load(D4)
                D = pygame.transform.scale(D4, (dice_width, dice_height))
                print ("je hebt 4 gegooid")

            elif player1_choice == 5:
                D5 = pygame.image.load(D5)
                D = pygame.transform.scale(D5, (dice_width, dice_height))
                print ("je hebt 5 gegooid")

            elif player1_choice == 6:
                D6 = pygame.image.load(D6)
                D = pygame.transform.scale(D6, (dice_width, dice_height))
                print ("je hebt 6 gegooid")


    screen.blit(D,(dice_x, dice_y))
    screen.blit(dob,(dob_x, dob_y))



    pygame.display.update()
