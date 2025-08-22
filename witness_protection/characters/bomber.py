from .alignments.hero import Hero
from .abilities.killer import Killer

'''
Can sacrifice themself to blow nearby characters
'''
class Bomber(Killer, Hero):

    def __init__(self):
        super().__init__()

    def kill(self, player):
        return super().kill(player)


if __name__=='__main__':
    b = Bomber()
    print(b)