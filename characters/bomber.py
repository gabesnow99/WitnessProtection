from alignments.hero import Hero
from abilities.healer import Healer

'''
Can sacrifice themself to blow nearby characters
'''
class Bomber(Healer, Hero):

    def __init__(self):
        super().__init__()

    def revive(self, player):
        if super().revive(player):
            print("My life to yours, my breath become yours.")
            self.alive = False
        return super().revive(player)


if __name__=='__main__':
    b = Bomber()
    print(b)