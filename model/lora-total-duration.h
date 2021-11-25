/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2017 University of Padova
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Author: Davide Magrin <magrinda@dei.unipd.it>
 *
 * The structure of this class is inspired by the YansWifiChannel
 * contained in the WiFi module.
 */

#ifndef LORA_TOTAL_DURATION_H
#define LORA_TOTAL_DURATION_H
#include "ns3/nstime.h"

namespace ns3 {
namespace lorawan {

class LoraTotalDuration
{
public:  
  // Constructor and destructor
  LoraTotalDuration ();
  virtual ~LoraTotalDuration ();

  void UpdateTotalDuration(Time duration, uint8_t sf) const;
  Time getTotalDuration(void);

  void Reset(void);


private:
  mutable  Time m_totalDuration;
  mutable int SF7=0, SF8=0, SF9=0, SF10=0,SF11=0, SF12=0;
  mutable Time durationSF7, durationSF8, durationSF9, durationSF10, durationSF11, durationSF12;
  //mutable Time m_totalDuration;
  //mutable int SF7=0, SF8=0, SF9=0, SF10=0,SF11=0, SF12=0;
  //mutable Time durationSF7, durationSF8, durationSF9, durationSF10, durationSF11, durationSF12;

};

} /* namespace ns3 */

}
#endif /* LORA_TOTAL_DURATION_H */
