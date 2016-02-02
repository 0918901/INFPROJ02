__author__ = 'quinnjansen'
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Animation")
terugNaarMenu               = 'Main/instructions/Kruis2.png'
tryAgain_knop               = 'Main/Game/tryagain_button.png'
# spelbord sprites
bs = 'Main/Game/test spelbord.png'

clock = pygame.time.Clock()

#Grootte van terugKnop aangeven
RodeKnopje_width        = 30
RodeKnopje_height       = 25

tk_x = 918
tk_y = 49

#Grootte van tryAgainknop aangeven
tryKnopje_width        = 100
try_height             = 50

try_x = 755
try_y = 440

#Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
terug_knop = pygame.image.load(terugNaarMenu)
terug_knop = pygame.transform.scale(terug_knop, (RodeKnopje_width , RodeKnopje_height))

#Play knop aanroepen en vervormen naar aangegeven grootte [boven aangegeven](regel 18-19)
tryy = pygame.image.load(tryAgain_knop)
tryy = pygame.transform.scale(tryy, (tryKnopje_width , try_height))


w1 = pygame.image.load("Main/Game/winRandBlue.jpg")
w1 = pygame.transform.scale(w1, (850, 600))
w2 = pygame.image.load("Main/Game/winRandRed.jpg")
w2 = pygame.transform.scale(w2, (850, 600))


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

        screen.blit(w1, (100,50))
        screen.blit(terug_knop,(tk_x,tk_y))
        screen.blit(tryy,(try_x,try_y))

    if (winnerCurrentImage==2):

        screen.blit(w2, (100,50))
        screen.blit(terug_knop,(tk_x,tk_y))
        screen.blit(tryy,(try_x,try_y))

    if (winnerCurrentImage==2):

        winnerCurrentImage=1

        screen.blit(terug_knop,(tk_x,tk_y))
        screen.blit(tryy,(try_x,try_y))
    else:

        winnerCurrentImage+=1;

    pygame.display.flip()

    clock.tick(5)

pygame.quit()
