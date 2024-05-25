from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # take environment variables from .env.

    print("Username:", os.getenv('USERNAME'))
    print("Password:", os.getenv('PASSWORD'))
    print("Servername:", os.getenv('SERVERNAME'))
    print("Safe:", s.getenv('SAFE'))

# --------------------    

main()