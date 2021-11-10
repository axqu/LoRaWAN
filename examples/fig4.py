import sys
import sem
import numpy as np
import matplotlib.pyplot as plt

import fig4a
import fig4b



def get_fig_4():
    runs = 20

    #G_SF7, S_SF7 = fig4a.runSimulation(runs)
    G_1000, S_1000 = fig4b.runSimulation(runs, 1000)
    G_1500, S_1500 = fig4b.runSimulation(runs, 1500)
    G_2000, S_2000 = fig4b.runSimulation(runs, 2000)
    G_2500, S_2500 = fig4b.runSimulation(runs, 2500)
    G_3000, S_3000 = fig4b.runSimulation(runs, 3000)
    G_3500, S_3500 = fig4b.runSimulation(runs, 3500)

    Psucc = np.array([0.0, 0.5])

    print("Plotting Figure 4")
    
    plt.plot(G_1000, S_1000, 'b')
    plt.plot(G_1500, S_1500, 'g')
    plt.plot(G_2000, S_2000, 'r')
    plt.plot(G_2500, S_2500, 'y')
    plt.plot(G_3000, S_3000, 'k')
    plt.plot(G_3500, S_3500, 'c')
    #plt.plot(G_SF7, S_SF7, 'b')
    #plt.plot(Psucc, Psucc, 'r:')
    #plt.legend(["All SF", "SF 7", "Psucc = 1"])
    plt.grid()
    plt.ylim([0,0.4])
    plt.xlim([0,3.5])
    #plt.title("Figure 4")
    plt.savefig('Fig4_diffradiusandpacketsize.png')
    print("Figure 4 done")

