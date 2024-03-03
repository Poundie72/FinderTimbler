# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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


    # Get the size of the window
    window_width, window_height = screen.get_size()

   
 
    
    # Draw the player as a 128px square
    player_size = 128
    player_color = (255, 255, 0)  # Yellow
    player_rect = pygame.Rect(player_pos.x - player_size/2, player_pos.y - player_size/2, player_size, player_size)
    pygame.draw.rect(screen, player_color, player_rect)

    #player_image = pygame.image.load("resources/algore.jpeg")
    #screen.blit(player_image, player_pos)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y > 50: # if pos = 50 && ,initiate level
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] and player_pos.y < screen.get_height() -50:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] and player_pos.x > 50:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] and player_pos.x < screen.get_width() - 50:
        player_pos.x += 300 * dt

    if player_pos.y == 50 and (player_pos.x > 540 and player_pos.x < 740): #Left door
        print("Level top")
    if player_pos.y == screen.get_height() - 50 and (player_pos.x > 540 and player_pos.x < 740): #Right door
        print("Level bottom")
    if player_pos.y == 50 and (player_pos.y > 10 and player_pos.y < 200): #Right door
        print("Level left")
    if player_pos.y == 50 and (player_pos.y > 10 and player_pos.y < 200): #Right door
        print("Level right")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()