import pygame
from .npc import NPC
from player import Player
from puzzles.puzzle1 import Puzzle1

# pygame setup

def run_level1(screen, player, clock, running, dt, background_image):
    background_image = pygame.image.load("resources/undamaged.jpeg")
    screen.blit(background_image, (0, 0))  # Blit the map image onto the screen
    tutorial = pygame.image.load("resources/fire.jpeg")  # Load the tutorial image

    npc = NPC("resources/algore.jpeg", screen, "Hello, my name is Al Gore Rhythm. I am here to explain the game to you. Would you like to learn about Queues?", tutorial)
    font = pygame.font.Font(None, 36)
    puzzle = Puzzle1(screen, font)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    
    dialogue_finished = False
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(background_image, (0, 0))

        if player.rect.colliderect(npc.rect):
            print("Collision detected")
            npc.draw_dialogue()
            keys = pygame.key.get_pressed()  # Get the current state of the keys
            if keys[pygame.K_1]:
                print("1 key pressed")
                npc.tutorial_active = True
            elif keys[pygame.K_0]:
                print("0 key pressed")
                npc.tutorial_active = False
                            

            # If the player interacts with the NPC, start the dialogue

        keys = pygame.key.get_pressed()
        player.update(dt, keys)
        screen.blit(player.image, player.rect)
        

        screen.blit(npc.image, npc.rect)

                        
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


        screen.blit(npc.image, npc.rect)
        
        # After drawing everything, flip the display
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    return int(1)
