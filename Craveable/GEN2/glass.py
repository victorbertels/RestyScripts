channel = 10220

qccount = "5e7bbf7265013b00010cb6aa"

link = pcli.channelLinks.list_all(q={"account" : qccount , "channel" : channel})


for chan in link:
    get_name = pcli.locations.get(chan.location).name

    print(chan.location, get_name)