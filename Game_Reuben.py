from random import *
from sys import exit

import pygame
from pygame.locals import *


class Scherm:
    def __init__(self, width, height):
        self.Width  =   width
        self.Height =   height

class Achtergrond:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Bord:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Pionnen:
    def __init__(self, kleur, image, width, height, pos_x, pos_y):
        self.Kleur  =   kleur
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Spelers:
    def __init__(self, naam, image, width, height, pos_x, pos_y):
        self.Naam  =    naam
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Dobbelstenen:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class SuperFighters:
    def __init__(self, nummer, image, width, height, pos_x, pos_y):
        self.Nummer  =  nummer
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Scorekaarten:
    def __init__(self, nummer, image, width, height, pos_x, pos_y):
        self.Nummer  =  nummer
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Levenspunten:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Conditiepunten:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Fightvakken:
    def __init__(self, nummer, pos_x, pos_y):
        self.Nummer  =  nummer
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class LiggendLoopvakken:
    def __init__(self, nummer, pos_x, pos_y):
        self.Nummer  =  nummer
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class StaandLoopvakken:
    def __init__(self, nummer, pos_x, pos_y):
        self.Nummer  =  nummer
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Knoppen:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class afbeeldingen:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Snelkoppelingen:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

screen_width        = 768
screen_height       = 1024

button_width        = 200
button_height       = 50

dobbel_x            = 810
dobbel_y            = 300

dobbelstn_width     = 200
dobbelstn_height    = 200
dobbelstn_x         = 810
dobbelstn_y         = 100

opt1_x            = 810
opt1_y            = 600

opt2_x            = 810
opt2_y            = 650

opt3_x            = 810
opt3_y            = 700

instr_x             = 10
instr_y             = 10

stop_x              = 810
stop_y              = 10

logo_width          = 600
logo_height         = 200
logo_y              = 0
logo_x              = 200

bord_width          = 500
bord_height         = 500
bord_y              = 200
bord_x              = 250


scherm      = Scherm        (screen_width, screen_height)
achtergrond = Achtergrond   ('Main/Game/wood.jpg',          scherm.Height,  scherm.Width,       0,              0           )

spellogo    = afbeeldingen  ('Button/SM/logo.png',          logo_width,     logo_height,        logo_x,         logo_y      )
spelbord    = Knoppen       ('Main/Game/board2.png',        bord_width,     bord_height,        bord_x,         bord_y      )

dobbelen    = Knoppen       ('Button/GM/dobbel.png',        button_width,   button_height,      dobbel_x,       dobbel_y    )


optie1      = Knoppen       ('Button/GM/optie1.png',        button_width,   button_height,      opt1_x,       opt1_y    )
optie2      = Knoppen       ('Button/GM/optie2.png',        button_width,   button_height,      opt2_x,       opt2_y    )
optie3      = Knoppen       ('Button/GM/optie3.png',        button_width,   button_height,      opt3_x,       opt3_y    )

instructie  = Knoppen       ('Button/SM/instructions.png',  button_width,   button_height,      instr_x,        instr_y     )
stopknop    = Knoppen       ('Button/SM/quitgame.png',      button_width,   button_height,      stop_x,         stop_y      )


screen = pygame.display.set_mode                    ((scherm.Height, scherm.Width))

background = pygame.image.load                      (achtergrond.Image)
background = pygame.transform.scale(background,     (scherm.Height, scherm.Width))

Game_logo = pygame.image.load                       (spellogo.Image)
Game_logo = pygame.transform.scale(Game_logo,       (spellogo.Width, spellogo.Height))

Game_board = pygame.image.load                       (spelbord.Image)
Game_board = pygame.transform.scale(Game_board,       (spelbord.Width, spelbord.Height))

Roll_dice = pygame.image.load                       (dobbelen.Image)
Roll_dice = pygame.transform.scale(Roll_dice,       (dobbelen.Width, dobbelen.Height))

dobbelsteen = Dobbelstenen  ('Main/Dice/D0.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
Dice_image = pygame.image.load(dobbelsteen.Image)
Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

Option1 = pygame.image.load                       (optie1.Image)
Option1 = pygame.transform.scale(Option1,       (optie1.Width, optie1.Height))

Option2 = pygame.image.load                       (optie2.Image)
Option2 = pygame.transform.scale(Option2,       (optie2.Width, optie2.Height))

Option3 = pygame.image.load                       (optie3.Image)
Option3 = pygame.transform.scale(Option3,       (optie3.Width, optie3.Height))

instr_button = pygame.image.load                    (instructie.Image)
instr_button = pygame.transform.scale(instr_button, (instructie.Width, instructie.Height))

stop_button = pygame.image.load                     (stopknop.Image)
stop_button = pygame.transform.scale(stop_button,   (stopknop.Width, stopknop.Height))

pygame.init()

dice_num = 0
dobbelsteen = Dobbelstenen  ('Main/Dice/D0.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
Dice_image = pygame.image.load(dobbelsteen.Image)
Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            print ("X =",mouseX, "Y =",mouseY)

            if mouseX >= dobbel_x \
                    and mouseY >= dobbel_y \
                    and mouseX <= dobbel_x+button_width \
                    and mouseY <= dobbel_y+button_height:
                print("je hebt de Roll Dice knop gedrukt")
                dice_num = randint(1,6)
                if dice_num == 1:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D1.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

                if dice_num == 2:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D2.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

                if dice_num == 3:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D3.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

                if dice_num == 4:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D4.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

                if dice_num == 5:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D5.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

                if dice_num == 6:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D6.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))


            if mouseX >= opt1_x \
                    and mouseY >= opt1_y \
                    and mouseX <= opt1_x+button_width \
                    and mouseY <= opt1_y+button_height:
                print("je hebt de 1ste optie knop gedrukt")

            if mouseX >= opt2_x \
                    and mouseY >= opt2_y \
                    and mouseX <= opt2_x+button_width \
                    and mouseY <= opt2_y+button_height:
                print("je hebt de 2de optie knop gedrukt")

            if mouseX >= opt3_x \
                    and mouseY >= opt3_y \
                    and mouseX <= opt3_x+button_width \
                    and mouseY <= opt3_y+button_height:
                print("je hebt de 3de optie knop gedrukt")


            if mouseX >= instr_x \
                    and mouseY >= instr_y \
                    and mouseX <= instr_x+button_width \
                    and mouseY <= instr_y+button_height:
                print("je hebt de Instruction knop gedrukt")
                import GameStartMenu_Reuben

            if mouseX >= stop_x \
                    and mouseY >= stop_y \
                    and mouseX <= stop_x+button_width \
                    and mouseY <= stop_y+button_height:
                print("je hebt de Quit knop gedrukt")
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
    screen.blit(Game_board,      (int(spelbord.Pos_x),       int(spelbord.Pos_y)))

    screen.blit(Roll_dice,    (int(dobbelen.Pos_x),      int(dobbelen.Pos_y)))
    screen.blit(Dice_image,    (int(dobbelsteen.Pos_x),      int(dobbelsteen.Pos_y)))

    screen.blit(Option1,    (int(optie1.Pos_x),      int(optie1.Pos_y)))
    screen.blit(Option2,    (int(optie2.Pos_x),      int(optie2.Pos_y)))
    screen.blit(Option3,    (int(optie3.Pos_x),      int(optie3.Pos_y)))

    screen.blit(instr_button,   (int(instructie.Pos_x),     int(instructie.Pos_y)))
    screen.blit(stop_button,    (int(stopknop.Pos_x),       int(stopknop.Pos_y)))

    pygame.display.update()