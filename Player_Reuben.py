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

class Startmenu:
    def __init__(self, image, width, height, pos_x, pos_y):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Instructiemenu:
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

class Knoppen:
    def __init__(self, image, width, height, pos_x, pos_y, link):
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y
        self.Link   =   link

class Pion:
    def __init__(self, kleur, image, width, height, pos_x, pos_y):
        self.Kleur  =   kleur
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Speler:
    def __init__(self, naam, image, width, height, pos_x, pos_y):
        self.Naam  =    naam
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Dobbelsteen:
    def __init__(self, ogen, image, width, height, pos_x, pos_y):
        self.Ogen  =    ogen
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class SuperFighter:
    def __init__(self, nummer, image, width, height, pos_x, pos_y):
        self.Nummer  =  nummer
        self.Image  =   image
        self.Width  =   width
        self.Height =   height
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Scorekaart:
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

class Fightvak:
    def __init__(self, nummer, pos_x, pos_y):
        self.Nummer  =  nummer
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Loopvak:
    def __init__(self, nummer, pos_x, pos_y):
        self.Nummer  =  nummer
        self.Pos_x  =   pos_x
        self.Pos_y  =   pos_y

class Startspelmenu:
    def __init__(self, image, width, height, pos_x, pos_y, link):
        self.Scherm         =   Scherm      (width, height)
        self.Achtergrond    =   Achtergrond (image, width, height, pos_x, pos_y)
        self.Startmenu      =   Startmenu   (image, width, height, pos_x, pos_y)
        self.Knoppen        =   Knoppen     (image, width, height, pos_x, pos_y)

scherm      = Scherm        (int(1024), int(768))
achtergrond = Achtergrond   ('Main/Menu/bg.jpg', scherm.Width, scherm.Height, 0, 0)

screen = pygame.display.set_mode((scherm.Width, scherm.Height))
background = pygame.image.load(achtergrond)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
