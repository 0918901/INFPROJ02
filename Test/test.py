import random

def dice_sim(die_size, rolls):

    results = 0
    dice_sum = 0

    for i in range(0,rolls):
        results = random.randint(1,die_size)
        print("Die %d rolled %d." % (i+1,results))
        dice_sum += results

    print("Total of %d dice rolls is: %d" % (rolls,dice_sum))

    return None

dice_sim(5,3)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('speler')

black = (0,0,0)
white = (50,255,255)
#foto laden
carImg = pygame.image.load('Player/Faces/S1.png')
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.25)
y = (display_height * 0.8)
x_change = 0
y_change = 0
    x+=x_change
    y+=y_change
    gameDisplay.fill(white)
    car(x,y)