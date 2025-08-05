from player import Player

'''
Base class for all villains
'''
class Hero(Player):

    def __init__(self):
        super().__init__(is_good=True)


if __name__=='__main__':
    h = Hero()
    print(h)