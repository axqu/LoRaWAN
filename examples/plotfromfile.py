import sys
import numpy as np
import matplotlib.pyplot as plt

with open('/home/steven/Project/ns-3/src/lorawan/examples/Slist_allSF.txt') as g:
    Sdata_allSF = [float(S) for S in g.readlines()]

g.close()

print(Sdata_allSF)

with open('/home/steven/Project/ns-3/src/lorawan/examples/Glist_allSF.txt') as g:
    Gdata_allSF = [float(G) for G in g.readlines()]

g.close()

print(Gdata_allSF)

plt.plot(Gdata_allSF, Sdata_allSF)

with open('/home/steven/Project/ns-3/src/lorawan/examples/Slist_noSF12.txt') as g:
    Sdata_noSF12 = [float(S) for S in g.readlines()]

g.close()

print(Sdata_noSF12)

with open('/home/steven/Project/ns-3/src/lorawan/examples/Glist_noSF12.txt') as g:
    Gdata_noSF12 = [float(G) for G in g.readlines()]

g.close()

print(Gdata_noSF12)

plt.plot(Gdata_allSF, Sdata_allSF)
plt.plot(Gdata_noSF12, Sdata_noSF12, 'r--')

#plt.plot(G, S_theory, '--')
#plt.legend(["All SF", "Theory"])
#plt.show()

plt.grid()
plt.xlabel('G')
plt.ylabel('S')

plt.savefig('Fig5_fromfileTEST.png')