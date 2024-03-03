import pygame

def create_frames_from_sheet(sheet, sprite_width, sprite_height, r_frames):
    sheet_width, sheet_height = sheet.get_size()
    frames = []
    for y in range(0, sheet_height, sprite_height):
        for x in range(0, sheet_width, sprite_width):
            rect = pygame.Rect(x, y, sprite_width, sprite_height)
            frames.append(sheet.subsurface(rect))
    return frames[:int (r_frames)]

class Direction(enumerate):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, frames_list, screen):
        super().__init__()
        self.frames = frames_list
        self.current_direction = Direction.DOWN
        self.current_frames = self.frames[self.current_direction]
        self.current_frame = 0
        self.image = self.current_frames[self.current_frame]
        self.frame_time = 0.1
        self.accumulated_time = 0
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.speed = 300

    def update(self, dt, keys):
        if keys[pygame.K_w]:
            self.current_direction = Direction.UP
            self.rect.y -= self.speed * dt
        elif keys[pygame.K_s]:
            self.current_direction = Direction.DOWN
            self.rect.y += self.speed * dt
        elif keys[pygame.K_a]:
            self.current_direction = Direction.LEFT
            self.rect.x -= self.speed * dt
        elif keys[pygame.K_d]:
            self.current_direction = Direction.RIGHT
            self.rect.x += self.speed * dt

        self.current_frames = self.frames[self.current_direction]
        self.accumulated_time += dt
        if self.accumulated_time > self.frame_time:
            self.accumulated_time -= self.frame_time
            if isinstance(self.current_frames, list):  # Check if current_frames is a list
                self.current_frame = (self.current_frame + 1) % len(self.current_frames)
                self.image = self.current_frames[self.current_frame]
            else:  # If not a list, use current_frames as the image
                self.image = self.current_frames

    def draw(self, screen):
        screen.blit(self.image, self.rect)

