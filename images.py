import decouple
import json
import os
import os.path
import requests
import urllib.request
import urllib
import sys
import time
from jsonpath_rw import parse
from pick import pick

# UBER_CLIENT_SECRET_PRODUCTION: str = decouple.config("UBER_CLIENT_SECRET_PRODUCTION")
# UBER_CLIENT_ID_PRODUCTION: str = decouple.config("UBER_CLIENT_ID_PRODUCTION")
LOGIN_UBER: str = "https://login.uber.com/oauth/v2/token"

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#posSystem = input("Choose your Pos : Lightspeed , Gastrofix , Rocketship, Revo , MOB , Ikentoo")

title = 'Choose your POS:'
options = ['Lightspeed' , 'Gastrofix' , 'Rocketship' , 'Revo' , 'Ikentoo']
posSystem = pick(options, title)
#print('---------------')

##print(posSystem)
#print(posSystem)

print('Choose your POS: \n POS System = ' + posSystem[0])


def log_cred(pos):
    if pos == 'Lightspeed':
        return {
            "client_secret": "Hrpl9-8LgU3p8dNH_3kFdejckvECqqGPH7tSGQaB",
            "client_id": "xX4VB0YQKxKaa3AErrmWnI1P8sxqeequ",
            "grant_type": "client_credentials",
            "scope": "eats.store",}


    elif pos == 'Gastrofix' :
        return {
            "client_secret": "Hrpl9-8LgU3p8dNH_3kFdejckvECqqGPH7tSGQaB",
            "client_id": "xX4VB0YQKxKaa3AErrmWnI1P8sxqeequ",
            "grant_type": "client_credentials",
            "scope": "eats.store",
            }


    elif pos == 'Rocketship' :
        return {
            "client_secret": "_XHmwnF_G2LKp0gpjF9K7LK3Gy0DDIhVQ76901nx",
            "client_id": "nL2qCqbVTBxL9AxQxNBv09VbJo12d1Wa",
            "grant_type": "client_credentials",
            "scope": "eats.store",
            }


    elif pos == 'Revo':
        return {
            "client_secret": "YZAdoA83u42dMLH1CR5STmmjtc-rJH_ze78VXuOx",
            "client_id": "7xFy7TnFF-OJtSvdRAP1B2TM1OlaXoe8",
            "grant_type": "client_credentials",
            "scope": "eats.store",
            }


#    elif pos == 'MOB':
 #       return {
  #          "client_secret": "WRONG",
    #        "client_id": "WRONG",
     #       "grant_type": "client_credentials",
      #      "scope": "eats.store",
       #     }

    elif pos == 'Ikentoo':
        return {
            "client_secret": "dYswIP6Mw-syUTwtoindnK2Ycz07IAG9WYpsnDR_",
            "client_id": "jJr8gX0UHlG4TvXaUwDdDnZ86AU5FAZ9",
            "grant_type": "client_credentials",
            "scope": "eats.store",
            }
            

    else:
        print('Dafuq is this bruh, i dont know this pos...')


currentPosSystem = log_cred(posSystem[0])
#print(currentPosSystem)
token = None
lst_location_uuids = [input("Enter the uuid of the restaurant: ")
]

restaurantname = input("Enter the name of the restaurant:")
if not os.path.exists(restaurantname):
    os.makedirs(restaurantname)

#destination_dir = os.path.join(__location__, restaurantname)
#if not os.path.exists(destination_dir):
#    os.makedirs(destination_dir)
#path1 = restaurantname
#if not os.path.exists(path1):
#    os.makedirs(path1)

#path = restaurantname
#destination_dir = os.path.join(__location__, restaurantname)
#if not os.path.exists(destination_dir):
#   os.makedirs(destination_dir)



def _getToken() -> str:
    global token
    if token is not None and token.get("expiryDate", 0) > time.time() - 10:
        return token.get("token", None)
    else:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = currentPosSystem
        uberResponse = requests.post(url=LOGIN_UBER, data=data, headers=headers).json()

        token = {
            "token": uberResponse.get("access_token", ""),
            "expiryDate": int(time.time()) + 2592,
        }

        return token.get("token", None)


def _getMenuForLocation(store_id: str):
    tk = _getToken()
    headers = {
        "Authorization": "Bearer {token}".format(token=tk),
        "Content-Type": "application/json",
    }
    url = "https://api.uber.com/v1/eats/stores/{store_id}/menu".format(
        store_id=store_id
    )
    uberResponse = requests.get(url=url, headers=headers)
    if uberResponse.status_code == 200:
        print("Created JSON for location: {}".format(store_id))
    else:
        print("Error for location: {}".format(store_id))
    return uberResponse.json()


def _writeMenus(location_uuids):

    for uuid in location_uuids:
        path = os.path.join(__location__, restaurantname, "{}menu.json".format(restaurantname))
        menu = _getMenuForLocation(uuid)
        with open(path, "w") as outfile:
            json.dump(menu, outfile)


_writeMenus(lst_location_uuids)


with open(os.path.join(restaurantname,"{}menu.json".format(restaurantname)), 'r') as f:
    json_data = json.load(f)
    #print(json_data)
    #print(json_data["sections"][0]["subsections"][0]["items"][1]["image_url"])
    lstImageUrls = list()

    l = [
        item["image_url"] for section in json_data["sections"] for subsection in section["subsections"] for item in subsection["items"] if item["image_url"] not in [0, "", None]
    ]
    
   # print("\n".join(l))
    sys.stdout=open(os.path.join(restaurantname,"urls.txt"),"w")
    print ("\n".join(l))
    sys.stdout.close()


links = open(os.path.join(restaurantname,"urls.txt"), 'r')
for link in links:
    link = link.strip()
    name = link.rsplit('/', 1)[-1]
    filename = os.path.join(restaurantname,name)
    filename2 = filename + '.jpg'

    if not os.path.exists(filename2):
        outfile = open(filename2, "wb")
        outfile.write(urllib.request.urlopen(link).read())
        outfile.close()

    


