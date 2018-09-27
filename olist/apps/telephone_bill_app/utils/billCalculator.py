from datetime import time

from django.utils.timezone import timedelta


def billing_calculator(call_start_stamp, call_finish_stamp):
    """
    A phone bill calculator
    :param call_start_stamp: a call pair start timestamp
    :param call_finish_stamp:  a call pair finish timestamp
    :return _bill_value: a bill value
    """

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    CALL PRICING RULES
    BE CAREFUL - CHANGES DONE TO THESE VALUES CAN IMPLY ON BILL MISCALCULATIONS  
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    _call_cycle_charge = 0.09
    _call_cycle_time = timedelta(seconds=60)
    _call_free_time_start = time(22, 00)
    _call_free_time_finish = time(6, 00)
    _call_standing_charge = 0.36
    _call_cycle_counter = timedelta()
    _time_part = timedelta(seconds=1)
    _bill_value = 0.00
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    """
    This piece of code is responsible for the bill value calculation.
     
    It first validates if the call record pair has: 
        - a start time 
        - a finish time 
        - if its finish time is grater than its start time
        
    After that, it just use plain simulation to check if a minute should be charged or not.  
    It does that by checking the time of that minute. 
        - If its grater than 2200 and less than 0600 -> that minute is not charged.
        - If not, that minute is charged. 
        
    The call standing charge is applied at the end of this logic. 
    """
    if call_finish_stamp and call_start_stamp and call_finish_stamp >= call_start_stamp:
        while call_start_stamp < call_finish_stamp:
            call_start_stamp += _time_part
            _call_cycle_counter += _time_part

            if _call_cycle_counter == _call_cycle_time:
                if _call_free_time_start > call_start_stamp.time() > _call_free_time_finish:
                    _bill_value += _call_cycle_charge

                _call_cycle_counter = timedelta()

    return _bill_value + _call_standing_charge
