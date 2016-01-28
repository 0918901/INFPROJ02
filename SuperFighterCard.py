import random
import pygame
from pygame.locals import *
from sys import exit


SFCA  = 'Cards/SFC/SFCA.jpg'
SFC1  = 'Cards/SFC/SFC1.jpg'
SFC2  = 'Cards/SFC/SFC2.jpg'
SFC3  = 'Cards/SFC/SFC3.jpg'
SFC4  = 'Cards/SFC/SFC4.jpg'
SFC5  = 'Cards/SFC/SFC5.jpg'
SFC6  = 'Cards/SFC/SFC6.jpg'
SFC7  = 'Cards/SFC/SFC7.jpg'
SFC8  = 'Cards/SFC/SFC8.jpg'
SFC9  = 'Cards/SFC/SFC9.jpg'
SFC10  = 'Cards/SFC/SFC10.jpg'
SFC11  = 'Cards/SFC/SFC11.jpg'
SFC12  = 'Cards/SFC/SFC12.jpg'
SFC13  = 'Cards/SFC/SFC13.jpg'
SFC14  = 'Cards/SFC/SFC14.jpg'
SFC15  = 'Cards/SFC/SFC15.jpg'
SFC16  = 'Cards/SFC/SFC16.jpg'
SFC17  = 'Cards/SFC/SFC17.jpg'
SFC18  = 'Cards/SFC/SFC18.jpg'

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

sfc_width  =   250
sfc_height =   400
sfc_x      =   50
sfc_y      =   200

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

D0 = pygame.image.load(D0).convert_alpha()
D = pygame.transform.scale(D0, (dice_width, dice_height))

SFCA = pygame.image.load(SFCA).convert_alpha()
SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))


player1_choice = 0

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
            if player1_choice == 1:
                D1 = pygame.image.load(D1).convert_alpha()
                D = pygame.transform.scale(D1, (dice_width, dice_height))
                SFC1 = pygame.image.load(SFC1).convert_alpha()
                SFC = pygame.transform.scale(SFC1, (sfc_width, sfc_height))
                print ("je hebt 1 gegooid")

            elif player1_choice == 2:
                D2 = pygame.image.load(D2).convert_alpha()
                D = pygame.transform.scale(D2, (dice_width, dice_height))
                SFC2 = pygame.image.load(SFC2).convert_alpha()
                SFC = pygame.transform.scale(SFC2, (sfc_width, sfc_height))
                print ("je hebt 2 gegooid")

            elif player1_choice == 3:
                D3 = pygame.image.load(D3).convert_alpha()
                D = pygame.transform.scale(D3, (dice_width, dice_height))
                SFC3 = pygame.image.load(SFC3).convert_alpha()
                SFC = pygame.transform.scale(SFC3, (sfc_width, sfc_height))
                print ("je hebt 3 gegooid")

            elif player1_choice == 4:
                D4 = pygame.image.load(D4).convert_alpha()
                D = pygame.transform.scale(D4, (dice_width, dice_height))
                SFC4 = pygame.image.load(SFC4).convert_alpha()
                SFC = pygame.transform.scale(SFC4, (sfc_width, sfc_height))
                print ("je hebt 4 gegooid")

            elif player1_choice == 5:
                D5 = pygame.image.load(D5).convert_alpha()
                D = pygame.transform.scale(D5, (dice_width, dice_height))
                SFC5 = pygame.image.load(SFC5).convert_alpha()
                SFC = pygame.transform.scale(SFC5, (sfc_width, sfc_height))
                print ("je hebt 5 gegooid")

            elif player1_choice == 6:
                D6 = pygame.image.load(D6).convert_alpha()
                D = pygame.transform.scale(D6, (dice_width, dice_height))
                SFC6 = pygame.image.load(SFC6).convert_alpha()
                SFC = pygame.transform.scale(SFC6, (sfc_width, sfc_height))
                print ("je hebt 6 gegooid")

    screen.blit(SFC,(sfc_x, sfc_y))
    screen.blit(D,(dice_x, dice_y))
    screen.blit(dob,(dob_x, dob_y))



    pygame.display.update()
