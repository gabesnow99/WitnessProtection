import pygame
import random

from environments.environment import Environment


pygame.init()

env = Environment('environments/park.json')
screen = pygame.display.set_mode((env.width, env.height))
pygame.display.set_caption(env.map_name)

point_x, point_y = 400, 300
point_size = 5

running = True
clock = pygame.time.Clock()
while running:

    screen.fill('WHITE')
    env.draw_brightness_map(screen)
    env.draw_objects_pygame(screen)

    pygame.draw.circle(screen, 'GREEN', (point_x, point_y), point_size)
    point_x += random.choice([-1, 0, 1])
    point_y += random.choice([-1, 0, 1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()