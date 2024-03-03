import pygame
def create_frames_from_sheet(sheet, sprite_width, sprite_height):
    sheet_width, sheet_height = sheet.get_size()
    frames = []
    for y in range(0, sheet_height, sprite_height):
        for x in range(0, sheet_width, sprite_width):
            rect = pygame.Rect(x, y, sprite_width, sprite_height)
            frames.append(sheet.subsurface(rect))
    return frames

class Player(pygame.sprite.Sprite):
    def __init__(self, image_paths, screen):
        super().__init__()
        self.frames = create_frames_from_sheet(pygame.image.load(image_paths['down']), 64, 64)
        self.current_frame = 0
        self.frame_time = 0.1
        self.accumulated_time = 0
        self.images = {
            'up': pygame.image.load(image_paths['up']),
            'down': pygame.image.load(image_paths['down']),
            'left': pygame.image.load(image_paths['left']),
            'right': pygame.image.load(image_paths['right']),
        }
        self.image = self.images['down']  # Set the initial image
        self.screen = screen  # Store the screen object
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center  # Set the player's initial position to the center of the screen
        self.speed = 300

    def update(self, dt, keys):
        self.accumulated_time += dt
        if self.accumulated_time > self.frame_time:
            self.accumulated_time -= self.frame_time
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
        if keys[pygame.K_w] and self.rect.y > 20:
            self.rect.y -= self.speed * dt
            self.image = self.images['up']
        if keys[pygame.K_s] and self.rect.y < self.screen.get_height() - 50:
            self.rect.y += self.speed * dt
            self.image = self.images['down']
        if keys[pygame.K_a] and self.rect.x > 50:
            self.rect.x -= self.speed * dt
            self.image = self.images['left']
        if keys[pygame.K_d] and self.rect.x < self.screen.get_width() - self.rect.width - 50:
            self.rect.x += self.speed * dt
            self.image = self.images['right']

    def draw(self, screen):
        # Draw the image centered on the player's rectangle
        screen.blit(self.frames[self.current_frame], self.rect)