import sys
import sem
import numpy as np
import matplotlib.pyplot as plt

import fig4a


def sim_duration(result):
    print(result)
    #outcomes = [float(a) for a in result['meta']['elapsed_time']]  
    outcomes = result['meta']['elapsed_time']  
    #print(outcomes)
    return outcomes

def G_psucc(result):
    outcomes = [float(a) for a in result['output']['stdout'].split()]    
    return outcomes[1]

def Stheory_psucc(result):
    #print(result)
    outcomes = [float(a) for a in result['output']['stdout'].split()]    
    return outcomes[2]

def S_psucc(result):
    outcomes = [float(a) for a in result['output']['stdout'].split()]    
    return outcomes[3]

#def G_psucc(result):
#    outcomes = [float(a) for a in result['output']['stdout'].split()]    
#    return outcomes[3]

def get_fig_4():
    print("fig_4")
    # Spreading Factor to DataRate mapping
    #  * SF7 -> DR5
    #  * SF8 -> DR4
    #  * SF9 -> DR3
    #  * SF10 -> DR2
    #  * SF11 -> DR1
    #  * SF12 -> DR0
    #header_size = 8

    # Create our SEM campaign
    ns_3_dir = '../../../'
    #script = 'aloha-throughput'
    script = 'figure4'
    results_dir = 'figure4-results'

    mylist = list(np.logspace(0.0, 3.2, num=50, endpoint=True))

    params = {
    #'nDevices': list(np.logspace(0.0, 3.0, num=50, endpoint=True)),
    'nDevices': mylist,
    'realisticChannelModel': True,
    'radius': 4000,
    'packetSize': 150
    }
    runs = 20

    print("nDevices:")
    print(params['nDevices'])

    campaign = sem.CampaignManager.new(ns_3_dir, script, results_dir,
                                   check_repo=False, overwrite=True)
    # Run simulations with the above parameter space
    campaign.run_missing_simulations(params, runs)

    #duration of SF7 message for fixed packet length
    duration = 0.256256
    simtime = 100


    G_sf7 = np.array(params['nDevices'])*duration/simtime

    duration = np.mean(campaign.get_results_as_numpy_array(params, sim_duration,
                                                            runs),
                        axis=-1).squeeze()

    #G = np.array(params['nDevices'])*duration
    #G = duration
    #print(G)

    S_theory = np.mean(campaign.get_results_as_numpy_array(params, Stheory_psucc,
                                                            runs),
                        axis=-1).squeeze()

    #G_theory = np.mean(campaign.get_results_as_numpy_array(params, Gtheory_psucc,
    #                                                    runs),
    #                axis=-1).squeeze()

    S = np.mean(campaign.get_results_as_numpy_array(params, S_psucc,
                                                            runs),
                        axis=-1).squeeze()

    G = np.mean(campaign.get_results_as_numpy_array(params, G_psucc,
                                                       runs),
                    axis=-1).squeeze()

    #print(succprobs)
    #S = np.multiply(succprobs_theory, G)
    S_sf7 = np.multiply(G_sf7, np.exp(-2*G_sf7))

    #plt.plot(G, S)
    plt.plot(G_sf7, S_sf7, 'm')
    plt.plot(G, S, 'b')
    plt.plot(G, S_theory, 'g--')
    plt.legend(["G_sf7", "All SF", "Theory (SF7 only)"])
    #plt.show()

    plt.grid()
    #plt.ylim([0,0.35])
    #plt.xlim([0,3.5])

    print("Plotting Figure 4")
    plt.title("Figure 4")
    plt.savefig('Fig4.png')

