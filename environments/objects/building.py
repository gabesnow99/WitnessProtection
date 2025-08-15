from .rectangular_object import RectangularObject

class Building(RectangularObject):

    def __init__(self, location, length, width, angle=0, plotting_color='BROWN'):
        super().__init__(location, length, width, angle, plotting_color)