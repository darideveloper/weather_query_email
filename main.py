#! python3
# Get the weasther from open weather api, and send by email

import logging, os
from apiWeather import getApiWeather, extractWeather
from apiLocation import getlocation
from sendMail import sendEmail

# Files and initial vars
currentDir = os.path.dirname(__file__)
credentailsPath = os.path.join(currentDir, 'credentials.json')
commandsPath = os.path.join(currentDir, 'commands.json')
logPath = os.path.join(currentDir, 'logs.txt')

logging.basicConfig(filename=logPath, level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Connect with location api
location = getlocation()
lat = location['lat']
lon = location['lon']

# Conect with weather api
apikey = "148200b8d1c12c3d891801dc216b8f87"

weatherList = getApiWeather (lat, lon, apikey)
text = extractWeather (weatherList)

# Send mail
myEmail   = "cidentymx@gmail.com"
password  = "duscordia de ceguera temporal 87"
to        = "hernandezdarifrancisco@gmail.com"
subject   = "Weather mail"
body      = "Weather information"
smtp      = "smtp.gmail.com"
port      = 587

sendEmail (myEmail, password, to, subject, body, smtp, port)