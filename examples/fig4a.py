import sys
import sem
import numpy as np
import matplotlib.pyplot as plt



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

def clearDatFile():
    file = open("/home/steven/Project/ns-3/src/lorawan/examples/endDevices.dat","r+")
    file.truncate(0)
    file.close()

def runSimulation(runs):
    print("Begin Figure 4a simulation")
    #clearDatFile()
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
    results_dir = 'figure4a-results'


    params = {
    'nDevices': list(np.logspace(0.0, 3.0, num=50, endpoint=True)),
    'realisticChannelModel': False,
    'radius': 4000,
    'packetSize': 10
    }
    #runs = 20

    #print(params['nDevices'])
    print("max number of ED: ", np.amax(params['nDevices']) )
    print("min number of ED: ", np.amin(params['nDevices']) )
    print("number of runs/simulation: ", runs )

    campaign = sem.CampaignManager.new(ns_3_dir, script, results_dir,
                                check_repo=False, overwrite=True)

    # Run simulations with the above parameter space
    campaign.run_missing_simulations(params, runs)

    S_theory = np.mean(campaign.get_results_as_numpy_array(params, Stheory_psucc,
                                                            runs),
                        axis=-1).squeeze()

    S = np.mean(campaign.get_results_as_numpy_array(params, S_psucc,
                                                            runs),
                        axis=-1).squeeze()

    G = np.mean(campaign.get_results_as_numpy_array(params, G_psucc,
                                                    runs),
                    axis=-1).squeeze()

    return G,S

