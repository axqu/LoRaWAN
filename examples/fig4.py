import sys
import sem
import numpy as np
import matplotlib.pyplot as plt

import fig4a
import fig4b



def get_fig_4():
    runs = 20

    #G_SF7, S_SF7 = fig4a.runSimulation(runs)
    G_1000, S_1000 = fig4b.runSimulation(runs, 5000, 20)


    Psucc = np.array([0.0, 0.5])

    print("Plotting Figure 4")
    
    plt.plot(G_1000, S_1000, 'b')

    #plt.plot(G_SF7, S_SF7, 'b')
    #plt.plot(Psucc, Psucc, 'r:')
    #plt.legend(["All SF", "SF 7", "Psucc = 1"])
    plt.plot(G_1000, S_1000, 'b')
    plt.grid()
    plt.ylim([0,0.4])
    plt.xlim([0,3.5])
    #plt.title("Figure 4")
    plt.savefig('Fig4_diff.png')
    print("Figure 4 done")

