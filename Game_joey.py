import pygame
pygame.init()
screen = pygame.display.set_mode((1280,1024))
screen.fill((80, 200, 250))
background_position = [50, 50]
pygame.display.set_caption('Survival game')
img = pygame.image.load('Button/GM/help.png')
img =  pygame.transform.scale(img,(40,40))
screen.blit(img,(1000,300))
pygame.display.flip()

done=False


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        pygame.display.update()