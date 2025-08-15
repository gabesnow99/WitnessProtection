import pygame
import random

from environments.environment import Environment
from environments.objects.rectangular_object import RectangularObject
from environments.objects.round_object import RoundObject


pygame.init()

env = Environment('environments/park.json')
screen = pygame.display.set_mode((env.width, env.height))
pygame.display.set_caption(env.map_name)

def shade_background():
    for x in range(env.width):
        for y in range(env.height):
            brightness = env.brightness_at([x, y])
            grayscale = int(brightness * 255)
            screen.set_at((x, y), (grayscale, grayscale, grayscale))

# shade_background()
screen.fill("GREY")
env.draw_objects_pygame(screen)

point_x, point_y = 400, 300
point_size = 5

running = True
clock = pygame.time.Clock()
while running:

    # Draw the moving point
    pygame.draw.circle(screen, 'GREEN', (point_x, point_y), point_size)

    # Move the point randomly
    point_x += random.choice([-1, 0, 1])
    point_y += random.choice([-1, 0, 1])

    # Event handling (exit on close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Update the display
    clock.tick(60)  # Cap the frame rate at 60 FPS

# Clean up
pygame.quit()
