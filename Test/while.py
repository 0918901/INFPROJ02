import os

import pygame
from pygame.constants import QUIT

screen = pygame.display.set_mode((1024, 768))

sfc_height          =   300
sfc_width           =   200
sfc_x               =   550
sfc_y               =   20


def kaarten():
    card = 0
    while (card < 9):
        card = card + 1


card = 0
while (card < 9):
    print ("Dit is kaart nummer", card),card
    card = card + 1
    kaarten()

print("de kaarten zijn op!")

while True:
    #ophalen van pygame event
    for event in pygame.event.get():
        #anders stop de pygame
        if event.type == QUIT:
            #detect sluitknop
            pygame.quit()
            #sluit de pygame
            exit()

    screen.blit(SFC, (sfc_x , sfc_y ))