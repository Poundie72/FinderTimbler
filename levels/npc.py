import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, image_file, screen, dialogue, tutorial):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center
        self.dialogue = dialogue
        self.font = pygame.font.Font(None, 24)  # Add a font attribute
        self.tutorial = tutorial
        self.tutorial_active = False

    def draw_dialogue(self):
        text_surface = self.font.render(self.dialogue, True, (255, 255, 255))
        self.screen.blit(text_surface, (self.rect.x, self.rect.y - text_surface.get_height()))
