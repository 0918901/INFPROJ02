from random import *
from sys import exit

import pygame
import sys
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

class Stappen:
    def __init__(self, vak_nr, buiten_pos_x, buiten_pos_y, binnen_pos_x, binnen_pos_y):
        self.Vak_nr =   vak_nr
        self.Bupos_x  =   buiten_pos_x
        self.Bupos_y  =   buiten_pos_y
        self.Bipos_x  =   binnen_pos_x
        self.Bipos_y  =   binnen_pos_y

class Pionnen:
    def __init__(self, image, width, height, pos_x, pos_y):
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

class Statusvak:
    def __init__(self, image, width, height, pos_x, pos_y):
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
instr_y             = 0

regel_x             = 10
regel_y             = instr_y + button_height

menu_x             = 10
menu_y             = regel_y + button_height

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

vlak_width          = 220
vlak_height         = 100
vlak_x              = 15

vlak_rood           = 200
vlak_groen          = vlak_rood + 125
vlak_geel           = vlak_rood + 250
vlak_blauw          = vlak_rood + 375

lp_width            = 50
lp_height           = 50

p1_lp_x             = vlak_x
p1_lp_y             = 200

p2_lp_x             = vlak_x
p2_lp_y             = vlak_rood + 125

p3_lp_x             = vlak_x
p3_lp_y             = vlak_rood + 250

p4_lp_x             = vlak_x
p4_lp_y             = vlak_rood + 375

cp_width            = 50
cp_height           = 50

p1_cp_x                = vlak_x
p1_cp_y                = 250

p2_cp_x                = vlak_x
p2_cp_y                = vlak_rood + 175

p3_cp_x                = vlak_x
p3_cp_y                = vlak_rood + 300

p4_cp_x                = vlak_x
p4_cp_y                = vlak_rood + 424

pion_width          = 25
pion_height         = 25

pion_rood_x         = bord_x + 435
pion_rood_y         = bord_y + 5

pion_groen_x        = bord_x + 495 - pion_width
pion_groen_y        = bord_y + 495 - pion_height

pion_geel_x         = bord_x + 5
pion_geel_y         = bord_y + 495 - pion_height

pion_blauw_x        = bord_x + 5
pion_blauw_y        = bord_y + 5

bx = bord_x
by = bord_y

vakjes = [[bx+470,by+5],    [bx+470,by+67.5],   [bx+470,by+105],    [bx+470,by+145],    [bx+470,by+180],
          [bx+470,by+240],  [bx+470,by+295],    [bx+470,by+330],    [bx+470,by+367.5],  [bx+470,by+405],
          [bx+470,by+470],  [bx+405,by+470],    [bx+367.5,by+470],  [bx+330,by+470],    [bx+295,by+470],
          [bx+240,by+470],  [bx+180,by+470],    [bx+145,by+470],    [bx+105,by+470],    [bx+67.5,by+470],
          [bx+5,by+470],    [bx+5,by+405],      [bx+5,by+367.5],    [bx+5,by+330],      [bx+5,by+295],
          [bx+5,by+240],    [bx+5,by+180],      [bx+5,by+145],      [bx+5,by+105],      [bx+5,by+67.5],
          [bx+5,by+5],      [bx+67.5,by+5],     [bx+105,by+5],      [bx+145,by+5],      [bx+180,by+5],
          [bx+240,by+5],    [bx+295,by+5],      [bx+330,by+5],      [bx+367.5,by+5],    [bx+405.5,by+5]]

vakjes2= [[bx+470,by+5],    [bx+470,by+67.5],   [bx+470,by+105],    [bx+470,by+145],    [bx+470,by+180],
          [bx+470,by+240],  [bx+470,by+295],    [bx+470,by+330],    [bx+470,by+367.5],  [bx+470,by+405],
          [bx+470,by+470],  [bx+405,by+470],    [bx+367.5,by+470],  [bx+330,by+470],    [bx+295,by+470],
          [bx+240,by+470],  [bx+180,by+470],    [bx+145,by+470],    [bx+105,by+470],    [bx+67.5,by+470],
          [bx+5,by+470],    [bx+5,by+405],      [bx+5,by+367.5],    [bx+5,by+330],      [bx+5,by+295],
          [bx+5,by+240],    [bx+5,by+180],      [bx+5,by+145],      [bx+5,by+105],      [bx+5,by+67.5],
          [bx+5,by+5],      [bx+67.5,by+5],     [bx+105,by+5],      [bx+145,by+5],      [bx+180,by+5],
          [bx+240,by+5],    [bx+295,by+5],      [bx+330,by+5],      [bx+367.5,by+5],    [bx+405.5,by+5]]


scherm      = Scherm        (screen_width, screen_height)
achtergrond = Achtergrond   ('Main/Game/wood.jpg',          scherm.Height,  scherm.Width,       0,            0           )

spellogo    = afbeeldingen  ('Button/SM/logo.png',          logo_width,     logo_height,        logo_x,       logo_y      )
spelbord    = Knoppen       ('Main/Game/board2.png',        bord_width,     bord_height,        bord_x,       bord_y      )

dobbelen    = Knoppen       ('Button/GM/dobbel.png',        button_width,   button_height,      dobbel_x,     dobbel_y    )

pion_rood   = Pionnen       ('Player/Piece/Rood.png',       pion_width,     pion_height,      pion_rood_x,    pion_rood_y    )
pion_groen  = Pionnen       ('Player/Piece/Groen.png',       pion_width,     pion_height,      pion_groen_x,   pion_groen_y    )
pion_geel   = Pionnen       ('Player/Piece/Geel.png',       pion_width,     pion_height,      pion_geel_x,    pion_geel_y    )
pion_blauw  = Pionnen       ('Player/Piece/Blauw.png',       pion_width,     pion_height,      pion_blauw_x,   pion_blauw_y    )

optie1      = Knoppen       ('Button/GM/optie1.png',        button_width,   button_height,      opt1_x,       opt1_y    )
optie2      = Knoppen       ('Button/GM/optie2.png',        button_width,   button_height,      opt2_x,       opt2_y    )
optie3      = Knoppen       ('Button/GM/optie3.png',        button_width,   button_height,      opt3_x,       opt3_y    )

instructie  = Knoppen       ('Button/SM/instructions.png',  button_width,   button_height,      instr_x,      instr_y     )
spelregels  = Knoppen       ('Button/SM/gamerules.png',     button_width,   button_height,      regel_x,      regel_y     )
spelmenu    = Knoppen       ('Button/SM/mainmenu.png',      button_width,   button_height,      menu_x,       menu_y     )
stopknop    = Knoppen       ('Button/SM/quitgame.png',      button_width,   button_height,      stop_x,       stop_y      )

status_rood = Statusvak     ('Main/Elements/red.png',      vlak_width,   vlak_height,      vlak_x,       vlak_rood      )
status_groen= Statusvak     ('Main/Elements/green.png',    vlak_width,   vlak_height,      vlak_x,       vlak_groen      )
status_geel = Statusvak     ('Main/Elements/yellow.png',   vlak_width,   vlak_height,      vlak_x,       vlak_geel      )
status_blauw= Statusvak     ('Main/Elements/blue.png',     vlak_width,   vlak_height,      vlak_x,       vlak_blauw      )

p1_lp       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p1_lp_x,       p1_lp_y      )
p1_cp       = Conditiepunten('Main/Elements/cp.png',     cp_width,   cp_height,      p1_cp_x,       p1_cp_y      )

p2_lp       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p2_lp_x,       p2_lp_y      )
p2_cp       = Conditiepunten('Main/Elements/cp.png',     cp_width,   cp_height,      p2_cp_x,       p2_cp_y      )

p3_lp       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p3_lp_x,       p3_lp_y      )
p3_cp       = Conditiepunten('Main/Elements/cp.png',     cp_width,   cp_height,      p3_cp_x,       p3_cp_y      )

p4_lp       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p4_lp_x,       p4_lp_y      )
p4_cp       = Conditiepunten('Main/Elements/cp.png',     cp_width,   cp_height,      p4_cp_x,       p4_cp_y      )



screen = pygame.display.set_mode                    ((scherm.Height, scherm.Width))

background = pygame.image.load                      (achtergrond.Image)
background = pygame.transform.scale(background,     (scherm.Height, scherm.Width))

Game_logo = pygame.image.load                       (spellogo.Image)
Game_logo = pygame.transform.scale(Game_logo,       (spellogo.Width, spellogo.Height))

Game_board = pygame.image.load                       (spelbord.Image)
Game_board = pygame.transform.scale(Game_board,       (spelbord.Width, spelbord.Height))

Roll_dice = pygame.image.load                       (dobbelen.Image)
Roll_dice = pygame.transform.scale(Roll_dice,       (dobbelen.Width, dobbelen.Height))

Red_piece = pygame.image.load                       (pion_rood.Image)
Red_piece = pygame.transform.scale(Red_piece,       (pion_rood.Width, pion_rood.Height))

Green_piece = pygame.image.load                       (pion_groen.Image)
Green_piece = pygame.transform.scale(Green_piece,       (pion_groen.Width, pion_groen.Height))

Yellow_piece = pygame.image.load                       (pion_geel.Image)
Yellow_piece = pygame.transform.scale(Yellow_piece,       (pion_geel.Width, pion_geel.Height))

Blue_piece = pygame.image.load                       (pion_blauw.Image)
Blue_piece = pygame.transform.scale(Blue_piece,       (pion_blauw.Width, pion_blauw.Height))

Option1 = pygame.image.load                       (optie1.Image)
Option1 = pygame.transform.scale(Option1,       (optie1.Width, optie1.Height))

Option2 = pygame.image.load                       (optie2.Image)
Option2 = pygame.transform.scale(Option2,       (optie2.Width, optie2.Height))

Option3 = pygame.image.load                       (optie3.Image)
Option3 = pygame.transform.scale(Option3,       (optie3.Width, optie3.Height))

Status_red      = pygame.image.load                    (status_rood.Image)
Status_red      = pygame.transform.scale(Status_red, (status_rood.Width, status_rood.Height))

Status_green    = pygame.image.load                    (status_groen.Image)
Status_green    = pygame.transform.scale(Status_green, (status_groen.Width, status_groen.Height))

Status_yellow   = pygame.image.load                    (status_geel.Image)
Status_yellow   = pygame.transform.scale(Status_yellow, (status_geel.Width, status_geel.Height))

Status_blue     = pygame.image.load                    (status_blauw.Image)
Status_blue     = pygame.transform.scale(Status_blue, (status_blauw.Width, status_blauw.Height))

P1_LP    = pygame.image.load                    (p1_lp.Image)
P1_LP     = pygame.transform.scale(P1_LP, (p1_lp.Width, p1_lp.Height))

P2_LP    = pygame.image.load                    (p2_lp.Image)
P2_LP     = pygame.transform.scale(P2_LP, (p2_lp.Width, p2_lp.Height))

P3_LP    = pygame.image.load                    (p3_lp.Image)
P3_LP     = pygame.transform.scale(P3_LP, (p3_lp.Width, p3_lp.Height))

P4_LP    = pygame.image.load                    (p4_lp.Image)
P4_LP     = pygame.transform.scale(P4_LP, (p4_lp.Width, p4_lp.Height))

P1_CP    = pygame.image.load                    (p1_cp.Image)
P1_CP     = pygame.transform.scale(P1_CP, (p1_cp.Width, p1_cp.Height))

P2_CP    = pygame.image.load                    (p2_cp.Image)
P2_CP     = pygame.transform.scale(P2_CP, (p2_cp.Width, p2_cp.Height))

P3_CP    = pygame.image.load                    (p3_cp.Image)
P3_CP     = pygame.transform.scale(P3_CP, (p3_cp.Width, p3_cp.Height))

P4_CP    = pygame.image.load                    (p4_cp.Image)
P4_CP     = pygame.transform.scale(P4_CP, (p4_cp.Width, p4_cp.Height))

instr_button = pygame.image.load                    (instructie.Image)
instr_button = pygame.transform.scale(instr_button, (instructie.Width, instructie.Height))

Rules_button = pygame.image.load                    (spelregels.Image)
Rules_button = pygame.transform.scale(Rules_button, (spelregels.Width, spelregels.Height))

Menu_button = pygame.image.load                    (spelmenu.Image)
Menu_button = pygame.transform.scale(Menu_button, (spelmenu.Width, spelmenu.Height))

stop_button = pygame.image.load                     (stopknop.Image)
stop_button = pygame.transform.scale(stop_button,   (stopknop.Width, stopknop.Height))

pygame.init()

dice_num = 0
dobbelsteen = Dobbelstenen  ('Main/Dice/D0.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y)
Dice_image = pygame.image.load(dobbelsteen.Image)
Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

p1_vak = 0
p2_vak = 10
p3_vak = 20
p4_vak = 30

while True:
    if p1_vak >= 1:
        vakjes.extend(vakjes2)
    if p2_vak >= 11:
        vakjes.extend(vakjes2)
    if p3_vak >= 21:
        vakjes.extend(vakjes2)
    if p4_vak >= 31:
        vakjes.extend(vakjes2)

    pion_rood.Pos_x = vakjes[p1_vak] [0]
    pion_rood.Pos_y = vakjes[p1_vak] [1]

    pion_groen.Pos_x = vakjes[p2_vak] [0]
    pion_groen.Pos_y = vakjes[p2_vak] [1]

    pion_geel.Pos_x = vakjes[p3_vak] [0]
    pion_geel.Pos_y = vakjes[p3_vak] [1]

    pion_blauw.Pos_x = vakjes[p4_vak] [0]
    pion_blauw.Pos_y = vakjes[p4_vak] [1]

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

                dice_num = randint(1, 6)
                p1_vak = p1_vak + dice_num
                p2_vak = p2_vak + dice_num
                p3_vak = p3_vak + dice_num
                p4_vak = p4_vak + dice_num

                if dice_num == 1:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D1.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                    print ("je hebt 1 gegooid")

                if dice_num == 2:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D2.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                    print ("je hebt 2 gegooid")

                if dice_num == 3:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D3.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                    print ("je hebt 3 gegooid")

                if dice_num == 4:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D4.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                    print ("je hebt 4 gegooid")

                if dice_num == 5:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D5.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                    print ("je hebt 5 gegooid")

                if dice_num == 6:
                    dobbelsteen = Dobbelstenen  ('Main/Dice/D6.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                    Dice_image = pygame.image.load(dobbelsteen.Image)
                    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                    print ("je hebt 6 gegooid")


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
                import GameInstructions_Reuben

            if mouseX >= regel_x \
                    and mouseY >= regel_y \
                    and mouseX <= regel_x+button_width \
                    and mouseY <= regel_y+button_height:
                print("je hebt de Game Rules knop gedrukt")
                import GameRules_Reuben

            if mouseX >= menu_x \
                    and mouseY >= menu_y \
                    and mouseX <= menu_x+button_width \
                    and mouseY <= menu_y+button_height:
                print("je hebt de Menu knop gedrukt")
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

    screen.blit(Red_piece,    (int(pion_rood.Pos_x),      int(pion_rood.Pos_y)))
    screen.blit(Green_piece,    (int(pion_groen.Pos_x),      int(pion_groen.Pos_y)))
    screen.blit(Yellow_piece,    (int(pion_geel.Pos_x),      int(pion_geel.Pos_y)))
    screen.blit(Blue_piece,    (int(pion_blauw.Pos_x),      int(pion_blauw.Pos_y)))

    screen.blit(Status_red,    (int(status_rood.Pos_x),      int(status_rood.Pos_y)))
    screen.blit(Status_green,    (int(status_groen.Pos_x),      int(status_groen.Pos_y)))
    screen.blit(Status_yellow,    (int(status_geel.Pos_x),      int(status_geel.Pos_y)))
    screen.blit(Status_blue,    (int(status_blauw.Pos_x),      int(status_blauw.Pos_y)))

    screen.blit(P1_LP,    (int(p1_lp.Pos_x),      int(p1_lp.Pos_y)))
    screen.blit(P2_LP,    (int(p2_lp.Pos_x),      int(p2_lp.Pos_y)))
    screen.blit(P3_LP,    (int(p3_lp.Pos_x),      int(p3_lp.Pos_y)))
    screen.blit(P4_LP,    (int(p4_lp.Pos_x),      int(p4_lp.Pos_y)))

    screen.blit(P1_CP,    (int(p1_cp.Pos_x),      int(p1_cp.Pos_y)))
    screen.blit(P2_CP,    (int(p2_cp.Pos_x),      int(p2_cp.Pos_y)))
    screen.blit(P3_CP,    (int(p3_cp.Pos_x),      int(p3_cp.Pos_y)))
    screen.blit(P4_CP,    (int(p4_cp.Pos_x),      int(p4_cp.Pos_y)))

    screen.blit(instr_button,   (int(instructie.Pos_x),     int(instructie.Pos_y)))
    screen.blit(Rules_button,   (int(spelregels.Pos_x),     int(spelregels.Pos_y)))
    screen.blit(Menu_button,   (int(spelmenu.Pos_x),     int(spelmenu.Pos_y)))
    screen.blit(stop_button,    (int(stopknop.Pos_x),       int(stopknop.Pos_y)))

    pygame.display.update()