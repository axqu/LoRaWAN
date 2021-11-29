

#include "ns3/lora-total-duration.h"
#include "ns3/nstime.h"


namespace ns3 {
namespace lorawan {


LoraTotalDuration::LoraTotalDuration ()
{
  m_packetTimes = { NanoSeconds(0), NanoSeconds(0), \
                    NanoSeconds(0), NanoSeconds(0), \
                    NanoSeconds(0), NanoSeconds(0)};
};

LoraTotalDuration::~LoraTotalDuration (){};


void 
LoraTotalDuration::UpdateTotalDuration(Time duration, uint8_t sf) const
{   
    
    if(sf == 7)
    {
      m_packetTimes.at (0) =  m_packetTimes.at (0) + duration;
    }
    if(sf == 8)
    {
      m_packetTimes.at (1) =  m_packetTimes.at (1) + duration;
    }
    if(sf == 9)
    {
      m_packetTimes.at (2) =  m_packetTimes.at (2) + duration;
    }
    if(sf == 10)
    {
      m_packetTimes.at (3) =  m_packetTimes.at (3) + duration;
    }
    if(sf == 11)
    {
      m_packetTimes.at (4) =  m_packetTimes.at (4) + duration;
    }
    if(sf == 12)
    {
      m_packetTimes.at (5) =  m_packetTimes.at (5) + duration;
    }

}

std::vector<Time>
LoraTotalDuration::getTotalDuration(void)
{
  return m_packetTimes;
}



void LoraTotalDuration::Reset(void)
{
    //m_totalDuration = NanoSeconds(0);
    
}

}
}
