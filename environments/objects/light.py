from .round_object import RoundObject

class Light(RoundObject):

    def __init__(self, location, intensity=.5, radius=.25, plotting_color='yellow'):
        super().__init__(location=location, radius=radius, plotting_color=plotting_color)
        self.inensity = intensity