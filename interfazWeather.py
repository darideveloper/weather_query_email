#! python3
# Specific interfaz for the program

import sys
from interfaz import runInterfaz
from requestsCredentials import returnCredentials, returnCredential, requestsCredentials, printCredentials

def runInterfazCrdentials (credentialsPath): 
    """ Run interfaz to request credetials and commands"""
    credentials = runInterfaz (credentialsPath, 'credentials', printCredentials, requestsCredentials, returnCredentials, 'c')
    password    = ''

    if not credentials: 
        sys.exit()
    elif credentials == 'help': 
        print ('write your email password, to run the program and send weather mails(example "yourPassword")')
        sys.exit()
    elif credentials == 'error': 
        print ('Syntaxis error... write --help for more information')
        sys.exit()
    else:
        password = sys.argv[1]
    
    info = {'credentials': credentials,
            'password': password}    
    return info
