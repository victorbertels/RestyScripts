#DoorDash images enable
acc_ids=["5e7bbf7265013b00010cb6aa","5fe17b1effe9e99933f9f58a"]
query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':12, "channelSettings.sendImagesOnMenuPush" : {"$exists":False}})



for i in query:
    pcli.channelLinks.update(i,{
        "channelSettings.sendImagesOnMenuPush" : True
    })

