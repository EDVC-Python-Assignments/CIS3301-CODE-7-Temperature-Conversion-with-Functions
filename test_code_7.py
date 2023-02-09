import os,sys
import random
from mock_input_tests import *
from code_7 import get_temperature_in_celsius
from code_7 import get_temperature_in_kelvin_from_c
from code_7 import get_temperature_in_kelvin_from_f
from code_7 import get_clothing_recommendation
from code_7 import cold_weather_clothing
from code_7 import cool_weather_clothing
from code_7 import warm_weather_clothing
from code_7 import hot_weather_clothing

def check_if_file_exists():
    try:
        exists = os.path.exists("code_7.py")
        assert exists == True
    except:
        sys.exit()

def test_conversion_farenheit_to_celsius():
    check_if_file_exists()
    random_temp_in_f = random.randint(32,70)
    temp_in_c = (random_temp_in_f-32)*0.5556
    assert temp_in_c == get_temperature_in_celsius(random_temp_in_f)

def test_conversion_celsius_to_kelvin():
    check_if_file_exists()
    random_temp_in_c = random.randint(0,40)
    temp_in_k = random_temp_in_c + 273.15
    assert temp_in_k == get_temperature_in_kelvin_from_c(random_temp_in_c)

def test_conversion_farenheit_to_kelvin():
    check_if_file_exists()
    random_temp_in_f = random.randint(0,40)
    temp_in_c = (random_temp_in_f-32)*0.5556
    temp_in_k = temp_in_c +273.15
    assert temp_in_k == get_temperature_in_kelvin_from_f(random_temp_in_f)

def test_clothing_recommendation():
    check_if_file_exists()
    cold_item = get_clothing_recommendation(random.randint(1,10))
    cool_item = get_clothing_recommendation(random.randint(11,15))
    warm_item = get_clothing_recommendation(random.randint(16,25))
    hot_item = get_clothing_recommendation(random.randint(26,35))

    assert cold_item in cold_weather_clothing
    assert cool_item in cool_weather_clothing
    assert warm_item in warm_weather_clothing
    assert hot_item in hot_weather_clothing

