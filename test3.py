import pygame
import time
import random

pygame.init()


display_width = 1024
display_height = 768

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (255,0,0)

car_width = 70

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('Player/Faces/S1.png')
p1=pygame.image.load('Main/Game/wood.jpg')
bg = 'Main/Menu/startmenu.jpg'
#gameIcon = pygame.image.load('carIcon.png')

#pygame.display.set_icon(gameIcon)

pause = False
#crash = True

#def car(x,y):
    #gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('arial',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    #pygame.display.update()

    #time.sleep(2)

    #game_loop()




    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Play Again",230,590,180,100,green,bright_green,game_loop)
        button("Quit",650,590,180,100,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("arial",50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("arial",200)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)

        BG = pygame.image.load(bg)
        BG = pygame.transform.scale(BG,(display_width,display_height))

    # locaties op het spelbord
        gameDisplay.blit(BG, (0, 0))
        button("Continue",230,590,180,100,green,bright_green,unpause)
        button("Quit",650,590,180,100,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("arial",200)
        TextSurf, TextRect = text_objects("Survival", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play!",230,590,180,100,green,bright_green,game_loop)
        button("Quit",650,590,180,100,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    pygame.mixer.music.load('Monopoly - NES - Auction.mp3')
    pygame.mixer.music.play(0)
    #x = (display_width * 0.45)
    #y = (display_height * 0.8)

    #x_change = 0

    #thing_startx = random.randrange(0, display_width)
    #thing_starty = -600
    #thing_speed = 4
    #thing_width = 100
    #thing_height = 100

    #thingCount = 1

    #dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_LEFT:
                    #x_change = -5
                #if event.key == pygame.K_RIGHT:
                    #x_change = 5
                #if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()


            #if event.type == pygame.KEYUP:
                #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
