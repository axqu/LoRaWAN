import sem
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#campaign = sem.CampaignManager.new(ns_3_dir, script, results_dir,
#                                   check_repo=False, overwrite=True)

#runs = 20

def get_psucc(result):
    """
    Extract the probability of success from the simulation output
    """
    outcomes = [float(a) for a in result['output']['stdout'].split()]
    #print(result)
    if outcomes[0] == 0:
        return 0
    else:
        return outcomes[1]/outcomes[0]

def get_fig_3():
    print("Figure 3")

    # Create our SEM campaign
    ns_3_dir = '../../../'
    #script = 'aloha-throughput'
    script = 'figure3'
    results_dir = 'figure3-results'

    # DR5/SF7. Max Packet size: Not Defined
    params = {
        'nDevices': list(np.logspace(0, 3, num=50)),
    }
    runs = 50

    print("Start Campaign")
    print("runs: ", runs)
    print("devices: ", len(params['nDevices']))
    campaign = sem.CampaignManager.new(ns_3_dir, script, results_dir,
                                   check_repo=False, overwrite=True)
    # Run simulations with the above parameter space
    campaign.run_missing_simulations(params, runs)

    duration = 0.256256
    simtime = 100
    G = np.array(params['nDevices'])*duration/simtime

    succprobs = np.mean(campaign.get_results_as_numpy_array(params, get_psucc,
                                                            runs),
                        axis=-1).squeeze()

    S = np.multiply(succprobs, G)
    S_theory = np.multiply(G, np.exp(-2*G))

    plt.plot(G, S)
    plt.plot(G, S_theory, '--')
    plt.grid()
    plt.legend(["LoRaWAN module", "Theory"])
    #plt.show()
    print("Plotting Figure 3")
    plt.title("Figure 3")
    plt.savefig('Fig3.png')
