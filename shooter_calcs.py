def distance_in_yards(object_size_actual,object_size_mils):
    try:
        float(object_size_actual) and float(object_size_mils)
    except ValueError:
        return "Please enter a valid number."

    object_distance_yards = (float(object_size_actual)*27.8)/float(object_size_mils)
    return round(object_distance_yards,2)

def correction_moa(correction_inches_seen,known_distance):
    try:
        float(correction_inches_seen) and float(known_distance)
    except ValueError:
        return "Please enter a valid number."

    correction_required = float(correction_inches_seen)/(float(known_distance)/100)
    return round(correction_required,2)

def wind_correction(range_to_target,windspeed):
    try:
        float(range_to_target) and float(windspeed)
    except ValueError:
        return "Please enter a valid number."

    if float(range_to_target) <= 500:
        wind_correction_factor = ((float(range_to_target)/100)*float(windspeed))/15
        return wind_correction_factor
    if 500 < float(range_to_target) <= 600:
        wind_correction_factor = ((float(range_to_target)/100)*float(windspeed))/14
        return wind_correction_factor
    if 600 < float(range_to_target) <= 800:
         wind_correction_factor = ((float(range_to_target)/100)*float(windspeed))/13
         return wind_correction_factor
    if 800 < float(range_to_target) <= 900:
        wind_correction_factor = ((float(range_to_target)/100)*float(windspeed))/12
        return wind_correction_factor
    if 900 < float(range_to_target) <= 1000:
        wind_correction_factor = ((float(range_to_target)/100)*float(windspeed))/11
        return wind_correction_factor
    else:
        return "Shot is too far for windage rule"

def hw_tw_correction (range_to_target_hw_tw,windspeed_hw_tw,hw_or_tw):
    try:
        float(range_to_target_hw_tw) and float(windspeed_hw_tw)
    except ValueError:
        return "Please enter a valid number."
    hw_tw_correction_final = ((float(range_to_target_hw_tw)/100)*float(windspeed_hw_tw))/4
    return round(hw_tw_correction_final,2)