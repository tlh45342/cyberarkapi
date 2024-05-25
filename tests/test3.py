import cyberarkapi

def main():
    cark = cyberarkapi.carkData()    
    cark.servername = "somevalue"
    cark.username = "somevalue"
    cark.password = ""

    cark.token = cyberarkapi.get_tokenfromark(cark)

# --------------------

main()