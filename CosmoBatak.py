"""
Approximation routine for transforming Gregorian Calendar into Batak Cosmogram.
We do the simulation of the place for observation (rukyatulhilal) from the Lake Toba, North Sumatera, Indonesia

Refer to the remarks within the function for detail.
Please refer to Institut Batakologi for more information.

20240325
part of the work for Budaya-Indonesia.org within the Bandung Fe Institute
"""

import ephem
from datetime import datetime, timedelta

# Names of Batak months 
batak_month_names = {
    1: "Sipaha Sada",
    2: "Sipaha Duwa",
    3: "Sipaha Tolu",
    4: "Sipaha Opat",
    5: "Sipaha Lima",
    6: "Sipaha Onom",
    7: "Sipaha Pitu",
    8: "Sipaha Walu",
    9: "Sipaha Siya",
    10: "Sipaha Sampulu",
    11: "Li",
    12: "Hurung",
    13: "Lamadu"
}

# Names of Batak Days 
batak_day_names = {
    1: "Artia",
    2: "Soma",
    3: "Anggara",
    4: "Muda",
    5: "Boraspati",
    6: "Singkora",
    7: "Samisara",
    8: "Antian ni Aek",
    9: "Suma ni Mangadop",
    10: "Anggara Sampulu",
    11: "Muda ni Mangadop",
    12: "Boraspati ni Tangkop",
    13: "Singkora Purnama",
    14: "Samisara Purnama",
    15: "Tula",
    16: "Suma ni Holom",
    17: "Anggara ni Holom",
    18: "Muda ni Holom",
    19: "Boraspati ni Holom",
    20: "Singkora Duapulu",
    21: "Samisara Mora Turun",
    22: "Antian ni Angga",
    23: "Suma ni Mate",
    24: "Anggara na Begu",
    25: "Muda ni Mate",
    26: "Boraspati ni Gok",
    27: "Singkora duduk",
    28: "Samisara bulan mate",
    29: "Hurung",
    30: "Ringkar"
}

def get_moonset_after_sunset(observer, date):
    """
    Determines if the moon sets after the sun on the date of the new moon.
    """
    observer.date = date
    sunset = observer.next_setting(ephem.Sun()).datetime()
    moonset = observer.next_setting(ephem.Moon()).datetime()
    return moonset > sunset

def check_constellations_visibility(observer, date):
    """
    Check if Scorpio (Antares) is rising and Orion (Betelgeuse) is setting
    on the same evening around sunset from Lake Toba, and the new moon sets after the sun.
    We use the approximation tolerance of sightings within 4 hours after the sunset.
    """
    observer.date = date
    sunset = observer.next_setting(ephem.Sun()).datetime()
    observer.date = sunset  # Set observer time to sunset for this date
    
    antares = ephem.star("Antares")
    betelgeuse = ephem.star("Betelgeuse")
    
    antares_rise = observer.next_rising(antares).datetime()
    betelgeuse_set = observer.next_setting(betelgeuse).datetime()
    
    valid_observation_window = timedelta(hours=3.5)  # Time window after sunset
    
    is_antares_rising_after_sunset = sunset <= antares_rise <= (sunset + valid_observation_window)
    is_betelgeuse_setting_after_sunset = sunset <= betelgeuse_set <= (sunset + valid_observation_window)
    
    # Additional check for the moon setting after the sun on the date of the new moon
    moon_sets_after_sunset = get_moonset_after_sunset(observer, date)
    
    return is_antares_rising_after_sunset and is_betelgeuse_setting_after_sunset and moon_sets_after_sunset

def find_batak_new_year_start(given_date, observer):
    """
    Find the Batak New Year start based on specific astronomical conditions, 
    iterating back through new moons until one meets the constellations visibility criteria and the new moon sets after the sun.
    """
    current_date = ephem.Date(given_date)
    while True:
        previous_new_moon = ephem.previous_new_moon(current_date)
        observer.date = previous_new_moon
        
        if check_constellations_visibility(observer, previous_new_moon):
            return previous_new_moon.datetime()
        
        # Go back one day before the previous new moon for the next iteration
        current_date = ephem.Date(previous_new_moon - 1)

def count_lunar_months_since_new_year(new_year_start, end_date):
    """
    Count the number of lunar months from the Batak New Year start to a given end date.
    """
    count = 0
    current_date = new_year_start
    while True:
        current_new_moon = ephem.next_new_moon(current_date).datetime()
        if current_new_moon > end_date:
            break
        count += 1
        current_date = current_new_moon
    return count

def gregorian_to_batak(gregorian_date):
    """
    Convert a Gregorian date to the corresponding Batak calendar date.
    """
    observer = ephem.Observer()
    observer.lat, observer.lon = '-2.55', '98.55'  # Approximate coordinates for Lake Toba
    observer.elevation = 900  # Approximate elevation in meters
    observer.pressure = 0  # Ignore atmospheric refraction
    observer.horizon = '-0:34'  # Adjust horizon to match sunset/sunrise
    
    bulan = ephem.previous_new_moon(gregorian_date) 
    batak_new_year_start = find_batak_new_year_start(gregorian_date, observer)
    
    # Calculate Batak month and day
    batak_month = count_lunar_months_since_new_year(batak_new_year_start, gregorian_date) + 1
    latest_new_moon = bulan.datetime()
    batak_day = (gregorian_date - latest_new_moon).days + 1
    
    return batak_month, batak_day, batak_new_year_start

# -------------
# User Input
# -------------
# gregorian_date = 1994-04-01
user_input = input("Enter a Gregorian date (YYYY-MM-DD) to convert to the Batak cosmogram: ")
try:
    # Parsing the user input into a datetime object
    gregorian_date = datetime.strptime(user_input, '%Y-%m-%d')
    
    # Call the conversion function with the user-provided date
    batak_month, batak_day, batak_new_year_start = gregorian_to_batak(gregorian_date)
    
    # Output the result
    batak_month_name = batak_month_names.get(batak_month)
    batak_day_name = batak_day_names.get(batak_day)
    print ("--------------------->oo<---------------------")
    print(f"For previously Batak New Year date is {batak_new_year_start.strftime('%Y-%m-%d')}, then")
    print(f"the Batak cosmogram date for {gregorian_date.strftime('%Y-%m-%d')} is Month({batak_month}): {batak_month_name}, Day: {batak_day} - {batak_day_name}")    

except ValueError:
    # Handles the error if the date format is incorrect
    print("Error: Please enter the date in YYYY-MM-DD format.")

