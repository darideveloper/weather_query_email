#! python3
# get the location with ipInfo page

import json, requests, pprint

def getlocation (): 
    # Get the location with free api
    urllocation = "http://ipinfo.io/json"
    response = requests.get(urllocation)
    response.raise_for_status
    locationInfo = json.loads(response.text)

    location = locationInfo['loc'].split(',')
    diccLocation = {'lat': location[0],
                    'lon': location[1]}

    return diccLocation
