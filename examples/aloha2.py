#import sem
import sys
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker

import fig3
import fig4
import fig5


def main():
    #fig3.get_fig_3()
    #fig4.get_fig_4()
    fig5.get_fig_5()
    sys.exit()

if __name__ == "__main__":
    main()


#campaign = sem.CampaignManager.new(ns_3_dir, script, results_dir,
#                                   check_repo=False, overwrite=True)

#runs = 20

#def get_psucc(result):
#    """
#    Extract the probability of success from the simulation output
#    """
#    outcomes = [float(a) for a in result['output']['stdout'].split()]
#    #print(result)
#    if outcomes[0] == 0:
#        return 0
#    else:
#        return outcomes[1]/outcomes[0]
#
#def fig_3():
#    print("fig_3")
#
#    # Create our SEM campaign
#    ns_3_dir = '../../../'
#    script = 'aloha-throughput'
#    results_dir = 'aloha-results'
#
#    # DR5/SF7. Max Packet size: Not Defined
#    params = {
#        'nDevices': list(np.logspace(0, 3, num=50)),
#        'DR': 5,
#        'packetSize': 150
#        #'realisticChannelModel': 0
#    }
#    runs = 20
#
#    campaign = sem.CampaignManager.new(ns_3_dir, script, results_dir,
#                                   check_repo=False, overwrite=True)
#    # Run simulations with the above parameter space
#    campaign.run_missing_simulations(params, runs)
#
#    duration = 0.256256
#    simtime = 100
#    G = np.array(params['nDevices'])*duration/simtime
#
#    succprobs = np.mean(campaign.get_results_as_numpy_array(params, get_psucc,
#                                                            runs),
#                        axis=-1).squeeze()
#
#    S = np.multiply(succprobs, G)
#    S_theory = np.multiply(G, np.exp(-2*G))
#
#    plt.plot(G, S)
#    plt.plot(G, S_theory, '--')
#    plt.legend(["LoRaWAN module", "Theory"])
#    #plt.show()
#    print("plot Fig3")
#    plt.savefig('Fig3.png')


#def fig_4():
#    print("fig_4")
#    # Spreading Factor to DataRate mapping
#    #  * SF7 -> DR5
#    #  * SF8 -> DR4
#    #  * SF9 -> DR3
#    #  * SF10 -> DR2
#    #  * SF11 -> DR1
#    #  * SF12 -> DR0
#    header_size = 8
#
#    # Create our SEM campaign
#    ns_3_dir = '../../../'
#    script = 'aloha-throughput'
#    results_dir = 'aloha-results'
#
#    params = {
#    'nDevices': list(np.logspace(0.0, 3.0, num=50, endpoint=True)),
#    'DR': 0,
#    #'realisticChannelModel': 1,
#    'packetSize': 11
#    }
#    runs = 5
#    succprobs = np.zeros(len(params.get('nDevices')))
#    a = np.zeros(len(params.get('nDevices')))
##std::vector<uint32_t>{59, 59, 59, 123, 230, 230, 230, 230});
#    for x in range(0,6,1):  
#        params['DR'] = x        
#        if x == 0:
#            # DR0/SF12. Max Packet size: N=51
#            params['packetSize'] = 59 - header_size        
#        elif x == 1:
#            # DR1/SF11. Max Packet size: N=51
#            params['packetSize'] = 59 - header_size
#        elif x == 2:
#            # DR2/SF10. Max Packet size: N=51
#            params['packetSize'] = 59 - header_size
#        elif x == 3:
#            # DR3/SF9. Max Packet size: N=115
#            params['packetSize'] = 123 - header_size 
#        elif x == 4:
#            # DR4/SF8. Max Packet size: N=222
#            params['packetSize'] = 230 - header_size         
#        elif x == 5:
#            # DR5/SF7. Max Packet size: Not Defined
#            params['packetSize'] = 230 - header_size
#
#        print("x= ",x) 
#        print("runs= ",runs)
#        print("nDevices= ",len(params['nDevices']))  
#        print("DR= ",params['DR'])
#        print("packetSize= ",params['packetSize'])
#        #print("realisticChannelModel= ",params['realisticChannelModel'])
#
#        campaign = sem.CampaignManager.new(ns_3_dir, script, results_dir,
#                                    check_repo=False, overwrite=True)
#
#        # Run simulations with the above parameter space
#        campaign.run_missing_simulations(params, runs)
#        a = np.mean(campaign.get_results_as_numpy_array(params, get_psucc, runs), axis=-1).squeeze()
#        #print(a)
#        if x == 0:
#            succprobs = a
#        else:
#            succprobs = np.vstack((succprobs, a))
#
#        print(succprobs)
#        print("-------------------------")
#
#    #succprobs = np.asarray(succprobs)
#    #print(succprobs)
#
#    # Get the maximum values of each column i.e. along axis 0
#    maxInColumns = np.amax(succprobs, axis=0)
#    print('Max value of every column: \n', maxInColumns)
#    print("plot fig4")
#    duration = 0.356356
#    simtime = 100
#    G = np.array(params['nDevices'])*duration/simtime
#
#    #succprobs = np.mean(campaign.get_results_as_numpy_array(params, get_psucc,
#    #                                                        runs),
#    #                    axis=-1).squeeze()
#
#    maxS = np.multiply(maxInColumns, G)
#    #S = np.multiply(succprobs, G)
#    S_theory = np.multiply(G, np.exp(-2*G))
#
#    plt.plot(G, maxS, 'r--')
#    #annot_max(G,maxS)
#    #plt.plot(G, S)
#    plt.plot(G, S_theory, '--')
#    plt.legend(["All SF", "SF7"])
#    plt.plot(G, G, ':')
#    #@plt.legend(["All SF", "SF7", "Psucc = 1"])
#    #plt.legend(["SF12", "Theory"])
#    #plt.show()
#    plt.grid()
#    plt.ylim([0,0.4])
#    plt.xlim([0,3.5])
#
#    plt.savefig('Fig4.png')
#
#    print('maxS: \n', maxS)
#    print('S_theory: \n', S_theory)
#    print('G: \n', G)
#
#def annot_max(x,y, ax=None):
#    xmax = x[np.argmax(y)]
#    ymax = y.max()
#    text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
#    if not ax:
#        ax=plt.gca()
#
#    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
#
#    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
#
#    kw = dict(xycoords='data',textcoords="axes fraction",
#            arrowprops=arrowprops, bbox=bbox_props, ha="right", va="center")
#
#    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)


