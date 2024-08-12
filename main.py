import pygame
import random
from pacman import PacMan
from ghost import Ghost
from pellet import Pellet
from maze import mazes, draw_maze
from utils import draw_welcome_message

# Initialize the game
pygame.init()

# Set up display
width, height = 500, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man")

# Define colors
BLACK = (0, 0, 0)

# Load images
pacman_images = {
    'RIGHT': pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\right_pacman.png'),
    'LEFT': pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\left_pacman.png'),
    'UP': pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\up_pacman.png'),
    'DOWN': pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\down_pacman.png')
}
ghost_images = [
    pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\gohst1.png'),
    pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\gohst2.png'),
    pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\gohst3.png'),
    pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\gohst4.png'),
]

# Load sound effects
pygame.mixer.init()
start_sound = pygame.mixer.Sound('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\start.ogg')
eat_sound = pygame.mixer.Sound('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\eat.ogg')
lose_sound = pygame.mixer.Sound('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\lose.ogg')
win_sound = pygame.mixer.Sound('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\win.ogg')

# Resize images
cell_size = 20
pacman_images = {key: pygame.transform.scale(img, (cell_size, cell_size)) for key, img in pacman_images.items()}
ghost_images = [pygame.transform.scale(img, (30, 30)) for img in ghost_images]

# Main function
def main():
    start_sound.play()  # Play start sound

    start_time = pygame.time.get_ticks()
    start_sound_length = int(start_sound.get_length() * 1000)
    last_eat_time = 0  # Initialize the time when the last eat sound was played

    level = 0  # Start at level 0

    def load_level(level):
        maze = mazes[level]  # Load the maze for the current level
        pacman = PacMan(pacman_images, maze)  # Pass the maze to PacMan
        pellets = [Pellet(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2) 
                   for row in range(len(maze)) 
                   for col in range(len(maze[row])) 
                   if maze[row][col] == '.']
        ghosts = [Ghost(random.randint(0, width - 20), random.randint(0, height - 20), ghost_images[i], width, height) for i in range(4)]
        return maze, pacman, pellets, ghosts

    maze, pacman, pellets, ghosts = load_level(level)

    clock = pygame.time.Clock()
    run = True

    while run:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Show welcome message while waiting for the start sound to finish
        current_time = pygame.time.get_ticks()
        if current_time < start_time + start_sound_length:
            win.fill(BLACK)
            draw_welcome_message(win, pygame.font.Font(None, 36))
            pygame.display.update()
        else:
            # Start the game after the welcome message
            pacman.move()
            for ghost in ghosts:
                ghost.move()

            # Check for pellet consumption
            new_pellets = []
            for pellet in pellets:
                if abs(pacman.x - pellet.x) < pacman.size and abs(pacman.y - pellet.y) < pacman.size:
                    current_time = pygame.time.get_ticks()
                    if current_time - last_eat_time > 300:
                        eat_sound.play()
                        last_eat_time = current_time
                else:
                    new_pellets.append(pellet)
            pellets = new_pellets

            # Check for collisions with ghosts
            collision_detected = any(pacman.collide(ghost) for ghost in ghosts)
            if collision_detected:
                lose_sound.play()
                pygame.display.update()
                pygame.time.wait(int(lose_sound.get_length() * 1000))
                print("Game Over!")
                run = False

            # Check win condition
            if not pellets:
                if level < len(mazes) - 1:  # Check if there are more levels
                    level += 1
                    maze, pacman, pellets, ghosts = load_level(level)
                    start_time = pygame.time.get_ticks()  # Restart timer for new level
                    start_sound.play()  # Play start sound again for the new level
                else:
                    win_sound.play()
                    pygame.display.update()
                    pygame.time.wait(int(win_sound.get_length() * 1000))
                    print("You Win!")
                    run = False

            win.fill(BLACK)
            draw_maze(win, maze, cell_size)  # Pass the maze to draw_maze
            pacman.draw(win)
            for pellet in pellets:
                pellet.draw(win)
            for ghost in ghosts:
                ghost.draw(win)

            pygame.display.update()
            clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
