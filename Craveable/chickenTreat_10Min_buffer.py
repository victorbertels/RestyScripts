acc = "615e8f1f4875a94524fa9947"
query = pcli.channelLinks.list_all(q={"account" : acc , "channel" : 7 })


for i in query:
    if i.name[-5:] == " HYPE":
        pcli.channelLinks.update(i,{
            "bufferOrders": True,
            "defaultPreparationTime": 10,
            "posSettings": {
                "simphony": {
                    "bufferOrders": True,
                    "averagePreparationTime": 10
                    }}})
