#! python3
# Specific interfaz for the program

import sys
from interfaz import runInterfaz
from requestsCredentialsAndCommands import returnCredentials, returnCredential, requestsCredentials, printCredentials, requestsCommands

def runInterfazCrdentialsCommands (credentialsPath, commandsPath): 
    """ Run interfaz to request credetials and commands"""
    #commands = runInterfaz (commandsPath, 'commands', printCredentials, requestsCommands, returnCredentials, 'comm')
    credentials = runInterfaz (credentialsPath, 'credentials', printCredentials, requestsCredentials, returnCredentials, 'c')
    commands    = runInterfaz (commandsPath, 'commands', printCredentials, requestsCommands, returnCredentials, 'com')
    password    = ''
    secredWord  = ''

    if not credentials or not commands: 
        sys.exit()
    elif credentials == 'help' and commands == 'help': 
        print ('write your password and secred word, to run the program and Controlling pc with email (example "yourPassword" "YourSecredWord")')
        sys.exit()
    elif credentials == 'error' and commands == 'error': 
        print ('Syntaxis error... write --help for more information')
        sys.exit()
    else:
        password = sys.argv[1]
        secredWord = sys.argv[2]
    
    info = {'credentials': credentials,
            'commands': commands,
            'password': password, 
            'secredWord': secredWord}    
    return info
