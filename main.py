#! python3
# Get the weasther from open weather api, and send by email

import logging, os
from apiWeather import getApiWeather, extractWeather
from apiLocation import getlocation
from sendMail import sendEmail
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
text = extractWeather (weatherList)

# Send mail and get cedentials

body      = "Weather information"
password  = info['password']

myEmail   = info['credentials']['myEmail']
subject   = info['credentials']['subject']
smtp      = info['credentials']['smtp']
portSmtp  = info['credentials']['portSmtp']

# Send each email
for forEmail in info['credentials']['emails']: 
    sendEmail (myEmail, password, forEmail, subject, body, smtp, portSmtp)