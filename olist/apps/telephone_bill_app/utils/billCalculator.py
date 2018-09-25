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
    _call_free_time_start = 22
    _call_free_time_finish = 6
    _call_standing_charge = 0.36
    _bill_value = 0.00
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    """
    This piece of code is responsible to do the bill value calculation.
     
    It first validates if the call record pair has: 
        - a start time 
        - a finish time 
        - if its finish time is grater than its start time
        
    After that, it just use plain simulation to check if a minute should be charged or not.  
    It does that by checking the hour value of that minute. 
        - If its between 2200 and 0600, that minute is free of charge.
        - If not, that minute is charged. 
        
    The call standing charge is applied at the end of this logic. 
    """
    if call_finish_stamp and call_start_stamp and call_finish_stamp >= call_start_stamp:
        while call_start_stamp < call_finish_stamp:
            call_start_stamp += _call_cycle_time
            if _call_free_time_start > call_start_stamp.hour > _call_free_time_finish:
                _bill_value += _call_cycle_charge

    return _bill_value + _call_standing_charge
