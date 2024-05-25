import cyberarkapi

def main():
    cark = cyberarkapi.carkData()    
    cark.servername = "somevalue"
    cark.username = ""
    cark.password = "somevalue"

    cark.token = cyberarkapi.get_tokenfromark(cark)

# --------------------

main()