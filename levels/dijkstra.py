import pygame
import random
#from levels.npc import NPC
from player import create_frames_from_sheet, Player
#from puzzles.puzzle1 import Puzzle1

# pygame setup


def dijkstra_fight(screen, player, clock, running, dt):
    background_image = pygame.image.load("resources/Djikstrarena.png")
    screen.blit(background_image, (600, 0))  # Blit the map image onto the screen
    level_num = 1
    #boss_image = pygame.image.load("resources/Djikstra.png")

    image_sheet = pygame.image.load("resources/DjikstraShuffle.png")
    frames = create_frames_from_sheet(image_sheet, 256, 256, 11)
    current_frame = 0
    frame_time = 0.1  # Change frames every 0.1 seconds
    accumulated_time = 0
    
    boss_direction_x = 0  # 1 is right, -1 is left, starts standing still
    boss_direction_y = 0 #random.choice([-1, 1])  # Randomly choose up or down
    
    boss_image_rect = frames[current_frame].get_rect(center=(frames[current_frame].get_width()/2, frames[current_frame].get_height()/2))
    hitbox_width = boss_image_rect.width  # Adjust as needed
    hitbox_height = boss_image_rect.height   # Adjust as needed
    boss_hitbox = pygame.Rect(0, 0, hitbox_width, hitbox_height)
    boss_hitbox.center = boss_image_rect.center
    threat = False 
    
    #npc = NPC("resources/algore.jpeg", screen, "Hello, my name is Al Gore Rhythm. I am here to explain the game to you. Would you like to learn about Queues?", tutorial)
    #font = pygame.font.Font(None, 36)f
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
        if player.rect.colliderect(boss_hitbox) and threat == False:
            threat = True
            player.rect.x = 800
            player.rect.y = 500
            font = pygame.font.Font(None, 48)
            text7 = font.render("I AM THE MIGHTY DIJKSTRA", True, (255, 0, 0))
            text_rect7 = text7.get_rect(center=(screen.get_width() / 2 , screen.get_height() / 2 - 50))
            screen.blit(text7, text_rect7)
            text = font.render("YOU DARE ENTER MY LAYER?", True, (255, 0, 0))
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
            screen.blit(text, text_rect)
            text1 = font.render("PREPARE TO TAKE THE SHORTEST PATH TO DOOM!!!", True, (255, 0, 0))
            text_rect1 = text.get_rect(center=(screen.get_width() / 2 - 200, screen.get_height() / 2 + 50))
            screen.blit(text1, text_rect1)
            #pygame.time.delay(7000)  # Delay for 7 seconds

            pygame.display.flip()
            pygame.time.delay(10000)  # Delay for 10 seconds
            screen.fill((0, 0, 0))  # Fill the screen with black to remove the text
            pygame.display.flip()
            player = player

        if player.rect.colliderect(boss_hitbox) and threat == True:
            text2 = font.render("GET GOT!!!", True, (255, 0, 0))
            text_rect2 = text.get_rect(center=(screen.get_width() / 2 - 200, screen.get_height() / 2 + 50))
            screen.blit(text2, text_rect2)
            player = player
            if player.rect.x > 640:
                player.rect.x -= 450
            elif player.rect.x < 640:
                player.rect.x += 450
            #pygame.time.delay(2000)  # Delay for 7 seconds

            
            pygame.display.flip()
            pygame.time.delay(1000)  # Delay for 10 seconds
            screen.fill((0, 0, 0))  # Fill the screen with black to remove the text
            pygame.display.flip()
            player = player
        
        

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

        screen.blit(frames[current_frame], boss_hitbox)
        #pygame.draw.rect(screen, (255, 0, 0), boss_hitbox, 2)  # Draw a red border around the hitbox


        #if player.rect.colliderect(boss_hitbox):
            #return 1
        

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
            current_frame = (current_frame + 1) % len(frames)  
       # accumulated_time += dt

       # if accumulated_time > frame_time:
        #    accumulated_time -= frame_time
         #   current_frame = (current_frame + 1) % len(frames)  # Cycle through the frames

    return int(1)



