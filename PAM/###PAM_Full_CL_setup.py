    #PAM_Full_CL_setup
deliveroo = {
        "posSettings": {
            "simphony": {
                "hasAuth": True,
                "revenueCenter": "11",
                "employeeObjectNumber": "8932",
                "itemMenuLevel": 1,
                "itemSubLevel": 3,
                "paidPaymentType": "308",
                "notPaidPaymentType": "902",
                "discountId": "826002002",
                "orderTypeId": "3",
                "posVersion": "18.2",
                "sendCheckId": True,
                "sendOrderType": False,
                "rushOrder": False,
                "vipOrder": False,
                "checkEmplOrder": False,
                "allowPartialOrder": False,
                "futureOrder": False,
                "tax1": 5,
                "taxObjectNumber1": 4,
                "timeZone": "Europe/London",
                "bufferOrders": False,
                "logOps": True,
                "anonymizeCustomer": False,
                "readonly": False,
                "useCommaAsDecimalCharacter": False,
                "cropCustomerName": False,
                "sendAddressInNoteItem": False,
                "checkToFireDateAsap": False,
                "dontSendPhoneNumber": False,
                "onlySendOrderDisplayIdForCheckId": False,
                "username": "svc_deliverect_prod",
                "password": "w2g@V$T2*ejR",
                "taxExcl": False,
                "dontLinkModGroups": True,
                "timezone": "Europe/London",
                "averagePreparationTime": 1,
                "autoFinalizeOrders": False
        }}}

uber = {"posSettings": {
            "simphony": {
            "hasAuth": True,
            "revenueCenter": "11",
            "employeeObjectNumber": "8955",
            "itemMenuLevel": 1,
            "itemSubLevel": 3,
            "paidPaymentType": "310",
            "notPaidPaymentType": "902",
            "discountId": "826002002",
            "orderTypeId": "5",
            "posVersion": "18.2",
            "sendCheckId": True,
            "sendOrderType": False,
            "rushOrder": False,
            "vipOrder": False,
            "checkEmplOrder": False,
            "allowPartialOrder": False,
            "futureOrder": False,
            "tax1": 5,
            "taxObjectNumber1": 4,
            "timeZone": "Europe/London",
            "bufferOrders": False,
            "logOps": True,
            "anonymizeCustomer": False,
            "readonly": False,
            "useCommaAsDecimalCharacter": False,
            "cropCustomerName": False,
            "sendAddressInNoteItem": False,
            "checkToFireDateAsap": False,
            "dontSendPhoneNumber": False,
            "onlySendOrderDisplayIdForCheckId": False,
            "username": "svc_deliverect_prod",
            "password": "w2g@V$T2*ejR",
            "taxExcl": False,
            "dontLinkModGroups": True,
            "timezone": "Europe/London",
            "averagePreparationTime": 1,
            "autoFinalizeOrders": False
        }}}

query = {'account' : '5e81f14758168e0001d981d5', 'location' : {'$in':["6092854a7cf1d971774ab133","6092854a7cf1d971774ab132"]}}
links = pcli.channelLinks.list_all(q=query)

for link in links: 
    channel = link.get('channel')
    print(channel)
    if channel == 7:
        pcli.channelLinks.update(link,uber)

    elif channel == 2:
        pcli.channelLinks.update(link,deliveroo)

    elif channel == 1:
        print("i'm not going to do any thing ")
