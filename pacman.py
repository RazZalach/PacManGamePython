import pygame
from maze import mazes

class PacMan:
    def __init__(self, open_mouth_images, closed_mouth_images, maze, initial_x=30, initial_y=30, speed=5):
        self.x = initial_x
        self.y = initial_y
        self.size = 20
        self.open_mouth_images = open_mouth_images
        self.closed_mouth_images = closed_mouth_images
        self.current_images = self.open_mouth_images
        self.image = self.current_images['RIGHT']
        self.speed = speed
        self.direction = 'RIGHT'
        self.maze = maze  # Store the maze
        self.animation_time = 100  # Time to switch images (in milliseconds)
        self.last_animation_time = pygame.time.get_ticks()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 'LEFT'
            self.image = self.current_images['LEFT']
        if keys[pygame.K_RIGHT]:
            self.direction = 'RIGHT'
            self.image = self.current_images['RIGHT']
        if keys[pygame.K_UP]:
            self.direction = 'UP'
            self.image = self.current_images['UP']
        if keys[pygame.K_DOWN]:
            self.direction = 'DOWN'
            self.image = self.current_images['DOWN']

        if self.direction == 'LEFT':
            self.x -= self.speed
        if self.direction == 'RIGHT':
            self.x += self.speed
        if self.direction == 'UP':
            self.y -= self.speed
        if self.direction == 'DOWN':
            self.y += self.speed

        # Check collision with walls
        row = self.y // self.size
        col = self.x // self.size
        if self.maze[row][col] == '#':  # Use the maze passed in the constructor
            if self.direction == 'LEFT':
                self.x += self.speed
            if self.direction == 'RIGHT':
                self.x -= self.speed
            if self.direction == 'UP':
                self.y += self.speed
            if self.direction == 'DOWN':
                self.y -= self.speed

        # Update animation (switch between open and closed mouth)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > self.animation_time:
            self.last_animation_time = current_time
            self.current_images = self.closed_mouth_images if self.current_images == self.open_mouth_images else self.open_mouth_images
            self.image = self.current_images[self.direction]

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def collide(self, ghost):
        distance = ((self.x - ghost.x) ** 2 + (self.y - ghost.y) ** 2) ** 0.5
        return distance < self.size // 2 + ghost.size // 2
