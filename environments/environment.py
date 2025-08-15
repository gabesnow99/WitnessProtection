import json

from .objects.tree import Tree
from .objects.building import Building
from .objects.light import Light

class Environment:

    def __init__(self, template):
        # TODO: Add [if json, if yaml, etc.]
        self.parse(template)
        print(self.__str__())

    def parse(self, template):
        # Open template json file
        with open(template, "r") as file:
            map_data = json.load(file)

        # Add properties to class
        self.map_name = map_data['map_name']
        self.width = map_data['dimensions']['width']
        self.height = map_data['dimensions']['height']
        self.time_of_day = map_data['time_of_day']

        # Add objects to class
        self.trees = []
        for t in map_data['objects']['trees']:
            t_loc = [t['position']['x'], t['position']['y']]
            self.trees.append(Tree(t_loc))
        self.buildings = []
        for b in map_data['objects']['buildings']:
            b_loc = [b['position']['x'], b['position']['y']]
            b_length = b['size']['length']
            b_width = b['size']['width']
            b_height = b['size']['height']
            self.buildings.append(Building(b_loc, b_length, b_width))
        self.lights = []
        for l in map_data['lights']:
            l_loc = [l['position']['x'], l['position']['y']]
            l_intensity = l['intensity']
            self.lights.append(Light(l_loc, l_intensity))

    # TODO: MAKE BETTER
    def __str__(self):
        to_return = ''
        return to_return