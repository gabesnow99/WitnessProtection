from .alignments.hero import Hero
from .abilities.killer import Killer

'''
Can revive the killer
'''
class Granny(Killer, Hero):

    def __init__(self):
        super().__init__()


if __name__=='__main__':
    g = Granny()
    print(g)