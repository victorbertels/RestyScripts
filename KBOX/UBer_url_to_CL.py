import requests

query = pcli.channelLinks.list_all(q={"account" : "62fc44dc934376949a733248" , "channel" : 7})


for i in query:
    uuid = i.APIKey
    url = f"https://api.uber.com/v1/eats/stores/{uuid}"
    payload={}
    headers = {
    'Authorization': 'Bearer IA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAGMAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAYAAAABwAAAAEAAAAEAAAAJuz5EvweZk6q4MYM4UkqCE8AAAAPeU4NSjadyUN-n8YxNIaa7aPf8v35Sj5aktKe6xzbmomK-Fxuv9NI0wd1Y_fHvezSol55SIReRXIJotxDAAAAJG2gQ96uTdhDmg39yQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.ok:
        json = response.json()
        menu_url = json.get("web_url")
        pcli.channelLinks.update(i,{
            "menuUrl" : menu_url
        })
    else:
        print("im not staged yet")
