uberquery = pcli.channelLinks.list_all(q={"channel": 7 , "channelSettings.storeId" : "d0d64d32-ac99-4e0b-9b6b-d644865b3f5f"})

for i in uberquery:
    print(i._id)