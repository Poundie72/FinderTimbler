import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, image_file, screen, dialogue):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center
        self.rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)

        self.dialogue = dialogue

    def interact(self):
        print(self.dialogue)
        repeat = input("Would you like the explanation again? Enter 1 for yes, 0 for no: ")
        return repeat == "0"