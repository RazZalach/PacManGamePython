import pygame

class Pellet:
    def __init__(self, x, y, size=10):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 255, 255)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size // 2)
