# Example file showing a circle moving on screen
import pygame
from player import Player, create_frames_from_sheet
from levels.level1 import run_level1
from levels.dijkstra import dijkstra_fight
from levels.nodeLevel import run_nodeLevel


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
numcompleted = 0
levels_completed = [False] * 8


# Load the sprite sheets
image_sheet_up = pygame.image.load("resources/DrFinderBack.png")
image_sheet_down = pygame.image.load("resources/DrFinderFWalk.png")
image_sheet_left = pygame.image.load("resources/DrFinderLWalk.png")
image_sheet_right = pygame.image.load("resources/DrFinderSWalk.png")

# Create frames from the sprite sheets
frames_down = create_frames_from_sheet(image_sheet_down, 128, 128, 10)
frames_left = create_frames_from_sheet(image_sheet_left, 128, 128, 6)
frames_right = create_frames_from_sheet(image_sheet_right, 128, 128, 7)

# Create the frames list
frames_list = [image_sheet_up, frames_down, frames_left, frames_right]

player = Player(frames_list, screen)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    # fill the screen with a color to wipe away anything from last frame
    #This determines which background to use and which door rectangles to create for collision detection
                #1-queueDoor = pygame.Rect(150, 90, 180, 170)
                #2-bubbleDoor = pygame.Rect(180, 610, 230, 110)
                #2-nodeDoor = pygame.Rect(820, 610, 230, 110)
                #4-edgeDoor = pygame.Rect(940, 90, 210, 170)
                #5-pqDoor  = pygame.Rect(0, 300, 100, 230)
                #6-graphDoor = pygame.Rect(1190, 300, 190, 240)
                #7-bfsDoor = pygame.Rect(520, 20, 220, 140)
                #8-dijkstraDoor = pygame.Rect(560, 560, 130, 130)
    
    #levels_completed[1] = True
    #alevels_completed[1] = True

    #print("completed result:", numcompleted)
    

    if numcompleted > 6:
        background_image = pygame.image.load("resources/allDoorsOpen.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = pygame.Rect(0, 300, 100, 230)
        graphDoor = pygame.Rect(1190, 300, 190, 240)
        bfsDoor = pygame.Rect(520, 20, 220, 140)
        dijkstraDoor = pygame.Rect(560, 560, 130, 130)
    elif numcompleted == 6:
        background_image = pygame.image.load("resources/3.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = pygame.Rect(0, 300, 100, 230)
        graphDoor = pygame.Rect(1190, 300, 190, 240)
        bfsDoor = pygame.Rect(520, 20, 220, 140)
        dijkstraDoor = None
    elif levels_completed[0] and levels_completed[1] and levels_completed[2] and levels_completed[3]:
        background_image = pygame.image.load("resources/2.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = pygame.Rect(0, 300, 100, 230)
        graphDoor = pygame.Rect(1190, 300, 190, 240)
        bfsDoor = None
        dijkstraDoor = None
    elif levels_completed[0] and levels_completed[1] and numcompleted < 5:
        background_image = pygame.image.load("resources/1b.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = pygame.Rect(0, 300, 100, 230)
        bfsDoor = None
        dijkstraDoor = None
    elif levels_completed[2] and levels_completed[3] and (levels_completed[0] == 0 or levels_completed[1] == 0):
        background_image = pygame.image.load("resources/1a.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        graphDoor = pygame.Rect(1190, 300, 190, 240)
        pqDoor  = None
        bfsDoor = None
        dijkstraDoor = None
    else:
        background_image = pygame.image.load("resources/0_begin.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = None
        graphDoor = None
        bfsDoor = None
        dijkstraDoor = None
        






    screen.blit(background_image, (0, 0))
    #screen.fill((255, 255, 255))
    # Define the color and thickness of the border
    
    border_color = (0, 0, 0)  # Black
    border_thickness = 10  # 10 pixels

    # Get the size of the window
    window_size = screen.get_size()

    # Draw the border
    pygame.draw.rect(screen, border_color, pygame.Rect((0, 0), window_size), border_thickness)

    #enter door-collision detection


    if player.rect.colliderect(queueDoor):
        level_result = run_level1(screen, player, clock, running, dt)
        player.rect.y = 300
        player.rect.x = 550
        if level_result == 1:
             levels_completed[0] = True
        numcompleted = 0
        for level in levels_completed:
            if level == True:
                numcompleted += 1
        
        
        print("completed result:", numcompleted) 

    if player.rect.colliderect(bubbleDoor):
            level_result = run_level1(screen, player, clock, running, dt)
            player.rect.y = 300
            player.rect.x = 550
            if level_result == 1:
                levels_completed[1] = True
            numcompleted = 0
            for level in levels_completed:
                if level == True:
                    numcompleted += 1
            print("Level result:", level_result)

    if player.rect.colliderect(nodeDoor):
            level_result = run_nodeLevel(screen, player, clock, running, dt)
            player.rect.y = 300
            player.rect.x = 550
            if level_result == 1:
                levels_completed[2] = True
            numcompleted = 0
            for level in levels_completed:
                if level == True:
                    numcompleted += 1
            print("Level result:", level_result)

    if player.rect.colliderect(edgeDoor):
            level_result = run_level1(screen, player, clock, running, dt)
            player.rect.y = 300
            player.rect.x = 550
            if level_result == 1:
                levels_completed[3] = True
            numcompleted = 0
            for level in levels_completed:
                if level == True:
                    numcompleted += 1
            print("Level result:", level_result)

    if pqDoor != None:
        if player.rect.colliderect(pqDoor):
                level_result = run_level1(screen, player, clock, running, dt)
                player.rect.y = 300
                player.rect.x = 550
                if level_result == 1:
                    levels_completed[4] = True
                numcompleted = 0
                for level in levels_completed:
                    if level == True:
                        numcompleted += 1
                print("Level result:", level_result)

    if graphDoor != None:
        if player.rect.colliderect(graphDoor):
                level_result = run_level1(screen, player, clock, running, dt)
                player.rect.y = 300
                player.rect.x = 550
                if level_result == 1:
                    levels_completed[5] = True
                numcompleted = 0
                for level in levels_completed:
                    if level == True:
                        numcompleted += 1
                print("Level result:", level_result)

    if bfsDoor != None:
        if player.rect.colliderect(bfsDoor):
                level_result = run_level1(screen, player, clock, running, dt)
                player.rect.y = 300
                player.rect.x = 550
                if level_result == 1:
                    levels_completed[6] = True
                numcompleted = 0
                for level in levels_completed:
                    if level == True:
                        numcompleted += 1
                print("Level result:", level_result)

    if dijkstraDoor != None:               
        if player.rect.colliderect(dijkstraDoor):
                level_result = dijkstra_fight(screen, player, clock, running, dt)
                player.rect.y = 300
                player.rect.x = 550
                if level_result == 1:
                    levels_completed[7] = True
                numcompleted = 0
                for level in levels_completed:
                    if level == True:
                        numcompleted += 1
                print("Level result:", level_result)
   
    
    if numcompleted > 6:
        background_image = pygame.image.load("resources/allDoorsOpen.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = pygame.Rect(0, 300, 100, 230)
        graphDoor = pygame.Rect(1190, 300, 190, 240)
        bfsDoor = pygame.Rect(520, 20, 220, 140)
        dijkstraDoor = pygame.Rect(560, 560, 130, 130)
    elif numcompleted == 6:
        background_image = pygame.image.load("resources/3.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = pygame.Rect(0, 300, 100, 230)
        graphDoor = pygame.Rect(1190, 300, 190, 240)
        bfsDoor = pygame.Rect(520, 20, 220, 140)
        dijkstraDoor = None
    elif levels_completed[0] and levels_completed[1] and levels_completed[2] and levels_completed[3]:
        background_image = pygame.image.load("resources/2.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = pygame.Rect(0, 300, 100, 230)
        graphDoor = pygame.Rect(1190, 300, 190, 240)
        bfsDoor = None
        dijkstraDoor = None
    elif levels_completed[0] and levels_completed[1] and numcompleted < 5:
        background_image = pygame.image.load("resources/1b.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = pygame.Rect(0, 300, 100, 230)
        bfsDoor = None
        dijkstraDoor = None
    elif levels_completed[2] and levels_completed[3] and (levels_completed[0] == 0 or levels_completed[1] == 0):
        background_image = pygame.image.load("resources/1a.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        graphDoor = pygame.Rect(1190, 300, 190, 240)
        pqDoor  = None
        bfsDoor = None
        dijkstraDoor = None
    else:
        background_image = pygame.image.load("resources/0_begin.jpeg")
        queueDoor = pygame.Rect(150, 90, 180, 170)
        bubbleDoor = pygame.Rect(180, 610, 230, 110)
        nodeDoor = pygame.Rect(820, 610, 230, 110)
        edgeDoor = pygame.Rect(940, 90, 210, 170)
        pqDoor  = None
        graphDoor = None
        bfsDoor = None
        dijkstraDoor = None
    
    screen.blit(background_image, (0, 0))

    # Get the size of the window
    window_width, window_height = screen.get_size()


    # Draw the player as a 128px square
    #player_image = pygame.image.load("resources/algore.jpeg")
    #screen.blit(player_image, player_pos)
    keys = pygame.key.get_pressed()
    player.update(dt, keys)
    
    player.draw(screen)
    

    
    # Commenting the chunk of code


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()