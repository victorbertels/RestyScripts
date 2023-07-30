acc_ids=["5e7bbf7265013b00010cb6aa","5fe17b1effe9e99933f9f58a"]
query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':12, "posSettings.simphony.bufferOrders" : True ,"bufferOrders" : True})




for i in query:
    print(i.account)
    pcli.channelLinks.update(i,{
        "posSettings":{
            "simphony":{
                "bufferOrders" : False
            }},
            "bufferOrders" : False
    })