

#include "ns3/lora-total-duration.h"
#include "ns3/nstime.h"


namespace ns3 {
namespace lorawan {


LoraTotalDuration::LoraTotalDuration ()
{
  m_totalDuration = NanoSeconds(0);
  durationSF7 = NanoSeconds(0);
  durationSF8 = NanoSeconds(0);
  durationSF9 = NanoSeconds(0);
  durationSF10 = NanoSeconds(0);
  durationSF11 = NanoSeconds(0);
  durationSF12 = NanoSeconds(0);

};

LoraTotalDuration::~LoraTotalDuration (){};


void LoraTotalDuration::UpdateTotalDuration(Time duration, uint8_t sf) const
{   
    m_totalDuration += duration;

    if(sf == 7)
    {
      SF7++;
      durationSF7 += duration;
    }
    if(sf == 8)
    {
      SF8++;
      durationSF8 += duration;
    }
    if(sf == 9)
    {
      SF9++;
      durationSF9 += duration;
    }
    if(sf == 10)
    {
      SF10++;
      durationSF10 += duration;
    }
    if(sf == 11)
    {
      SF11++;
      durationSF11 += duration;
    }
    if(sf == 12)
    {
      SF12++;
      durationSF12 += duration;
    }

   // std::cout << m_totalDuration << " " << SF7 << " " <<SF8 << " "<< SF9 << " "<< SF10 << " "<< SF11 << " "<< SF12 << std::endl;
}

Time LoraTotalDuration::getTotalDuration(void)
{
  return m_totalDuration;
}

void LoraTotalDuration::Reset(void)
{
    m_totalDuration = NanoSeconds(0);
    
}

}
}
