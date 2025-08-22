from .alignments.hero import Hero

'''
Survive
'''
class Witness(Hero):

    def __init__(self):
        super().__init__()

    def hide(self):
        pass


if __name__=='__main__':
    w = Witness()
    print(w)