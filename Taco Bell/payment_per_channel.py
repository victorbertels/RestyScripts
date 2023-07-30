account = "605335af9a090bd16d42350d"

query = pcli.channelLinks.list_all(q={
    "account" : account
})


for i in query:
    if i.channel == 12:
        pcli.channelLinks.update(i,{
            "posSettings": {
                "ncr": {
                    "eatinPaymentType": "26",
                    "pickupPaymentType": "26",
                    "paymentType": "26",
                    }
                    }
                    })
    elif i.channel == 7:
        pcli.channelLinks.update(i,{
            "posSettings": {
                "ncr": {
                    "eatinPaymentType": "27",
                    "pickupPaymentType": "27",
                    "paymentType": "27",
                    }
                    }
                    })
    elif i.channel == 26:
        pcli.channelLinks.update(i,{
            "posSettings": {
                "ncr": {
                    "eatinPaymentType": "10",
                    "pickupPaymentType": "10",
                    "paymentType": "10",
                    }
                    }
                    })

