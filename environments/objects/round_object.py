from .object import Object

class RoundObject(Object):

    def __init__(self, location, radius, plotting_color='grey'):
        super().__init__(location, plotting_color)
        self.radius = radius