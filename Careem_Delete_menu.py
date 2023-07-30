import time

import requests
import json

# put a list of channelLinks here

channelLinks = input('What channelLink needs to go habibi???: ')
print(channelLinks)


'''
def getToken():
    url = "https://identity.careem.com/token"

    payload = {'client_id': '259e1dee-56b7-45f2-88ad-15a946792d33',
               'client_secret': 'b71a4a22-c7f8-43bd-a663-5eb1ead3240a',
               'scope': 'pos',
               'grant_type': 'client_credentials'}


    response = requests.request("POST", url, data=payload)
    return response.json().get("access_token")

def changeChannelLinksStatus(status: bool):
    payload = json.dumps({
        "active": status
    })

    for channelLink in channelLinks:
        url = f"https://apigateway.careemdash.com/pos/api/v1/branches/{channelLink}/status"
        headers = {
            'Authorization': f'Bearer {token}',
            'Branch-Id': channelLink,
            'Content-Type': 'application/json',
            'Brand-Id': '608fae8c9985df54ea0315b8'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)
        if not response.ok:
            print(f"Failed to change branch status. Branch id: {channelLink}. Response: {response.text}")
        else:
            print(f"Successful change of branch status. Branch id: {channelLink}.")
        time.sleep(1)


def deleteCatalog():
    url = "https://apigateway.careemdash.com/pos/api/v1/catalogs"


    for channelLink in channelLinks:
        payload = {}
        headers = {
            'Authorization': f'Bearer {token}',
            'Branch-Id': channelLink
        }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        if not response.ok:
            print(f"Failed to delete catalog. Branch id: {channelLink}. Response: {response.text}")
        else:
            print(f"Branch catalog deleted. Branch id: {channelLink}.")


token = getToken()

# deactivate branches. Mandatory!
changeChannelLinksStatus(False)
# clear out catalogs
deleteCatalog()
# activate branches
changeChannelLinksStatus(True)

'''