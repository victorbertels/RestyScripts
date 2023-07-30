import requests

uber_test_list = ["7922bfcf-472e-4310-a3a8-7157b107a934"]
acc_ids=["603fa3225de02e8e2fd835d5"]

# query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':7,'channelSettings.enableReleaseCall' : {'$exists' : True}})
query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':7})
token = "IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAABOeMhOmPPaQqqzrDCBCm6Y8AAAAFxBzk6t5ny4F24nBwwWou0slGFHt9LFriN9wTyzNlFTKezR-UxoRzHwCi7fzvJseMD5eXP3vUKgJuwpIDAAAAEIF3md6vCDT0bgVOCQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU"





for i in query:
    
    uuid = i.channelSettings.storeId
    location = i.location
    loc_name = pcli.locations.get(location)
    # print(
    #     "Channel link with id :" ,i._id ,"and name: ",i.name," on location" , loc_name.name," has UUID:",uuid , "and has Order Release set to " ,i.channelSettings.enableReleaseCall
    # )
    url = f"https://api.uber.com/v1/eats/stores/{uuid}/pos_data"

    payload={}
    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    if response.ok:
        jsonResponse = response.json()
        pos_integration = "Enabled" if jsonResponse.get("pos_integration_enabled") else "Disabled"
        order_release = "Enabled" if jsonResponse.get("order_release_enabled") else "Disabled"
        print(f"Order integration is {pos_integration} , Order Release is {order_release} for this {uuid}, channelLink:  {i._id}")

    
    
    else:
        print(response.text,"for UUID: ",uuid,"---" ,i._id)
    


    

# for uuid in uber_test_list:

#     url = f"https://api.uber.com/v1/eats/stores/{uuid}/pos_data"

#     payload={}
#     headers = {
#     'Authorization': f'Bearer {token}'
#     }

#     response = requests.request("GET", url, headers=headers, data=payload)
    
#     if response.ok:
#         jsonResponse = response.json()
#         pos_integration = "Enabled" if jsonResponse.get("pos_integration_enabled") else "Disabled"
#         order_release = "Enabled" if jsonResponse.get("order_release_enabled") else "Disabled"
#         print(f"Order integration is {pos_integration} , Order Release is {order_release} for this {uuid}")
    
    
#     else:
#         print(response.text,"for UUID: ",uuid)
    



