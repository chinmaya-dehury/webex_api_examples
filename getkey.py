# Make sure that you have a key file with only the key in the first line
# Filename: key
# first and only line 
#       123456xyz 

import json

def getkey():   
    try:
        key=open("key").readline().rstrip()
        return key
    except:
        print("It seems the key file is not present. \n Create a filename with the name 'key'. Provide your Webex API key in the first line.")
        exit()

