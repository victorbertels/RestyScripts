query = {'account' : '5f9147e1a94e333fef335737'}

links = pcli.channelLinks.list_all(q=query)
for link in links:
    channel = link.get('channel')
    posSystem = link.get('posSystemId')
    #print(channel,posSystem)
    if posSystem == 27 and channel == 7:
        pcli.channelLinks.update(link,
        {
            "productLocation": "5f91499341dc4479c8785b23",
            "posSettings":{
                "res3700":{
                    "discountPLU": "100021",
                    "employeeObjectNumber" : "9000003",
                    "paidPaymentId" : 410,
                    "notPaidPaymentId": 410,
                    "noteTemplate": "{displayOrderId}{pickUpTime}",
                    "checkIdTemplate": "{orderId}, {pickUpTime}",
                    "revenueCenter": 1,
                    "averagePreparationTime": 455,
                    "bufferOrders": True,
                    "timeZone": "Europe/Amsterdam",
                    "sendCheckId": True,
                    "orderTypeId": 2,
                }}})
    elif posSystem == 27 and channel == 2 :
                pcli.channelLinks.update(link,
        {
            "productLocation": "5f91499341dc4479c8785b23",
            "posSettings":{
                "res3700":{
                    "discountPLU": "100021",
                    "employeeObjectNumber" : "9000001",
                    "paidPaymentId" : 410,
                    "notPaidPaymentId": 410,
                    "noteTemplate": "{displayOrderId}{pickUpTime}",
                    "checkIdTemplate": "{orderId}, {pickUpTime}",
                    "revenueCenter": 1,
                    "averagePreparationTime": 455,
                    "bufferOrders": True,
                    "timeZone": "Europe/Amsterdam",
                    "sendCheckId": True,
                    "orderTypeId": 2,
                }}})
    elif posSystem == 27 and channel ==  1:
        pcli.channelLinks.update(link,
        {
            "productLocation": "5f91499341dc4479c8785b23",
            "posSettings":{
                "res3700":{
                    "discountPLU": "100021",
                    "employeeObjectNumber" : "9000000",
                    "paidPaymentId" : 410,
                    "notPaidPaymentId": 410,
                    "noteTemplate": "{displayOrderId}{pickUpTime}",
                    "checkIdTemplate": "{orderId}, {pickUpTime}",
                    "revenueCenter": 1,
                    "averagePreparationTime": 455,
                    "bufferOrders": True,
                    "timeZone": "Europe/Amsterdam",
                    "sendCheckId": True,
                    "orderTypeId": 2,
                }}})
    elif posSystem == 27 and channel == 8:
          pcli.channelLinks.update(link,
        {
            "productLocation": "5f91499341dc4479c8785b23",
            "posSettings":{
                "res3700":{
                    "discountPLU": "100021",
                    "employeeObjectNumber" : "9000002",
                    "paidPaymentId" : 410,
                    "notPaidPaymentId": 410,
                    "noteTemplate": "{displayOrderId}{pickUpTime}",
                    "checkIdTemplate": "{orderId}, {pickUpTime}",
                    "revenueCenter": 1,
                    "averagePreparationTime": 455,
                    "bufferOrders": True,
                    "timeZone": "Europe/Amsterdam",
                    "sendCheckId": True,
                    "orderTypeId": 2,
                }}})
    else:
        print('suck it')



        









