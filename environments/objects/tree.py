from .round_object import RoundObject

class Tree(RoundObject):

    def __init__(self, location, radius=.5, canopy_radius=4., shade_coef=.1):
        super().__init__(location, radius, plotting_color='DARKGREEN')
        self.canopy_radius = canopy_radius
        self.shade_coef = shade_coef

    def shade_at_point(self, p):
        if self.distance_from_coordinates(p) < self.canopy_radius:
            return self.shade_coef
        else:
            return 0.