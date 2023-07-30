## SET prodLoc

# Whole account
#query ={'account' : '5f3a9a3c1d3f1ba68382d311'}

#links = pcli.channelLinks.list_all(q=query)
#for link in links:
#    pcli.channelLinks.update(link,{"productLocation": "5f3a9a74cce756ca773bfeea"})
#account = "5f3a9a3c1d3f1ba68382d311"
locs = pcli.locations.list_all(q={"_id":"612cb78e310de5d8a3d79b7c"})
#locs = pcli.locations.list_all(q={"account":account})
for loc in locs: 
    pcli.locations.update(loc,{
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
                    "orderNoteTemplate": "",
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