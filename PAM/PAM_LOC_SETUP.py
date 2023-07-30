# Add multiple location id's you need to setup after the {"$in" : [
some_loc_query = {'account' : '5e81f14758168e0001d981d5',"_id" :{"$in" : [
        "61e8413dcfc8401a166231dc",
        "61e840f1cfc8401a1661e5b3",
        "61e841131140f879337902d7"
        ] }}
# if changing only 1, set it after the "_id" :
one_loc_query = {'account' : '5e81f14758168e0001d981d5',"_id": "61b870aa058fd8331c42c941"}

#change the part list_all(q= by one_loc_query or some_loc_query if need to update 1 or many and copy paste the whole thing in terminal
locs = pcli.locations.list_all(q=some_loc_query)


for loc in locs: 
    pcli.locations.update(loc,{
            "productLocation": "5f0830509f26c0077d566597",
            "posSettings": {
                "simphony": {
                "sendCheckId": False,
                "sendOrderType": False,
                "rushOrder": False,
                "vipOrder": False,
                "checkEmplOrder": False,
                "allowPartialOrder": False,
                "futureOrder": False,
                "hasAuth": True,
                "revenueCenter": "11",
                "employeeObjectNumber": "8963",
                "itemSubLevel": 3,
                "itemMenuLevel": 1,
                "posVersion": "18.2",
                "paidPaymentType": "101",
                "discountId": "104",
                "orderTypeId": "2",
                "notPaidPaymentType": "902",
                "tax1": 5,
                "taxObjectNumber1": 4,
                "priceLevel": 2,
                "username": "svc_deliverect_prod",
                "password": "w2g@V$T2*ejR",
                "timeZone": "Europe/London",
                "bufferOrders": False,
                "logOps": True,
                "anonymizeCustomer": False,
                "readonly": False,
                "useCommaAsDecimalCharacter": False,
                "cropCustomerName": False,
                "noteTemplate": "",
                "sendAddressInNoteItem": False,
                "noteItemPlu": "",
                "checkToFireDateAsap": False,
                "orderNoteTemplate": "",
                "discountPLU": "",
                "serviceChargePLU": "",
                "deliveryPLU": "",
                "modifierMultiplier": "",
                "taxExcl": False,
                "productsSyncRanges": "",
                "productsFamilyGroups": "",
                "dontLinkModGroups": False,
                "tax2": 20,
                "taxObjectNumber2": 2,
                "autoFinalizeOrders": True,
                "averagePreparationTime": 1,
                "usePLUForCharges": False,
                "pCheckInfoLinesTemplate": "",
                "dontSendPhoneNumber": False,
                "onlySendOrderDisplayIdForCheckId": False,
                "putNoteItemsAtTop": False,
                "paginateProductSync": False,
                "replaceNonAsciiSymbols": False
                }}},override=1,propagate = 'all')