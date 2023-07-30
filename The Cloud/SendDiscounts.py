locs = pcli.locations.list_all(q={'account' : "6017e71bcb8a91b4944db5fe" ,"posSettings.generic.sendDiscount" : False })
unexist_locs = pcli.locations.list_all(q={'account' : "6017e71bcb8a91b4944db5fe" ,"posSettings.generic.sendDiscount" : {"$exists" :False }})
channels = pcli.channelLinks.list_all(q={'account' : "6017e71bcb8a91b4944db5fe" ,"posSettings.generic.sendDiscount" : False })
unexist_cL = pcli.channelLinks.list_all(q={'account' : "6017e71bcb8a91b4944db5fe" ,"posSettings.generic.sendDiscount" : {"$exists" :False }})

for i in locs:
    pcli.locations.update(i,{
        'posSettings.generic.sendDiscount' : True
    },propagate='all', override=1)

for i in noElocs:
    pcli.locations.update(i,{
        'posSettings.generic.sendDiscount' : True
    },propagate='all', override=1)


for i in channels:
    pcli.channelLinks.update(i,{
        'posSettings.generic.sendDiscount' : True
    })