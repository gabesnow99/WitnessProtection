import numpy as np
import json

from .objects.rectangular_object import RectangularObject
from .objects.round_object import RoundObject
from .objects.tree import Tree
from .objects.building import Building
from .objects.light import Light


class Environment:

    def __init__(self, template):
        # TODO: Add [if json, if yaml, etc.]
        self.parse(template)

    def parse(self, template):
        # Open template json file
        with open(template, "r") as file:
            map_data = json.load(file)

        # Add properties to self
        self.map_name = map_data['map_name']
        self.width = map_data['dimensions']['width']
        self.height = map_data['dimensions']['height']
        self.ambient_light = map_data['ambient_light']

        # Add objects to self
        self.objects = {}
        # Trees
        trees = []
        for t in map_data['objects']['trees']:
            t_loc = [t['position']['x'], t['position']['y']]
            trees.append(Tree(t_loc))
        self.objects['trees'] = trees
        # Buildings
        buildings = []
        for b in map_data['objects']['buildings']:
            b_loc = [b['position']['x'], b['position']['y']]
            b_length = b['size']['length']
            b_width = b['size']['width']
            b_height = b['size']['height']
            buildings.append(Building(b_loc, b_length, b_width))
        self.objects['buildings'] = buildings
        # Lights
        lights = []
        for l in map_data['objects']['lights']:
            l_loc = [l['position']['x'], l['position']['y']]
            l_intensity = l['intensity']
            lights.append(Light(l_loc, l_intensity))
        self.objects['lights'] = lights

    # Returns the brightness at a given [x, y] point
    def brightness_at(self, coordinates):
        coordinates = np.array(coordinates).flatten()
        brightness = self.ambient_light
        for l in self.objects['lights']:
            brightness += l.brightness_at_point(coordinates)
        for t in self.objects['trees']:
            brightness -= t.shade_at_point(coordinates)
        if brightness > 1:
            brightness = 1.
        if brightness < 0:
            brightness = 0.
        return brightness

    # Returns semi-permanent brightness map
    # TODO: UNFINISHED
    def brightness_map(self):
        to_return = np.zeros((self.height, self.width))
        for ii in range(self.width):
            for jj in range(self.height):
                to_return[ii, jj] = self.brightness_at([ii, jj])
        return np.array(to_return)

    # Draw objects when using pygame screen
    def draw_objects_pygame(self, screen):
        import pygame
        for obj_type in self.objects:
            for obj in self.objects[obj_type]:
                if isinstance(obj, RectangularObject):
                    pygame.draw.rect(screen, obj.plotting_color, (obj.location[0], obj.location[1], obj.width, obj.length))
                elif isinstance(obj, RoundObject):
                    pygame.draw.circle(screen, obj.plotting_color, (obj.location[0], obj.location[1]), obj.radius)

    # What is displayed when print(environment) is used
    def __str__(self):
        to_print = '===============================\n'
        to_print += f'Name:        {self.map_name}\n'
        to_print += f'Dimensions:  {self.width}m x {self.height}m\n'
        to_print += '-------------------------------\n'
        to_print += f'Trees:       {len(self.objects['trees'])}\n'
        to_print += f'Buildings:   {len(self.objects['buildings'])}\n'
        to_print += '==============================='
        return to_print