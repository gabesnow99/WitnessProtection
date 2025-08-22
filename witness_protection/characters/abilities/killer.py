from ..player import Player

'''
Can kill
'''
class Killer(Player):

    def __init__(self):
        super().__init__()

    def kill(self, player):
        pass


if __name__=='__main__':
    k = Killer()
    print(k)