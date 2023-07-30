### Check All KBOX UBER STATUS 
import requests
import time
import json
import datetime
import csv  


dt = datetime.datetime.now()
dt_string = dt.strftime("%Y-%m-%d___%H:%M:%S")

acc_ids=["5e7bbf7265013b00010cb6aa" ,"615e8f1f4875a94524fa9947" , "5fe17b1effe9e99933f9f58a" ]


with open(f'/Users/victorbertels/Desktop/KBOX/Craveable-Uber-STATE-all-accounts{dt_string}.csv', 'w', newline='') as f:
    header = ['locationName','ChannelLink Name','UberUUID',"Deliverect Order Release" ,"Uber Order Release",'PosIntegration', 'Integration', 'OrderManager'  ,'UberResponse']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    token = "IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAALgdxD3BOzN7OpQiS2-8FBg8AAAAH09HBHmxPhdqI5uq2h8Js9284tmeTtehFCHrA9DlUmjlj0Oe3tlA1gCNbihZqzXwP4SuhB-vKmDS6XJYDAAAAP39lq9RuOcBQ2ZIgCQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU"
    query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':7, "APIKey" : {"$exists" : True}})
    for i in query:
        try:
            uuid = i.channelSettings.storeId
            print(uuid , "--", i._id)
            DeliverectOrderrelease = i.channelSettings.enableReleaseCall
            locationId = i.location
            get_location_name = pcli.locations.get(locationId).name
            url = f"https://api.uber.com/v1/eats/stores/{uuid}/pos_data"
            print(url)
            payload={}
            headers = {
                'Authorization': f'Bearer {token}'
                }
            response = requests.request("GET", url, headers=headers, data=payload)
            jsonResponse = response.json()
            pos_integration = "Enabled" if jsonResponse.get("pos_integration_enabled") else "Disabled"
            integration = "Enabled" if jsonResponse.get("integration_enabled") else "Disabled"
            uberReleaseCall = "Enabled" if jsonResponse.get("order_release_enabled") else "Disabled"
            order_manager = jsonResponse.get("order_manager_client_id")
            # print(f"ChannelLink Name : {i.name} , UberUUID : {uuid} , PosIntegration : {pos_integration} , Integration : {integration},  OrderManager : {order_manager}")
            if response.ok:
                
                writer.writerow({"locationName": get_location_name, "ChannelLink Name" : i.name , "UberUUID" : uuid ,"Deliverect Order Release" : DeliverectOrderrelease , "Uber Order Release" : uberReleaseCall,"PosIntegration" : pos_integration , "Integration" : integration,  "OrderManager" : order_manager , "UberResponse" : response.text })
            else:
                print(response.text,"for UUID: ",uuid)
                writer.writerow({"locationName": get_location_name, "ChannelLink Name" : i.name , "UberUUID" : uuid , "PosIntegration" : pos_integration , "Integration" : integration,  "OrderManager" : order_manager,"UberResponse" : response.text })
        except:
            writer.writerow({"locationName": get_location_name, "ChannelLink Name" : i.name , "UberUUID" : "not there"})
            