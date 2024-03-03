import pygame
from player import Player


# pygame setup

def run_nodePuzzle(screen, player, clock, running, dt):
    tutorial_image = pygame.image.load("resources/node_tutorial.jpg")
    screen.blit(tutorial_image, (0, 0))  # Blit the map image onto the screen
    keys = pygame.key.get_pressed()

    #player = player
    #player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    
    #dialogue_finished = False
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        
        if keys[pygame.K_SPACE]:  # Replace with the key you want to use
            puzzle_image = pygame.image.load("resources/nodePuzzle.jpg") 
            screen.blit(puzzle_image, (0, 0))

        if keys[pygame.K_1]:
            font = pygame.font.Font(None, 36) 
            text = font.render("WRONG!!", True, (255, 0, 0))  # Create a surface with the text
            screen.blit(text, (0, 600))  # Draw the text to the screen at position (100, 100)
        if keys[pygame.K_2]:
            return int(1)
        if keys[pygame.K_3]: #correct answer
            font = pygame.font.Font(None, 36) 
            text = font.render("WRONG!!", True, (255, 0, 0))  # Create a surface with the text
            screen.blit(text, (0, 600))  # Draw the text to the screen at position (100, 100)
       
                
        #screen.blit(puzzle_image, (0, 0))
        #image = pygame.image.load("resources/alGoreRhythm.jpeg")
        #screen.blit(image, (640, 200))
        #goreLoc = pygame.Rect(640, 200, 128, 128)
        
            # If the player interacts with the NPC, start the dialogue

        keys = pygame.key.get_pressed()
        #player.update(dt, keys)
        #screen.blit(player.image, player.rect)
        

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


        


        #screen.blit(npc.image, npc.rect)
        
        # After drawing everything, flip the display
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    return int(1)