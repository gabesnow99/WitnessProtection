from .alignments.villian import Villian

'''
Can take a hostage
'''
class HostageTaker(Villian):

    def __init__(self):
        super().__init__()


if __name__=='__main__':
    h = HostageTaker()
    print(h)