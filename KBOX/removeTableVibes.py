location_list = pcli.channelLinks.list_all(q={"account" : "62fc44dc934376949a733248" , "channelSettings.channelLocationId": "TO BE ADDED"})


for i in location_list:
    print(i.channelSettings.channelLocationId)
    print(i.name , i.location)
    pcli.channelLinks.delete(i)