__author__ = 'quinnjansen'

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Animation")

white = (255,255,255)

clock = pygame.time.Clock()

# winner sprites
bg = 'Main/Game/wood.jpg'

w1 = pygame.image.load("Main/Game/winner-text-Red.png")
w2 = pygame.image.load("Main/Game/winner-text-Red.png")


screen = pygame.display.set_mode((1024, 768))
BG = pygame.image.load(bg).convert()

screen.blit(BG, (0, 0))

marioCurrentImage = 1

gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):

            gameLoop=False

    screen.fill(white)

    if (marioCurrentImage==1):

        screen.blit(w1, (10,10))

    if (marioCurrentImage==2):

        screen.blit(w2, (10,10))


    if (marioCurrentImage==2):

        marioCurrentImage=1

    else:

        marioCurrentImage+=1;

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
