import pygame
import random
#from levels.npc import NPC
from player import create_frames_from_sheet, Player
#from puzzles.puzzle1 import Puzzle1

# pygame setup


def dijkstra_fight(screen, player, clock, running, dt):
    background_image = pygame.image.load("resources/Djikstrarena.png")
    screen.blit(background_image, (0, 0))  # Blit the map image onto the screen
    level_num = 1
    boss_image = pygame.image.load("resources\Djikstra.png")
    
    boss_direction_x = 0  # 1 is right, -1 is left, starts standing still
    boss_direction_y = 0 #random.choice([-1, 1])  # Randomly choose up or down
    
    boss_image_rect = boss_image.get_rect(center=(boss_image.get_width()/2, boss_image.get_height()/2))
    hitbox_width = boss_image_rect.width * 0.5  # Adjust as needed
    hitbox_height = boss_image_rect.height * 0.25  # Adjust as needed
    boss_hitbox = pygame.Rect(0, 0, hitbox_width, hitbox_height)
    boss_hitbox.center = boss_image_rect.center
    threat = False
    
    #npc = NPC("resources/algore.jpeg", screen, "Hello, my name is Al Gore Rhythm. I am here to explain the game to you. Would you like to learn about Queues?", tutorial)
    #font = pygame.font.Font(None, 36)
    #puzzle = Puzzle1(screen, font)\
    #player_pos = pygame.Vector2(screen.get_width() / 2, 600)

    player.rect.y = 600
    #dialogue_finished = False
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(background_image, (0, 0))   
        if (boss_image_rect.right >= screen.get_width()) & threat == True:
            boss_direction_x = -1
        elif (boss_image_rect.left <= 0) & threat == True:
            boss_direction_x = 1

        if (boss_image_rect.bottom >= screen.get_height()) & threat == True:
            boss_direction_y = -1
        elif (boss_image_rect.top <= 0) & threat == True:
            boss_direction_y = 1

        # Move the boss around
        boss_image_rect.x += 5 * boss_direction_x
        boss_image_rect.y += 5 * boss_direction_y  # Adjust the value as needed
        boss_hitbox.center = (boss_image_rect.centerx, boss_image_rect.centery + 50)  # Adjust as needed

        screen.blit(boss_image, boss_hitbox)
        pygame.draw.rect(screen, (255, 0, 0), boss_hitbox, 2)  # Draw a red border around the hitbox


        if player.rect.colliderect(boss_hitbox):
            return 1
        

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
       # accumulated_time += dt

       # if accumulated_time > frame_time:
        #    accumulated_time -= frame_time
         #   current_frame = (current_frame + 1) % len(frames)  # Cycle through the frames

    return int(1)



