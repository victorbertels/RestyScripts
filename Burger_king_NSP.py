query ={'account' : '607ea092ebe636845abc1fdf',"location" : {"$in":["60af56be61e33cf240b7d7dd","60af56f86f00d645a5fd9eb0","60af56d26f00d645a5fd8262"]}}
links = pcli.channelLinks.list_all(q=query)

urlReferenceMap={
        "608aa6f83103cfcafb01ab0c":"http://62.181.248.138:3070/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1232":"http://62.181.248.138:3011/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1234":"http://62.181.248.138:3150/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1235":"http://62.181.248.138:3020/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1236":"http://62.181.248.138:3040/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1237":"http://62.181.248.138:3210/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1238":"http://62.181.248.138:3145/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e123a":"http://62.181.248.138:3212/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e123b":"http://62.181.248.138:3013/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e123c":"http://62.181.248.138:3010/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e123d":"http://62.181.248.138:3230/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e123e":"http://62.181.248.138:3050/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e123f":"http://62.181.248.138:3140/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1240":"http://62.181.248.138:3118/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1241":"http://62.181.248.138:3165/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1242":"http://62.181.248.138:3220/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1243":"http://62.181.248.138:3012/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1244":"http://62.181.248.138:3250/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1246":"http://62.181.248.138:3090/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1247":"http://62.181.248.138:3014/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1248":"http://62.181.248.138:3290/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e1249":"http://62.181.248.138:3060/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e124a":"http://62.181.248.138:3310/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e124b":"http://62.181.248.138:3041/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e124c":"http://62.181.248.138:3225/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e124d":"http://62.181.248.138:3115/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "608fd4e2b714b84ad92e124e":"http://62.181.248.138:3315/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "607fe0ac14c33bd414c955b6":"http://62.181.248.138:9001/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "60af56d26f00d645a5fd8262":"http://62.181.248.138:3030/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "60af56f86f00d645a5fd9eb0":"http://62.181.248.138:3120/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl",
        "60af56be61e33cf240b7d7dd":"http://62.181.248.138:3131/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl"
    }

for link in links:
    channel =   link.get('channel')
    location = link.get('location')
    print(channel , location)
    print(str(urlReferenceMap.get(location,"something"))),
    if channel == 7:        
        pcli.channelLinks.update(link,{
            "productLocation": "607fe0ac14c33bd414c955b6",
            "posSettings": {
                "res3700": {
                    "noteItemPlu": "8999997",
                    "checkIdTemplate": "",
                    "serverEndpoint": str(urlReferenceMap.get(location,"something")),
                    "noteTemplate": "",
                    "itemMenuLevel": 1,
                    "serviceChargePLU": "",
                    "deliveryPLU": "",
                    "orderNoteTemplate": "",
                    "productsFamilyGroups": "",
                    "productsSyncRanges": "",
                    "itemSubLevel": 0,
                    "sortModifiers": 1,
                    "revenueCenter": 5,
                    "priceId": 1,
                    "employeeObjectNumber": 10001,
                    "paidPaymentId": 408,
                    "notPaidPaymentId": 901,
                    "orderTypeId": 6,
                    "skipProductSecondName": True,
                    "logOps": True,
                    "overrideEndpoint": True,
                    "averagePreparationTime": 15,
                    "overrideEndpoint": True

                    }},
                "channelSettings" : {
                    "application" : "MICROS",
                    "sendServiceCharge": False,
                    "sendDeliveryFee": False
        }})
    elif channel == 3:
        pcli.channelLinks.update(link,{
            "productLocation": "607fe0ac14c33bd414c955b6",
            "posSettings": {
                "res3700": {
                    "noteItemPlu": "8999997",
                    "checkIdTemplate": "",
                    "noteTemplate": "",
                    "itemMenuLevel": 1,
                    "serviceChargePLU": "",
                    "deliveryPLU": "",
                    "serverEndpoint": str(urlReferenceMap.get(location,"something")),
                    "orderNoteTemplate": "",
                    "productsFamilyGroups": "",
                    "productsSyncRanges": "",
                    "itemSubLevel": 0,
                    "sortModifiers": 1,
                    "revenueCenter": 5,
                    "priceId": 1,
                    "employeeObjectNumber": 10001,
                    "paidPaymentId": 406,
                    "notPaidPaymentId": 901,
                    "orderTypeId": 6,
                    "skipProductSecondName": True,
                    "logOps": True,
                    "overrideEndpoint": True,
                    "averagePreparationTime": 15,
                    "overrideEndpoint": True
                    }},
                "channelSettings": {
                    "region": "EU",
                    "application": "PRODUCTION",
                    "chainCode" : "Burger-King-SE",
                    "sendServiceCharge": False,
                    "sendDeliveryFee": False

                }})
            
    elif channel == 1:
        pcli.channelLinks.update(link,{
            "productLocation": "607fe0ac14c33bd414c955b6",
            "posSettings": {
                "res3700": {
                    "noteItemPlu": "8999997",
                    "checkIdTemplate": "",
                    "noteTemplate": "",
                    "itemMenuLevel": 1,
                    "serviceChargePLU": "",
                    "serverEndpoint": str(urlReferenceMap.get(location,"something")),
                    "deliveryPLU": "",
                    "orderNoteTemplate": "",
                    "productsFamilyGroups": "",
                    "productsSyncRanges": "",
                    "itemSubLevel": 0,
                    "sortModifiers": 1,
                    "revenueCenter": 5,
                    "priceId": 1,
                    "employeeObjectNumber": 10001,
                    "paidPaymentId": 408,
                    "notPaidPaymentId": 901,
                    "orderTypeId": 6,
                    "skipProductSecondName": True,
                    "logOps": True,
                    "overrideEndpoint": True,
                    "averagePreparationTime": 15,
                    "overrideEndpoint": True
                    }}})


query ={'account' : '607ea092ebe636845abc1fdf'}
links = pcli.locations.list_all(q=query)

for loc in links: 
    locs = loc.get('_id')
    print(locs)
    print(str(urlReferenceMap.get(locs,"something")))
    pcli.locations.update(loc,{
            "productLocation": "607fe0ac14c33bd414c955b6",
            "posSettings": {
                "res3700": {
                    "noteItemPlu": "8999997",
                    "checkIdTemplate": "",
                    "serverEndpoint": str(urlReferenceMap.get(locs,"something")),
                    "noteTemplate": "",
                    "itemMenuLevel": 1,
                    "serviceChargePLU": "",
                    "deliveryPLU": "",
                    "orderNoteTemplate": "",
                    "productsFamilyGroups": "",
                    "productsSyncRanges": "",
                    "itemSubLevel": 0,
                    "sortModifiers": 1,
                    "revenueCenter": 5,
                    "priceId": 1,
                    "employeeObjectNumber": 10001,
                    "paidPaymentId": 406,
                    "notPaidPaymentId": 901,
                    "orderTypeId": 6,
                    "skipProductSecondName": True,
                    "logOps": True,
                    "overrideEndpoint": True,
                    "averagePreparationTime": 15,
                    "overrideEndpoint": True
                    }}})