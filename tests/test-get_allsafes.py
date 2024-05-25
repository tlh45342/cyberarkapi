import cyberarkapi
import base64
from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # take environment variables from .env.
    
    cark = cyberarkapi.carkData()    
    cark.servername = os.getenv('SERVERNAME')
    cark.username = os.getenv('USERNAME')
    cark.password = os.getenv('PASSWORD')

    #print("Servername:", cark.servername)
    #print("Password:", cark.username)
    #print("Password:", cark.password)

    cark.token = cyberarkapi.get_tokenfromark(cark)

    data = cyberarkapi.get_allsafes(cark)

    cyberarkapi.save_jsonfile(data, "dataset1.json")

# --------------------

main()