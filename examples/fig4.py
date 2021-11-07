import sem
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import json

def get_elapsedtime(result):
#    """
#    Extract the probability of success from the simulation output
#    """
    #print(result)
    #return 0
    #f = open("./savefiles/fig3results.txt", "a")
    #f.write(json.dumps(result))
    #f.close()
    print(result['meta']['elapsed_time'])
    #outcomes = [float(a) for a in result['meta']['elapsed_time']]
    #print(outcomes[0])
    return result['meta']['elapsed_time']


def get_prob_tp(result):
#    """
#    Extract the probability of success from the simulation output
#    """
    #print(result)
    #return 0
    #f = open("./savefiles/fig3results.txt", "a")
    #f.write(json.dumps(result))
    #f.close()
    outcomes = [float(a) for a in result['output']['stdout'].split()]
    #print(outcomes[6])
    if outcomes[6] == 0:
        return 0
    else:
        return outcomes[6]

def get_psucc(result):
#    """
#    Extract the probability of success from the simulation output
#    """
    #print(result)
    #return 0
    #f = open("./savefiles/fig3results.txt", "a")
    #f.write(json.dumps(result))
    #f.close()
    outcomes = [float(a) for a in result['output']['stdout'].split()]
    #print(outcomes[6])
    if outcomes[0] == 0:
        return 0
    else:
        return outcomes[1]/outcomes[0]

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
    results_dir = 'aloha-results'

    params = {
    #'nDevices': list(np.logspace(0.0, 3.0, num=50, endpoint=True))
    'nDevices': list(np.logspace(0.0, 4.136, num=50, endpoint=True)),
    #'DR': 0,
    #'packetSize': 150
    }
    runs = 20

    print("nDevices:")
    print(params['nDevices'])

    campaign = sem.CampaignManager.new(ns_3_dir, script, results_dir,
                                   check_repo=False, overwrite=True)
    # Run simulations with the above parameter space
    campaign.run_missing_simulations(params, runs)

    #duration of SF7 message for fixed packet length
    #duration = 0.256256
    duration = 0.256256
    simtime = 100
    #print("nDevices:")
    #print(params['nDevices'])
    G = np.array(params['nDevices'])*duration/simtime

    print("G:")
    print(G)

    #etprobs = np.mean(campaign.get_results_as_numpy_array(params, get_elapsedtime,
    #                                                        runs),
    #                    axis=-1).squeeze()
    #print("etprobs:")
    #print(etprobs)

    #tpprobs = np.mean(campaign.get_results_as_numpy_array(params, get_prob_tp,
    #                                                        runs),
    #                    axis=-1).squeeze()
    #print("tpprobs:")
    #print(tpprobs)

    #print("tpprobs/100:")
    #print(tpprobs/100)

    succprobs = np.mean(campaign.get_results_as_numpy_array(params, get_psucc,
                                                            runs),
                        axis=-1).squeeze()

    #print("succprobs:")
    #print(succprobs)

    #E = np.multiply(succprobs, etprobs)

    #T = np.multiply(succprobs, tpprobs/100)

    S = np.multiply(succprobs, G)
    S_theory = np.multiply(G, np.exp(-2*G))

    #print("T:")
    #print(T)

    #print("S:")
    #print(S)

    #plt.plot(etprobs, E)
    #plt.plot(tpprobs/100, T)
    plt.plot(G, S)
    plt.plot(G, S_theory, '--')
    plt.legend(["All SF", "Theory"])
    plt.title("r=6400");
    #plt.show()
    plt.grid()
    #plt.ylim([0,0.35])
    plt.xlim([0,3.5])

    print("plot Fig4")
    plt.savefig('Fig4a.png')

