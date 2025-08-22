from ..environments.environment import Environment
from ..characters.all_characters import *


class Game:

    def __init__(self, template):
        self.env = Environment(template)
        print(self.env)
        self.initizalize_characters()
        self.witness.hide()

    def initizalize_characters(self):
        self.witness = Witness()
        self.murderer = Murderer()
