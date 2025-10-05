import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_HEIGHT = 400
PIPE_GAP = 150

# Load images
bird_image = pygame.image.load('bird.png')
background_image = pygame.image.load('background.png')

# Bird class
class Bird:
    def __init__(self):
        self.image = bird_image
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 300)
        self.top = self.height - PIPE_HEIGHT
        self.bottom = self.height + PIPE_GAP

    def update(self):
        self.x -= 5

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.top, PIPE_WIDTH, PIPE_HEIGHT))
        pygame.draw.rect(screen, GREEN, (self.x, self.bottom, PIPE_WIDTH, PIPE_HEIGHT))

# Main game function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(3)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.flap()

        bird.update()
        for pipe in pipes:
            pipe.update()
            if pipe.x < -PIPE_WIDTH:
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH))

        screen.blit(background_image, (0, 0))
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()