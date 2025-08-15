import numpy as np

class Object():

    def __init__(self, location, plotting_color='grey'):
        self.location = np.array(location).flatten()
        self.plotting_color = plotting_color
