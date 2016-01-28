import pygame
import random
from pygame.locals import *
from sys import exit

# afbeeldingen locaties aangeven
bg = 'Main/Game/wood.jpg'
board = 'Main/Game/board.png'

pygame.init()
sound = pygame.mixer.Sound()
sound.play()
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
        # anders stop de pygame
        if event.type == QUIT:
            # detect sluitknop
            pygame.quit()
            # sluit de pygame
            exit()








    # locaties op het spelbord
    screen.blit(BG, (0, 0))
    screen.blit(gameboard, (20, 100))


    # Scherm vernieuwen bij verandering
    pygame.display.update()