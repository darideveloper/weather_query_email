#! python3
# Save, edit and query credentials in credentials file

from rwJsonFile import readJsonFile, writeJsonFile

def validateCredentail (menssage='', content='', lenght=0): 
    """ Validate the information with extension of text of content"""
    while True: 
        credential = input(menssage)
        if lenght:
            if len(credential) > lenght: 
                break
        else: 
            if content in credential: 
                break
        print ('Incorrect information, try again')
    return credential

def returnCredentials (credentailsPath): 
    """ Return all crdentials"""
    credentials = readJsonFile(credentailsPath)
    if credentials: 
        return credentials

def printCredentials (credentailsPath): 
    """ Print a list of the credentials"""
    credentials = readJsonFile(credentailsPath)
    if credentials: 
        for name, credential in credentials.items(): 
            print (name, ': ', credential)

def returnCredential (credentailsPath, credential): 
    """ Return specific credential"""
    credentials = readJsonFile(credentailsPath)
    info = credentials[credential]
    return info
