# https://github.com/SwarnadeepGhosh 
# Six Days Weather Forecast using Python and MetaWeather API

import requests
import time

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='  # + city
API_WEATHER = '/api/location/'  # + woeid

def print_pause(printable_data):
    time.sleep(1)
    print(printable_data+'\n')


def display_weather(weather_data):
    for i in range(len(weather_data)):
        date = weather_data[i]['applicable_date']
        state = weather_data[i]['weather_state_name']
        max_temp = weather_data[i]['max_temp']
        max_temp = round(max_temp, 2)
        min_temp = weather_data[i]['min_temp']
        min_temp = round(min_temp, 2)
        print(f" {date} \t {state} \t High: {max_temp}°C \t Low: {min_temp}°C")


def check_again():
    again = input('\nDo You want to check again ? (y/n) ').lower()
    if again == 'n':
        print_pause('Have a Good Day ..')
        time.sleep(1.5)
    elif again == 'y':
        weather_report()
    else:
        print('I cant understand, Please try again..')
        check_again()


def weather_report():
    try:
        print('Swarnadeep Welcomes you to the Weather Report Forecast.\n')
        time.sleep(1)
        city = input('Where in the World are you ? ')
        print_pause('\nGetting Location Data...')
        r1 = requests.get(API_ROOT + API_LOCATION + city)
        # if r1.status_code == 200:
        location_data = r1.json()
        woeid = location_data[0]['woeid']
        # print("Where on Earth ID is : "+str(woeid))
        print_pause('Location Data Fetched successfully...')
        time.sleep(1)

        r2 = requests.get(API_ROOT + API_WEATHER + str(woeid))
        print_pause('Getting Weather Data, Please wait...')
        print_pause('Weather Data of ' + city.capitalize() + ':')
        # We will get a dictionary having keys: consolidated_weather, time, sun_rise, sun_set, timezone_name, parent, sources, title, location_type, woeid, latt_long, timezone.
        weather_data = r2.json()['consolidated_weather']
        # We will get 6 day Weather Forecast data in weather data as a list of dictionaries.
        # Each day having keys: id,weather_state_name, weather_state_abbr, wind_direction_compass, created, applicable_date, min_temp, max_temp, the_temp, wind_speed, wind_direction, air_pressure, humidity, visibility, predictability
        display_weather(weather_data)
        check_again()

    except requests.exceptions.ConnectionError:
        print('Sorry there is a network error')
        time.sleep(1)

    except:
        print("I don't know where that is. Please enter only famous cities.\n")
        time.sleep(1)
        weather_report()


if __name__ == '__main__':
    weather_report()
