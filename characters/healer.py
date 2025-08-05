from player import Player

'''
Can revive
'''
class Healer(Player):

    def __init__(self):
        super().__init__()


if __name__=='__main__':
    h = Healer()
    print(h)