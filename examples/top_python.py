
import sys
import numpy as np
import matplotlib.pyplot as plt

import fig5

def main():

    G, S, S_theory = fig5.runSimulation(40, 7000, 20)
        #plt.plot(G, S)
    print("G")
    print(G)
    print("S")
    print(S)

    np.savetxt('Glist_allSF.txt', G, delimiter=',')
    np.savetxt('Slist_allSF.txt', S, delimiter=',')

    #np.savetxt('Glist_noSF12.txt', G, delimiter=',')
    #np.savetxt('Slist_noSF12.txt', S, delimiter=',')

    plt.plot(G, S)
    #plt.plot(G, S_theory, '--')
    #plt.legend(["All SF", "Theory"])
    #plt.show()

    plt.grid()
    plt.xlabel('G')
    plt.ylabel('S')
    #plt.ylim([0,0.4])
    #plt.xlim([0,3.5])
    #plt.ylim([0,0.35])
    #plt.xlim([0,3.5])

    print("plot Fig5")
    #plt.savefig('Fig5_noSF12.png')
    plt.savefig('Fig5_allSF.png')


    sys.exit()

if __name__ == "__main__":
    main()
