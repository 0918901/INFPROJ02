import pygame
pygame.init()
screen = pygame.display.set_mode((1280,1024))
screen.fill((80, 200, 250))
pygame.display.set_caption('Survival game')
img=pygame.image.load('help.png')
done=False
pygame.display.flip()


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True