import requests
import json

query = pcli.channelLinks.list_all(q={"account" : "5e7bbf7265013b00010cb6aa" , "channel" : 7})
updated_locs = []

for i in query:
    uuid = i.APIKey
    location = i.location
    is_unique = updated_locs.count(location)
    if is_unique == 0:
        url = f"https://api.uber.com/v1/eats/stores/{uuid}"
        payload={}
        headers = {
        'Authorization': 'Bearer IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAAG4rzcEuna35F2qUSbmPlHI8AAAA-1zi9QJ--1qDrGqIGhJYWkdSTTU47qsNP-1QjIi5vwZNDel7RmRxwEWEwEfd9hZbkbK-_MW1Y25kuyRRDAAAANdMmudKuwSDTKexHSQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.ok:
            json = response.json()
            jsonrespsonse = response.json()
            print(jsonrespsonse)
            datajson = json.dumps(jsonrespsonse)
            data = json.loads(datajson)
            address = data["location"]["address"]
            country = data["location"]["country"]
            city =  data["location"]["city"]
            postal_code =  data["location"]["postal_code"]
            get_location = pcli.locations.list_all(q={"_id":location})
            for loc in get_location:
                pcli.locations.update(loc,{
                    "address": {
                            "city": city,
                            "postalCode": postal_code,
                            "street": address,
                            "remarks": "",
                            "country": country,
                }})
            updated_locs.append(location)
            break
        else:
            print("could not update address info")
    else:
        print("location is already updated. Skipping it")
    
