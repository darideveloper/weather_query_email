#! python3
# Basic terminal interfaz to save crdentials in json file

import sys

def runInterfaz (infoPath, infoName, printInfo, editInfo, getInfo, keyChar): 
    info = getInfo (infoPath)

    if info:
        if sys.argv [1:] == ['--help']:
            menssage = 'write "-%s -list" to see all %s ' % (keyChar, infoName)
            menssage += '\nwrite "-%s -edit" to edit all %s ' % (keyChar, infoName)
            print (menssage)
            return 'help'
        elif sys.argv [1:] == ['-' + keyChar, '-list']:
            # Return list of info
            printInfo(infoPath)
        elif sys.argv [1:] == ['-' + keyChar, '-edit']:
            # Edit info file
            editInfo (infoPath)
        else: 
            if len(sys.argv) == 2: 
                return info
            else: 
                return ('error')
    else:  
        print ('No registred %s.' % infoName)
        editInfo (infoPath)
        sys.exit()
    