from .alignments.villian import Villian
from .abilities.healer import Healer

from .murderer import Murderer

'''
Can revive the killer
'''
class Lawyer(Healer, Villian):

    def __init__(self):
        super().__init__()

    def announce_to_dead(self, player):
        pass

    def revive(self, player: Murderer):
        self.announce_to_dead(player)
        if type(player) is not Murderer:
            print("Not the murderer.")
            return False
        return super().revive(player)


if __name__=='__main__':
    l = Lawyer()
    print(l)