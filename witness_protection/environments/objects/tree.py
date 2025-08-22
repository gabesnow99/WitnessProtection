from .round_object import RoundObject

class Tree(RoundObject):

    def __init__(self, location, radius=5., shade_coef=.1):
        super().__init__(location, radius, plotting_color='DARKGREEN')
        self.shade_coef = shade_coef

    def shade_at_point(self, p):
        if self.distance_from_coordinates(p) < self.radius:
            return self.shade_coef
        else:
            return 0.