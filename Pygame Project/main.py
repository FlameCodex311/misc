import pygame
import os

WIDTH, HEIGHT = 800, 800

# GROUND = pygame.Rect(0, 710 , 800, HEIGHT)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pygame Test")

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 75, 75

VEL = 2

SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'Spaceship.png'))
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

def draw_window(spaceship):
    WIN.fill(WHITE)
    # pygame.draw.rect(WIN, BLACK, GROUND)
    WIN.blit(SPACESHIP, (spaceship.x, spaceship.y))
    pygame.display.update()

def handle_boy_movement(keys_pressed, spaceship):
    if keys_pressed[pygame.K_a] and spaceship.x - VEL > 0: # LEFT
        spaceship.x -= VEL
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_d] and spaceship.x + VEL + spaceship.width < 800: # RIGHT
        spaceship.x += VEL
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and spaceship.y - VEL > 0: # UP
        spaceship.y -= VEL
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_s] and spaceship.y + VEL + spaceship.height < 800: # DOWN
        spaceship.y += VEL

def main():
    spaceship = pygame.Rect(350, 600, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_boy_movement(keys_pressed, spaceship)


        draw_window(spaceship)

    pygame.quit()

if __name__ == "__main__":
    main()