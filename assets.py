import os
import pygame

# Get the directory of the current script (assets.py)
base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')

# Load images using the assets directory
## open mouth:
pacman_images = {
    'RIGHT': pygame.image.load(os.path.join(assets_dir, 'right_pacman.png')),
    'LEFT': pygame.image.load(os.path.join(assets_dir, 'left_pacman.png')),
    'UP': pygame.image.load(os.path.join(assets_dir, 'up_pacman.png')),
    'DOWN': pygame.image.load(os.path.join(assets_dir, 'down_pacman.png'))
}
## close mouth:
pacman_images2 = {
    'RIGHT': pygame.image.load(os.path.join(assets_dir, 'close_mouth_right.png')),
    'LEFT': pygame.image.load(os.path.join(assets_dir, 'close_mouth_left.png')),
    'UP': pygame.image.load(os.path.join(assets_dir, 'close_mouth_up.png')),
    'DOWN': pygame.image.load(os.path.join(assets_dir, 'close_mouth_down.png'))
}
ghost_images = [
    pygame.image.load(os.path.join(assets_dir, 'gohst1.png')),
    pygame.image.load(os.path.join(assets_dir, 'gohst2.png')),
    pygame.image.load(os.path.join(assets_dir, 'gohst3.png')),
    pygame.image.load(os.path.join(assets_dir, 'gohst4.png')),
]

# Load sound effects
pygame.mixer.init()
start_sound = pygame.mixer.Sound(os.path.join(assets_dir, 'start.ogg'))
eat_sound = pygame.mixer.Sound(os.path.join(assets_dir, 'eat2.ogg'))
lose_sound = pygame.mixer.Sound(os.path.join(assets_dir, 'lose.ogg'))
win_sound = pygame.mixer.Sound(os.path.join(assets_dir, 'win.ogg'))
