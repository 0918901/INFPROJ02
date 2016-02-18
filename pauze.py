import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1024, 768)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

bg = 'Main/Menu/startmenu.jpg'


BG=pygame.image.load(bg)
BG=pygame.transform.scale(BG,(size))
# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #screen.fill(RED)
        screen.blit(BG,(0,0))
    # --- Game logic should go here
        if event.key == pygame.MOUSEBUTTONDOWN():
            (mouseX,mouseY) = pygame.mouse.get_pos()
            print('je hebt gedrukt')

    # --- Screen-clearing code goes here
    pygame.draw.rect(screen, RED,(180,580,250,100))
    pygame.draw.rect(screen, RED,(580,580,250,100))
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.