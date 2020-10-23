#! python3
import json, os, sys

class Interfaz ():
    """Class to execute an interface from terminal, managing user credentials"""
    # Read and write json files

    def __init__ (self, pathCredentialsFile, pathConfigCredentialsFile):
        """ Run the inefaz"""
        """Run the complite interfaz"""

        # Initical vars
        self.credentailsPath = pathCredentialsFile
        self.configCredentialsPath = pathConfigCredentialsFile


        # Menssages
        helpMenssage = "Run the interfaz.py to request credentials or configuration of credentials. \
        \n interfaz.py return the current credentials.\
        \n write '-l --cred' to see all credentials \
        \n write '-l --config' to see all credentials configuration options. \
        \n write '-e --config' to edit all credentials configuration options. \
        \n write '-e --cred' to edit all credentials"
        
        errorMenssage = "Incorrect input. Write --help for more information"

        # Run interfaz
        if len(sys.argv) == 2: 
            if sys.argv [1] == '--help':
                # Print help menssage
                print (helpMenssage)
                sys.exit()
            else: 
                print (errorMenssage)
                sys.exit()
        elif len(sys.argv) == 3: 
            if sys.argv [1] == '-l':
                # List json files info
                if sys.argv [2] == '--config':
                    # Return list of info
                    self.printConfigCredentials()
                elif sys.argv [2] == '--cred':
                    # Return list of info
                    self.printCredentials()
                else: 
                    print (errorMenssage)
                    sys.exit()
            elif sys.argv [1] == '-e':
                # Edit json files
                if sys.argv [2] == '--config':
                    # Return list of info
                    self.requestConfigCredentials()
                elif sys.argv [2] == '--cred':
                    # Return list of info
                    self.requestCredentials()
                else: 
                    print (errorMenssage)
                    sys.exit()
            else: 
                print (errorMenssage)

        # Read files. 
        configCredentials = self.readJsonFile (pathConfigCredentialsFile)
        credentials = self.readJsonFile (pathCredentialsFile)

        # if files are empty, requet it
        if not configCredentials: 
            self.requestConfigCredentials ()
        
        if not credentials: 
            self.requestCredentials ()
                
    def readJsonFile (self, path): 
        """Read paths of json files, and return the information inside"""
        if str(path).endswith('.json'):
            infoReturn = ''
            file = open (path, 'a').close() # If the file dosent exist, make it
            file = open (path, 'r')
            info = file.read()
            if info:
                infoReturn = json.loads(info)
            file.close()
            return infoReturn

    def writeJsonFile (self, path, info): 
        """Write information in json file"""
        if str(path).endswith('.json'):
            file = open (path, 'a').close() # If the file dosent exist, make it
            file = open (path, 'w')
            infoJson = json.dumps(info)
            file.write(infoJson)

    def printCredentials (self): 
        """ Print a list of the credentials"""
        credentials = self.readJsonFile(self.credentailsPath)
        if credentials: 
            for name, credential in credentials.items(): 
                print (name, ': ', credential)
        else: 
            print ("No credentials yet")

    def printConfigCredentials (self): 
        """ Print a list of the config of credentials"""
        credentialConfigCounter = 0
        configCredentials = self.readJsonFile(self.configCredentialsPath)
        if configCredentials: 
            for configCredentail in configCredentials: 
                credentialConfigCounter += 1
                print (credentialConfigCounter)
                for name, value in configCredentail.items(): 
                    print (name, ': ', value)
        else: 
            print ("No config of credentials yet")

    def requestConfigCredentials (self): 
        """Set the info for request credentials"""
        # Request setting for credentials

        print ('\nPlease, capture configuration of credentials')

        credentialCounter = 1
        credentialsSettings = []
        while True: 
            # Request credentiual settings
            name = input ('Credential %s name: ' % credentialCounter)
            description = input ('Credential %s description: ' % credentialCounter)
            validation = input ('Credential %s validation: ' % credentialCounter)
            other = input ('Other credential? (y/n): ')
            
            # Add current credential to list
            credentialsSettings.append ({'name': name, 
                                        'description': description, 
                                        'validation': validation})

            if other.strip()[0] != 'y': 
                break

            credentialCounter += 1
            
        # Write credentials settings in the file
        self.writeJsonFile (self.configCredentialsPath, credentialsSettings)

    def requestCredentials (self): 
        """ Request the credentials with the credentials configuration file"""
        credentials = {}

        print ("\nPlase, capture your information")

        # Get configuration for each credential
        configCredentials = self.readJsonFile (self.configCredentialsPath)

        # Request to user each credential
        for configCredential in configCredentials: 
            while True:
                # Extract config info
                name = configCredential['name']
                description = configCredential['description']
                validation = configCredential['validation']
                # Request credential and add to the dictionary
                credential = input (name + ' (%s): ' % description)
                # Validate credential
                try: 
                    validation = int (validation)
                    if len(credential) >= validation: 
                        break
                    else: 
                        print ('Incorrect lenght. The credential needs at least %s characters' % int (validation))
                except: 
                    # Convert validation items to list
                    if validation: 
                        # Convert validation info to python data
                        validation = json.loads (validation)
                        if type (validation) != list:
                            validation = [validation] 

                        # Count correct validations
                        validationCounter = 0                
                        for validationItem in validation: 
                            if validationItem in credential: 
                                validationCounter += 1
                            else: 
                                print ('The credential needs to have "%s"' % validationItem)
                        
                        # Check number of validations
                        if validationCounter == len (validation): 
                            break
                    else: 
                        break

            credentials [configCredential['name']] = credential

        # Save credentials
        self.writeJsonFile (self.credentailsPath, credentials)

    def getCredentials (self): 
        credentials = self.readJsonFile (self.credentailsPath)
        return (credentials)
