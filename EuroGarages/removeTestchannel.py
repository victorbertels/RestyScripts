account = "61df8c560706d58e1016f00d"

channel = 1

name = "Test channel"


channellLinks = pcli.channelLinks.list_all(q={"account" : account , "channel" : channel, "name" : name})


for channel in channellLinks:
    pcli.channelLinks.delete(channel)
    print(channel.name)
