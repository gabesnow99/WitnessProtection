from player import Player

'''
Base class for all villains
'''
class Villian(Player):

    def __init__(self):
        super().__init__(is_good=False)


if __name__=='__main__':
    v = Villian()
    print(v)