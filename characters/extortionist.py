from .alignments.villian import Villian

'''
Can prevent the witness from winning
'''
class Extortionist(Villian):

    def __init__(self):
        super().__init__()


if __name__=='__main__':
    e = Extortionist()
    print(e)