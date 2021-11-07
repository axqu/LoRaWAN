import sys
import sem
import numpy as np
import matplotlib.pyplot as plt


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

def get_fig_5():
    print("fig_5")
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
    script = 'figure5'
    results_dir = 'aloha-results'

    params = {
    'nDevices': list(np.logspace(0.0, 3.0, num=50, endpoint=True))
    #'nDevices': [100, 200, 500, 1000, 2000, 3000]
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
    #duration = 0.256256
    simtime = 100

    #G = np.array(params['nDevices'])*duration/simtime

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
    #S_theory = np.multiply(G_theory, np.exp(-2*G_theory))

    #plt.plot(G, S)
    plt.plot(G, S)
    plt.plot(G, S_theory, '--')
    plt.legend(["All SF", "Theory"])
    #plt.show()

    plt.grid()
    #plt.ylim([0,0.35])
    #plt.xlim([0,3.5])

    #print("plot Fig5")
    plt.savefig('Fig5.png')

if __name__ == '__main__':
    sys.exit(get_fig_5())

#if __name__ == "__main__":
#    main()
