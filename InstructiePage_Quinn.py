# Reuben heeft het bijgewerkt
#Bestanden importeren
import pygame
from pygame.locals import *
from sys import exit


#afbeeldingen inladen
background_image    = 'Main/Instructions/SH.jpg'
back               = 'Main/instructions/Kruis2.png'

#Grootte van scherm aangeven
screen_width        = 768
screen_height       = 1024

#Grootte van knoppen aangeven
RodeKnopje_width        = 50
RodeKnopje_height       = 50
tk_x    =   200
tk_y    =   15

#venster aanroepen met dubble buffer [extra snelheid](sneller laden)
screen = pygame.display.set_mode((screen_height,screen_width))

#Achtergrond aanroepen en vervormen naar schermgrootte [boven aangegeven](regel 14-15)
background_image = pygame.image.load(background_image)
background_image = pygame.transform.scale(background_image, (screen_height,screen_width))

#Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
terug_knop = pygame.image.load(back)
terug_knop = pygame.transform.scale(terug_knop, (RodeKnopje_width , RodeKnopje_height))


while True:
    #ophalen van pygame event
    for event in pygame.event.get():

        #als event = stop
        if event.type == QUIT:
            #detect sluitknop
            pygame.quit()
            #sluit de pygame
            exit()

        #als event = muisingedrukt
        if event.type == pygame.MOUSEBUTTONDOWN:
            #zoek x & y van muis op
            (mouseX, mouseY) = pygame.mouse.get_pos()
            #print x & y van muis op
            print ("X =",mouseX, "Y =",mouseY)

            #als muis zich bevindt tussen x & y as
            if mouseX >= tk_x and mouseY>= tk_y and mouseX<= tk_x+RodeKnopje_width and mouseY<= tk_y+RodeKnopje_height:
                #print dat de play knop is vonden (muisdetectie) [controle]
                print("je hebt de stop knop gevonden")
                #Haal informatie op van Python file
                from Game_joey import *


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #Haal informatie op van Python file
            from Game_Reuben import *

    #toon in venster (image, (x, y))
    screen.blit(background_image, (0, 0))
    screen.blit(terug_knop,(tk_x,tk_y))

    #vernieuw de venster op verandering
    pygame.display.update()

