#! python3
# Request specific credentials of the project

from rwJsonFile import writeJsonFile
from credentials import validateCredentail, returnCredentials, returnCredential, printCredentials

def requestsCredentials (credentailsPath): 
    """ Request all the credentials"""
    emailNum = 0
    emails = [] 
    print ('Please capture your information\n')
    myEmail  = validateCredentail('Your email (example: example@mail.com): ', content='@')
    subject  = validateCredentail('The subject in the mail. (examle: Weather email): ', lenght=2)

    print ('Write the emails destination. (write "@" to quit)')
    while True: 
        emailNum +=1
        email = validateCredentail(menssage='email %s: ' % emailNum, content='@')
        if email == "@": 
            break
        else: 
            emails.append(email)
        
    apiKey   = validateCredentail('Open Weather Api Key (example: 439d4b804bc8187953eb36d2a8c26a02): ', lenght=20)
    smtp     = validateCredentail('SMPT server of your email. (examle: smtp.gmail.com): ', content='smtp')
    portSmtp = validateCredentail('SMPT PORT server of your email. (examle: 587): ', lenght=2)
    
    credentials = {'myEmail': myEmail, 
                    'smtp': smtp,
                    'portSmtp': portSmtp,
                    'emails': emails,
                    'apiKey': apiKey, 
                    'subject': subject}

    print ('\nNew credentials saved.\n')
    writeJsonFile (credentailsPath, credentials)
