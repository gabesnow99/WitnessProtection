from .alignments.hero import Hero
from .abilities.healer import Healer

'''
Can revive any character by drawing a cross on their arm
'''
class Doctor(Healer, Hero):

    def __init__(self):
        super().__init__()

    def revive(self, player):
        return super().revive(player)


if __name__=='__main__':
    d = Doctor()
    print(d)