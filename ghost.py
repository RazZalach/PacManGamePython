import pygame
import random

class Ghost:
    def __init__(self, x, y, image, width, height, speed=3):
        self.x = x
        self.y = y
        self.size = 20
        self.image = image
        self.speed = speed
        self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
        self.width = width
        self.height = height

    def move(self):
        if self.direction == 'LEFT':
            self.x -= self.speed
        elif self.direction == 'RIGHT':
            self.x += self.speed
        elif self.direction == 'UP':
            self.y -= self.speed
        elif self.direction == 'DOWN':
            self.y += self.speed

        # Keep ghost within bounds
        self.x = max(0, min(self.x, self.width - self.size))
        self.y = max(0, min(self.y, self.height - self.size))

        # Change direction randomly
        if random.random() < 0.02:
            self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
