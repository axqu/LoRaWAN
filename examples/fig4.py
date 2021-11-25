import sys
import sem
import numpy as np
import matplotlib.pyplot as plt

import fig4a
import fig4b



def get_fig_4():
    runs = 50

    #G_SF7, S_SF7 = fig4a.runSimulation(runs)
    #G_1000, S_1000 = fig4b.runSimulation(runs, 1000, 20)

    Ga, Sa, Sa_theory = fig4a.runSimulation(runs, 3200, 20)
    Gb, Sb = fig4b.runSimulation(runs, 3200, 20)
    #Ga2000, Sa2000, Sa_theory2000 = fig4a.runSimulation(runs, 2000, 10)
    #Ga3000, Sa3000, Sa_theory3000 = fig4a.runSimulation(runs, 3000, 10)
    #Ga4000, Sa4000, Sa_theory4000 = fig4a.runSimulation(runs, 4000, 10)
    #Ga5000, Sa5000, Sa_theory5000 = fig4a.runSimulation(runs, 5000, 10)

    #Gb, Sb = fig4b.runSimulation(runs, 1000, 20)


    Psucc = np.array([0.0, 0.5])

    print("Plotting Figure 4")
    


    #plt.plot(G_SF7, S_SF7, 'b')
    #plt.plot(Psucc, Psucc, 'r:')
    #plt.legend(["All SF", "SF 7", "Psucc = 1"])
    #plt.plot(G_1000, S_1000, 'b')
    plt.plot(Ga, Sa, 'r--')
    plt.plot(Gb, Sb, 'k')
    plt.legend(['SF7', 'All SF'])
    plt.xlabel('G')
    plt.ylabel('S')
    #plt.plot(Ga2000, Sa2000, 'g')
    #plt.plot(Ga3000, Sa3000, 'c')
    #plt.plot(Ga4000, Sa4000, 'm')
    #plt.plot(Ga5000, Sa5000, 'k')
    #plt.legend(['Theory', '2km', '3km', '4km', '5km'])
    #plt.title('Packetsize 10, simulationTime 200')
    plt.grid()
    plt.ylim([0,0.4])
    plt.xlim([0,3.5])
    plt.title("Figure 4")
    plt.savefig('Fig4_diff.png')
    print("Figure 4 done")

