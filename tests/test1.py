import cyberarkapi

def main():
    cark = cyberarkapi.carkData()    
    cark.servername = ""
    cark.username = "somvalue"
    cark.password = "somevalue"

    cark.token = cyberarkapi.get_tokenfromark(cark)

# --------------------

main()