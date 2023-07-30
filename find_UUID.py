uberquery = pcli.channelLinks.list_all(q={"channel": 7 , "channelSettings.storeId" :  "9a5e97c6-9bfe-504c-8736-ad41b57cc0b7"})

apiquery = pcli.channelLinks.list_all(q={"channel": 7 , "APIKey" : "9a5e97c6-9bfe-504c-8736-ad41b57cc0b7"})


for i in uberquery:
    print(i._id)

for i in apiquery:
    print(i._id)