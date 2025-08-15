import numpy as np

from .round_object import RoundObject

class Light(RoundObject):

    def __init__(self, location, intensity=.5, radius=.25, plotting_color='YELLOW'):
        super().__init__(location=location, radius=radius, plotting_color=plotting_color)
        self.intensity = intensity

    def brightness_at_point(self, c):
        c = np.array(c).flatten()
        r = self.distance_from_coordinates(c)
        return self.brightness_at_range(r)

    # TODO: Calibrate
    def brightness_at_range(self, r):
        if r < self.radius:
            r = self.radius
        return self.intensity / r**2