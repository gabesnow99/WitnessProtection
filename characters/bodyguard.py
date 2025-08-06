from alignments.hero import Hero
from abilities.healer import Healer

'''
Can revive any character by drawing a cross on their arm
'''
class Bodyguard(Healer, Hero):

    def __init__(self):
        super().__init__()

    def revive(self, player):
        if super().revive(player):
            print("My life to yours, my breath become yours.")
            self.die()
        return super().revive(player)


if __name__=='__main__':
    b = Bodyguard()
    print(b)