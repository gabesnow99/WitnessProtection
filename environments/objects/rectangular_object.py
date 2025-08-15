from .object import Object

class RectangularObject(Object):

    # Angle defined as rotation about z (out of screen) in radians
    def __init__(self, location, length, width, angle=0., plotting_color='grey'):
        super().__init__(location, plotting_color)
        self.length = length
        self.width = width
        self.angle = angle