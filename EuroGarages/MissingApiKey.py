account = "61df8c560706d58e1016f00d"
channel = 7 

count = 0
links = pcli.channelLinks.list_all(q={"account" : account , "channel" : channel})

for link in links:
    try:
        if link.channelSettings.storeId != link.APIKey:
            uuid = link.channelSettings.storeId
            print(link._id)
            count += 1
            print(count)
            # pcli.channelLinks.update(link,{
            #       "APIKey": uuid,
            #     "channelSettings": {
            #             "APIKey": uuid

            # }})

    except:
        print("no key fond for " , link._id) 