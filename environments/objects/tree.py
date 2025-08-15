from .round_object import RoundObject

class Tree(RoundObject):

    def __init__(self, location, radius=.5):
        super().__init__(location, radius, plotting_color='brown')
