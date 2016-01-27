import pygame
from pygame.locals import *
from sys import exit

#afbeeldingen inladen
background_image    = 'Main/Menu/bg.jpg'
play_button         = 'Button/SM/play.png'
stop_button         = 'Button/SM/quit.png'

screen_width        = 768
screen_height       = 1024

button_width        = 600
button_height       = 100

#Venstergrootte aangeven
screen = pygame.display.set_mode((screen_height,screen_width), DOUBLEBUF, 32)

background_image = pygame.image.load(background_image)
background_image = pygame.transform.scale(background_image, (screen_height,screen_width))

play_button = pygame.image.load(play_button)
play_button = pygame.transform.scale(play_button, (button_width, button_height))

stop_button = pygame.image.load(stop_button)
stop_button = pygame.transform.scale(stop_button, (button_width, button_height))

while True:
    #ophalen van pygame event
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
            if mouseX >= 200 and mouseY >= 300 and mouseX <= 800 and mouseY <= 400:
                print("je hebt de play knop gevonden")
            if mouseX >= 200 and mouseY >= 450 and mouseX <= 950 and mouseY <= 550:
                print("je hebt de stop knop gevonden")



    screen.blit(background_image, (0, 0))
    screen.blit(play_button, (200, 300))
    screen.blit(stop_button, (200, 450))

    pygame.display.update()
