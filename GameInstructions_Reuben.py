import pygame
from pygame.locals import *
from sys import exit


class Achtergrond:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Scherm:
    def __init__(self, width, height):
        self.Width  =   width
        self.Height =   height

class Knoppen:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y


screen_width        = 768
screen_height       = 1024

element_x            = 0
element_y            = 0

vorige_x            = 200
vorige_y            = 650

startmenu_x         = 400
startmenu_y         = 650

volgende_x          = 600
volgende_y          = 650

button_width        = 200
button_height       = 50

scherm      = Scherm                                (screen_width, screen_height)
screen = pygame.display.set_mode                    ((scherm.Height, scherm.Width))

elementen   = Knoppen       ('Main/Instructions/elements.jpg',          scherm.Height,  scherm.Width,       element_x,      element_y     )
vorige      = Knoppen       ('Button/IM/previous.png',                  button_width,   button_height,      vorige_x,       vorige_y     )
startmenu   = Knoppen       ('Button/IM/mainmenu.png',                  button_width,   button_height,      startmenu_x,    startmenu_y  )
volgende    = Knoppen       ('Button/IM/next.png',                      button_width,   button_height,      volgende_x,     volgende_y   )



background = pygame.image.load                              (elementen.Image)
background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))

previous_button = pygame.image.load                         (vorige.Image)
previous_button = pygame.transform.scale(previous_button,   (vorige.Width, vorige.Height))

gamemenu = pygame.image.load                                (startmenu.Image)
gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))

second_button = pygame.image.load                           (volgende.Image)
second_button = pygame.transform.scale(second_button,       (volgende.Width, volgende.Height))



player_choice = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            print ("X =",mouseX, "Y =",mouseY)

            if mouseX >= vorige_x \
                    and mouseY >= vorige_y \
                    and mouseX <= vorige_x+button_width \
                    and mouseY <= vorige_y+button_height:
                print("je hebt de Previous knop gevonden")
                player_choice = player_choice - 1
                print(player_choice)
                if player_choice == 1:
                    elementen   = Knoppen       ('Main/Instructions/elements.jpg',  scherm.Height,  scherm.Width,   element_x,      element_y     )
                    background = pygame.image.load                              (elementen.Image)
                    background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))

                elif player_choice == 2:
                    elementen   = Knoppen       ('Main/Instructions/controls.jpg',         scherm.Height,       scherm.Width,   element_x,      element_y     )
                    background = pygame.image.load                              (elementen.Image)
                    background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))

            if mouseX >= startmenu_x \
                    and mouseY >= startmenu_y \
                    and mouseX <= startmenu_x+button_width \
                    and mouseY <= startmenu_y+button_height:
                print("je hebt de Startmenu knop gevonden")
                import GameStartMenu_Reuben


            if mouseX >= volgende_x \
                    and mouseY >= volgende_y \
                    and mouseX <= volgende_x+button_width \
                    and mouseY <= volgende_y+button_height:
                print("je hebt de Next knop gevonden")
                player_choice = player_choice + 1
                print(player_choice)
                if player_choice == 1:
                    elementen   = Knoppen       ('Main/Instructions/elements.jpg',         scherm.Height,       scherm.Width,   element_x,      element_y     )
                    background = pygame.image.load                              (elementen.Image)
                    background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))


                elif player_choice == 2:
                    elementen   = Knoppen       ('Main/Instructions/controls.jpg',         scherm.Height,       scherm.Width,   element_x,      element_y     )
                    background = pygame.image.load                              (elementen.Image)
                    background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))


        if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_ESCAPE:
            print("je hebt het spel afgesloten")
            pygame.QUIT
            quit()


        if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_1:
            print("je hebt op 1 gedrukt")

        if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_2:
            print("je hebt op 2 gedrukt")

        if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_3:
            print("je hebt op 3 gedrukt")

    screen.blit(background,         (int(elementen.Pos_x),      int(elementen.Pos_y)))
    screen.blit(previous_button,    (int(vorige.Pos_x),         int(vorige.Pos_y)))
    screen.blit(gamemenu,           (int(startmenu.Pos_x),      int(startmenu.Pos_y)))
    screen.blit(second_button,      (int(volgende.Pos_x),       int(volgende.Pos_y)))

    pygame.display.update()