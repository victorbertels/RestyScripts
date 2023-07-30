import requests
account  = "630c507964ffb8c1f3b8bb7b"

query = pcli.locations.list_all(q={"account" : account ,"tags" : {"$in" : ["Batch #2 - Thursday 3rd Nov","Batch #4 - Monday 7th Nov","Batch #3 - Friday 4th Nov"]}})
Ubers = []
for i in query:
    for channel in i.channelLinks:
        get_cl = pcli.channelLinks.get(channel)
        if get_cl.channel == 7:
            Ubers.append(get_cl._id)

uber =['631dc62871c3a68d02022e89',
 '630eaa649a14616b9c9d2c07',
 '630eaa649a14616b9c9d2be9',
 '630eaa649a14616b9c9d2bcb',
 '630eaa649a14616b9c9d2bc5',
 '630eaa649a14616b9c9d2ba7',
 '630eaa649a14616b9c9d2b9b',
 '630eaa649a14616b9c9d2b95',
 '630eaa649a14616b9c9d2b8f',
 '630eaa649a14616b9c9d2b89',
 '630eaa649a14616b9c9d2b83',
 '630eaa649a14616b9c9d2b7d',
 '630eaa649a14616b9c9d2b71',
 '630eaa649a14616b9c9d2b6b',
 '630eaa649a14616b9c9d2b59',
 '630eaa649a14616b9c9d2b4d',
 '630eaa649a14616b9c9d2b47',
 '630eaa649a14616b9c9d2b3b',
 '630eaa649a14616b9c9d2b35',
 '630eaa649a14616b9c9d2b2f',
 '630eaa649a14616b9c9d2b29',
 '630eaa649a14616b9c9d2b23',
 '630eaa649a14616b9c9d2b1d',
 '630eaa649a14616b9c9d2b11',
 '630eaa649a14616b9c9d2b05',
 '630eaa649a14616b9c9d2aff',
 '630eaa649a14616b9c9d2af9',
 '630eaa649a14616b9c9d2ae7',
 '630eaa649a14616b9c9d2ad5',
 '630eaa649a14616b9c9d2acf',
 '630eaa649a14616b9c9d2ac9',
 '630eaa649a14616b9c9d2ac3',
 '630eaa649a14616b9c9d2aab',
 '630eaa649a14616b9c9d2aa5',
 '630eaa649a14616b9c9d2a9f',
 '630eaa649a14616b9c9d2a99',
 '630eaa649a14616b9c9d2a8d',
 '630eaa649a14616b9c9d2a87',
 '630eaa649a14616b9c9d2a7b',
 '630eaa649a14616b9c9d2a75',
 '630eaa649a14616b9c9d2a69',
 '630eaa649a14616b9c9d2a63',
 '630eaa649a14616b9c9d2a5d',
 '630ea93a4ea4cd1b45b637cf',
 '631dc5d69af069f857ae18d9']


query = pcli.channelLinks.list_all(q={"_id" : {"$in" : uber}})

for i in query:
    pcli.channelLinks.update(i,{
        "status" : 0
    })