import sys
import sem
import numpy as np
import matplotlib.pyplot as plt

import fig4a
import fig4b



def get_fig_4():
    runs = 50

    G_SF7, S_SF7 = fig4a.runSimulation(runs)
    G_AllSF, S_AllSF = fig4b.runSimulation(runs)

    print("Plotting Figure 4")
    plt.plot(G_SF7, S_SF7, 'b')
    plt.plot(G_AllSF, S_AllSF, 'm')
    #plt.plot(G, S_theory, 'g--')
    plt.legend(["All SF"])
    plt.grid()
    plt.title("Figure 4")
    plt.savefig('Fig4.png')
    print("Figure 4 done")

