/*
 * This script simulates a complex scenario with multiple gateways and end
 * devices. The metric of interest for this script is the throughput of the
 * network.
 */
#include "/home/steven/Project/ns-3/src/lorawan/model/lora-total-duration.h"
#include "ns3/end-device-lora-phy.h"
#include "ns3/gateway-lora-phy.h"
#include "ns3/end-device-lorawan-mac.h"
#include "ns3/gateway-lorawan-mac.h"
#include "ns3/simulator.h"
#include "ns3/log.h"
#include "ns3/pointer.h"
#include "ns3/constant-position-mobility-model.h"
#include "ns3/lora-helper.h"
#include "ns3/node-container.h"
#include "ns3/mobility-helper.h"
#include "ns3/position-allocator.h"
#include "ns3/double.h"
#include "ns3/random-variable-stream.h"
#include "ns3/periodic-sender-helper.h"
#include "ns3/command-line.h"
#include "ns3/network-server-helper.h"
#include "ns3/correlated-shadowing-propagation-loss-model.h"
#include "ns3/building-penetration-loss.h"
#include "ns3/building-allocator.h"
#include "ns3/buildings-helper.h"
#include "ns3/forwarder-helper.h"
#include <algorithm>
#include <ctime>

using namespace ns3;
using namespace lorawan;

NS_LOG_COMPONENT_DEFINE ("figure4");

// Network settings
//int nDevices = 5853;
int nDevices = 200;
int nGateways = 1;
//double radius = 1000;
double radius = 5000;
//double simulationTime = 100;
double simulationTime = 20;

// Channel model
bool realisticChannelModel = true;
bool includeBuildings = false;

// Output control
bool print = true;

int appPeriodSeconds = simulationTime;
int transientPeriods = 0;

int packetSize = 150;



int
main (int argc, char *argv[])
{

  CommandLine cmd;
  cmd.AddValue ("nDevices", "Number of end devices to include in the simulation", nDevices);
  cmd.AddValue ("realisticChannelModel", "realisticChannelModel", realisticChannelModel);
  cmd.AddValue ("radius", "radius", radius);
  cmd.AddValue ("packetSize", "packetSize", packetSize);
  cmd.Parse (argc, argv);



  // Set up logging
  LogComponentEnable ("figure4", LOG_LEVEL_ALL);
  // Set up logging
  //LogComponentEnable ("AlohaThroughput", LOG_LEVEL_ALL);
  //LogComponentEnable ("Simulator", LOG_LEVEL_ALL);
  //LogComponentEnable ("GatewayLorawanMac", LOG_LEVEL_ALL);
  // LogComponentEnable("LoraFrameHeader", LOG_LEVEL_ALL);
  //LogComponentEnable("LorawanMacHeader", LOG_LEVEL_ALL);
  // LogComponentEnable("MacCommand", LOG_LEVEL_ALL);
  // LogComponentEnable("GatewayLoraPhy", LOG_LEVEL_ALL);
  //LogComponentEnable("LoraPhy", LOG_LEVEL_ALL);
  //LogComponentEnable("LoraChannel", LOG_LEVEL_ALL);
  // LogComponentEnable("SimpleEndDeviceLoraPhy", LOG_LEVEL_ALL);
  //LogComponentEnable("EndDeviceLoraPhy", LOG_LEVEL_ALL);
  //LogComponentEnable("LogicalLoraChannelHelper", LOG_LEVEL_ALL);
  //LogComponentEnable("LorawanMacHelper", LOG_LEVEL_ALL);
  //LogComponentEnable ("EndDeviceLorawanMac", LOG_LEVEL_ALL);
  //LogComponentEnable ("ClassAEndDeviceLorawanMac", LOG_LEVEL_ALL);
  // LogComponentEnable ("OneShotSender", LOG_LEVEL_ALL);
  // LogComponentEnable("PointToPointNetDevice", LOG_LEVEL_ALL);
  // LogComponentEnable ("Forwarder", LOG_LEVEL_ALL);
  // LogComponentEnable ("OneShotSender", LOG_LEVEL_ALL);
  //LogComponentEnable ("DeviceStatus", LOG_LEVEL_ALL);
  // LogComponentEnable ("GatewayStatus", LOG_LEVEL_ALL);
  //LogComponentEnable ("PropagationLossModel", LOG_LEVEL_ALL);
  //LogComponentEnable ("BuildingPenetrationLoss", LOG_LEVEL_ALL);

  //LogComponentEnable ("LoraPacketTracker", LOG_LEVEL_ALL);


  // Default matrix is goursaud
  if (realisticChannelModel)
  {      
    LoraInterferenceHelper::collisionMatrix = LoraInterferenceHelper::GOURSAUD;
  }
  else
  {
    Config::SetDefault ("ns3::EndDeviceLorawanMac::DataRate", UintegerValue (5));
    LoraInterferenceHelper::collisionMatrix = LoraInterferenceHelper::ALOHA;
  }

  /***********
   *  Setup  *
   ***********/

  // Create the time value from the period
  Time appPeriod = Seconds (appPeriodSeconds);

  // Mobility
  MobilityHelper mobility;
  mobility.SetPositionAllocator ("ns3::UniformDiscPositionAllocator", "rho", DoubleValue (radius),
                                 "X", DoubleValue (0.0), "Y", DoubleValue (0.0));
  mobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");

  /************************
   *  Create the channel  *
   ************************/

  // Create the lora channel object
  Ptr<LogDistancePropagationLossModel> loss = CreateObject<LogDistancePropagationLossModel> ();
  loss->SetPathLossExponent (3.76);
  //loss->SetReference (1, 7.7);
  loss->SetReference (1, 8.1);

  if (realisticChannelModel)
    {
      // Create the correlated shadowing component
      Ptr<CorrelatedShadowingPropagationLossModel> shadowing =
          CreateObject<CorrelatedShadowingPropagationLossModel> ();

      // Aggregate shadowing to the logdistance loss
      loss->SetNext (shadowing);

      // Add the effect to the channel propagation loss
      Ptr<BuildingPenetrationLoss> buildingLoss = CreateObject<BuildingPenetrationLoss> ();

      shadowing->SetNext (buildingLoss);
    }

  Ptr<PropagationDelayModel> delay = CreateObject<ConstantSpeedPropagationDelayModel> ();

  Ptr<LoraChannel> channel = CreateObject<LoraChannel> (loss, delay);

  /************************
   *  Create the helpers  *
   ************************/

  // Create the LoraPhyHelper
  LoraPhyHelper phyHelper = LoraPhyHelper ();
  phyHelper.SetChannel (channel);

  // Create the LorawanMacHelper
  LorawanMacHelper macHelper = LorawanMacHelper ();
  macHelper.SetRegion (LorawanMacHelper::ALOHA);
  //macHelper.SetRegion (LorawanMacHelper::EU);

  // Create the LoraHelper
  LoraHelper helper = LoraHelper ();
  helper.EnablePacketTracking (); // Output filename

  //Create the NetworkServerHelper
  NetworkServerHelper nsHelper = NetworkServerHelper ();

  //Create the ForwarderHelper
  ForwarderHelper forHelper = ForwarderHelper ();

  /************************
   *  Create End Devices  *
   ************************/

  // Create a set of nodes
  NodeContainer endDevices;
  endDevices.Create (nDevices);

  // Assign a mobility model to each node
  mobility.Install (endDevices);

  // Make it so that nodes are at a certain height > 0
  for (NodeContainer::Iterator j = endDevices.Begin (); j != endDevices.End (); ++j)
    {
      Ptr<MobilityModel> mobility = (*j)->GetObject<MobilityModel> ();
      Vector position = mobility->GetPosition ();
      position.z = 1.2;
      mobility->SetPosition (position);
    }

  // Create the LoraNetDevices of the end devices
  uint8_t nwkId = 54;
  uint32_t nwkAddr = 1864;
  Ptr<LoraDeviceAddressGenerator> addrGen =
      CreateObject<LoraDeviceAddressGenerator> (nwkId, nwkAddr);

  // Create the LoraNetDevices of the end devices
  macHelper.SetAddressGenerator (addrGen);
  phyHelper.SetDeviceType (LoraPhyHelper::ED);
  macHelper.SetDeviceType (LorawanMacHelper::ED_A);
  helper.Install (phyHelper, macHelper, endDevices);

  // Now end devices are connected to the channel

  // Connect trace sources
  for (NodeContainer::Iterator j = endDevices.Begin (); j != endDevices.End (); ++j)
    {
      Ptr<Node> node = *j;
      Ptr<LoraNetDevice> loraNetDevice = node->GetDevice (0)->GetObject<LoraNetDevice> ();
      Ptr<LoraPhy> phy = loraNetDevice->GetPhy ();
    }

  /*********************
   *  Create Gateways  *
   *********************/

  // Create the gateway nodes (allocate them uniformely on the disc)
  NodeContainer gateways;
  gateways.Create (nGateways);

  Ptr<ListPositionAllocator> allocator = CreateObject<ListPositionAllocator> ();
  // Make it so that nodes are at a certain height > 0
 allocator->Add (Vector (0.0, 0.0, 15.0));
  mobility.SetPositionAllocator (allocator);
  mobility.Install (gateways);

  // Create a netdevice for each gateway
  phyHelper.SetDeviceType (LoraPhyHelper::GW);
  macHelper.SetDeviceType (LorawanMacHelper::GW);
  helper.Install (phyHelper, macHelper, gateways);

  /**********************
   *  Handle buildings  *
   **********************/

      double xLength = 130;
      double deltaX = 32;
      double yLength = 64;
      double deltaY = 17;
      int gridWidth = 2 * radius / (xLength + deltaX);
      int gridHeight = 2 * radius / (yLength + deltaY);
      //if (realisticChannelModel == false)
      if (includeBuildings == false)
        {
          gridWidth = 0;
          gridHeight = 0;
        }
      Ptr<GridBuildingAllocator> gridBuildingAllocator;
      gridBuildingAllocator = CreateObject<GridBuildingAllocator> ();
      gridBuildingAllocator->SetAttribute ("GridWidth", UintegerValue (gridWidth));
      gridBuildingAllocator->SetAttribute ("LengthX", DoubleValue (xLength));
      gridBuildingAllocator->SetAttribute ("LengthY", DoubleValue (yLength));
      gridBuildingAllocator->SetAttribute ("DeltaX", DoubleValue (deltaX));
      gridBuildingAllocator->SetAttribute ("DeltaY", DoubleValue (deltaY));
      gridBuildingAllocator->SetAttribute ("Height", DoubleValue (6));
      gridBuildingAllocator->SetBuildingAttribute ("NRoomsX", UintegerValue (2));
      gridBuildingAllocator->SetBuildingAttribute ("NRoomsY", UintegerValue (4));
      gridBuildingAllocator->SetBuildingAttribute ("NFloors", UintegerValue (2));
      gridBuildingAllocator->SetAttribute (
          "MinX", DoubleValue (-gridWidth * (xLength + deltaX) / 2 + deltaX / 2));
      gridBuildingAllocator->SetAttribute (
          "MinY", DoubleValue (-gridHeight * (yLength + deltaY) / 2 + deltaY / 2));
      BuildingContainer bContainer = gridBuildingAllocator->Create (gridWidth * gridHeight);

      BuildingsHelper::Install (endDevices);
      BuildingsHelper::Install (gateways);

  /**********************************************
   *  Set up the end device's spreading factor  *
   **********************************************/
  if (realisticChannelModel)
  {
    std::vector<int> sfQuantity (6);
    sfQuantity = macHelper.SetSpreadingFactorsUp (endDevices, gateways, channel);

    std::string output ("");
    for (int i = 0; i < 6; ++i)
    {
      output += std::to_string (sfQuantity.at (i)) + " ";
    }
    //std::cout << "output results: " << output << std::endl;
  }


  if (print)
  {
    std::ofstream myfile;
    myfile.open ("/home/steven/Project/ns-3/src/lorawan/examples/endDevices.dat");
    std::vector<Ptr<Node>>::const_iterator it;
      for (NodeContainer::Iterator j = endDevices.Begin (); j != endDevices.End (); ++j)
      {
        
        Ptr<Node> object = *j;
        Ptr<MobilityModel> mobility = object->GetObject<MobilityModel> ();
        NS_ASSERT (mobility != 0);
        Vector position = mobility->GetPosition ();
        

        Ptr<NetDevice> netDevice = object->GetDevice (0);
        Ptr<LoraNetDevice> loraNetDevice = netDevice->GetObject<LoraNetDevice> ();
        NS_ASSERT (loraNetDevice != 0);

        Ptr<EndDeviceLorawanMac> mac = loraNetDevice->GetMac ()->GetObject<EndDeviceLorawanMac> ();
        int sf = int(mac->GetDataRate ());

        myfile << position.x << " " << position.y  << " " << sf << std::endl;

      }

    myfile.close ();
  }
  NS_LOG_DEBUG ("Completed configuration");

  /*********************************************
   *  Install applications on the end devices  *
   *********************************************/

  Time appStopTime = Seconds (simulationTime);
  PeriodicSenderHelper appHelper = PeriodicSenderHelper ();
  appHelper.SetPeriod (Seconds (appPeriodSeconds));
  //appHelper.SetPacketSize (150);
  appHelper.SetPacketSize (packetSize);
  appHelper.SetRealisticChannelModel (realisticChannelModel);
  Ptr<RandomVariableStream> rv = CreateObjectWithAttributes<UniformRandomVariable> (
      "Min", DoubleValue (0), "Max", DoubleValue (10));
  ApplicationContainer appContainer = appHelper.Install (endDevices);

  appContainer.Start (Seconds (0));
  appContainer.Stop (appStopTime);

  /**************************
   *  Create Network Server  *
   ***************************/

  // Create the NS node
  NodeContainer networkServer;
  networkServer.Create (1);

  // Create a NS for the network
  nsHelper.SetEndDevices (endDevices);
  nsHelper.SetGateways (gateways);
  nsHelper.Install (networkServer);

  //Create a forwarder for each gateway
  forHelper.Install (gateways);

  ////////////////
  // Simulation //
  ////////////////

  Simulator::Stop (appStopTime + Hours (1));

  NS_LOG_INFO ("Running simulation...");
  Simulator::Run ();

  Simulator::Destroy ();

  /////////////////////////////
  // Print results to stdout //
  /////////////////////////////
  NS_LOG_INFO ("Computing performance metrics...");

  LoraPacketTracker &tracker = helper.GetPacketTracker ();  

 // std::cout << tracker.PrintPhyPacketsPerGw (Seconds (0), appStopTime + Hours (1), nDevices) << std::endl;

  std::vector<int> packetresults (6);
  packetresults = tracker.CountPhyPacketsPerGw(Seconds (0), appStopTime + Hours (1), nDevices);
/*
    std::string output ("");
    for (int i = 0; i < 6; ++i)
    {
      output += std::to_string (packetresults.at (i)) + " ";
    }
*/
  //Time t = channel -> getTotalDuration();

  double t = channel -> getTotalDuration().GetSeconds();
  
  //double G = nDevices * (0.256256/simulationTime);
  double G = t / simulationTime;
 

  // G = for all packets, sum: (time packets occupy channel / total time of simulation)
  //double G =  t.GetSeconds() / simulationTime;
  //S = G * (number of packets recieved at GW / number of packets sent)
  double S = G * packetresults.at (1) / packetresults.at (0);
  double S_theory = G * exp(-2*G) ;
  
  //std::cout << "output results: " << output << "  total duration: " << t << std::endl;
  std::cout << nDevices ;
  std::cout << " " << G;
  std::cout << " " << S_theory;
  std::cout << " " << S;
  std::cout << " " << t << std::endl;

  return 0;
}