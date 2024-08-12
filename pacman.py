import pygame
from maze import mazes

class PacMan:
    def __init__(self, images, maze, initial_x=30, initial_y=30, speed=5):
        self.x = initial_x
        self.y = initial_y
        self.size = 20
        self.images = images
        self.image = self.images['RIGHT']
        self.speed = speed
        self.direction = 'RIGHT'
        self.maze = maze  # Store the maze

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 'LEFT'
            self.image = self.images['LEFT']
        if keys[pygame.K_RIGHT]:
            self.direction = 'RIGHT'
            self.image = self.images['RIGHT']
        if keys[pygame.K_UP]:
            self.direction = 'UP'
            self.image = self.images['UP']
        if keys[pygame.K_DOWN]:
            self.direction = 'DOWN'
            self.image = self.images['DOWN']

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

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def collide(self, ghost):
        distance = ((self.x - ghost.x) ** 2 + (self.y - ghost.y) ** 2) ** 0.5
        return distance < self.size // 2 + ghost.size // 2
