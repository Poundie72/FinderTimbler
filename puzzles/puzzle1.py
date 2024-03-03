import pygame
from player import Player


# pygame setup

def run_puzzle1(screen, player, clock, running, dt):
    tutorial_image = pygame.image.load("resources/tutorial_queue.jpeg")
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
            puzzle_image = pygame.image.load("resources/puzzTest.jpg") 
            screen.blit(puzzle_image, (0, 0))

        if keys[pygame.K_1]:
            font = pygame.font.Font(None, 36) 
            text = font.render("WRONG!!", True, (255, 0, 0))  # Create a surface with the text
            screen.blit(text, (0, 600))  # Draw the text to the screen at position (100, 100)
        if keys[pygame.K_2]:
            return int(0)
        if keys[pygame.K_3]: #correct answer
            return int(1)
        if keys[pygame.K_4]:
            return int(0)

                
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

























class Puzzle1:
    # Create a font object
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.questions = [
            "Question 1: Which is a better representative of a queue: 1. A line at an amusement park or 2. A stack of plates?",
            "Question 2: Lets think about your kitchen as a queue, and in it are the items you need for a bowl of cereal. What would be the correct order to enqueue them (i.e. to be taken out to make a bowl of cereal)? 1. Cereal, Milk, Bowl or 2. Bowl, Cereal, Milk?",
            "Question 3: Now look at this queue: Q = [(bread), (eggs), (mustard), (grapes), (cereal), (mayo), (chocolate)]. Now, do the following: pop, pop, enqueue(orange), pop, enqueue(pizza), pop. What is the final queue after these operations? Is it 1. [(mustard), (grapes), (cereal), (mayo), (chocolate), (orange)] or 2. [(cereal), (mayo), (chocolate), (orange), (pizza)] or 3. [(cereal), (mayo), (chocolate), (orange), (pizza), (bread)]?" 
        ]
        self.answers = ["1", "2", "2"]
        self.current_question = 0
        self.completed = False
        self.tutorial_active = True

    def draw(self):
        # Draw the current question on the screen
        if self.tutorial_active:
            text = self.font.render("Press 1 to start the puzzle or 0 to go back", True, (255, 255, 255))
            self.screen.blit(text, (50, 50))
            return
        else:
            text = self.font.render(self.questions[self.current_question], True, (255, 255, 255))
            self.screen.blit(text, (50, 50))

    def handle_input(self, event):
        answer = None  # Initialize answer to a default value
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                answer = "1"
            elif event.key == pygame.K_2:
                answer = "2"
            elif event.key == pygame.K_3:
                answer = "3"
            elif event.key == pygame.K_b:  # Go back to the lobby
                return 'lobby'
        if answer is not None and answer == self.answers[self.current_question]:
            self.current_question += 1
            if self.current_question == len(self.questions):
                self.completed = True
        elif answer is not None:
            self.current_question = 0  # Start over if the answer is incorrect
    def handle_tutorial(self, event, dialogue_finished, keys):
        if keys[pygame.K_1]:
            self.tutorial_active = False
            return dialogue_finished == True
        elif event.key == pygame.K_0:
            self.tutorial_active = False
            return dialogue_finished == False
        return None

    def check_completion(self):
        # Check if the puzzle is completed
        return self.completed