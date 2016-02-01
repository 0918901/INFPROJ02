import pygame
import random
from pygame.locals import *
from sys import exit

# afbeeldingen locaties aangeven
bg = 'Main/Game/wood.jpg'
board = 'Main/Game/board.png'

pygame.init()
#sound = pygame.mixer.Sound()
#sound.play()
font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Hello, World", True, (0, 128, 0))
# grootte van het scherm aangeven
screen = pygame.display.set_mode((1024, 768))
BG = pygame.image.load(bg).convert()
# achtergrondkleurscreen.fill((80, 200, 250))

# Laden van afbeelding
spelbord = pygame.image.load(board)

# Hervormen van de afbeelding
gameboard = pygame.transform.scale(spelbord, (500, 500))


while True:
    # ophalen van pygame event
    for event in pygame.event.get():

        screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))# anders stop de pygame
        if event.type == QUIT:
            # detect sluitknop
            pygame.quit()
            # sluit de pygame
            exit()



pygame.display.flip()





    # locaties op het spelbord
    screen.blit(BG, (0, 0))
    screen.blit(gameboard, (20, 100))


    # Scherm vernieuwen bij verandering
    pygame.display.update()