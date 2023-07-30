import requests
import json

url = "https://www.hungryjacks.com.au/api/storelist"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
jsonresponse = response.json()


for item in jsonresponse:

    storeId = item["store_id"]
    name = item["name"]
    address = item["location"]["address"]
    postal = item["location"]["postcode"]
    state = item["location"]["state"]
    longitude = item["location"]["long"]
    suburb = item["location"]["suburb"]
    latitude = item["location"]["lat"]
    phone = item["location"]["phone"]
    latitude = item["location"]["lat"]
    hours = item["hours"]["dine_in"]
    for hour in hours:
        index = hour["day_idx"]
        open = hour["open"]
        close = hour["close"]

    
        print(open , close , index)
    print(f"Name : {storeId} - {name} - Address : {address}, {postal}, {suburb}- Lat: {latitude}")
        






