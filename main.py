#! python3
# Get the weasther from open weather api, and send by email

import logging, os, pprint
from apiWeather import getApiWeather, extractWeather, getTodayWeather
from apiLocation import getlocation
from sendMail import sendEmail, getTextAndHtml
from interfazWeather import runInterfazCrdentials

# Files and initial vars
currentDir = os.path.dirname(__file__)
credentailsPath = os.path.join(currentDir, 'credentials.json')
commandsPath = os.path.join(currentDir, 'commands.json')
logPath = os.path.join(currentDir, 'logs.txt')

logging.basicConfig(filename=logPath, level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#Start interfaz
info = runInterfazCrdentials (credentailsPath)

# Connect with location api
location = getlocation()
lat = location['lat']
lon = location['lon']

# Conect with weather api
apikey = info['credentials']['apiKey']

weatherList = getApiWeather (lat, lon, apikey)
infoWeather = extractWeather (weatherList)

# Get credentials
password  = info['password']

myEmail   = info['credentials']['myEmail']
subject   = info['credentials']['subject']
smtp      = info['credentials']['smtp']
portSmtp  = info['credentials']['portSmtp']

# Process information to text and html
todayWeather = getTodayWeather (infoWeather, infoWeather[0]['day'])
textAndHtml = getTextAndHtml(infoWeather, todayWeather)

# Add max weather to subject
subject += ' ' + todayWeather['max']

# Send each email
for forEmail in info['credentials']['emails']: 
    sendEmail (myEmail, password, forEmail, subject, smtp, portSmtp, textAndHtml)