

# while True:
import requests
import json
import random

url = "https://zambrerodevapi.xchangefusion.com/api/v3/OnlineOrders"
random_integer = random.randint(1, 1000000000)
# print(random_integer)
payload = json.dumps({
"id": None,
"source": None,
"saleName": "onlineORderTypetozero0",
"pickupLocation": 47,
"pickUpDate": "2023-07-03T08:38:48Z",
"orderedDate": "2023-07-03T08:23:49Z",
"tableNumber": None,
"isDelivery": True,
"status": None,
"memberId": None,
"covers": None,
"addedDate": None,
"extraInstructions": "This is a test order",
"displayNumber": None,
"partialMember": None,
"clerkId": None,
"onlineOrderType": 8,
"masterOrderID": None,
"sendToKMS": True,
"sendToPrinters": True,
"totalNettValue": None,
"totalNettValueBeforeSaleDiscount": None,
"totalGrossValue": None,
"totalSaleValueInitial": None,
"totalSaleValueFinal": None,
"totalTaxes": [],
"totalLeftToPay": None,
"totalSaleDiscountAppliedAmount": None,
"totalPaid": None,
"orderTypeId": 0,
"transactionId": None,
"isRated": None,
"sendReceiptOnEmail": None,
"loyaltyAppId": None,
"receiptNotificationEmailAdresses": [],
"favouriteId": None,
"posPrepaid": None,
"externalSaleName": None,
"canceledDate": None,
"items": [
    {
    "id": 102368,
    "freeProductID": None,
    "displayName": "Corn Chips",
    "displayDescription": None,
    "orderId": None,
    "plu": 102368,
    "quantity": 1,
    "initialQuantity": None,
    "excludeFromExternalPartnerPricing": None,
    "type": None,
    "value": 3.5,
    "initialUnitPrice": 3.5,
    "unitPrice": 3.5,
    "redeemedProductId": None,
    "isRedeemedByPoints": None,
    "pointsValue": None,
    "modifiers": [],
    "ingredientsChanges": {
        "ingredientsModified": [],
        "ingredientsRemoved": [],
        "ingredientsAdded": [],
        "ingredientsSwapped": [],
        "standaloneModifier": []
    },
    "specialInstructions": None,
    "isHiddenFromUser": None,
    "discount": None,
    "voucherId": None,
    "voucherCode": None,
    "taxBase": None,
    "taxes": [],
    "grossValue": None,
    "nettValue": None,
    "saleValueInitial": None,
    "saleValueFinal": None
    }
],
"medias": [
    {
    "id": None,
    "mediaDescription": "Cash",
    "customerFriendlyName": "Cash",
    "mediaId": 1,
    "orderId": None,
    "value": 3.5,
    "paymentType": 1,
    "paymentTransactionId": None,
    "isTax": False
    }
],
"menuFlowActivations": [],
"onlineDiscounts": [],
"externalPartners": [],
"surcharges": [],
"orderTypeDetails": [],
"orderTypeDisclaimers": [],
"deliveryDetails": {
    "street": "4 The Krook",
    "building": "4",
    "unit": None,
    "city": "Gent",
    "postCode": "8888KL",
    "latitude": None,
    "longitude": None,
    "extraInstructions": "",
    "desiredDeliveryTime": "2023-07-01T08:53:48Z",
    "estimatedDeliveryTime": "2023-07-01T08:53:48Z"
},
"activatedVouchers": []
})
headers = {
'ClientAppKey': 'deliverect-olo',
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)






