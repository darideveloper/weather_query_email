#! python3
# get the location with ipInfo page

import json, requests, logging, sys

def getlocation (): 
    # Get the location with free api
    urllocation = "http://ipinfo.io/json"
    response = requests.get(urllocation)
    try: 
        response.raise_for_status
        locationInfo = json.loads(response.text)
    except: 
        menssage = 'Error to conect ' + urllocation
        print (menssage)
        logging.error(menssage)
        sys.exit()
    else: 
        location = locationInfo['loc'].split(',')
        diccLocation = {'lat': location[0],
                        'lon': location[1]}

        return diccLocation
