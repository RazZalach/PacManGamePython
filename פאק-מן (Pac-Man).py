import pygame
import random

# Initialize the game
pygame.init()

# Set up display
width, height = 500, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
pacman_right_img = pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\right_pacman.png')
pacman_left_img = pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\left_pacman.png')
pacman_up_img = pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\up_pacman.png')
pacman_down_img = pygame.image.load('C:\\Users\\raz62\\Desktop\\all\\python\\pacman\\down_pacman.png')

# Load ghost images into a list
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
pacman_right_img = pygame.transform.scale(pacman_right_img, (cell_size, cell_size))
pacman_left_img = pygame.transform.scale(pacman_left_img, (cell_size, cell_size))
pacman_up_img = pygame.transform.scale(pacman_up_img, (cell_size, cell_size))
pacman_down_img = pygame.transform.scale(pacman_down_img, (cell_size, cell_size))
ghost_images = [pygame.transform.scale(img, (30, 30)) for img in ghost_images]

# Define the Maze
maze = [
    "#########################",
    "#.......................#",
    "###########..############",
    "#.........#..#..........#",
    "#.....#...#..#..........#",
    "#.....#...#..#..######..#",
    "#.....#...#..#.......#..#",
    "#.....#...#..#.......#..#",
    "#.....#####..#########..#",
    "#.......................#",
    "#.......................#",
    "#.#####################.#",
    "#.#........#..#.......#.#",
    "#.#........#..#.......#.#",
    "#.#........#..#.......#.#",
    "#.#........#..#.......#.#",
    "#.#........#..#.......#.#",
    "#.#........#..#.......#.#",
    "#.#........#..#.......#.#",
    "#.#........#..#.......#.#",
    "#.#.....................#",
    "#.##########..###########",
    "#.......................#",
    "#########################",
]

# Define the Pac-Man class
class PacMan:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.size = cell_size
        self.image = pacman_right_img
        self.speed = 5
        self.direction = 'RIGHT'
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 'LEFT'
            self.image = pacman_left_img
        if keys[pygame.K_RIGHT]:
            self.direction = 'RIGHT'
            self.image = pacman_right_img
        if keys[pygame.K_UP]:
            self.direction = 'UP'
            self.image = pacman_up_img
        if keys[pygame.K_DOWN]:
            self.direction = 'DOWN'
            self.image = pacman_down_img
        
        if self.direction == 'LEFT':
            self.x -= self.speed
        if self.direction == 'RIGHT':
            self.x += self.speed
        if self.direction == 'UP':
            self.y -= self.speed
        if self.direction == 'DOWN':
            self.y += self.speed

        # Check collision with walls
        row = self.y // cell_size
        col = self.x // cell_size
        if maze[row][col] == '#':
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

# Define the Pellet class
class Pellet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.color = WHITE

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size // 2)

# Define the Ghost class
class Ghost:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.size = cell_size
        self.image = image  # Use the provided image
        self.speed = 3
        self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])

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
        self.x = max(0, min(self.x, width - self.size))
        self.y = max(0, min(self.y, height - self.size))

        # Change direction randomly
        if random.random() < 0.02:  # Change direction with a small probability
            self.direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

# Draw maze
def draw_maze(win):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == '#':
                pygame.draw.rect(win, WHITE, (col * cell_size, row * cell_size, cell_size, cell_size))

# Define the font for the welcome message
font = pygame.font.Font(None, 36)

# Draw welcome message function
def draw_welcome_message(win, font):
    text = font.render("Welcome to Pac-Man!", True, WHITE)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    win.blit(text, text_rect)

# Main function
def main():
    start_sound.play()  # Play start sound

    start_time = pygame.time.get_ticks()
    start_sound_length = int(start_sound.get_length() * 1000)
    last_eat_time = 0  # Initialize the time when the last eat sound was played

    pacman = PacMan()
    pellets = [Pellet(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2) 
               for row in range(len(maze)) 
               for col in range(len(maze[row])) 
               if maze[row][col] == '.']
    
    # Create ghosts with unique images
    ghosts = [Ghost(random.randint(0, width - cell_size), random.randint(0, height - cell_size), ghost_images[i]) for i in range(4)]

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
            draw_welcome_message(win, font)
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
                    if current_time - last_eat_time > 300:  # Check if 0.11 seconds have passed
                        eat_sound.play()  # Play eat sound
                        last_eat_time = current_time  # Update last eat time
                else:
                    new_pellets.append(pellet)
            pellets = new_pellets

            # Check for collisions with ghosts
            collision_detected = any(pacman.collide(ghost) for ghost in ghosts)
            if collision_detected:
                lose_sound.play()  # Play lose sound
                pygame.display.update()
                pygame.time.wait(int(lose_sound.get_length() * 1000))
                print("Game Over!")
                run = False

            # Check win condition
            if not pellets:
                win_sound.play()  # Play win sound
                pygame.display.update()
                pygame.time.wait(int(win_sound.get_length() * 1000))
                print("You Win!")
                run = False

            win.fill(BLACK)
            draw_maze(win)
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
