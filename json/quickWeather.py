#! python3
# quickWeather.py - Prints the current weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
# Note: This commented out URL is old; replaced with the new one on 10/18/16
# Source: http://openweathermap.org/current#name
# url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
#
# TURNS OUT YOU NEED TO SIGN UP FOR AN ACCOUNT TO GET AN API KEY AND INCLUDE THAT IN THE URL
#
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
