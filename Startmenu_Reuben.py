#Bestanden importeren
import pygame
from pygame.locals import *
from sys import exit


#afbeeldingen inladen
background_image    = 'Main/Menu/bg.jpg'
logo_image          = 'Main/Logo2.png'
play_button         = 'Button/SM/play.png'
stop_button         = 'Button/SM/quit.png'

#Grootte van scherm aangeven
screen_width        = 768
screen_height       = 1024

#Grootte van knoppen aangeven
button_width        = 600
button_height       = 100

#Grootte van logo aangeven
logo_width          = 800
logo_height         = 200

#venster aanroepen met dubble buffer [extra snelheid](sneller laden)
screen = pygame.display.set_mode((screen_height,screen_width),FULLSCREEN, 32)

#Achtergrond aanroepen en vervormen naar schermgrootte [boven aangegeven](regel 14-15)
background_image = pygame.image.load(background_image)
background_image = pygame.transform.scale(background_image, (screen_height,screen_width))

#Logo aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 22-23)
logo_image = pygame.image.load(logo_image)
logo_image = pygame.transform.scale(logo_image, (logo_width, logo_height))

#Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
play_button = pygame.image.load(play_button)
play_button = pygame.transform.scale(play_button, (button_width, button_height))

#Stop knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
stop_button = pygame.image.load(stop_button)
stop_button = pygame.transform.scale(stop_button, (button_width, button_height))

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
            if mouseX >= 200 and mouseY >= 300 and mouseX <= 800 and mouseY <= 400:
                #print dat de play knop is vonden (muisdetectie) [controle]
                print("je hebt de play knop gevonden")
                #Haal informatie op van Python file
                from Game_Reuben import main

            #als muis zich bevindt tussen x & y as
            if mouseX >= 200 and mouseY >= 450 and mouseX <= 950 and mouseY <= 550:
                #print dat de stop knop is vonden (muisdetectie) [controle]
                print("je hebt de stop knop gevonden")
                #detect sluit knop
                pygame.quit()
                #sluit de pygame
                exit()

        #als escape wordt ingedrukt
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            #detect sluit knop
            pygame.quit()
            #sluit de pygame
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #Haal informatie op van Python file
            from Game_Reuben import *

    #toon in venster (image, (x, y))
    screen.blit(background_image, (0, 0))
    screen.blit(logo_image, (100, 50))
    screen.blit(play_button, (200, 300))
    screen.blit(stop_button, (200, 450))

    #vernieuw de venster op verandering
    pygame.display.update()
