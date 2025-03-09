import pygame
import random
pygame.init()

WIDTH, HEIGHT = 1000, 650
BIRD_X, BIRD_Y = 50, HEIGHT // 2
BIRD_RADIUS = 15
GRAVITY = 0.5
JUMP_STRENGTH = -8
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3

WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()

bird_y = BIRD_Y
bird_velocity = 0
pipes = []
for i in range(2):
    pipe_x = WIDTH + i * 200
    pipe_height = random.randint(100, 400)
    pipes.append([pipe_x, pipe_height])

running = True
score = 0
while running:
    screen.fill(BLUE)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = JUMP_STRENGTH  # Make the bird jump

    bird_velocity += GRAVITY
    bird_y += bird_velocity
    pygame.draw.circle(screen, RED, (BIRD_X, int(bird_y)), BIRD_RADIUS)

    for pipe in pipes:
        pipe[0] -= PIPE_SPEED  

        pygame.draw.rect(screen, GREEN, (pipe[0], 0, PIPE_WIDTH, pipe[1]))
        pygame.draw.rect(screen, GREEN, (pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe[1] - PIPE_GAP))

        if pipe[0] < -PIPE_WIDTH:
            pipe[0] = WIDTH
            pipe[1] = random.randint(100, 400)
            score += 1

        if (BIRD_X + BIRD_RADIUS > pipe[0] and BIRD_X - BIRD_RADIUS < pipe[0] + PIPE_WIDTH) and \
           (bird_y - BIRD_RADIUS < pipe[1] or bird_y + BIRD_RADIUS > pipe[1] + PIPE_GAP):
            running = False  # Game Over

    if bird_y + BIRD_RADIUS > HEIGHT:
        running = False
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
