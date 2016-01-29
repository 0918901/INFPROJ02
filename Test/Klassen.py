import pygame
from pygame.locals import *
from sys import  exit


class Beeld_scherm:
    def __init__( self, lengte, brede, achtergrond ):
        self.Lengte = lengte
        self.Brede = brede
        self.Achtergrond = achtergrond

class Pionnen:
    def __init__(self, afbeelding, startpositie_x, startpositie_y, pion_width, pion_height ):
        self.Afbeelding = afbeelding
        self.Startpositie_x = startpositie_x
        self.Startpositie_y = startpositie_y
        self.Pion_height = pion_height
        self.Pion_width = pion_width


pion_rood = Pionnen ('Player/Piece/Rood.png', 500, 300, 55, 55 )
pion_geel = Pionnen ('Player/Piece/Geel.png', 350, 512, 55, 55 )
pion_blauw = Pionnen ('Player/Piece/Blauw.png', 450, 450, 55, 55 )

eerste_pion = pygame.image.load (pion_rood.Afbeelding)
eerste_pion_grote = pygame.transform.scale(eerste_pion, (pion_rood.Pion_height,pion_rood.Pion_width))

tweede_pion = pygame.image.load (pion_geel.Afbeelding)
tweede_pion = pygame.transform.scale(tweede_pion, (pion_geel.Pion_height,pion_geel.Pion_width))

derde_pion = pygame.image.load (pion_blauw.Afbeelding)
derde_pion = pygame.transform.scale(derde_pion, (pion_blauw.Pion_height,pion_blauw.Pion_height))


screen = Beeld_scherm ( 1024, 728,'Main/Game/wood.jpg')
screen = pygame.display.set_mode          ((screen.Lengte, screen.Brede))






while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(eerste_pion_grote, (pion_rood.Startpositie_y, pion_rood.Startpositie_x))
    screen.blit(tweede_pion, (pion_geel.Startpositie_y, pion_geel.Startpositie_x))
    screen.blit(derde_pion, (pion_blauw.Startpositie_y, pion_blauw.Startpositie_x))

    pygame.display.update()



