from alignments.hero import Hero

'''
Citizens try to find and protect the witness.
'''
class Citizen(Hero):

    def __init__(self):
        super().__init__()


if __name__=='__main__':
    c = Citizen()
    print(c)