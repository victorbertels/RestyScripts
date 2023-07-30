### Check All KBOX UBER STATUS 
import requests
import time
import json
import datetime
import csv  


dt = datetime.datetime.now()
dt_string = dt.strftime("%Y-%m-%d___%H:%M:%S")

acc_ids=["6335c4b0aa8c958f74195c4a"]


with open(f'/Users/victorbertels/Desktop/KBOX/KBOX-UBER-STATE-{dt_string}.csv', 'w', newline='') as f:
    header = ['locationName','ChannelLink Name','UberUUID', 'PosIntegration', 'Integration', 'OrderManager' , 'UberResponse']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    token = "IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAAJzyWc0G6IkpvGee-c2R6xw8AAAAopicCpkGY4FsZgUxamvJqT9TnIrZbzj6OSMJlQpMwU_Rg5c9Eljc8v2QwqXHXSKOIxIWfnM-Ha9uHSoZDAAAACChQVm6bo6MlsbAbSQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU"
    query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':7})
    for i in query:
        try:
            uuid = i.channelSettings.storeId
            locationId = i.location
            get_location_name = pcli.locations.get(locationId)
            url = f"https://api.uber.com/v1/eats/stores/{uuid}/pos_data"
            payload={}
            headers = {
                'Authorization': f'Bearer {token}'
                }
            response = requests.request("GET", url, headers=headers, data=payload)
            jsonResponse = response.json()
            pos_integration = "Enabled" if jsonResponse.get("pos_integration_enabled") else "Disabled"
            integration = "Enabled" if jsonResponse.get("integration_enabled") else "Disabled"
            order_manager = jsonResponse.get("order_manager_client_id")
            print(f"ChannelLink Name : {i.name} , UberUUID : {uuid} , PosIntegration : {pos_integration} , Integration : {integration},  OrderManager : {order_manager}")
            if response.ok:
                
                writer.writerow({"locationName": get_location_name.name, "ChannelLink Name" : i.name , "UberUUID" : uuid , "PosIntegration" : pos_integration , "Integration" : integration,  "OrderManager" : order_manager , "UberResponse" : response.text })
            else:
                print(response.text,"for UUID: ",uuid)
                writer.writerow({"locationName": get_location_name.name, "ChannelLink Name" : i.name , "UberUUID" : uuid , "PosIntegration" : pos_integration , "Integration" : integration,  "OrderManager" : order_manager,"UberResponse" : response.text })
        except:
            writer.writerow({"locationName": get_location_name.name, "ChannelLink Name" : i.name , "UberUUID" : "not there"})