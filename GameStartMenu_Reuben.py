import pygame
from pygame.locals import *

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

class Startmenu:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Knoppen:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y



screen_width        = 768
screen_height       = 1024

button_width        = 400
button_height       = 100

start_x             = 50
start_y             = 350

instr_x             = 50
instr_y             = 450

regels_x            = 50
regels_y            = 550

stop_x              = 50
stop_y              = 650

logo_width          = 600
logo_height         = 200
logo_y              = 0
logo_x              = 250

menu_width          = 400
menu_height         = 150
menu_y              = 200
menu_x              = 50


scherm      = Scherm        (screen_width, screen_height)
achtergrond = Achtergrond   ('Main/Menu/bg2.jpg',           scherm.Height,  scherm.Width,   0,          0)

spellogo    = Knoppen       ('Button/SM/logo.png',          logo_width,     logo_height,    logo_x,     logo_y   )
spelmenu    = Knoppen       ('Button/SM/menu.png',          menu_width,     menu_height,    menu_x,     menu_y   )

startknop   = Knoppen       ('Button/SM/newgame.png',       button_width,   button_height,  start_x,    start_y  )
instructie  = Knoppen       ('Button/SM/instructions.png',  button_width,   button_height,  instr_x,    instr_y  )
regels      = Knoppen       ('Button/SM/gamerules.png',     button_width,   button_height,  regels_x,   regels_y  )
stopknop    = Knoppen       ('Button/SM/quitgame.png',      button_width,   button_height,  stop_x,     stop_y   )


screen = pygame.display.set_mode                    ((scherm.Height, scherm.Width))

background = pygame.image.load                      (achtergrond.Image)
background = pygame.transform.scale(background,     (scherm.Height, scherm.Width))

Game_logo = pygame.image.load                       (spellogo.Image)
Game_logo = pygame.transform.scale(Game_logo,       (spellogo.Width, spellogo.Height))

Game_menu = pygame.image.load                       (spelmenu.Image)
Game_menu = pygame.transform.scale(Game_menu,       (spelmenu.Width, spelmenu.Height))

play_button = pygame.image.load                     (startknop.Image)
play_button = pygame.transform.scale(play_button,   (startknop.Width, startknop.Height))

instr_button = pygame.image.load                    (instructie.Image)
instr_button = pygame.transform.scale(instr_button, (instructie.Width, instructie.Height))

rules_button = pygame.image.load                    (regels.Image)
rules_button = pygame.transform.scale(rules_button, (regels.Width, regels.Height))

stop_button = pygame.image.load                     (stopknop.Image)
stop_button = pygame.transform.scale(stop_button,   (stopknop.Width, stopknop.Height))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            print ("X =",mouseX, "Y =",mouseY)

            if mouseX >= start_x \
                    and mouseY >= start_y \
                    and mouseX <= start_x+button_width \
                    and mouseY <= start_y+button_height:
                print("je hebt de New Game knop gevonden")
                import Game_joey

            if mouseX >= instr_x \
                    and mouseY >= instr_y \
                    and mouseX <= instr_x+button_width \
                    and mouseY <= instr_y+button_height:
                print("je hebt de Instructions knop gevonden")
                import GameInstructions_Reuben

            if mouseX >= regels_x \
                    and mouseY >= regels_y \
                    and mouseX <= regels_x+button_width \
                    and mouseY <= regels_y+button_height:
                print("je hebt de Game Rules knop gevonden")
                import GameRules_Reuben

            if mouseX >= stop_x \
                    and mouseY >= stop_y \
                    and mouseX <= stop_x+button_width \
                    and mouseY <= stop_y+button_height:
                print("je hebt de Quit knop gevonden")
                pygame.quit()
                exit()

        if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_ESCAPE:
            print("je hebt het spel afgesloten")
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_1:
            print("je hebt op 1 gedrukt")

        if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_2:
            print("je hebt op 2 gedrukt")

        if event.type == pygame.KEYDOWN \
                and event.key == pygame.K_3:
            print("je hebt op 3 gedrukt")

    screen.blit(background,     (int(achtergrond.Pos_x),    int(achtergrond.Pos_y)))
    screen.blit(Game_logo,      (int(spellogo.Pos_x),       int(spellogo.Pos_y)))
    screen.blit(Game_menu,      (int(spelmenu.Pos_x),       int(spelmenu.Pos_y)))
    screen.blit(play_button,    (int(startknop.Pos_x),      int(startknop.Pos_y)))
    screen.blit(instr_button,   (int(instructie.Pos_x),     int(instructie.Pos_y)))
    screen.blit(rules_button,   (int(regels.Pos_x),         int(regels.Pos_y)))
    screen.blit(stop_button,    (int(stopknop.Pos_x),       int(stopknop.Pos_y)))

    pygame.display.update()