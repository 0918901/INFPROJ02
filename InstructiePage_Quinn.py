# Reuben heeft het bijgewerkt
#Bestanden importeren
import pygame
from sys import exit
from pygame import *


#afbeeldingen inladen
background_image   = 'Main/Instructions/SH.jpg'
terug              = 'Main/instructions/Kruis2.png'

#Grootte van scherm aangeven
screen_width        = 768
screen_height       = 1024

#Grootte van knoppen aangeven
RodeKnopje_width        = 40
RodeKnopje_height       = 40

tk_x = 915
tk_y = 15

#venster aanroepen met dubble buffer [extra snelheid](sneller laden)
screen = pygame.display.set_mode((screen_height,screen_width))

#Achtergrond aanroepen en vervormen naar schermgrootte [boven aangegeven](regel 14-15)
background_image = pygame.image.load(background_image)
background_image = pygame.transform.scale(background_image, (screen_height,screen_width))

#Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
terug_knop = pygame.image.load(terug)
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
            if mouseX >= tk_x and mouseY >= tk_y and mouseX <= tk_x + RodeKnopje_width  and mouseY <= tk_y +RodeKnopje_height :
                #print dat de play knop is vonden (muisdetectie) [controle]
                print("je hebt de terug knop gevonden")
                #Haal informatie op van Python file
                from Game_joey import *

    #toon in venster (image, (x, y))
    screen.blit(background_image, (0, 0))
    screen.blit(terug_knop,(tk_x,tk_y))

    #vernieuw de venster op verandering
    pygame.display.update()

