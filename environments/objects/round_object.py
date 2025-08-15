from .object import Object

class RoundObject(Object):

    def __init__(self, location, radius, plotting_color='GRAY'):
        super().__init__(location, plotting_color)
        self.radius = radius