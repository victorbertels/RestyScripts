from turtle import update
import requests

account = "5d67c3f06f006f00012b83d1"
uberquery = pcli.channelLinks.list_all(q={"account" : account, "channel": 7 , "channelSettings.storeId" : {"$exists" : True} , "APIKey" : ""})
uberquery = pcli.channelLinks.list_all(q={"channel": 7 , "channelSettings.storeId" : "a8f3b5fb-bf66-5c48-931a-451fe2ed21d9"})
uberquery = pcli.channelLinks.list_all(q={"channel": 7 , "APIKey" : "a8f3b5fb-bf66-5c48-931a-451fe2ed21d9"})


for i in uberquery:
    print(i.channelSettings.storeId)
    pcli.channelLinks.update(i,{
        "APIKey" : i.channelSettings.storeId
    })


for i in uberquery:
    if i.channelSettings.storeId and not i.APIKey:
        pcli.channelLinks.update(i,{
        "APIKey" : i.channelSettings.storeId
    })

     


for i in uberquery:
    uuid = i.channelSettings.storeId
    name = i.name
    newName = name + " - not staged"
    url = f"https://api.uber.com/v1/eats/stores/{uuid}/pos_data"
    payload={}

    headers = {
    'Authorization': 'Bearer IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAABznylJ-bywOk3bC7mp4kJ88AAAAknbKJRn0MdX_c_jnOPLxXtPUbNFOLEKszeaoClr-isBswltF2e-iL0aGv672p9OTXlwmVG3YWGWlcm_hDAAAALGrS-zRWF4y6shXjCQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.ok:
        print(response.text)
        print(i.name)
        print("good")
        
        pcli.channelLinks.update(i,{
            "status" : 3
        })
        print("-*-*-*--**--*-*-*-*-*-*-*-*-*-")
    else : 
        print(response.text)
        print("not good" , i._id)
        
        pcli.channelLinks.update(i,{
            "status" : 2,
            "name" : name + " - not staged"

        })
        print("-*-*-*--**--*-*-*-*-*-*-*-*-*-")




for updated in uberquery:
    if updated.name[-4:] != "aged":
        print(updated.name , "*-*-*-*-",updated._id, "**--**" , updated.channelSettings.storeId)





