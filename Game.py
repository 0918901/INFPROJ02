import os
import random
from sys import exit
import pygame
import sys
import copy
from pygame.locals import *


def Intro():
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

    speler1_x           = 450
    speler1_y           = 350
    speler2_x           = 450
    speler2_y           = 450

    logo_width          = 600
    logo_height         = 200
    logo_y              = 0
    logo_x              = 250

    menu_width          = 400
    menu_height         = 150
    menu_y              = 200
    menu_x              = 50

    logo2_width          = 600
    logo2_height         = 200
    logo2_y              = 0
    logo2_x              = 250

    menu2_width          = 400
    menu2_height         = 150
    menu2_y              = 200
    menu2_x              = 50


    scherm      = Scherm        (screen_width, screen_height)
    achtergrond = Achtergrond   ('Main/Menu/bg2.jpg',           scherm.Height,  scherm.Width,   0,          0)

    spellogo    = Knoppen       ('Button/SM/logo.png',          logo_width,     logo_height,    logo_x,     logo_y   )
    spellogo2    = Knoppen       ('Button/SM/logo2.png',          logo2_width,     logo2_height,    logo2_x,     logo2_y   )
    spelmenu    = Knoppen       ('Button/SM/menu.png',          menu_width,     menu_height,    menu_x,     menu_y   )
    spelmenu2    = Knoppen       ('Button/SM/menu2.png',          menu2_width,     menu2_height,    menu2_x,     menu2_y   )

    Game_logo2 = pygame.image.load                       (spellogo2.Image)
    Game_logo2 = pygame.transform.scale(Game_logo2,       (spellogo2.Width, spellogo2.Height))

    Game_menu2 = pygame.image.load                       (spelmenu2.Image)
    Game_menu2 = pygame.transform.scale(Game_menu2,       (spelmenu2.Width, spelmenu2.Height))


    startknop   = Knoppen       ('Button/SM/playgame.png',       button_width,   button_height,  start_x,    start_y  )
    instructie  = Knoppen       ('Button/SM/instructions.png',  button_width,   button_height,  instr_x,    instr_y  )
    regels      = Knoppen       ('Button/SM/gamerules.png',     button_width,   button_height,  regels_x,   regels_y  )
    stopknop    = Knoppen       ('Button/SM/quitgame.png',      button_width,   button_height,  stop_x,     stop_y   )

    stopknop    = Knoppen       ('Button/SM/quitgame.png',      button_width,   button_height,  stop_x,     stop_y   )
    stopknop    = Knoppen       ('Button/SM/quitgame.png',      button_width,   button_height,  stop_x,     stop_y   )

    screen = pygame.display.set_mode                    ((scherm.Height, scherm.Width),HWSURFACE|DOUBLEBUF,32)

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

    clock = pygame.time.Clock()
    LogoMenuCurrentImage = 1

    pygame.init()


    music = 1
    pygame.mixer.music.load('Sound/game2.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    if music == 1:
        pygame.mixer.music.play()

    players = 0
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
                    players = players + 1

                    if players == 1:
                        speler1    = Knoppen       ('Button/SM/pvp.png',      button_width,   button_height,  speler1_x,     speler1_y   )
                        Speler1 = pygame.image.load                         (speler1.Image)
                        Speler1 = pygame.transform.scale(Speler1,            (speler1.Width, speler1.Height))
                    if players == 2:
                        speler2    = Knoppen       ('Button/SM/pvsc.png',      button_width,   button_height,  speler2_x,     speler2_y   )
                        Speler2 = pygame.image.load                         (speler2.Image)
                        Speler2 = pygame.transform.scale(Speler2,            (speler2.Width, speler2.Height))

                if mouseX >= speler1_x \
                        and mouseY >= speler1_y \
                        and mouseX <= speler1_x+button_width \
                        and mouseY <= speler1_y+button_height:
                    print("je hebt de speler1 knop gevonden")
                    pygame.mixer.music.stop()
                    Game()

                if mouseX >= speler2_x \
                        and mouseY >= speler2_y \
                        and mouseX <= speler2_x+button_width \
                        and mouseY <= speler2_y+button_height:
                    print("je hebt de speler2 knop gevonden")
                    pygame.mixer.music.stop()
                    Game()

                if mouseX >= instr_x \
                        and mouseY >= instr_y \
                        and mouseX <= instr_x+button_width \
                        and mouseY <= instr_y+button_height:
                    print("je hebt de Instructions knop gevonden")
                    Instructions()

                if mouseX >= regels_x \
                        and mouseY >= regels_y \
                        and mouseX <= regels_x+button_width \
                        and mouseY <= regels_y+button_height:
                    print("je hebt de Game Rules knop gevonden")
                    Gamerules()

                if mouseX >= stop_x \
                        and mouseY >= stop_y \
                        and mouseX <= stop_x+button_width \
                        and mouseY <= stop_y+button_height:
                    print("je hebt de Quit knop gevonden")
                    pygame.mixer.music.stop()
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
                pygame.mixer.music.set_volume(0.0)

            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_2:
                print("je hebt op 2 gedrukt")
                pygame.mixer.music.set_volume(0.5)

            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_3:
                print("je hebt op 3 gedrukt")
                pygame.mixer.music.set_volume(1.0)


        if (LogoMenuCurrentImage==1):

            screen.blit(Game_logo2,      (int(spellogo2.Pos_x),       int(spellogo2.Pos_y)))
            screen.blit(Game_menu2,      (int(spelmenu2.Pos_x),       int(spelmenu2.Pos_y)))

        if (LogoMenuCurrentImage==2):

                screen.blit(Game_logo,      (int(spellogo.Pos_x),       int(spellogo.Pos_y)))
                screen.blit(Game_menu,      (int(spelmenu.Pos_x),       int(spelmenu.Pos_y)))

        if (LogoMenuCurrentImage==2):

                LogoMenuCurrentImage=1
        else:

            LogoMenuCurrentImage+=1;

        pygame.display.flip()
        clock.tick(5)


        screen.blit(background,     (int(achtergrond.Pos_x),    int(achtergrond.Pos_y)))
        screen.blit(Game_logo,      (int(spellogo.Pos_x),       int(spellogo.Pos_y)))
        screen.blit(Game_menu,      (int(spelmenu.Pos_x),       int(spelmenu.Pos_y)))
        screen.blit(play_button,    (int(startknop.Pos_x),      int(startknop.Pos_y)))
        screen.blit(instr_button,   (int(instructie.Pos_x),     int(instructie.Pos_y)))
        screen.blit(rules_button,   (int(regels.Pos_x),         int(regels.Pos_y)))
        screen.blit(stop_button,    (int(stopknop.Pos_x),       int(stopknop.Pos_y)))
        if players >= 1:
            screen.blit(Speler1,        (int(speler1.Pos_x),        int(speler1.Pos_y)))
        if players >= 2:
            screen.blit(Speler2,        (int(speler2.Pos_x),        int(speler2.Pos_y)))
        pygame.display.update()

def Game():
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
        def __init__(self, image, width, height, pos_x, pos_y):
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

    players = 1

    screen_width        = 768
    screen_height       = 1024

    button_width        = 200
    button_height       = 50

    button2_width        = 100
    button2_height       = 50

    st_button_width        = 50
    st_button_height       = 50

    stop_x              = 970
    stop_y              = 10

    menu_x              = stop_x - 50
    menu_y              = 10

    instr_x             = stop_x - 100
    instr_y             = 10

    regel_x             = stop_x - 150
    regel_y             = 10

    sound_x             = stop_x - 200
    sound_y             = 10

    dobbel_x            = 810
    dobbel_y            = 300

    dobbel2_x            = 920
    dobbel2_y            = 300

    dobbelstn_width     = 200
    dobbelstn_height    = 200
    dobbelstn_x         = 810
    dobbelstn_y         = 100

    opt1_x            = 810
    opt1_y            = 500

    opt2_x            = 810
    opt2_y            = opt1_y + 50

    opt3_x            = 810
    opt3_y            = opt1_y + 100

    opt1_text_x            = 790
    opt1_text_y            = 425

    opt2_text_x            = opt1_text_x
    opt2_text_y            = opt1_text_y + 25

    opt3_text_x            = opt1_text_x
    opt3_text_y            = opt1_text_y + 50

    logo_width          = 600
    logo_height         = 200
    logo_y              = 0
    logo_x              = 200

    bord_width          = 500
    bord_height         = 500
    bord_y              = 200
    bord_x              = 250

    vlak_width          = 225
    vlak_height         = 100
    vlak_x              = 15

    vlak_rood           = 200
    vlak_groen          = vlak_rood + 125
    vlak_geel           = vlak_rood + 250
    vlak_blauw          = vlak_rood + 375

    status_width          = 1000
    status_height         = 50
    vlak_grijs_x          = 10
    vlak_grijs_y          = 710

    lp_width            = 30
    lp_height           = 30

    p1_lp_x             = vlak_x + 165
    p1_lp_y             = 215

    p2_lp_x             = vlak_x + 165
    p2_lp_y             = vlak_rood + 140

    p3_lp_x             = vlak_x + 165
    p3_lp_y             = vlak_rood + 265

    p4_lp_x             = vlak_x + 165
    p4_lp_y             = vlak_rood + 390

    cp_width            = 30
    cp_height           = 30

    p1_cp_x                = vlak_x + 165
    p1_cp_y                = 255

    p2_cp_x                = vlak_x + 165
    p2_cp_y                = vlak_rood + 180

    p3_cp_x                = vlak_x + 165
    p3_cp_y                = vlak_rood + 305

    p4_cp_x                = vlak_x + 165
    p4_cp_y                = vlak_rood + 430

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

    p1_lp_tekst_x             = vlak_x + 75
    p1_lp_tekst_y             = vlak_rood + 20

    p2_lp_tekst_x             = vlak_x + 50
    p2_lp_tekst_y             = vlak_rood + 10

    p3_lp_tekst_x             = vlak_x + 50
    p3_lp_tekst_y             = vlak_rood + 10

    p4_lp_tekst_x             = vlak_x + 50
    p4_lp_tekst_y             = vlak_rood + 10

    SC_width        =   200
    SC_height       =   75
    SC_x            =   810
    SC_y            =   425
    SC_name_x       =   810
    SC_name_y       =   350

    klok_vak_width  =   250
    klok_vak_height =   100
    klok_vak_x      =   10
    klok_vak_y      =   10
    klok_x          =   20
    klok_y          =   10


    sfc_width           =   200
    sfc_height          =   300
    sfc_x               =   400
    sfc_y               =   300

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

    vakjes2 = list(vakjes)

    scherm      = Scherm        (screen_width, screen_height)
    achtergrond = Achtergrond   ('Main/Game/wood.jpg',          scherm.Height,  scherm.Width,       0,            0           )

    spellogo    = afbeeldingen  ('Button/SM/logo.png',          logo_width,     logo_height,        logo_x,       logo_y      )
    spelbord    = Knoppen       ('Main/Game/board2.png',        bord_width,     bord_height,        bord_x,       bord_y      )

    dobbelen    = Knoppen       ('Button/GM/roll.png',        button2_width,   button2_height,      dobbel_x,     dobbel_y    )
    dobbelen2   = Knoppen       ('Button/GM/fight.png',        button2_width,   button2_height,      dobbel2_x,     dobbel2_y    )
    optie1      = Knoppen       ('Button/GM/optie1.png',        button_width,   button_height,      opt1_x,       opt1_y    )
    optie2      = Knoppen       ('Button/GM/optie2.png',        button_width,   button_height,      opt2_x,       opt2_y    )
    optie3      = Knoppen       ('Button/GM/optie3.png',        button_width,   button_height,      opt3_x,       opt3_y    )

    pion_rood   = Pionnen       ('Player/Piece/Rood.png',       pion_width,     pion_height,      pion_rood_x,    pion_rood_y    )
    pion_groen  = Pionnen       ('Player/Piece/Groen.png',      pion_width,     pion_height,      pion_groen_x,   pion_groen_y    )
    pion_geel   = Pionnen       ('Player/Piece/Geel.png',       pion_width,     pion_height,      pion_geel_x,    pion_geel_y    )
    pion_blauw  = Pionnen       ('Player/Piece/Blauw.png',      pion_width,     pion_height,      pion_blauw_x,   pion_blauw_y    )

    instructie  = Snelkoppelingen       ('Button/GM/help.png',          st_button_width,   st_button_height,      instr_x,      instr_y     )
    spelregels  = Snelkoppelingen       ('Button/GM/regels.png',        st_button_width,   st_button_height,      regel_x,      regel_y     )
    spelmenu    = Snelkoppelingen       ('Button/GM/Home.png',          st_button_width,   st_button_height,      menu_x,       menu_y     )
    stopknop    = Snelkoppelingen       ('Button/GM/Kruis.png',         st_button_width,   st_button_height,      stop_x,       stop_y      )
    geluidknop  = Snelkoppelingen       ('Button/GM/Sound.png',         st_button_width,   st_button_height,      sound_x,       sound_y      )
    dempknop    = Snelkoppelingen       ('Button/GM/Sound_off.png',     st_button_width,   st_button_height,      sound_x,       sound_y      )

    status_rood = Statusvak     ('Main/Elements/statusVakP1.png',      vlak_width,   vlak_height,      vlak_x,       vlak_rood      )
    status_groen= Statusvak     ('Main/Elements/statusVakP2.png',    vlak_width,   vlak_height,      vlak_x,       vlak_groen      )
    status_geel = Statusvak     ('Main/Elements/statusVakP3.png',   vlak_width,   vlak_height,      vlak_x,       vlak_geel      )
    status_blauw= Statusvak     ('Main/Elements/statusVakP4.png',     vlak_width,   vlak_height,      vlak_x,       vlak_blauw      )
    status_grijs= Statusvak     ('Main/Elements/grey.png',     status_width,   status_height,      vlak_grijs_x,       vlak_grijs_y      )

    p1_lp       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p1_lp_x,       p1_lp_y      )
    p1_cp       = Conditiepunten('Main/Elements/cp.png',     cp_width,   cp_height,      p1_cp_x,       p1_cp_y      )

    p2_lp       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p2_lp_x,       p2_lp_y      )
    p2_cp       = Conditiepunten('Main/Elements/cp.png',     cp_width,   cp_height,      p2_cp_x,       p2_cp_y      )

    p3_lp       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p3_lp_x,       p3_lp_y      )
    p3_cp       = Conditiepunten('Main/Elements/cp.png',     cp_width,   cp_height,      p3_cp_x,       p3_cp_y      )

    p4_lp       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p4_lp_x,       p4_lp_y      )
    p4_cp       = Conditiepunten('Main/Elements/cp.png',     cp_width,   cp_height,      p4_cp_x,       p4_cp_y      )

    tekst       = Levenspunten  ('Main/Elements/lp.png',     lp_width,   lp_height,      p1_lp_tekst_x, p1_lp_tekst_y  )

    sk1_name    = Scorekaarten  ('Cards/SC/png/SC1_Name.png',        SC_width,      SC_height,       SC_name_x,           SC_name_y  )
    sk1_0       = Scorekaarten  ('Cards/SC/png/SC1_Aanval_0.png',        SC_width,      SC_height,       SC_x,           SC_y  )
    sk1_1       = Scorekaarten  ('Cards/SC/png/SC1_Aanval_1.png',        SC_width,      SC_height,       SC_x,           SC_y  )
    sk1_2       = Scorekaarten  ('Cards/SC/png/SC1_Aanval_2.png',        SC_width,      SC_height,       SC_x,           SC_y  )
    sk1_3       = Scorekaarten  ('Cards/SC/png/SC1_Aanval_3.png',        SC_width,      SC_height,       SC_x,           SC_y  )
    sk1_4       = Scorekaarten  ('Cards/SC/png/SC1_Aanval_4.png',        SC_width,      SC_height,       SC_x,           SC_y  )
    sk1_5       = Scorekaarten  ('Cards/SC/png/SC1_Aanval_5.png',        SC_width,      SC_height,       SC_x,           SC_y  )
    sk1_6       = Scorekaarten  ('Cards/SC/png/SC1_Aanval_6.png',        SC_width,      SC_height,       SC_x,           SC_y  )

    screen = pygame.display.set_mode                    ((scherm.Height, scherm.Width),HWSURFACE|DOUBLEBUF,32)

    background = pygame.image.load                      (achtergrond.Image)
    background = pygame.transform.scale(background,     (scherm.Height, scherm.Width))

    Game_logo = pygame.image.load                       (spellogo.Image)
    Game_logo = pygame.transform.scale(Game_logo,       (spellogo.Width, spellogo.Height))

    Game_board = pygame.image.load                       (spelbord.Image)
    Game_board = pygame.transform.scale(Game_board,       (spelbord.Width, spelbord.Height))

    Roll_dice = pygame.image.load                       (dobbelen.Image)
    Roll_dice = pygame.transform.scale(Roll_dice,       (dobbelen.Width, dobbelen.Height))

    Fight_dice = pygame.image.load                       (dobbelen2.Image)
    Fight_dice = pygame.transform.scale(Fight_dice,       (dobbelen2.Width, dobbelen2.Height))

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

    Status_grey     = pygame.image.load                    (status_grijs.Image)
    Status_grey     = pygame.transform.scale(Status_grey, (status_grijs.Width, status_grijs.Height))

    Status_clock     = pygame.image.load                    (status_grijs.Image)
    Status_clock     = pygame.transform.scale(Status_clock, (klok_vak_width, klok_vak_height))

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

    Music_on = pygame.image.load                     (geluidknop.Image)
    Music_button = pygame.transform.scale(Music_on,   (geluidknop.Width, geluidknop.Height))

    Sk1_name = pygame.image.load                     (sk1_name.Image)
    Sk1_name = pygame.transform.scale(Sk1_name,   (sk1_name.Width+5, sk1_name.Height))

    Sk1_0 = pygame.image.load                     (sk1_0.Image)
    Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))


    pygame.init()

    clock = pygame.time.Clock()

    player_name = str("Player 1 ")
    game_status = str("is aan de beurt")

    p1_lp_start         = int(100)
    font = pygame.font.Font(None, 36)
    p1_lp_st = font.render("LP: "+str(p1_lp_start), 1, (10, 10, 10))

    p1_cp_start         = int(15)
    font = pygame.font.Font(None, 36)
    p1_cp_st = font.render("CP: "+str(p1_cp_start), 1, (10, 10, 10))

    font = pygame.font.Font(None, 15)
    klok = font.render("Time: "+str(clock), 1, (10, 10, 10))
    FPS  = font.render("Time: "+str(clock.get_fps), 1, (10, 10, 10))



    dice_num = 0
    dobbelsteen = Dobbelstenen  ('Main/Dice/D0.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y)
    Dice_image = pygame.image.load(dobbelsteen.Image)
    Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))

    p1_vak = 0
    p2_vak = 10
    p3_vak = 20
    p4_vak = 30

    punten      = 0
    aanval      = 0
    verdediging = 0

    SFCA = pygame.image.load('Cards/SFC/SFCA.png')
    SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))

    music = 1
    pygame.mixer.music.load(os.path.join('Sound/game2.mp3'))
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    if music == 1:
        pygame.mixer.music.play()
    dice_num2 = 0

    while True:
        if p1_vak >= 40:
            p1_vak = p1_vak - 40

        if p1_vak >= 0 and p1_vak <= 4:

            SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
            SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
            screen.blit(SFC, (sfc_x , sfc_y ))
            Sk1_0 = pygame.image.load                     (sk1_0.Image)
            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))

        if p1_vak ==  5:
            if dice_num2 == 1:
                aanval_sfc = 10
            if dice_num2 == 2:
                aanval_sfc = 15
            if dice_num2 == 3:
                aanval_sfc = 25
            if dice_num2 == 4:
                aanval_sfc = 20
            if dice_num2 == 5:
                aanval_sfc = 15
            if dice_num2 == 6:
                aanval_sfc = 10

            SFC1 = pygame.image.load(os.path.join('Cards/SFC/SFC1.png'))
            SFC = pygame.transform.scale(SFC1, (sfc_width, sfc_height))
            screen.blit(SFC, (sfc_x , sfc_y ))
        if p1_vak >= 6 and p1_vak <= 14:
            SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
            SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
            Sk1_0 = pygame.image.load                     (sk1_0.Image)
            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
            screen.blit(SFC, (sfc_x , sfc_y ))

        if p1_vak == 15:
            if dice_num2 == 1:
                aanval_sfc = 15
            if dice_num2 == 2:
                aanval_sfc = 17
            if dice_num2 == 3:
                aanval_sfc = 19
            if dice_num2 == 4:
                aanval_sfc = 21
            if dice_num2 == 5:
                aanval_sfc = 23
            if dice_num2 == 6:
                aanval_sfc = 26

            SFC2 = pygame.image.load(os.path.join('Cards/SFC/SFC2.png'))
            SFC = pygame.transform.scale(SFC2, (sfc_width, sfc_height))
            screen.blit(SFC, (sfc_x , sfc_y ))
        if p1_vak >= 16 and p1_vak <= 24:

            SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
            SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
            Sk1_0 = pygame.image.load                     (sk1_0.Image)
            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))

            screen.blit(SFC, (sfc_x , sfc_y ))
        if p1_vak == 25:
            if dice_num2 == 1:
                aanval_sfc = 10
            if dice_num2 == 2:
                aanval_sfc = 12
            if dice_num2 == 3:
                aanval_sfc = 14
            if dice_num2 == 4:
                aanval_sfc = 16
            if dice_num2 == 5:
                aanval_sfc = 14
            if dice_num2 == 6:
                aanval_sfc = 12

            SFC3 = pygame.image.load(os.path.join('Cards/SFC/SFC3.png'))
            SFC = pygame.transform.scale(SFC3, (sfc_width, sfc_height))
            screen.blit(SFC, (sfc_x , sfc_y ))

        if p1_vak >= 26 and p1_vak <= 34:
            SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
            SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
            Sk1_0 = pygame.image.load                     (sk1_0.Image)
            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
            screen.blit(SFC, (sfc_x , sfc_y ))

        if p1_vak == 35:
            if dice_num2 == 1:
                aanval_sfc = 10
            if dice_num2 == 2:
                aanval_sfc = 30
            if dice_num2 == 3:
                aanval_sfc = 12
            if dice_num2 == 4:
                aanval_sfc = 25
            if dice_num2 == 5:
                aanval_sfc = 14
            if dice_num2 == 6:
                aanval_sfc = 23

            SFC4 = pygame.image.load(os.path.join('Cards/SFC/SFC4.png'))
            SFC = pygame.transform.scale(SFC4, (sfc_width, sfc_height))
            screen.blit(SFC, (sfc_x , sfc_y ))

        if p1_vak >= 36 and p1_vak <= 40:
            SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
            SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
            Sk1_0 = pygame.image.load                     (sk1_0.Image)
            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
            screen.blit(SFC, (sfc_x , sfc_y ))

        if p1_vak >= 40:
            vakjes.extend(vakjes2)
        if p2_vak >= 11:
            vakjes.extend(vakjes2)
        if p3_vak >= 21:
            vakjes.extend(vakjes2)
        if p4_vak >= 31:
            vakjes.extend(vakjes2)

        pion_rood.Pos_x = vakjes[p1_vak] [0] or vakjes2[p1_vak] [0]
        pion_rood.Pos_y = vakjes[p1_vak] [1] or vakjes2[p1_vak] [1]

        pion_groen.Pos_x = vakjes[p2_vak] [0] or vakjes2[p1_vak] [0]
        pion_groen.Pos_y = vakjes[p2_vak] [1] or vakjes2[p1_vak] [1]

        pion_geel.Pos_x = vakjes[p3_vak] [0] or vakjes2[p1_vak] [0]
        pion_geel.Pos_y = vakjes[p3_vak] [1] or vakjes2[p1_vak] [1]

        pion_blauw.Pos_x = vakjes[p4_vak] [0] or vakjes2[p1_vak] [0]
        pion_blauw.Pos_y = vakjes[p4_vak] [1] or vakjes2[p1_vak] [1]



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print ("X =",mouseX, "Y =",mouseY)

                if mouseX >= dobbel_x \
                        and mouseY >= dobbel_y \
                        and mouseX <= dobbel_x+button2_width \
                        and mouseY <= dobbel_y+button2_height:
                    print("je hebt de Roll Dice knop gedrukt")

                    dice_num = random.randint(1, 6)
                    p1_vak = p1_vak + dice_num
                    p2_vak = p2_vak + dice_num
                    p3_vak = p3_vak + dice_num
                    p4_vak = p4_vak + dice_num

                    if dice_num == 1:
                        dobbelsteen = Dobbelstenen  ('Main/Dice/D1.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                        Dice_image = pygame.image.load(dobbelsteen.Image)
                        Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                        game_status = str("je hebt 1 gegooid")

                    if dice_num == 2:
                        dobbelsteen = Dobbelstenen  ('Main/Dice/D2.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                        Dice_image = pygame.image.load(dobbelsteen.Image)
                        Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                        game_status = str("je hebt 2 gegooid")

                    if dice_num == 3:
                        dobbelsteen = Dobbelstenen  ('Main/Dice/D3.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                        Dice_image = pygame.image.load(dobbelsteen.Image)
                        Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                        game_status = str("je hebt 3 gegooid")

                    if dice_num == 4:
                        dobbelsteen = Dobbelstenen  ('Main/Dice/D4.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                        Dice_image = pygame.image.load(dobbelsteen.Image)
                        Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                        game_status = str("je hebt 4 gegooid")

                    if dice_num == 5:
                        dobbelsteen = Dobbelstenen  ('Main/Dice/D5.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                        Dice_image = pygame.image.load(dobbelsteen.Image)
                        Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                        game_status = str("je hebt 5 gegooid")

                    if dice_num == 6:
                        dobbelsteen = Dobbelstenen  ('Main/Dice/D6.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                        Dice_image = pygame.image.load(dobbelsteen.Image)
                        Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                        game_status = str("je hebt 6 gegooid")

                if p1_vak == 5 or p1_vak == 15 or p1_vak == 25 or p1_vak == 35:
                    if mouseX >= dobbel2_x \
                        and mouseY >= dobbel2_y \
                        and mouseX <= dobbel2_x+button2_width \
                        and mouseY <= dobbel2_y+button2_height:
                        print("je hebt de Fight Dice knop gedrukt")
                        dice_num2 = random.randint(1, 6)

                        if dice_num2 == 1:
                            dobbelsteen = Dobbelstenen  ('Main/Dice/D1.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                            Dice_image = pygame.image.load(dobbelsteen.Image)
                            Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                            Sk1_0 = pygame.image.load                     (sk1_1.Image)
                            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
                            game_status = str("je hebt 1 gegooid")

                        if dice_num2 == 2:
                            dobbelsteen = Dobbelstenen  ('Main/Dice/D2.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                            Dice_image = pygame.image.load(dobbelsteen.Image)
                            Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                            Sk1_0 = pygame.image.load                     (sk1_2.Image)
                            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
                            game_status = str("je hebt 2 gegooid")

                        if dice_num2 == 3:
                            dobbelsteen = Dobbelstenen  ('Main/Dice/D3.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                            Dice_image = pygame.image.load(dobbelsteen.Image)
                            Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                            Sk1_0 = pygame.image.load                     (sk1_3.Image)
                            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
                            game_status = str("je hebt 3 gegooid")

                        if dice_num2 == 4:
                            dobbelsteen = Dobbelstenen  ('Main/Dice/D4.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                            Dice_image = pygame.image.load(dobbelsteen.Image)
                            Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                            Sk1_0 = pygame.image.load                     (sk1_4.Image)
                            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
                            game_status = str("je hebt 4 gegooid")

                        if dice_num2 == 5:
                            dobbelsteen = Dobbelstenen  ('Main/Dice/D5.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                            Dice_image = pygame.image.load(dobbelsteen.Image)
                            Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                            Sk1_0 = pygame.image.load                     (sk1_5.Image)
                            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
                            game_status = str("je hebt 5 gegooid")

                        if dice_num2 == 6:
                            dobbelsteen = Dobbelstenen  ('Main/Dice/D6.png', dobbelstn_width, dobbelstn_height,  dobbelstn_x,   dobbelstn_y  )
                            Dice_image = pygame.image.load(dobbelsteen.Image)
                            Dice_image = pygame.transform.scale(Dice_image,(dobbelsteen.Width, dobbelsteen.Height))
                            Sk1_0 = pygame.image.load                     (sk1_6.Image)
                            Sk1 = pygame.transform.scale(Sk1_0,   (sk1_0.Width, sk1_0.Height))
                            game_status = str("je hebt 6 gegooid")

                if mouseX >= opt1_x \
                        and mouseY >= opt1_y \
                        and mouseX <= opt1_x+button_width \
                        and mouseY <= opt1_y+button_height:
                    print("je hebt de 1ste optie knop gedrukt")
                    choice = 0 + 1
                    if choice == 1:
                        if p1_vak == 5 or p1_vak == 15 or p1_vak == 25 or p1_vak == 35:
                            if dice_num2 == 1:
                                punten      = 2
                                aanval      = aanval_sfc
                                verdediging = 10
                            if dice_num2 == 2:
                                punten      = 3
                                aanval      = aanval_sfc
                                verdediging = 8
                            if dice_num2 == 3:
                                punten      = 1
                                aanval      = aanval_sfc
                                verdediging = 3
                            if dice_num2 == 4:
                                punten      = 2
                                aanval      = aanval_sfc
                                verdediging = 5
                            if dice_num2 == 5:
                                punten      = 2
                                aanval      = aanval_sfc
                                verdediging = 7
                            if dice_num2 == 6:
                                punten      = 1
                                aanval      = aanval_sfc
                                verdediging = 2

                if mouseX >= opt2_x \
                        and mouseY >= opt2_y \
                        and mouseX <= opt2_x+button_width \
                        and mouseY <= opt2_y+button_height:
                    print("je hebt de 2de optie knop gedrukt")
                    choice = 0 + 2
                    if choice == 2:
                        if p1_vak == 5 or p1_vak == 15 or p1_vak == 25 or p1_vak == 35:
                            if dice_num2 == 1:
                                punten      = 5
                                aanval      = aanval_sfc
                                verdediging = 20
                            if dice_num2 == 2:
                                punten      = 4
                                aanval      = aanval_sfc
                                verdediging = 13
                            if dice_num2 == 3:
                                punten      = 2
                                aanval      = aanval_sfc
                                verdediging = 9
                            if dice_num2 == 4:
                                punten      = 3
                                aanval      = aanval_sfc
                                verdediging = 11
                            if dice_num2 == 5:
                                punten      = 3
                                aanval      = aanval_sfc
                                verdediging = 12
                            if dice_num2 == 6:
                                punten      = 2
                                aanval      = aanval_sfc
                                verdediging = 4



                if mouseX >= opt3_x \
                        and mouseY >= opt3_y \
                        and mouseX <= opt3_x+button_width \
                        and mouseY <= opt3_y+button_height:
                    print("je hebt de 3de optie knop gedrukt")

                    choice = 0 + 3
                    if choice == 3:
                        if p1_vak == 5 or p1_vak == 15 or p1_vak == 25 or p1_vak == 35:
                            if dice_num2 == 1:
                                punten      = 8
                                aanval      = aanval_sfc
                                verdediging = 30
                            if dice_num2 == 2:
                                punten      = 5
                                aanval      = aanval_sfc
                                verdediging = 17
                            if dice_num2 == 3:
                                punten      = 3
                                aanval      = aanval_sfc
                                verdediging = 19
                            if dice_num2 == 4:
                                punten      = 5
                                aanval      = aanval_sfc
                                verdediging = 15
                            if dice_num2 == 5:
                                punten      = 4
                                aanval      = aanval_sfc
                                verdediging = 16
                            if dice_num2 == 6:
                                punten      = 3
                                aanval      = aanval_sfc
                                verdediging = 6

                if p1_lp_start < 100:
                    if p1_vak == 40 or p1_vak == 0 or p1_vak == 1:
                        p1_lp_huidig = p1_lp_start
                        p1_lp_start = int(p1_lp_start) + int(10)
                        lp = int(p1_lp_start)
                        font = pygame.font.Font(None, 36)
                        p1_lp_st = font.render("LP: "+str(lp), 1, (10, 10, 10))
                        game_status = str(("LP:  ",str(p1_lp_huidig),"+ 10 ","= LP: ",str(p1_lp_start)))

                if p1_cp_start < 15:
                    if p1_vak == 40 or p1_vak == 0 or p1_vak == 1:
                            p1_cp_huidig = p1_cp_start
                            p1_cp_start = int(15)
                            cp = int(p1_cp_start)
                            font = pygame.font.Font(None, 36)
                            p1_cp_st = font.render("CP: "+str(cp), 1, (10, 10, 10))
                            game_status = str(("CP:  ",str(p1_cp_huidig),"= 15 ","= CP: ",str(p1_cp_start)))

                if p1_cp_start >= 0 and p1_cp_start <= 15:
                    if p1_vak == 5 or p1_vak == 15 or p1_vak == 25 or p1_vak == 35:
                        p1_lp_huidig = p1_cp_start
                        p1_cp_start = int(p1_cp_start) - int(punten)
                        cp = int(p1_cp_start)
                        font = pygame.font.Font(None, 36)
                        p1_cp_st = font.render("CP: "+str(cp), 1, (10, 10, 10))
                        game_status = str(("LP:",str(p1_lp_huidig),"ATT: ",str(aanval),"CP: ",str(p1_cp_start),"DEF: ",str(verdediging),"LP = ",str(p1_lp_start)))

                if p1_lp_start > 0 and p1_lp_start <= 100:
                    if p1_vak == 5 or p1_vak == 15 or p1_vak == 25 or p1_vak == 35:
                        p1_lp_huidig = p1_lp_start
                        p1_lp_start = (int(p1_lp_start) - int(aanval))
                        p1_lp_start = p1_lp_start + int(verdediging)
                        if p1_lp_start >= 100:
                            p1_lp_start = int(100)
                        lp = int(p1_lp_start)
                        font = pygame.font.Font(None, 36)
                        p1_lp_st = font.render("LP: "+str(lp), 1, (10, 10, 10))
                        game_status = str(("LP:",str(p1_lp_huidig),"ATT: ",str(aanval),"CP: ",str(p1_cp_start),"DEF: ",str(verdediging),"LP = ",str(p1_lp_start)))

                if p1_lp_start >= 100:
                    p1_lp_start = int(100)
                if p1_cp_start <=0:
                    p1_cp_start = int(0)
                    game_status = str("Je hebt geen conditiepunten meer")
                if p1_lp_start <=0:
                    p1_lp_start = int(0)
                    game_status = str("Je hebt geen levenspunten meer")
                    Loser()


                if mouseX >= instr_x \
                        and mouseY >= instr_y \
                        and mouseX <= instr_x+st_button_width \
                        and mouseY <= instr_y+st_button_height:
                    print("je hebt de Instruction knop gedrukt")
                    Instructions()

                if mouseX >= regel_x \
                        and mouseY >= regel_y \
                        and mouseX <= regel_x+st_button_width \
                        and mouseY <= regel_y+st_button_height:
                    print("je hebt de Game Rules knop gedrukt")
                    Gamerules()

                if mouseX >= menu_x \
                        and mouseY >= menu_y \
                        and mouseX <= menu_x+st_button_width \
                        and mouseY <= menu_y+st_button_height:
                    print("je hebt de Menu knop gedrukt")
                    Intro()

                if mouseX >= stop_x \
                        and mouseY >= stop_y \
                        and mouseX <= stop_x+st_button_width \
                        and mouseY <= stop_y+st_button_height:
                    print("je hebt de Quit knop gedrukt")
                    pygame.quit()
                    exit()

                if mouseX >= sound_x \
                        and mouseY >= sound_y \
                        and mouseX <= sound_x+st_button_width \
                        and mouseY <= sound_y+st_button_height:
                    print("je hebt de Geluids knop gedrukt")
                    music = random.randint(1,2)
                    if music == 1:
                        pygame.mixer.music.unpause()
                        Music_on = pygame.image.load                     (geluidknop.Image)
                        Music_button = pygame.transform.scale(Music_on,   (geluidknop.Width, geluidknop.Height))
                    elif music == 2:
                        pygame.mixer.music.pause()
                        Music_off = pygame.image.load                     (dempknop.Image)
                        Music_button = pygame.transform.scale(Music_off,   (geluidknop.Width, geluidknop.Height))

            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_ESCAPE:
                game_status = str("je hebt het spel afgesloten")
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_1:
                print("je hebt op 1 gedrukt")
                if players >= 1:
                    players = 1

            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_2:
                print("je hebt op 2 gedrukt")
                if players >= 1:
                    players = 2

            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_3:
                print("je hebt op 3 gedrukt")
                if players >= 1:
                    players = 3

            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_4:
                print("je hebt op 3 gedrukt")
                if players >= 1:
                    players = 4


        font = pygame.font.Font(None, 36)
        status = font.render(str(player_name)+str(game_status), 1, (10, 10, 10))
        font = pygame.font.Font(None, 30)
        opt1 = font.render("1: ", 1, (10, 10, 10))
        opt2 = font.render("2: ", 1, (10, 10, 10))
        opt3 = font.render("3: ", 1, (10, 10, 10))

        screen.blit(background,     (int(achtergrond.Pos_x),    int(achtergrond.Pos_y)))

        screen.blit(Game_logo,      (int(spellogo.Pos_x),       int(spellogo.Pos_y)))
        screen.blit(Game_board,     (int(spelbord.Pos_x),       int(spelbord.Pos_y)))

        screen.blit(Roll_dice,      (int(dobbelen.Pos_x),      int(dobbelen.Pos_y)))
        screen.blit(Fight_dice,      (int(dobbelen2.Pos_x),      int(dobbelen2.Pos_y)))
        screen.blit(Dice_image,     (int(dobbelsteen.Pos_x),   int(dobbelsteen.Pos_y)))

        screen.blit(Option1,        (int(optie1.Pos_x),         int(optie1.Pos_y)))
        screen.blit(opt1,           (int(opt1_text_x),          int(opt1_text_y)))
        screen.blit(Option2,        (int(optie2.Pos_x),         int(optie2.Pos_y)))
        screen.blit(opt2,           (int(opt2_text_x),          int(opt2_text_y)))
        screen.blit(Option3,        (int(optie3.Pos_x),         int(optie3.Pos_y)))
        screen.blit(opt3,           (int(opt3_text_x),          int(opt3_text_y)))

        if players == 1:
            screen.blit(Red_piece,          (int(pion_rood.Pos_x),      int(pion_rood.Pos_y)))
            screen.blit(Status_red,         (int(status_rood.Pos_x),    int(status_rood.Pos_y)))
            screen.blit(P1_CP,              (int(p1_cp.Pos_x),          int(p1_cp.Pos_y)))
            screen.blit(P1_LP,              (int(p1_lp.Pos_x),          int(p1_lp.Pos_y)))
            screen.blit(p1_lp_st,           (int(tekst.Pos_x),          int(tekst.Pos_y)))
            screen.blit(p1_cp_st,           (int(tekst.Pos_x),          int(tekst.Pos_y+ 40)))


        if players == 2:
            screen.blit(Green_piece,        (int(pion_groen.Pos_x),     int(pion_groen.Pos_y)))
            screen.blit(Status_green,       (int(status_groen.Pos_x),   int(status_groen.Pos_y)))
            screen.blit(P2_LP,              (int(p2_lp.Pos_x),          int(p2_lp.Pos_y)))
            screen.blit(P2_CP,              (int(p2_cp.Pos_x),          int(p2_cp.Pos_y)))
            screen.blit(p1_lp_st,           (int(tekst.Pos_x),          int(tekst.Pos_y+ 120)))
            screen.blit(p1_cp_st,           (int(tekst.Pos_x),          int(tekst.Pos_y+ 160)))


        if players == 3:
            screen.blit(Yellow_piece,       (int(pion_geel.Pos_x),      int(pion_geel.Pos_y)))
            screen.blit(Status_yellow,      (int(status_geel.Pos_x),    int(status_geel.Pos_y)))
            screen.blit(P3_CP,              (int(p3_cp.Pos_x),          int(p3_cp.Pos_y)))
            screen.blit(P3_LP,              (int(p3_lp.Pos_x),          int(p3_lp.Pos_y)))
            screen.blit(p1_lp_st,           (int(tekst.Pos_x),          int(tekst.Pos_y+ 245)))
            screen.blit(p1_cp_st,           (int(tekst.Pos_x),          int(tekst.Pos_y+ 285)))


        if players == 4:
            screen.blit(Blue_piece,     (int(pion_blauw.Pos_x),     int(pion_blauw.Pos_y)))
            screen.blit(Status_blue,    (int(status_blauw.Pos_x),   int(status_blauw.Pos_y)))
            screen.blit(P4_CP,          (int(p4_cp.Pos_x),          int(p4_cp.Pos_y)))
            screen.blit(P4_LP,          (int(p4_lp.Pos_x),          int(p4_lp.Pos_y)))
            screen.blit(p1_lp_st,       (int(tekst.Pos_x),          int(tekst.Pos_y+ 375)))
            screen.blit(p1_cp_st,       (int(tekst.Pos_x),          int(tekst.Pos_y+ 415)))

        screen.blit(instr_button,   (int(instructie.Pos_x),     int(instructie.Pos_y)))
        screen.blit(Rules_button,   (int(spelregels.Pos_x),     int(spelregels.Pos_y)))
        screen.blit(Menu_button,    (int(spelmenu.Pos_x),       int(spelmenu.Pos_y)))
        screen.blit(stop_button,    (int(stopknop.Pos_x),       int(stopknop.Pos_y)))
        screen.blit(Music_button,   (int(geluidknop.Pos_x),     int(geluidknop.Pos_y)))

        screen.blit(SFC,            (int(sfc_x),                        int(sfc_y)))
        screen.blit(Status_grey,    (int(status_grijs.Pos_x),           int(status_grijs.Pos_y)))
        screen.blit(status,         (int(vlak_grijs_x+vlak_width//3),   int(vlak_grijs_y+10)))


        #screen.blit(Status_clock,   (int(klok_vak_x),                   int(klok_vak_y)))
        #screen.blit(klok,          (int(klok_x),                       int(klok_y)))
        #screen.blit(FPS,            (int(klok_x),                       int(klok_y+20)))

        screen.blit(Sk1_name,       (int(sk1_name.Pos_x-3),             int(sk1_name.Pos_y)))
        screen.blit(Sk1,            (int(sk1_0.Pos_x),                  int(sk1_0.Pos_y)))

        pygame.display.update()

def Instructions():
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
        screen = pygame.display.set_mode                    ((scherm.Height, scherm.Width),HWSURFACE|DOUBLEBUF,32)

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
                        player_choice = 1
                        print(player_choice)
                        if player_choice == 1:
                            elementen   = Knoppen       ('Main/Instructions/elements.jpg',  scherm.Height,  scherm.Width,   element_x,      element_y     )
                            background = pygame.image.load                              (elementen.Image)
                            background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))

                    if mouseX >= startmenu_x \
                            and mouseY >= startmenu_y \
                            and mouseX <= startmenu_x+button_width \
                            and mouseY <= startmenu_y+button_height:
                        print("je hebt de Startmenu knop gevonden")
                        Intro()


                    if mouseX >= volgende_x \
                            and mouseY >= volgende_y \
                            and mouseX <= volgende_x+button_width \
                            and mouseY <= volgende_y+button_height:
                        print("je hebt de Next knop gevonden")
                        player_choice = 2
                        print(player_choice)
                        if player_choice == 2:
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
            screen.blit(gamemenu,           (int(startmenu.Pos_x),      int(startmenu.Pos_y)))
            if player_choice == 2:
                screen.blit(previous_button,    (int(vorige.Pos_x),         int(vorige.Pos_y)))
            if player_choice == 1:
                screen.blit(second_button,      (int(volgende.Pos_x),       int(volgende.Pos_y)))

            pygame.display.update()

def Gamerules():
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

    regels_x            = 0
    regels_y            = 0

    vorige_x            = 200
    vorige_y            = 650

    startmenu_x         = 400
    startmenu_y         = 650

    volgende_x          = 600
    volgende_y          = 650

    button_width        = 200
    button_height       = 50


    scherm      = Scherm        (screen_width, screen_height)
    screen = pygame.display.set_mode                    ((scherm.Height, scherm.Width),HWSURFACE|DOUBLEBUF,32)

    spelregels1 = Knoppen       ('Main/Rules/page1.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
    vorige      = Knoppen       ('Button/IM/previous.png', button_width,   button_height,       vorige_x,    vorige_y     )
    startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )
    volgende    = Knoppen       ('Button/IM/next.png',     button_width,   button_height,       volgende_x,  volgende_y   )



    background = pygame.image.load                              (spelregels1.Image)
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
                        spelregels1 = Knoppen       ('Main/Rules/page1.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
                        startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )
                        volgende    = Knoppen       ('Button/IM/next.png',     button_width,   button_height,       volgende_x,  volgende_y   )

                        background = pygame.image.load                              (spelregels1.Image)
                        background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))
                        gamemenu = pygame.image.load                                (startmenu.Image)
                        gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))
                        second_button = pygame.image.load                           (volgende.Image)
                        second_button = pygame.transform.scale(second_button,       (volgende.Width, volgende.Height))

                    elif player_choice == 2:
                        spelregels1 = Knoppen       ('Main/Rules/page2.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
                        vorige      = Knoppen       ('Button/IM/previous.png', button_width,   button_height,       vorige_x,    vorige_y     )
                        startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )
                        volgende    = Knoppen       ('Button/IM/next.png',     button_width,   button_height,       volgende_x,  volgende_y   )

                        background = pygame.image.load                              (spelregels1.Image)
                        background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))
                        previous_button = pygame.image.load                         (vorige.Image)
                        previous_button = pygame.transform.scale(previous_button,   (vorige.Width, vorige.Height))
                        gamemenu = pygame.image.load                                (startmenu.Image)
                        gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))
                        second_button = pygame.image.load                           (volgende.Image)
                        second_button = pygame.transform.scale(second_button,       (volgende.Width, volgende.Height))

                    elif player_choice == 3:
                        spelregels1 = Knoppen       ('Main/Rules/page3.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
                        vorige      = Knoppen       ('Button/IM/previous.png', button_width,   button_height,       vorige_x,    vorige_y     )
                        startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )
                        volgende    = Knoppen       ('Button/IM/next.png',     button_width,   button_height,       volgende_x,  volgende_y   )

                        background = pygame.image.load                              (spelregels1.Image)
                        background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))
                        previous_button = pygame.image.load                         (vorige.Image)
                        previous_button = pygame.transform.scale(previous_button,   (vorige.Width, vorige.Height))
                        gamemenu = pygame.image.load                                (startmenu.Image)
                        gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))
                        second_button = pygame.image.load                           (volgende.Image)
                        second_button = pygame.transform.scale(second_button,       (volgende.Width, volgende.Height))

                    elif player_choice == 4:
                        spelregels1 = Knoppen       ('Main/Rules/page4.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
                        vorige      = Knoppen       ('Button/IM/previous.png', button_width,   button_height,       vorige_x,    vorige_y     )
                        startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )

                        background = pygame.image.load                              (spelregels1.Image)
                        background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))
                        previous_button = pygame.image.load                         (vorige.Image)
                        previous_button = pygame.transform.scale(previous_button,   (vorige.Width, vorige.Height))
                        gamemenu = pygame.image.load                                (startmenu.Image)
                        gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))




                if mouseX >= startmenu_x \
                        and mouseY >= startmenu_y \
                        and mouseX <= startmenu_x+button_width \
                        and mouseY <= startmenu_y+button_height:
                    print("je hebt de Startmenu knop gevonden")
                    Intro()

                if mouseX >= volgende_x \
                        and mouseY >= volgende_y \
                        and mouseX <= volgende_x+button_width \
                        and mouseY <= volgende_y+button_height:
                    print("je hebt de Next knop gevonden")
                    player_choice = player_choice + 1
                    print(player_choice)
                    if player_choice == 1:
                        spelregels1 = Knoppen       ('Main/Rules/page1.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
                        startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )
                        volgende    = Knoppen       ('Button/IM/next.png',     button_width,   button_height,       volgende_x,  volgende_y   )

                        background = pygame.image.load                              (spelregels1.Image)
                        background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))
                        gamemenu = pygame.image.load                                (startmenu.Image)
                        gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))
                        second_button = pygame.image.load                           (volgende.Image)
                        second_button = pygame.transform.scale(second_button,       (volgende.Width, volgende.Height))

                    elif player_choice == 2:
                        spelregels1 = Knoppen       ('Main/Rules/page2.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
                        vorige      = Knoppen       ('Button/IM/previous.png', button_width,   button_height,       vorige_x,    vorige_y     )
                        startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )
                        volgende    = Knoppen       ('Button/IM/next.png',     button_width,   button_height,       volgende_x,  volgende_y   )

                        background = pygame.image.load                              (spelregels1.Image)
                        background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))
                        previous_button = pygame.image.load                         (vorige.Image)
                        previous_button = pygame.transform.scale(previous_button,   (vorige.Width, vorige.Height))
                        gamemenu = pygame.image.load                                (startmenu.Image)
                        gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))
                        second_button = pygame.image.load                           (volgende.Image)
                        second_button = pygame.transform.scale(second_button,       (volgende.Width, volgende.Height))

                    elif player_choice == 3:
                        spelregels1 = Knoppen       ('Main/Rules/page3.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
                        vorige      = Knoppen       ('Button/IM/previous.png', button_width,   button_height,       vorige_x,    vorige_y     )
                        startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )
                        volgende    = Knoppen       ('Button/IM/next.png',     button_width,   button_height,       volgende_x,  volgende_y   )

                        background = pygame.image.load                              (spelregels1.Image)
                        background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))
                        previous_button = pygame.image.load                         (vorige.Image)
                        previous_button = pygame.transform.scale(previous_button,   (vorige.Width, vorige.Height))
                        gamemenu = pygame.image.load                                (startmenu.Image)
                        gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))
                        second_button = pygame.image.load                           (volgende.Image)
                        second_button = pygame.transform.scale(second_button,       (volgende.Width, volgende.Height))

                    elif player_choice == 4:
                        spelregels1 = Knoppen       ('Main/Rules/page4.jpg',   scherm.Height,  scherm.Width,        regels_x,    regels_y     )
                        vorige      = Knoppen       ('Button/IM/previous.png', button_width,   button_height,       vorige_x,    vorige_y     )
                        startmenu   = Knoppen       ('Button/IM/mainmenu.png', button_width,   button_height,       startmenu_x, startmenu_y  )

                        background = pygame.image.load                              (spelregels1.Image)
                        background = pygame.transform.scale(background,             (scherm.Height, scherm.Width))
                        previous_button = pygame.image.load                         (vorige.Image)
                        previous_button = pygame.transform.scale(previous_button,   (vorige.Width, vorige.Height))
                        gamemenu = pygame.image.load                                (startmenu.Image)
                        gamemenu = pygame.transform.scale(gamemenu,                 (startmenu.Width, startmenu.Height))

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

        screen.blit(background,         (int(spelregels1.Pos_x),    int(spelregels1.Pos_y)))
        screen.blit(gamemenu,           (int(startmenu.Pos_x),      int(startmenu.Pos_y)))
        if player_choice == 2 or player_choice == 3 or player_choice == 4:
            screen.blit(previous_button,    (int(vorige.Pos_x),         int(vorige.Pos_y)))
        if player_choice == 1 or player_choice == 2 or player_choice == 3:
            screen.blit(second_button,      (int(volgende.Pos_x),       int(volgende.Pos_y)))

        pygame.display.update()

def Winner():
    pygame.init()

    screen = pygame.display.set_mode((800,800))

    pygame.display.set_caption("Animation")
    terugNaarMenu               = 'Main/instructions/Kruis2.png'
    tryAgain_knop               = 'Main/Game/winKnop.png'
    # spelbord sprites
    bs = 'Main/Game/achtergrondWinLose.png'

    clock = pygame.time.Clock()

    #Grootte van terugKnop aangeven
    RodeKnopje_width        = 30
    RodeKnopje_height       = 25

    #positie van terugKnop
    tk_x = 970
    tk_y = 38

    #Grootte van tryAgainknop aangeven
    tryKnopje_width        = 150
    try_height             = 50

    #positie van tryAgainKnop
    try_x = 800
    try_y = 540

    #Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
    terug_knop = pygame.image.load(terugNaarMenu)
    terug_knop = pygame.transform.scale(terug_knop, (RodeKnopje_width , RodeKnopje_height))

    #Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
    tryy = pygame.image.load(tryAgain_knop)
    tryy = pygame.transform.scale(tryy, (tryKnopje_width , try_height))


    w1 = pygame.image.load("Main/Game/winSituatieBlauw.png")
    w1 = pygame.transform.scale(w1, (1024, 728))
    w2 = pygame.image.load("Main/Game/winSituatieRed.png")
    w2 = pygame.transform.scale(w2, (1024, 728))


    screen = pygame.display.set_mode((1024, 728))
    BG = pygame.image.load(bs).convert()

    screen.blit(BG, (0, 0))


    winnerCurrentImage = 1

    gameLoop=True
    while gameLoop:

        for event in pygame.event.get():

            if (event.type==pygame.QUIT):

                gameLoop=False

        if (winnerCurrentImage==1):

            screen.blit(w1, (0,0))
            screen.blit(terug_knop,(tk_x,tk_y))
            screen.blit(tryy,(try_x,try_y))
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print ("X =",mouseX, "Y =",mouseY)
                if mouseX >= try_x \
                        and mouseY >= try_y \
                        and mouseX <= try_x+tryKnopje_width \
                        and mouseY <= try_y+try_height:
                    print("je hebt de terug knop gevonden")
                    Intro()

        if (winnerCurrentImage==2):

            screen.blit(w2, (0,0))
            screen.blit(terug_knop,(tk_x,tk_y))
            screen.blit(tryy,(try_x,try_y))
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print ("X =",mouseX, "Y =",mouseY)
                if mouseX >= try_x \
                        and mouseY >= try_y \
                        and mouseX <= try_x+tryKnopje_width \
                        and mouseY <= try_y+try_height:
                    print("je hebt de terug knop gevonden")
                    Intro()

        if (winnerCurrentImage==2):

            winnerCurrentImage=1

            screen.blit(terug_knop,(tk_x,tk_y))
            screen.blit(tryy,(try_x,try_y))
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print ("X =",mouseX, "Y =",mouseY)
                if mouseX >= try_x \
                        and mouseY >= try_y \
                        and mouseX <= try_x+tryKnopje_width \
                        and mouseY <= try_y+try_height:
                    print("je hebt de terug knop gevonden")
                    Intro()

        else:

            winnerCurrentImage+=1;

        pygame.display.flip()

        clock.tick(5)

    pygame.quit()

def Loser():
    pygame.init()

    screen = pygame.display.set_mode((800,800))

    pygame.display.set_caption("Animation")
    terugNaarMenu               = 'Main/instructions/Kruis2.png'
    tryAgain_knop               = 'Main/Game/winKnop.png'
    # spelbord sprites
    bs = 'Main/Game/achtergrondWinLose.png'

    clock = pygame.time.Clock()

    #Grootte van terugKnop aangeven
    RodeKnopje_width        = 30
    RodeKnopje_height       = 25

    #positie van terugKnop
    tk_x = 970
    tk_y = 38

    #Grootte van tryAgainknop aangeven
    tryKnopje_width        = 150
    try_height             = 50

    #positie van tryAgainKnop
    try_x = 800
    try_y = 540

    #Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
    terug_knop = pygame.image.load(terugNaarMenu)
    terug_knop = pygame.transform.scale(terug_knop, (RodeKnopje_width , RodeKnopje_height))

    #Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
    tryy = pygame.image.load(tryAgain_knop)
    tryy = pygame.transform.scale(tryy, (tryKnopje_width , try_height))


    w1 = pygame.image.load("Main/Game/winSituatieBlauw2.png")
    w1 = pygame.transform.scale(w1, (1024, 728))
    w2 = pygame.image.load("Main/Game/winSituatieRed2.png")
    w2 = pygame.transform.scale(w2, (1024, 728))


    screen = pygame.display.set_mode((1024, 728))
    BG = pygame.image.load(bs).convert()

    screen.blit(BG, (0, 0))


    winnerCurrentImage = 1

    gameLoop=True
    while gameLoop:

        for event in pygame.event.get():

            if (event.type==pygame.QUIT):

                gameLoop=False

        if (winnerCurrentImage==1):

            screen.blit(w1, (0,0))
            screen.blit(terug_knop,(tk_x,tk_y))
            screen.blit(tryy,(try_x,try_y))
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print ("X =",mouseX, "Y =",mouseY)
                if mouseX >= try_x \
                        and mouseY >= try_y \
                        and mouseX <= try_x+tryKnopje_width \
                        and mouseY <= try_y+try_height:
                    print("je hebt de terug knop gevonden")
                    Intro()

        if (winnerCurrentImage==2):

            screen.blit(w2, (0,0))
            screen.blit(terug_knop,(tk_x,tk_y))
            screen.blit(tryy,(try_x,try_y))
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print ("X =",mouseX, "Y =",mouseY)
                if mouseX >= try_x \
                        and mouseY >= try_y \
                        and mouseX <= try_x+tryKnopje_width \
                        and mouseY <= try_y+try_height:
                    print("je hebt de terug knop gevonden")
                    Intro()

        if (winnerCurrentImage==2):

            winnerCurrentImage=1

            screen.blit(terug_knop,(tk_x,tk_y))
            screen.blit(tryy,(try_x,try_y))
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print ("X =",mouseX, "Y =",mouseY)
                if mouseX >= try_x \
                        and mouseY >= try_y \
                        and mouseX <= try_x+tryKnopje_width \
                        and mouseY <= try_y+try_height:
                    print("je hebt de terug knop gevonden")
                    Intro()

        else:

            winnerCurrentImage+=1;

        pygame.display.flip()

        clock.tick(5)

    pygame.quit()


Intro()