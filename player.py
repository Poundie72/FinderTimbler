import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, screen):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.screen = screen  # Store the screen object
        self.rect = self.image.get_rect()

        # Set the player's initial position to the center of the screen
        self.rect.center = self.screen.get_rect().center
        self.speed = 300

    def update(self, dt, keys):
        if keys[pygame.K_w] and self.rect.y > 20:
            self.rect.y -= self.speed * dt
        if keys[pygame.K_s] and self.rect.y < self.screen.get_height() - 50:
            self.rect.y += self.speed * dt
        if keys[pygame.K_a] and self.rect.x > 50:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_d] and self.rect.x < self.screen.get_width() - self.rect.width - 50:
            self.rect.x += self.speed * dt
    
    def draw(self, screen):
        # Draw the image centered on the player's rectangle
        screen.blit(self.image, self.rect)