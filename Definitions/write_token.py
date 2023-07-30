from email import header
from http.client import OK
from pathlib import Path
import requests
import json



    



def _getPath(name):
        path = Path(f"/Users/victorbertels/Desktop/Deliverect_code/CL-Settings/Definitions/{name}.txt")
        if path.is_file() == True:
            open('token.txt', 'r')
            return path
        else:
            open('token.txt', 'w')
            open('token.txt', 'r')
            return path



def _validateToken(token):
    url = "https://api.deliverect.com/accounts/5e7b70272bb18e000197dedb"
    payload = {}
    token = open("token.txt" , "w+")
    print(token.read())
    headers = {
    'Authorization': 'Bearer {token}',
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    if not response.ok:
        print("token invalid, paste your token")
        new_token = str(input())
        token.write(new_token)
        print(token.read())
        # do stuff





_getPath("token")
_validateToken(1234)

