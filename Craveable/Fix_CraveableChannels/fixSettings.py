account = "615e8f1f4875a94524fa9947"


channelLinks = pcli.channelLinks.list_all(q={"account" : account , "channel" : 10220 })


for channel in channelLinks:
    location = channel.location
    get_location_revCenter = pcli.locations.get(location).posSettings.simphony.revenueCenter
    revenueCenter = channel.posSettings.simphony.revenueCenter
    if revenueCenter != get_location_revCenter:
        print(channel._id)
    # print("channelRevCenter: ", revenueCenter , "locReveCenter : " , get_location_revCenter)





channelLinks = pcli.channelLinks.list_all(q={"account" : account , "channel" : 10220 , "channelSettings.channelLocationId" : "0cb9df09-6c1c-43eb-8067-a5ba35b905a3"})


channelLinks = pcli.channelLinks.list_all(q={"account" : account , "channel" : 10220 , "posSettings.simphony.revenueCenter" : "3072"})

for link in channelLinks:
    print(link._id)deltle acouunt noiw 


    