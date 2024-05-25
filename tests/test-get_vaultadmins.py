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
    cark.safe = os.getenv('SAFE')
    
    #print("Servername:", cark.servername)
    #print("Password:", cark.username)
    #print("Password:", cark.password)
    print("Safe:", cark.safe)

    cark.token = cyberarkapi.get_tokenfromark(cark)

    data = cyberarkapi.get_vaultadmins(cark)

    print(data)
    #cyberarkapi.save_jsonfile(data, "dataset1.json")

# --------------------

main()