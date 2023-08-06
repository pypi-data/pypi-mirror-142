"""
  Copyright (c) 2016- 2021, Wiliot Ltd. All rights reserved.

  Redistribution and use of the Software in source and binary forms, with or without modification,
   are permitted provided that the following conditions are met:

     1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

     2. Redistributions in binary form, except as used in conjunction with
     Wiliot's Pixel in a product or a Software update for such product, must reproduce
     the above copyright notice, this list of conditions and the following disclaimer in
     the documentation and/or other materials provided with the distribution.

     3. Neither the name nor logo of Wiliot, nor the names of the Software's contributors,
     may be used to endorse or promote products or services derived from this Software,
     without specific prior written permission.

     4. This Software, with or without modification, must only be used in conjunction
     with Wiliot's Pixel or with Wiliot's cloud service.

     5. If any Software is provided in binary form under this license, you must not
     do any of the following:
     (a) modify, adapt, translate, or create a derivative work of the Software; or
     (b) reverse engineer, decompile, disassemble, decrypt, or otherwise attempt to
     discover the source code or non-literal aspects (such as the underlying structure,
     sequence, organization, ideas, or algorithms) of the Software.

     6. If you create a derivative work and/or improvement of any Software, you hereby
     irrevocably grant each of Wiliot and its corporate affiliates a worldwide, non-exclusive,
     royalty-free, fully paid-up, perpetual, irrevocable, assignable, sublicensable
     right and license to reproduce, use, make, have made, import, distribute, sell,
     offer for sale, create derivative works of, modify, translate, publicly perform
     and display, and otherwise commercially exploit such derivative works and improvements
     (as applicable) in conjunction with Wiliot's products and services.

     7. You represent and warrant that you are not a resident of (and will not use the
     Software in) a country that the U.S. government has embargoed for use of the Software,
     nor are you named on the U.S. Treasury Department’s list of Specially Designated
     Nationals or any other applicable trade sanctioning regulations of any jurisdiction.
     You must not transfer, export, re-export, import, re-import or divert the Software
     in violation of any export or re-export control laws and regulations (such as the
     United States' ITAR, EAR, and OFAC regulations), as well as any applicable import
     and use restrictions, all as then in effect

   THIS SOFTWARE IS PROVIDED BY WILIOT "AS IS" AND "AS AVAILABLE", AND ANY EXPRESS
   OR IMPLIED WARRANTIES OR CONDITIONS, INCLUDING, BUT NOT LIMITED TO, ANY IMPLIED
   WARRANTIES OR CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, NONINFRINGEMENT,
   QUIET POSSESSION, FITNESS FOR A PARTICULAR PURPOSE, AND TITLE, ARE DISCLAIMED.
   IN NO EVENT SHALL WILIOT, ANY OF ITS CORPORATE AFFILIATES OR LICENSORS, AND/OR
   ANY CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
   OR CONSEQUENTIAL DAMAGES, FOR THE COST OF PROCURING SUBSTITUTE GOODS OR SERVICES,
   FOR ANY LOSS OF USE OR DATA OR BUSINESS INTERRUPTION, AND/OR FOR ANY ECONOMIC LOSS
   (SUCH AS LOST PROFITS, REVENUE, ANTICIPATED SAVINGS). THE FOREGOING SHALL APPLY:
   (A) HOWEVER CAUSED AND REGARDLESS OF THE THEORY OR BASIS LIABILITY, WHETHER IN
   CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE);
   (B) EVEN IF ANYONE IS ADVISED OF THE POSSIBILITY OF ANY DAMAGES, LOSSES, OR COSTS; AND
   (C) EVEN IF ANY REMEDY FAILS OF ITS ESSENTIAL PURPOSE.
"""

from time import sleep
from collections import Counter
import json
import numpy as np
import pandas as pd
from pathlib import Path
import serial

from wiliot.gateway_api.gateway import *

from wiliot.packet_data_tools.multi_tag import MultiTag
from wiliot.packet_data_tools.packet_list import PacketList
from wiliot.packet_data_tools.packet import Packet

from wiliot.wiliot_testers.test_equipment import Attenuator, EquipmentError
from wiliot.wiliot_testers.tester_utils import update_json_field


def set_attn_power(external_attn, attn_obj, gw_obj, attn_power):
    """
    configure Attenuator to a specific value
    gets:
        attn_obj:       Attenuator obj
        attn_power:     value to set attn

    return:
        status if Attenuator is set correctly

    """
    status = True
    if not external_attn:
        try:
            gw_obj.set_gw_output_power_by_index(attn_power)
        except:
            status = False
    else:
        print('Setting Attenuator to {attn_power}dB'.format(attn_power=attn_power))
        attn_obj.Setattn(attn_power)
        sleep(2)

        attn_current_config = attn_obj.Getattn()
        if (float(attn_current_config) - attn_power) != 0:
            print('Error setting ATTENUATOR')
            status = False
        print(
            "Attenuator is set to: {attn_current_config} dB".format(
                attn_current_config=attn_current_config.split('.')[0]))
    return status


def build_range(target_range):
    new_range = range(target_range[0], target_range[-1])
    if len(target_range) > 2:
        new_range = range(target_range[0], target_range[-1], target_range[1])
    return new_range


def get_statistics(gw_obj, external_attn, attn_obj, attn_power, energy_pattern_val, time_profile_on=5,
                   time_profile_period=15):
    multi_tag = MultiTag()
    gw_obj.config_gw(time_profile_val=[0, 6])
    set_attn_power(external_attn, attn_obj, gw_obj, attn_power)
    sleep(1)
    gw_obj.reset_buffer()
    gw_obj.reset_listener()
    gw_obj.config_gw(filter_val=True, pacer_val=0, energy_pattern_val=energy_pattern_val,
                     time_profile_val=[time_profile_on, time_profile_period], received_channel=37,
                     beacons_backoff_val=0)

    gw_answer = gw_obj.start_get_packets(action_type=ActionType.FIRST_SAMPLES, num_of_packets=100, max_time=20)
    for packet in gw_answer.packet_list:
        multi_tag.append(packet)
    sleep(3)
    multi_tag_statistics = multi_tag.get_statistics()
    if multi_tag_statistics.empty:
        return multi_tag_statistics

    multi_tag_statistics['absGwTxPowerIndex'] = attn_power
    multi_tag_statistics['abs_power'] = gw_obj.valid_output_power_vals[attn_power]['abs_power']
    multi_tag_statistics['gw_output_power'] = gw_obj.valid_output_power_vals[attn_power]['gw_output_power']
    multi_tag_statistics['bypass_pa'] = gw_obj.valid_output_power_vals[attn_power]['bypass_pa']
    multi_tag_statistics['time_profile_on'] = time_profile_on
    multi_tag_statistics['time_profile_period'] = time_profile_period

    optimal_tag_statistics = multi_tag_statistics[
        multi_tag_statistics.rssi_mean == multi_tag_statistics.rssi_mean.min()]
    return optimal_tag_statistics


def start_calibration(target_tbp=100, sweep_scan=[12, 1, 18], time_profiles_on=[5], time_profiles_period=[15],
                      external_attn=False, inlay_type='Single Band'):
    """
    calibration process
    :type inlay_type: string
    :param inlay_type: will determine the energizing patterns we will use

    return:
        df with closest tbp value to target
    """
    if inlay_type == 'Single Band':
        energy_pattern_values = [18]
    else:
        energy_pattern_values = [18, 51]

    attn_obj = None
    # create equipment objects
    if external_attn:
        try:
            attn_obj = Attenuator('API').GetActiveTE()
            current_attn = attn_obj.Getattn()
        except Exception as e:
            raise EquipmentError('Attenuator Error - Verify Attenuator connection')

    try:
        gw_obj = WiliotGateway(auto_connect=True, logger_name='root', verbose=False)
        gw_obj.write('!set_tester_mode 1')
        gw_obj.write('!listen_to_tag_only 1')

        if not gw_obj.get_connection_status()[0]:
            raise EquipmentError('Gateway Error - Verify WiliotGateway connection')
    except Exception as e:
        raise EquipmentError('Gateway Error - Verify WiliotGateway connection')
        gw_obj.close_port()

    for energy_pattern_val in energy_pattern_values:
        attn_range = build_range(sweep_scan)

        statistics_df = pd.DataFrame()

        gw_obj.config_gw(filter_val=True, pacer_val=0, energy_pattern_val=energy_pattern_val, time_profile_val=[5, 15],
                         received_channel=37, beacons_backoff_val=0)
        sleep(2)

        gw_obj.start_continuous_listener()
        for attn_power in attn_range:
            print('attn_power: ' + str(attn_power))
            optimal_tag_statistics = get_statistics(gw_obj, external_attn, attn_obj, attn_power, energy_pattern_val,
                                                    time_profile_on=int(
                                                        (time_profiles_on[0] + time_profiles_on[-1]) / 2),
                                                    time_profile_period=int(
                                                        (time_profiles_period[0] + time_profiles_period[-1]) / 2))
            if optimal_tag_statistics.empty:
                print('skipped')
                continue
            statistics_df = pd.concat([statistics_df, optimal_tag_statistics], axis=0)

        print(statistics_df)
        top_score = statistics_df.iloc[(statistics_df['tbp_mean'] - target_tbp).abs().argsort()[1:3]]

        if time_profiles_on != [5] or time_profiles_period != [15]:
            if time_profiles_on != [5]:
                time_profiles_on = build_range(time_profiles_on)
            if time_profiles_period != [15]:
                time_profiles_period = build_range(time_profiles_period)
            for index, row in top_score.iterrows():
                attn_power = row['absGwTxPowerIndex']
                for tpo in time_profiles_on:
                    for tpp in time_profiles_period:
                        print('time_profiles_on: ' + str(tpo) + '/time_profiles_period: ' + str(tpp))
                        optimal_tag_statistics = get_statistics(gw_obj, external_attn, attn_obj, attn_power,
                                                                energy_pattern_val, time_profile_on=tpo,
                                                                time_profile_period=tpp)
                        if optimal_tag_statistics.empty:
                            print('skipped')
                            continue
                        statistics_df = pd.concat([statistics_df, optimal_tag_statistics], axis=0)

        gw_obj.stop_continuous_listener()
        gw_obj.close_port()

        top_score = statistics_df.iloc[(statistics_df['tbp_mean'] - target_tbp).abs().argsort()[:1]]

        return top_score


# main
if __name__ == '__main__':
    start_calibration(sweep_scan=[12, 1, 18], time_profiles_period=[8, 1, 15])
