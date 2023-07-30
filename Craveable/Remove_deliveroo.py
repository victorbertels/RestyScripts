account = ["5e7bbf7265013b00010cb6aa" , "5fe17b1effe9e99933f9f58a" , "615e8f1f4875a94524fa9947"]

channellinks = pcli.channelLinks.list_all(q={"account" : {"$in" : account}, "channel" : 2})


for channelLink in channellinks:
    print(channelLink.name)
    pcli.channelLinks.delete(channelLink)