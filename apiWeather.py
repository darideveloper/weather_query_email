#! python3
# Get information from the api: Open Weather

import json, requests, datetime

def getApiWeather (lat, lon, apiKey): 
    """Get the weather from the api"""
    # Download the json data from openWeatherMap.org's API
    # apiKey '148200b8d1c12c3d891801dc216b8f87'
    urlWeather = 'https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=minutely,daily&appid=%s'% (lat, lon, apiKey)
    response = requests.get(urlWeather)
    response.raise_for_status
    wetaherInfo = json.loads(response.text)
    
    #Get new information of the weather
    try: 
        weather = []
        currentWeather = wetaherInfo['current']
        hourlyWeather  = wetaherInfo['hourly']
    except KeyError:
        menssage = 'Key api error or location doesn\'t exist. Check your information. '
        menssage += 'Write --help for more information'
        return None
    else: 
        weather.append(currentWeather['weather'][0])
        for hourWeather in hourlyWeather: 
            weather.append(hourWeather['weather'][0])

        return weather

def extractWeather (weatherList): 
    """ Convert the current weather information, to text"""
    hourCounter = 0
    weatherText = []
    for weatherItem in weatherList: 
        hourCounter += 1
        
        currentTime = datetime.datetime.now()
        hourIncress = datetime.timedelta (hours=hourCounter)
        currentTime += hourIncress

        textDate = str(currentTime.date())
        textHour = ''

        if len(str(currentTime.hour)) == 2: 
            textHour  = str(currentTime.hour)
        else: 
            textHour = '0' + str(currentTime.hour)


        hourWeather = {'day': textDate,
                        'hour': textHour,
                        'main': weatherItem['main'], 
                        'description': weatherItem['description']}

        weatherText.append(hourWeather)

    return weatherText

