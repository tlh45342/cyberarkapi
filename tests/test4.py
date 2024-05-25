import cyberarkapi

def main():
    cark = cyberarkapi.carkData()    
    cark.servername = "somevalue"
    cark.username = "somevalue"
    cark.password = ""
    try: 
        cark.token = cyberarkapi.get_tokenfromark(cark)
        print(type(cark))
    except:
        print("Caught an oppsie.")

# --------------------

main()