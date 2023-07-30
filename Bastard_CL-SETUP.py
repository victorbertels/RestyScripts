#BASTARD POS SETTINGS 
 
#whole account
acc_query ={'account' : '5f3a9a3c1d3f1ba68382d311'}

#1 location
loc_query ={'account' : '5f3a9a3c1d3f1ba68382d311','location' : {"$in":["6025568fd29fa5270cf43338", "6025568fd29fa5270cf43346" , "6025568fd29fa5270cf43344"]}}

#1 CL

cl_query ={'account' : '5f3a9a3c1d3f1ba68382d311','_id' : '612cb7a8071cd31e8620c826'}


links = pcli.channelLinks.list_all(q=cl_query)

for link in links:
    channel =   link.get('channel')
    if channel == 3:
        pcli.channelLinks.update(link,{
            "productLocation": "5f3a9a74cce756ca773bfeea",
            "posSettings": {
                "simphony": {
                "posVersion": "2.7",
                "sendOrderType": True,
                "timeZone": "Europe/Amsterdam",
                "employeeObjectNumber": "8",
                "revenueCenter": "4",
                "paidPaymentType": "8502",
                "orderTypeId": "5",
                "itemMenuLevel": 1,
                "itemSubLevel": 1,
                "priceLevel": 0,
                "noteItemPlu": "900000001-1",
                "bufferOrders": False,
                "logOps": True,
                "anonymizeCustomer": False,
                "readonly": False,
                "pCheckInfoLinesTemplate": "",
                "dontSendPhoneNumber": False,
                "vipOrder": False,
                "rushOrder": False,
                "useCommaAsDecimalCharacter": False,
                "cropCustomerName": False,
                "onlySendOrderDisplayIdForCheckId": False,
                "sendCheckId": False,
                "noteTemplate": "",
                "sendAddressInNoteItem": False,
                "checkToFireDateAsap": False,
                "orderNoteTemplate": "F: {displayOrderId}, {pickUpTime}, {customerName}",
                "paginateProductSync": False,
                "dontLinkModGroups": False,
                "productsFamilyGroups": "",
                "productsSyncRanges": "",
                "modifierMultiplier": "",
                "replaceNonAsciiSymbols": False,
                "hasAuth": False,
                "autoFinalizeOrders": True,
                "usePLUForCharges": False,
                "putNoteItemsAtTop": False,
                "tipPLU": "",
                "serviceChargePLU": "",
                "deliveryPLU": ""
            }}})
    elif channel == 7:
        pcli.channelLinks.update(link,{
            "productLocation": "5f3a9a74cce756ca773bfeea",
            "posSettings": {
                "simphony": {
                "itemMenuLevel": 0,
                "itemSubLevel": 0,
                "revenueCenter": "4",
                "employeeObjectNumber": "8",
                "posVersion": "2.7",
                "paidPaymentType": "8501",
                "orderTypeId": "5",
                "noteItemPlu": "900000001-1",
                "sendOrderType": True,
                "timeZone": "Europe/Amsterdam",
                "priceLevel": 0,
                "bufferOrders": False,
                "logOps": True,
                "anonymizeCustomer": False,
                "readonly": False,
                "pCheckInfoLinesTemplate": "",
                "dontSendPhoneNumber": False,
                "vipOrder": False,
                "rushOrder": False,
                "useCommaAsDecimalCharacter": False,
                "cropCustomerName": False,
                "onlySendOrderDisplayIdForCheckId": False,
                "sendCheckId": False,
                "noteTemplate": "",
                "sendAddressInNoteItem": False,
                "checkToFireDateAsap": False,
                "orderNoteTemplate": "U: {displayOrderId}, {pickUpTime}, {customerName}",
                "paginateProductSync": False,
                "dontLinkModGroups": False,
                "productsFamilyGroups": "",
                "productsSyncRanges": "",
                "modifierMultiplier": "",
                "replaceNonAsciiSymbols": False,
                "hasAuth": False,
                "autoFinalizeOrders": True,
                "usePLUForCharges": False,
                "putNoteItemsAtTop": False,
                "tipPLU": "",
                "serviceChargePLU": "",
                "deliveryPLU": ""
                }}})
    elif channel == 1:
            pcli.channelLinks.update(link,{
                "productLocation": "5f3a9a74cce756ca773bfeea",
                "posSettings": {
                    "simphony": {
                    "itemMenuLevel": 0,
                    "itemSubLevel": 0,
                    "revenueCenter": "4",
                    "employeeObjectNumber": "8",
                    "posVersion": "2.7",
                    "paidPaymentType": "8501",
                    "orderTypeId": "5",
                    "noteItemPlu": "900000001-1",
                    "sendOrderType": True,
                    "timeZone": "Europe/Amsterdam",
                    "priceLevel": 0,
                    "bufferOrders": False,
                    "logOps": True,
                    "anonymizeCustomer": False,
                    "readonly": False,
                    "pCheckInfoLinesTemplate": "",
                    "dontSendPhoneNumber": False,
                    "vipOrder": False,
                    "rushOrder": False,
                    "useCommaAsDecimalCharacter": False,
                    "cropCustomerName": False,
                    "onlySendOrderDisplayIdForCheckId": False,
                    "sendCheckId": False,
                    "noteTemplate": "",
                    "sendAddressInNoteItem": False,
                    "checkToFireDateAsap": False,
                    "orderNoteTemplate": "DEL: {displayOrderId}, {pickUpTime}, {customerName}",
                    "paginateProductSync": False,
                    "dontLinkModGroups": False,
                    "productsSyncRanges": "",
                    "modifierMultiplier": "",
                    "productsFamilyGroups": "",
                    "replaceNonAsciiSymbols": False,
                    "hasAuth": False,
                    "autoFinalizeOrders": True,
                    "usePLUForCharges": False,
                    "putNoteItemsAtTop": False,
                    "tipPLU": "",
                    "serviceChargePLU": "",
                    "deliveryPLU": ""
                    }}})
    elif channel == 16:
            pcli.channelLinks.update(link,{
                "productLocation": "5f3a9a74cce756ca773bfeea",
                "posSettings": {
                    "simphony": {
                    "itemMenuLevel": 0,
                    "itemSubLevel": 0,
                    "revenueCenter": "4",
                    "employeeObjectNumber": "8",
                    "posVersion": "2.7",
                    "paidPaymentType": "8503",
                    "orderTypeId": "5",
                    "noteItemPlu": "900000001-1",
                    "sendOrderType": True,
                    "timeZone": "Europe/Amsterdam",
                    "priceLevel": 0,
                    "bufferOrders": False,
                    "logOps": False,
                    "anonymizeCustomer": False,
                    "readonly": False,
                    "pCheckInfoLinesTemplate": "",
                    "dontSendPhoneNumber": False,
                    "vipOrder": False,
                    "rushOrder": False,
                    "useCommaAsDecimalCharacter": False,
                    "cropCustomerName": False,
                    "onlySendOrderDisplayIdForCheckId": False,
                    "sendCheckId": False,
                    "noteTemplate": "",
                    "sendAddressInNoteItem": False,
                    "checkToFireDateAsap": False,
                    "orderNoteTemplate": "W: {displayOrderId}, {pickUpTime}, {customerName}",
                    "paginateProductSync": False,
                    "dontLinkModGroups": False,
                    "productsSyncRanges": "",
                    "modifierMultiplier": "",
                    "productsFamilyGroups": "",
                    "replaceNonAsciiSymbols": False,
                    "hasAuth": False,
                    "autoFinalizeOrders": True,
                    "usePLUForCharges": False,
                    "putNoteItemsAtTop": False,
                    "tipPLU": "",
                    "serviceChargePLU": "",
                    "deliveryPLU": ""
                    }}})


