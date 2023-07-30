account = "63435e96e54f9c12e91c9745"

query = pcli.channelLinks.list_all(q={"account" : account , "productLocation" : {"$exists" : True}})


for i in query:
    new_loc = i.location
    # pcli.channelLinks.update(i,{"productLocation": new_loc})
    print(i.productLocation)