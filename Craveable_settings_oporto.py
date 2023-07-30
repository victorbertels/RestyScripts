Oporto = pcli.channelLinks.list_all(q={'account' : '5e7bbf7265013b00010cb6aa','channel': 2,"posSettings.simphony.paidPaymentType" : {"$exists" : False}  })


for i in Oporto:
    pcli.channelLinks.update(i,{
        "posSettings.simphony.paidPaymentType" : 310

    })

