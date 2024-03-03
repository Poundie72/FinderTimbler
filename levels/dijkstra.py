import pygame
#from levels.npc import NPC
from player import create_frames_from_sheet, Player
#from puzzles.puzzle1 import Puzzle1

# pygame setup


def dijkstra_fight(screen, player, clock, running, dt):
    background_image = pygame.image.load("resources/undamaged.jpeg")
    screen.blit(background_image, (0, 0))  # Blit the map image onto the screen
    tutorial = pygame.image.load("resources/fire.jpeg")  # Load the tutorial image
    tutorial_complete = 0
    level_num = 1
    


    # Boss setup
    boss_image = pygame.image.load("resources/.png")
    boss_rect = boss_image.get_rect()
    boss_pos = pygame.Vector2(screen.get_width() / 2, 200)
    boss_speed = 5
    boss_direction = 1  # 1 for moving right, -1 for moving left

    while running:
        # ...

        # Update boss position
        boss_pos.x += boss_speed * boss_direction

        # Check if boss hits the screen edges
        if boss_pos.x <= 0 or boss_pos.x >= screen.get_width() - boss_rect.width:
            boss_direction *= -1  # Reverse direction

        # Draw boss on screen
        screen.blit(boss_image, boss_pos)

        # ...

        pygame.display.flip()

        # ...

    #npc = NPC("resources/algore.jpeg", screen, "Hello, my name is Al Gore Rhythm. I am here to explain the game to you. Would you like to learn about Queues?", tutorial)
    #font = pygame.font.Font(None, 36)
    #puzzle = Puzzle1(screen, font)

    player_pos = pygame.Vector2(screen.get_width() / 2, 600)

    player.rect.y = 600
    #dialogue_finished = False
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(background_image, (0, 0))
        screen.blit(frames[current_frame], (550, 100))        
        goreLoc = pygame.Rect(640, 200, 128, 128)

        if player.rect.colliderect(goreLoc) and tutorial_complete == 0:
            font = pygame.font.Font(None, 36) 
            text = font.render("Hello! Would you like to learn about queues? Type 1 for yes and 0 for no", True, (255, 255, 255))  # Create a surface with the text
            screen.blit(text, (100, 600))  # Draw the text to the screen at position (100, 100)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        tutorial_complete = 1
                        return 1
                    if event.key == pygame.K_0:
                        player.rect.y += 100

        if player.rect.colliderect(goreLoc) and tutorial_complete == 1:
            font = pygame.font.Font(None, 36)  # Create a font object
            text = font.render("You wanna learn about queues again? Type 1 for yes and 0 for no", True, (255, 255, 255))  # Create a surface with the text
            screen.blit(text, (100, 100))  # Draw the text to the screen at position (100, 100)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                if event.key == pygame.K_0:
                    player.rect.y += 100


                            

            # If the player interacts with the NPC, start the dialogue

        keys = pygame.key.get_pressed()
        player.update(dt, keys)
        screen.blit(player.image, player.rect)
        

        #screen.blit(npc.image, npc.rect)

                        
        #screen.blit(player_image, player_pos)
        # fill the screen with a color to wipe away anything from last frame

        #screen.fill("black")
        # Define the color and thickness of the border
        border_color = (0, 0, 0)  # Black
        border_thickness = 10  # 10 pixels

        # Get the size of the window
        window_size = screen.get_size()

        # Draw the border
        pygame.draw.rect(screen, border_color, pygame.Rect((0, 0), window_size), border_thickness)


        keys = pygame.key.get_pressed()


        #screen.blit(npc.image, npc.rect)
        
        # After drawing everything, flip the display
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        accumulated_time += dt

        if accumulated_time > frame_time:
            accumulated_time -= frame_time
            current_frame = (current_frame + 1) % len(frames)  # Cycle through the frames

    return int(1)
