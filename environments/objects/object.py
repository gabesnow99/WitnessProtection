import numpy as np

class Object():

    def __init__(self, location, plotting_color='GRAY'):
        self.location = np.array(location).flatten()
        self.plotting_color = plotting_color

    def distance_from_coordinates(self, coordinates):
        coordinates = np.array(coordinates).flatten()
        return np.linalg.norm(self.location - coordinates)