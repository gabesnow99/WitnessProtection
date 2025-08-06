from player import Player

'''
Can revive
'''
class Healer(Player):

    def __init__(self):
        super().__init__()

    def revive(self, player):
        if not player.alive:
            player.alive = True
            return True
        else:
            print("The whole need no physician.")
            return False


if __name__=='__main__':
    h = Healer()
    print(h)