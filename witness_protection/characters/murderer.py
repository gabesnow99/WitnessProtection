from .alignments.villian import Villian
from .abilities.killer import Killer

'''
Can revive the killer
'''
class Murderer(Killer, Villian):

    def __init__(self):
        super().__init__()


if __name__=='__main__':
    m = Murderer()
    print(m)