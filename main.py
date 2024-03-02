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
    screen.fill("purple")
    # Define the color and thickness of the border
    border_color = (0, 0, 0)  # Black
    border_thickness = 10  # 10 pixels

    # Get the size of the window
    window_size = screen.get_size()

    # Draw the border
    pygame.draw.rect(screen, border_color, pygame.Rect((0, 0), window_size), border_thickness)
    # Define the color and size of the doors
    door_color = (165, 42, 42)  # Brown
    door_width = 50  # 50 pixels
    door_height = 200  # 200 pixels

    # Get the size of the window
    window_width, window_height = screen.get_size()

    # Calculate the positions of the doors
    left_door_x = 0
    right_door_x = window_width - door_width
    side_door_y = window_height /2 - door_height /2
    top_door_y = 0
    bottom_door_y = window_height - door_width
    middle_door_x = window_width /2 - door_width /2

    # Draw the doors
    pygame.draw.rect(screen, door_color, pygame.Rect((left_door_x, side_door_y), (door_width, door_height)))
    pygame.draw.rect(screen, door_color, pygame.Rect((right_door_x, side_door_y), (door_width, door_height)))  
    pygame.draw.rect(screen, door_color, pygame.Rect((middle_door_x, top_door_y), (door_height, door_width)))
    pygame.draw.rect(screen, door_color, pygame.Rect((middle_door_x, bottom_door_y), (door_height, door_width)))  
 

    player_image = pygame.image.load("resources/algore.jpeg")
    screen.blit(player_image, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos.y > 50:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] and player_pos.y < screen.get_height() -50:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] and player_pos.x > 50:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] and player_pos.x < screen.get_width() - 50:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()