import pygame
import random
import os
from pygame.locals import *
from sys import exit

# pygame initialiseren( deze heb je nodig bijj hte begin van deze pygame
pygame.init()
pygame.display.set_caption('Survival game')

# afbeeldingen locaties aangeven
bg = 'Main/Game/wood.jpg'
board = 'Main/Game/board.png'
lp = 'Button/GM/levenspunten.png'
cp = 'Button/GM/conditiepunten.png'

#dobbelsteen
ds = 'Main/Dice/D1.png'
ds2 = 'Main/Dice/D2.png'
ds3 = 'Main/Dice/D3.png'
ds4 = 'Main/Dice/D4.png'
ds5 = 'Main/Dice/D5.png'
ds6 = 'Main/Dice/D6.png'

sf = 'Cards/SFC/SFC1.jpg'
score = 'Cards/SC/SC1.jpg'
speler = 'Player/Faces/S1.png'

#Pionnen
pion1 = 'Player/Piece/Rood.png'
pion2 = 'Player/Piece/Blauw.png'
pion3 = 'Player/Piece/Groen.png'
pion4 = 'Player/Piece/Geel.png'

#stop knop
quit = 'Button/GM/Kruis.png'

#help knop
help1 = 'Button/GM/help.png'

#roll knop
roll = 'Button/GM/knop_roll.png'

#kies knop
knop1 = 'Button/GM/kies_1.png'
knop2 = 'Button/GM/kies_2.png'
knop3 = 'Button/GM/kies_3.png'

#kaarten
SFCA  = 'Cards/SFC/SFCA.png'
SFC1  = 'Cards/SFC/SFC1.png'
SFC2  = 'Cards/SFC/SFC2.png'
SFC3  = 'Cards/SFC/SFC3.png'
SFC4  = 'Cards/SFC/SFC4.png'
SFC5  = 'Cards/SFC/SFC5.png'
SFC6  = 'Cards/SFC/SFC6.png'
SFC7  = 'Cards/SFC/SFC7.png'
SFC8  = 'Cards/SFC/SFC8.png'
SFC9  = 'Cards/SFC/SFC9.png'
SFC10  = 'Cards/SFC/SFC10.png'
SFC11  = 'Cards/SFC/SFC11.png'
SFC12  = 'Cards/SFC/SFC12.png'
SFC13  = 'Cards/SFC/SFC13.png'
SFC14  = 'Cards/SFC/SFC14.png'
SFC15  = 'Cards/SFC/SFC15.png'
SFC16  = 'Cards/SFC/SFC16.png'
SFC17  = 'Cards/SFC/SFC17.png'
SFC18  = 'Cards/SFC/SFC18.png'

#geluid aan
sound='Button/GM/Sound.png'

#geluid uit
soundOff='Button/GM/Sound_off.png'

#logo
logo ='Main/Logo2.png'

#verversingsnelheid van het scherm
clock = pygame.time.Clock()

#afmetingen
#knop afsluiten
close_width         =   40
close_height        =   40
close_x             =   950
close_y             =   15

#knop1 formaten
button_width        =   100
button_height       =   100
button_x            =   900
button_y            =   200

#dice formaten
dice_width          =   100
dice_height         =   100
dice_x              =   900
dice_y              =   80


#superfight kaart formaten
sfc_width           =   200
sfc_height          =   300
sfc_x               =   50
sfc_y               =   200

#hulp knop formante
hulp_width          =   40
hulp_height         =   40
hulp_x              =   900
hulp_y              =   15

#knop1 formaten
knop1_width     =       60
knop1_height    =       60
knop1_x         =       550
knop1_y         =       650

#knop 2 formaten
knop2_width     =       60
knop2_height    =       60
knop2_x         =       650
knop2_y         =       650

#knop3 formaten
knop3_width     =       60
knop3_height    =       60
knop3_x         =       750
knop3_y         =       650

#boksbal formaten
roodPion_width      =    25
roodPion_height     =    25

blauw_width         =    25
blauw_height        =    25

#sfc kaart formaten
sfc_height          =   280
sfc_width           =   180
sfc_x               =   180
sfc_y               =   210

#score formaten
score_height    =   300
score_width     =   300
score_x         =   550
score_y         =   350

#speler formaten
speler_height        =   100
speler_width         =   100
speler_x             =   850
speler_y             =   450

#gameboard formaten
gameboard_width     =   500
gameboard_height    =   500
gameboard_x         =   900
gameboard_y         =   50

#geluid icon formaten
sound_width =   40
sound_height =  40
sound_x     =   850
sound_y     =   15

#geluid uit formaten
soundOff_width =   40
soundOff_height =  40
soundOff_x     =   850
soundOff_y     =   15

#logo formaten
logo_width =    300
logo_height =   100
logo_x       =  100
logo_y       =  650

#logo
Logo= pygame.image.load(logo)
Logo = pygame.transform.scale(Logo,(logo_width,logo_height))

#geluid uit
SoundOff=pygame.image.load(soundOff)
SoundOff = pygame.transform.scale(SoundOff,(soundOff_width,soundOff_height))

#geluid
Sound=pygame.image.load(sound)
Sound = pygame.transform.scale(Sound,(sound_width,sound_height))


#rode pion
red_Pion = pygame.image.load(pion1)
red_Pion = pygame.transform.scale(red_Pion, (roodPion_width, roodPion_height))

#blauw pion
Blauw_Pion = pygame.image.load(pion2)
Blauw_Pion = pygame.transform.scale(Blauw_Pion,(blauw_width,blauw_height))

# grootte van het scherm aangeven
screen = pygame.display.set_mode((1024, 768))
BG = pygame.image.load(bg)
# achtergrondkleur
# screen.fill((80, 200, 250))

# Laden van afbeelding
spelbord = pygame.image.load(board)

# Hervormen van de afbeelding
gameboard = pygame.transform.scale(spelbord, (gameboard_width , gameboard_height ))

# Laden van afbeelding
levenspunt = pygame.image.load(lp)

# Hervormen van de afbeelding
#lifepoints = pygame.transform.scale(levenspunt, (Lp_height, 50))

# conditiepunten afbeelding
#CP = pygame.image.load(cp)
#CP = pygame.transform.scale(CP, (40, 40))

# Quit button
Quit = pygame.image.load(quit)
Quit = pygame.transform.scale(Quit, (close_width, close_width))

# help button
Help = pygame.image.load(help1)
Help = pygame.transform.scale(Help, (hulp_width, hulp_height))

# dobbelsteen
DS = pygame.image.load(ds)
DS = pygame.transform.scale(DS, (dice_width,dice_height))

# knop roll
Roll = pygame.image.load(roll)
Roll = pygame.transform.scale(Roll, (button_width, button_height))

# superfight kaart
SFCA = pygame.image.load(SFCA)
SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))

# score
Score = pygame.image.load(score)
Score = pygame.transform.scale(Score, (score_height, score_width))

# player
Speler = pygame.image.load(speler)
Speler = pygame.transform.scale(Speler, (speler_width, speler_height))


# knop1
Knop1 = pygame.image.load(knop1)
Knop1 = pygame.transform.scale(Knop1, (knop1_width, knop1_height))

# knop2
Knop2 = pygame.image.load(knop2)
Knop2 = pygame.transform.scale(Knop2, (knop2_width, knop2_height))

# knop3
Knop3 = pygame.image.load(knop3)
Knop3 = pygame.transform.scale(Knop3, (knop3_height, knop3_width))


# zolang de bovenstaande kloptKnop3 = pygame.transform.scale(Knop3, (60, 60))
D1 = pygame.image.load(ds)
D = pygame.transform.scale(D1, (dice_width, dice_height))

Pion3 = pygame.image.load(pion3)
Pion3 = pygame.transform.scale(Pion3, (40,40))
#LP
font = pygame.font.SysFont("Arial Black", 20)
text = font.render("Speler 1 LP:", True, (0, 0, 0))
#CP
font2 = pygame.font.SysFont('Arial Black', 20)
text2 = font2.render("CP:15", True, (0, 0, 0))

bx=20
by=100
pygame.mixer.music.load('Monopoly - NES - Auction.mp3')
pygame.mixer.music.play()
# Coördinaten vakken
vakjes = [[bx+470,by+10],   [bx+470,by+67.5],   [bx+470,by+105],    [bx+470,by+145],    [bx+470,by+180],
          [bx+470,by+240],  [bx+470,by+295],    [bx+470,by+330],    [bx+470,by+367.5],  [bx+470,by+405],
          [bx+470,by+470],  [bx+405,by+470],    [bx+367.5,by+470],  [bx+330,by+470],    [bx+295,by+470],
          [bx+240,by+470],  [bx+180,by+470],    [bx+145,by+470],    [bx+105,by+470],    [bx+67.5,by+470],
          [bx+5,by+470],    [bx+5,by+405],      [bx+5,by+367.5],    [bx+5,by+330],      [bx+5,by+295],
          [bx+5,by+240],    [bx+5,by+180],      [bx+5,by+145],      [bx+5,by+105],      [bx+5,by+67.5],
          [bx+5,by+5],      [bx+67.5,by+5],     [bx+105,by+5],      [bx+145,by+5],      [bx+180,by+5],
          [bx+240,by+5],    [bx+295,by+5],      [bx+330,by+5],      [bx+367.5,by+5],    [bx+405.5,by+5]]

vakjes2 = list(vakjes)

# pion positie
# pion positie
vak = 0
p2_vak = 10
p3_vak = 20
p4_vak = 30

SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))



while True:
    if vak >= 40:
        vak = vak - 40
    if vak >= 1 and vak <= 4:
        print ("leeg vakje")
        SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
        SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))
    if vak ==  5:
        print ("je bent in een gevecht!!")
        SFC1 = pygame.image.load(os.path.join('Cards/SFC/SFC1.png'))
        SFC = pygame.transform.scale(SFC1, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))
    if vak >= 6 and vak <= 14:
        print ("leeg vakje")
        SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
        SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))
    if vak == 15:
        print ("je bent in een gevecht!!")
        SFC2 = pygame.image.load(os.path.join('Cards/SFC/SFC2.png'))
        SFC = pygame.transform.scale(SFC2, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))
    if vak >= 16 and vak <= 24:
        print ("leeg vakje")
        SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
        SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))
    if vak == 25:
        print ("je bent in een gevecht!!")
        SFC3 = pygame.image.load(os.path.join('Cards/SFC/SFC3.png'))
        SFC = pygame.transform.scale(SFC3, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))
    if vak >= 26 and vak <= 34:
        print ("leeg vakje")
        SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
        SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))
    if vak == 35:
        print ("je bent in een gevecht!!")
        SFC4 = pygame.image.load(os.path.join('Cards/SFC/SFC4.png'))
        SFC = pygame.transform.scale(SFC4, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))
    if vak >= 36 and vak <= 40:
        print ("leeg vakje")
        SFCA = pygame.image.load(os.path.join('Cards/SFC/SFCA.png'))
        SFC = pygame.transform.scale(SFCA, (sfc_width, sfc_height))
        screen.blit(SFC, (sfc_x , sfc_y ))


    if vak >= 40:
        vakjes.extend(vakjes2)
    if p2_vak >= 11:
        vakjes.extend(vakjes2)
    if p3_vak >= 21:
        vakjes.extend(vakjes2)
    if p4_vak >= 31:
        vakjes.extend(vakjes2)

    roodPion_x = vakjes[vak] [0] or vakjes2[vak] [0]
    roodPion_y = vakjes[vak] [1] or vakjes2[vak] [1]

    blauw_x = vakjes[p2_vak] [0] or vakjes2[vak] [0]
    blauw_y = vakjes[p2_vak] [1] or vakjes2[vak] [1]
    #kruisje is aan
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("je hebt het spel afgesloten")
            pygame.QUIT
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            print ("X =",mouseX, "Y =",mouseY)

            if mouseX >= button_x and mouseY >= button_y and mouseX <= button_x+button_width and mouseY <= button_y+button_height:
                print("je hebt de Roll Dice knop gedrukt")

                font3 = pygame.font.Font(None, 36)
                text = font3.render("LP: "+str(lp), 1, (10, 10, 10))

                dice_choice = random.randint(1, 6)
                vak = vak + dice_choice
                p2_vak = p2_vak + dice_choice
                p3_vak = p3_vak + dice_choice
                p4_vak = p4_vak + dice_choice

                if dice_choice == 1:
                    D1 = pygame.image.load(ds)
                    D = pygame.transform.scale(D1, (dice_width, dice_height))
                    print ("je hebt 1 gegooid")


                if dice_choice == 2:
                    D2 = pygame.image.load(ds2)
                    D = pygame.transform.scale(D2, (dice_width, dice_height))
                    print ("je hebt 2 gegooid")


                if dice_choice == 3:
                    D3 = pygame.image.load(ds3)
                    D = pygame.transform.scale(D3, (dice_width, dice_height))
                    print ("je hebt 2 gegooid")

                if dice_choice == 4:
                    D4 = pygame.image.load(ds4)
                    D = pygame.transform.scale(D4, (dice_width, dice_height))

                    print ("je hebt 2 gegooid")

                if dice_choice == 5:
                    D5 = pygame.image.load(ds5)
                    D = pygame.transform.scale(D5, (dice_width, dice_height))
                    print ("je hebt 2 gegooid")

                if dice_choice== 6:
                    D2 = pygame.image.load(ds6)
                    D = pygame.transform.scale(D2, (dice_width, dice_height))
                    print ("je hebt 2 gegooid")


            if mouseX >= hulp_x and mouseY>= hulp_y  and mouseX<=(hulp_x+hulp_width) and mouseY<= (hulp_y+hulp_height):
                print("je hebt de instruction knop gevonden")
                import GameInstructions_Reuben

            if mouseX >=close_x and mouseY>= close_y and mouseX<=(close_x+close_width) and mouseY<= (close_y+close_height):
                print("je hebt de stop knop gevonden")


            if mouseX >=sound_x and mouseY>= sound_y and mouseX<=(sound_x+sound_width) and mouseY<= (sound_y+sound_height):
                geluid = random.randint(1,2)
                if geluid == 1:
                    Sound=pygame.image.load(sound)
                    Sound = pygame.transform.scale(Sound,(sound_width,sound_height))
                    pygame.mixer.music.play()
                if geluid == 2:
                    SoundOff=pygame.image.load(soundOff)
                    Sound = pygame.transform.scale(SoundOff,(soundOff_width,soundOff_height))
                    pygame.mixer.music.stop()





    # locaties op het spelbord
    screen.blit(BG, (0, 0))

    #screen.blit(lifepoints, (20, 15))
    screen.blit(gameboard, (bx, by))
    #screen.blit(CP, (300, 15))
    screen.blit(Sound,(sound_x,sound_y))
    screen.blit(Quit, (close_x, close_y))
    screen.blit(Help, (hulp_x, hulp_y))
    screen.blit(D, (dice_x,dice_y ))
    screen.blit(Roll, (button_x,button_y))
    screen.blit(SFC, (sfc_x , sfc_y ))
    screen.blit(Speler, (speler_x, speler_y ))
    screen.blit(red_Pion, (roodPion_x,roodPion_y))
    screen.blit(Score, (score_x , score_y ))
    screen.blit(Knop1, (knop1_x, knop1_y))
    screen.blit(Knop2, (knop2_x, knop2_y))
    screen.blit(Knop3, (knop3_x, knop3_y))
    screen.blit(Logo,(logo_x, logo_y))
    screen.blit(Blauw_Pion,(blauw_x, blauw_y))
    #screen.blit(Pion3,(Pion3_x, Pion3_y))

    screen.blit(text,
    (110 - text.get_width() // 2, 40 - text.get_height() // 2))


    screen.blit(text2,
    (320 - text.get_width() // 2, 40 - text.get_height() // 2))

    # Scherm vernieuwen bij verandering
    pygame.display.update()
    #zet de limite
    clock.tick(60)

#Afsluiten
pygame.quit()
quit()