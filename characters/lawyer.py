from villian import Villian
from healer import Healer

'''
Can revive the killer
'''
class Lawyer(Healer, Villian):

    def __init__(self):
        super().__init__()


if __name__=='__main__':
    l = Lawyer()
    print(l)