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

def requestEmails (emailsPath): 
    """Requet a list of emails and names"""
    print ("\nNo recipient information. Please enter their names and emails.\n")

    # open file
    csvFile = open (emailsPath, 'w')
    csvWriter = csv.writer (csvFile)

    emailCounter = 1
    otherRecipient = True
    while otherRecipient:
        # Request name and email
        name = input ("Recipient %s name: " % emailCounter)
        while True:
            email = input ("Recipient %s email: " % emailCounter)
            # Validate email
            if "@" in email and "." in email:
                break
        
        # Save information
        csvWriter.writerow ([email, name])

        other = input ("Other recipient (y/n) ")
        if other.lower()[0] != 'y': 
            otherRecipient = False
        
        emailCounter += 1


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
while True: 

    if os.path.exists (emailsPath): 
        emailsCSV = open (emailsPath, 'r')
        readerCSV = csv.reader (emailsCSV)
        emails = list (readerCSV)

        if emails: 
            break

    requestEmails(emailsPath)


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
    # Gat HTML menssage and add greeting
    greeting = "Hello %s. " % (name.title())
    textAndHtml =  getTextAndHtml(infoWeather, todayWeather, greeting)
    sendEmail (myEmail, password, email, subject, smtp, portSmtp, textAndHtml)