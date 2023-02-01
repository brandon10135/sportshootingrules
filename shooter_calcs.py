import pandas as pd


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

def new_range_zero(sight_height,known_zero_range,desired_zero_range,bullet_type):
    try: float(sight_height)
    except ValueError:
        return "Please enter a valid number"

    df_ballistics_chart = pd.read_excel(r"C:\Users\bnofi\OneDrive\Desktop\Long_range_shooting\hornady_excel_document.xlsx")
    bullet_drop_known_zero = df_ballistics_chart.query('BULLET == @bullet_type')[known_zero_range]
    bullet_drop_desired_zero = df_ballistics_chart.query('BULLET == @bullet_type' )[desired_zero_range]

    sight_adjustment = (float(bullet_drop_known_zero) - float(sight_height)) + (float(known_zero_range)/float(desired_zero_range)) * (float(sight_height) - (float(bullet_drop_desired_zero)))
    return round(sight_adjustment,2)

def new_range_zero_moa(sight_height_moa,known_zero_range_moa,desired_zero_range_moa,bullet_type_moa):
    try: float(sight_height_moa)
    except ValueError:
        return "Please enter a valid number"

    df_ballistics_chart = pd.read_excel(r"C:\Users\bnofi\OneDrive\Desktop\Long_range_shooting\hornady_excel_document.xlsx")

    bullet_drop_known_zero_moa = df_ballistics_chart.query('BULLET == @bullet_type_moa')[known_zero_range_moa]
    bullet_drop_desired_zero_moa = df_ballistics_chart.query('BULLET == @bullet_type_moa' )[desired_zero_range_moa]

    a_one = 95.493*((float(sight_height_moa)-(float(bullet_drop_known_zero_moa)))/float(known_zero_range_moa))
    a_two = 95.493*((float(sight_height_moa)-(float(bullet_drop_desired_zero_moa)))/float(desired_zero_range_moa))

    final_moa_correction = float(a_two) - float(a_one)

    return round(final_moa_correction,2)
