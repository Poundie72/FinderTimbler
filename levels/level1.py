import pygame
from npc import NPC

# pygame setup

def run_level1(screen, player, clock, running, dt):
    npc = NPC("resources/algore.jpeg", screen, "Hello, I am an NPC. I am here to explain the game to you.")
    
    player_image = pygame.image.load("resources/algore.jpeg")
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    
    dialogue_finished = False
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # If the player interacts with the NPC, start the dialogue
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Assuming space is the interaction key
                    if npc.interact():
                        # If the player doesn't want to repeat the explanation, start the puzzle
                        puzzle1.start()
                        
        screen.blit(player_image, player_pos)
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        # Define the color and thickness of the border
        border_color = (0, 0, 0)  # Black
        border_thickness = 10  # 10 pixels

        # Get the size of the window
        window_size = screen.get_size()

        # Draw the border
        pygame.draw.rect(screen, border_color, pygame.Rect((0, 0), window_size), border_thickness)


        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and player_pos.y > 50:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s] and player_pos.y < screen.get_height() -50:
            player_pos.y += 300 * dt
        if keys[pygame.K_a] and player_pos.x > 50:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d] and player_pos.x < screen.get_width() - 50:
            player_pos.x += 300 * dt

        screen.blit(npc.image, npc.rect)
        
        # After drawing everything, flip the display
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    return int(1)
