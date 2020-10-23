#! python3
# Get the weasther from open weather api, and send by email

import logging, os, pprint, csv
from apiWeather import getApiWeather, extractWeather, getTodayWeather
from apiLocation import getlocation
from sendMail import sendEmail, getTextAndHtml
from interfaz import Interfaz

# Files and initial vars
currentDir = os.path.dirname(__file__)
credentialsPath = os.path.join(currentDir, 'credentials.json')
configPath = os.path.join(currentDir, 'config.json')
logPath = os.path.join(currentDir, 'logs.txt')
emailsPath = os.path.join (currentDir, 'emails.csv')

myInterfaz = Interfaz (credentialsPath, configPath)

logging.basicConfig(filename=logPath, level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#Start interfaz
info = myInterfaz.getCredentials()

# Connect with location api
location = getlocation()
lat = location['lat']
lon = location['lon']

# Conect with weather api
apikey = info['apiKey']

weatherList = getApiWeather (lat, lon, apikey)
infoWeather = extractWeather (weatherList)

# read emails
emailsCSV = open (emailsPath, 'r')
readerCSV = csv.reader (emailsCSV)
emails = list (readerCSV)


# Get credentials
password  = info['password']
myEmail   = info['myEmail']
subject   = info['subject']
smtp      = info['smtp']
portSmtp  = info['portSmtp']

# Process information to text and html
todayWeather = getTodayWeather (infoWeather, infoWeather[0]['day'])


# Add max weather to subject
subject += ' ' + todayWeather['max']

# Extract forEmail
for toEmail in emails: 
    email = toEmail[0]
    name = toEmail[1]
    position = toEmail[2]
    # Gat HTML menssage and add greeting
    greeting = "Hello %s %s. " % (position.title(), name.title())
    textAndHtml =  getTextAndHtml(infoWeather, todayWeather, greeting)
    sendEmail (myEmail, password, email, subject, smtp, portSmtp, textAndHtml)