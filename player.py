import pygame

def create_frames_from_sheet(sheet, sprite_width, sprite_height):
    sheet_width, sheet_height = sheet.get_size()
    frames = []
    for y in range(0, sheet_height, sprite_height):
        for x in range(0, sheet_width, sprite_width):
            rect = pygame.Rect(x, y, sprite_width, sprite_height)
            frames.append(sheet.subsurface(rect))
    return frames[:8]

class Player(pygame.sprite.Sprite):
    def __init__(self, image_paths, screen):
        super().__init__()
        self.frames = {
            'up': create_frames_from_sheet(pygame.image.load(image_paths['up']), 64, 64),
            'down': create_frames_from_sheet(pygame.image.load(image_paths['down']), 64, 64),
            'left': create_frames_from_sheet(pygame.image.load(image_paths['left']), 64, 64),
            'right': create_frames_from_sheet(pygame.image.load(image_paths['right']), 64, 64),
        }
        self.current_frames = self.frames['down']
        self.current_frame = 0
        self.image = self.current_frames[self.current_frame]  # Define self.image here
        self.frame_time = 0.1
        self.accumulated_time = 0
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.speed = 300

    def update(self, dt, keys):
        self.accumulated_time += dt
        if self.accumulated_time > self.frame_time:
            self.accumulated_time -= self.frame_time
            self.current_frame = (self.current_frame + 1) % len(self.current_frames)
            self.image = self.current_frames[self.current_frame]
        if keys[pygame.K_w] and self.rect.y > 20:
            self.rect.y -= self.speed * dt
            self.current_frames = self.frames['up']
        if keys[pygame.K_s] and self.rect.y < self.screen.get_height() - 50:
            self.rect.y += self.speed * dt
            self.current_frames = self.frames['down']
        if keys[pygame.K_a] and self.rect.x > 50:
            self.rect.x -= self.speed * dt
            self.current_frames = self.frames['left']
        if keys[pygame.K_d] and self.rect.x < self.screen.get_width() - self.rect.width - 50:
            self.rect.x += self.speed * dt
            self.current_frames = self.frames['right']

    def draw(self, screen):
        screen.blit(self.image, self.rect)