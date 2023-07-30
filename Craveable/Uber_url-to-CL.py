import requests

query = pcli.channelLinks.list_all(q={"account" : "5e7bbf7265013b00010cb6aa" , "channel" : 7})


for i in query:
    uuid = i.APIKey
    url = f"https://api.uber.com/v1/eats/stores/{uuid}"
    payload={}
    headers = {
    'Authorization': 'Bearer IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAAG4rzcEuna35F2qUSbmPlHI8AAAA-1zi9QJ--1qDrGqIGhJYWkdSTTU47qsNP-1QjIi5vwZNDel7RmRxwEWEwEfd9hZbkbK-_MW1Y25kuyRRDAAAANdMmudKuwSDTKexHSQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.ok:
        json = response.json()
        menu_url = json.get("web_url")
        pcli.channelLinks.update(i,{
            "menuUrl" : menu_url
        })
    else:
        print("------------------------------------------------------------------------------------------------")
        print(i._id)
        print(i.APIKey)
        print("im not staged yet")
        print("------------------------------------------------------------------------------------------------")
