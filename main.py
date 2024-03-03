# Example file showing a circle moving on screen
import pygame
from player import Player
from levels.test import main as run_level1

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player = Player("resources/testImg.jpeg", screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    background_image = pygame.image.load("resources/allDoorsOpen.jpeg")
    screen.blit(background_image, (0, 0))
    #screen.fill((255, 255, 255))
    # Define the color and thickness of the border
    
    border_color = (0, 0, 0)  # Black
    border_thickness = 10  # 10 pixels

    # Get the size of the window
    window_size = screen.get_size()

    # Draw the border
    pygame.draw.rect(screen, border_color, pygame.Rect((0, 0), window_size), border_thickness)

    #create doors
    queueDoor = pygame.Rect(150, 90, 180, 170)
    if player.rect.colliderect(queueDoor):
         level_result = run_level1()
         print("Level result:", level_result)


    # Get the size of the window
    window_width, window_height = screen.get_size()


    # Draw the player as a 128px square
    #player_image = pygame.image.load("resources/algore.jpeg")
    #screen.blit(player_image, player_pos)
    
    keys = pygame.key.get_pressed()
    player.update(dt, keys)
    player.draw(screen)
    
    # Commenting the chunk of code
    """
    if player.rect.top == 50 and (player.rect.centerx > 540 and player.rect.centerx < 740): #Left door
        print("Level top")
    if player.rect.bottom == screen.get_height() - 50 and (player.rect.centerx > 540 and player.rect.centerx < 740): #Right door
        print("Level bottom")
    if player.rect.left == 50 and (player.rect.centery > 10 and player.rect.centery < 200): #Right door
        print("Level left")
    if player.rect.right == 50 and (player.rect.centery > 10 and player.rect.centery < 200): #Right door
        print("Level right")
    """

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()