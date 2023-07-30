#HMS SCRIPT SETTINGS

locationIdReferenceMap = {
    "5f3d0dc56b72c16c9191edbe" : 201524,
    "5f464d092918df92767abcde" : 201518,
    "5f47c46696246163227b1f3b" : 201517,
    "5f8448558ddd5086352ba441" : 201515,
    "5f84488c8ddd5086352bab86" : 201533,
    "5fa3e5e650f6ac7edbcceacf" : 201516,    
    "5fa3f675e0fe9ef2f5c1ff4c" : 201520,
    "603f52735de02e8e2fb9ecff" : 201519,
    "6051c2a7df73da810e75354b" : 201526,
    "5efc61d5a05ce1c014da6ca4" : 201528
    }



query ={'account' : '5e9eef1bc766d30001c6294c'}
links = pcli.channelLinks.list_all(q=query)

links = pcli.channelLinks.list_all(q=query)  
for link in links:
    channel =   link.get('channel')
    location = link.get('location')
    print(channel , location)
    print(str(locationIdReferenceMap.get(location,"something")))
    if channel == 2:        
        pcli.channelLinks.update(link,{
            "posSettings": {
                "simphony": {
                    "revenueCenter": str(locationIdReferenceMap.get(location,"something")),
                    "orderTypeId": "11",
                    "paidPaymentType": "310300002",
                    "notPaidPaymentType": "1002",
                    "employeeObjectNumber": "131012",
                    "noteItemPlu": "291000011-1",
                    "sendAddressInNoteItem": True,
                    "sendCheckId": True,
                    "logOps": True

            }}})
    elif channel == 8:
        pcli.channelLinks.update(link,{
            "posSettings": {
                "simphony": {
                    "revenueCenter": str(locationIdReferenceMap.get(location,"something")),
                    "orderTypeId": "11",
                    "paidPaymentType": "310300010",
                    "notPaidPaymentType": "1002",
                    "employeeObjectNumber": "131012",
                    "noteItemPlu": "291000011-1",
                    "sendAddressInNoteItem": True,
                    "sendCheckId": True,
                    "logOps": True
                
            }}})
            
    elif channel == 7:
        pcli.channelLinks.update(link,{
            "posSettings": {
                "simphony": {
                    "revenueCenter": str(locationIdReferenceMap.get(location,"something")),
                    "orderTypeId": "11",
                    "paidPaymentType": "310300015",
                    "notPaidPaymentType": "1002",
                    "employeeObjectNumber": "131012",
                    "noteItemPlu": "291000011-1",
                    "sendAddressInNoteItem": True,
                    "sendCheckId": True,
                    "logOps": True
            }}})
    elif channel == 1:
        pcli.channelLinks.update(link,{
            "posSettings": {
                "simphony": {
                    "revenueCenter": str(locationIdReferenceMap.get(location,"something")),
                    "orderTypeId": "11",
                    "paidPaymentType": "310300015",
                    "notPaidPaymentType": "1002",
                    "employeeObjectNumber": "131012",
                    "noteItemPlu": "291000011-1",
                    "sendAddressInNoteItem": True,
                    "sendCheckId": True,
                    "logOps": True
            }}})

second_query = {'account' : '5e9eef1bc766d30001c6294c' , 'posSettings':{'simphony':{'revenueCenter' : 'something'}} }    
check = pcli.channelLinks.list_all(q=query)

###sendDiscounts is on:
query ={'account' : '5e9eef1bc766d30001c6294c'}

links = pcli.channelLinks.list_all(q=query)  
for link in links:
    channel =   link.get('channel')
    if channel == 2:        
        pcli.channelLinks.update(link,{
          "sendDiscount": True,
          "channelSettings.sendDiscount" : True,
          "posSettings.simphony.discountId" : "310300302"
          
      
            })
    elif channel == 8:
        pcli.channelLinks.update(link,{
          "sendDiscount": True,
          "channelSettings.sendDiscount" : True,
          "posSettings.simphony.discountId" : "310300301"
                
            })
            
    elif channel == 7:
        pcli.channelLinks.update(link,{
          "sendDiscount": True,
          "channelSettings.sendDiscount" : True,
          "posSettings.simphony.discountId" : "310300303"
            })
    elif channel == 1:
        pcli.channelLinks.update(link,{
          "sendDiscount": True,
          "channelSettings.sendDiscount" : True,
          "posSettings.simphony.discountId" : "310300303"
            })



