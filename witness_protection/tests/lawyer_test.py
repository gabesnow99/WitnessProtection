from characters.lawyer import Lawyer
from characters.murderer import Murderer
from characters.witness import Witness

l = Lawyer()
m = Murderer()
w = Witness()

# Test revive a non-murderer
w.die()
l.revive(w)

print(l)