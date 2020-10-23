#! python3
# Functions to read and write json files
import json

def readJsonFile (path): 
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

def writeJsonFile (path, info): 
    """Write information in json file"""
    if str(path).endswith('.json'):
        file = open (path, 'a').close() # If the file dosent exist, make it
        file = open (path, 'w')
        infoJson = json.dumps(info)
        file.write(infoJson)