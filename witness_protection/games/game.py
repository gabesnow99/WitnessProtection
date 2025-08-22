import numpy as np
import random
import pygame

from ..environments.environment import Environment
from ..characters.all_characters import *


class Game:

    def __init__(self, template):
        # Initialize game
        self.env = Environment(template)
        self.initialize_game()
        self.initizalize_characters()
        self.running = True
        self.clock = pygame.time.Clock()
        # Go
        self.go()

    # Set up the game using pygame
    def initialize_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.env.width, self.env.height))
        pygame.display.set_caption(self.env.map_name)

    # Initialize characters
    def initizalize_characters(self):
        self.witness = Witness()
        self.murderer = Murderer()
        self.characters = [self.witness, self.murderer]

    # Go
    def go(self):
        point_size = 5
        color = 'green'
        self.witness.hide()
        while self.running:

            self.screen.fill('WHITE')
            # self.env.draw_brightness_map(self.screen)
            self.env.draw_objects_pygame(self.screen)

            for c in self.characters:
                c.location += np.array([random.choice([-1, 0, 1]), random.choice([-1, 0, 1])])
                pygame.draw.circle(self.screen, color, (c.location + [250, 250]), point_size)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
            self.clock.tick(60)