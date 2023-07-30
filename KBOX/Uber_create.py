import json
from unicodedata import name
from urllib import request
import requests

location_list = ["WATERLOO",
"BORONIA",
"CHATSWOOD",
"DANDENONG",
"GLEN WAVERLEY",
"WEST PYMBLE",
"ALTONA",
"CENTRE ROAD, BENTLEIGH",
"HOPPERS CROSSING",
"KEILOR",
"MELTON",
"PHILLIP",
"SUNBURY",
"SURRY HILLS",
"CHADSTONE",
"ROUSE HILL",
"SOUTH YARRA",
"BANKSTOWN",
"BAYSWATER",
"LIVERPOOL ROAD, ASHFIELD",
"MITCHELL",
"NARRE WARREN SOUTH",
"WETHERILL PARK",
"BALWYN NORTH",
"BENTLEIGH",
"BURKE ROAD, KEW",
"CABRAMATTA",
"COLLAROY",
"COOGEE",
"DONCASTER",
"DUNDAS",
"FOOTSCRAY",
"GLADESVILLE",
"GUILDFORD",
"KINGSTON",
"LALOR",
"MAGILL",
"MITCHAM",
"PAGE",
"RIVERSDALE BLD, MERNDA",
"ROSEBUD",
"UNION RD, ASCOT VALE",
"WANTIRNA SOUTH",
"BLACKTOWN ROAD, BLACKTOWN",
"CARINGBAH",
"HINCHINBROOK",
"PRESTONS",
"WATSON",
"WINDSOR",
"CAROLINE SPRINGS",
"DOREEN",
"BRIGHTON-LE-SANDS",]

location_quantity = {"WATERLOO": "13",
"BORONIA ": "9",
"CHATSWOOD ": "9",
"DANDENONG ": "9",
"GLEN WAVERLEY ": "9",
"WEST PYMBLE ": "9",
"ALTONA ": "7",
"CENTRE ROAD, BENTLEIGH ": "7",
"HOPPERS CROSSING ": "7",
"KEILOR ": "7",
"MELTON ": "7",
"PHILLIP ": "7",
"SUNBURY ": "7",
"SURRY HILLS ": "7",
"CHADSTONE ": "6",
"ROUSE HILL ": "6",
"SOUTH YARRA ": "6",
"BANKSTOWN ": "5",
"BAYSWATER ": "5",
"LIVERPOOL ROAD, ASHFIELD ": "5",
"MITCHELL ": "5",
"NARRE WARREN SOUTH ": "5",
"WETHERILL PARK ": "5",
"BALWYN NORTH ": "4",
"BENTLEIGH ": "4",
"BURKE ROAD, KEW ": "4",
"CABRAMATTA ": "4",
"COLLAROY ": "4",
"COOGEE ": "4",
"DONCASTER ": "4",
"DUNDAS ": "4",
"FOOTSCRAY ": "4",
"GLADESVILLE ": "4",
"GUILDFORD ": "4",
"KINGSTON ": "4",
"LALOR ": "4",
"MAGILL ": "4",
"MITCHAM ": "4",
"PAGE ": "4",
"RIVERSDALE BLD, MERNDA ": "4",
"ROSEBUD ": "4",
"UNION RD, ASCOT VALE ": "4",
"WANTIRNA SOUTH ": "4",
"BLACKTOWN ROAD, BLACKTOWN ": "3",
"CARINGBAH ": "3",
"HINCHINBROOK ": "3",
"PRESTONS ": "3",
"WATSON ": "3",
"WINDSOR ": "3",
"CAROLINE SPRINGS ": "2",
"DOREEN ": "2",
"BRIGHTON-LE-SANDS ": "1",
}

for i in location_list:
        
    url = "https://api.deliverect.com/locations"
    print(i)

    payload = json.dumps({
    "posSettings": {
        "dma": {
        "locationId": "",
        "ordersWebhookURL": "",
        "syncTablesURL": "",
        "syncFloorsURL": "",
        "customHeaders": "",
        "setDefaultPriceLevelOnSync": False,
        "syncProductsURL": "",
        "anonymizeCustomer": False,
        "sendStreetNumber": False,
        "syncBillsURL": "",
        "hasDirectTableIntegration": False,
        "sendDiscount": False,
        "sendDeliveryFee": False,
        "sendServiceCharge": False,
        "sendDeliveryFeeCondition": 0,
        "posOrdersAreAlwaysPaid": False,
        "sendTip": False,
        "sendRebate": False,
        "receiptPaymentURL": "",
        "sortModifiers": 0,
        "bufferOrders": False,
        "deliveryByChannelIsPickup": False,
        "ignoreUnknownOrderStatuses": False,
        "recalcPriceOverrides": False,
        "enableCourierUpdates": False,
        "dontSendCancel": False,
        "orderNoteTemplate": "",
        "readonly": False,
        "logOps": False
        }
    },
    "status": "TESTING",
    "subscriptions": [
        {
        "brandId": "62fc44dc934376949a733247",
        "subscriptionId": "1"
        }
    ],
    "comment": "",
    "enableOutOfStock": False,
    "splitOrderItems": False,
    "enableWorkstations": False,
    "ignorePOSOrderStatuses": False,
    "posSystemId": 20000,
    "address": {
        "remarks": "",
        "phoneNumber": "",
        "houseNumber": "",
        "street": "",
        "postalCode": "",
        "city": "",
        "restaurantName": ""
    },
    "contact": {
        "phoneNumber": "",
        "email": "",
        "firstName": "",
        "lastName": ""
    },
    "timezone": "Australia/Sydney",
    "name": f"{i}",
    "taxExcl": False,
    "enablePickupScreen": False,
    "enablePickupScreenQR": False,
    "pickupScreenSubscriptionId": "",
    "account": "62fc44dc934376949a733248"
    })
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjI3MTE2ODYsImV4cCI6MTY2Mjc5ODA4NiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.UAsDYVzs-Q34Fs1usBcBvBhHQk3-78yv-AwFQOo8fykiEGPzl0pzNM_Tv7vJkk4EiQj_9IOl7gkkawHqx1nLhFZnRugFvw8K4YU66G_A-_KdmH836HrXIBVYJQO9WpaAYW12R_CaQWIvfyiyLzxl0-24cR9P0brP9T7pE2lVoThP6wLWisLOi_sZ0Fz0PjdrB4BBuKCbumKsrx-wDZt8L8JGkXeOwystzYayD91NPuMjWlMv9tzdRc3Oh16nwHwJ_dmhs4GGlhIGzj8f97nB1mwzHOIIrLiwONn3fUnHoRf4nJO55yPLjWIxEBYb9guUCQo2OJY9xFkZbbK3STM3QA',
  'Content-Type': 'application/json'
}

    # response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)


for lq in location_quantity:
    print(location_quantity[lq])

    for i in range(int(location_quantity[lq])):
        print(i)
        print(location_quantity[lq])


    url = "https://api.deliverect.com/channelLinks"

    payload = json.dumps({
    "location": f"{locaitonID}",
    "account": "62fc44dc934376949a733248",
    "posSystemId": 20000,
    "taxExcl": False,
    "timezone": "Australia/Sydney",
    "fulfillmentEnabled": False,
    "channelSettings": {
        "enableReleaseCall": False,
        "pollPickupTime": False,
        "autoAcceptOrderStatus": 1,
        "orderNoteTemplate": "",
        "excludeContactInfo": False,
        "enableItemLevelNotes": False,
        "sendReceiptId": False,
        "logChannelOperations": False,
        "sendRejectStatus": False,
        "sendMenuId": False,
        "skipImageResizer": False,
        "sendCaloriesAsKJ": False,
        "coreFlatten": False,
        "storeId": "",
        "application": "ROCKETSHIP",
        "provisioning": 0,
        "validateMenu": False,
        "checkRemoteSnoozes": False
    },
    "posSettings": {
        "dma": {
        "locationId": "",
        "ordersWebhookURL": "",
        "syncTablesURL": "",
        "syncFloorsURL": "",
        "customHeaders": "",
        "setDefaultPriceLevelOnSync": False,
        "syncProductsURL": "",
        "anonymizeCustomer": False,
        "sendStreetNumber": False,
        "syncBillsURL": "",
        "hasDirectTableIntegration": False,
        "sendDiscount": False,
        "sendDeliveryFee": False,
        "sendServiceCharge": False,
        "sendDeliveryFeeCondition": 0,
        "posOrdersAreAlwaysPaid": False,
        "sendTip": False,
        "sendRebate": False,
        "receiptPaymentURL": "",
        "sortModifiers": 0,
        "bufferOrders": False,
        "deliveryByChannelIsPickup": False,
        "ignoreUnknownOrderStatuses": False,
        "recalcPriceOverrides": False,
        "enableCourierUpdates": False,
        "dontSendCancel": False,
        "orderNoteTemplate": "",
        "readonly": False,
        "logOps": False,
        "orderItemRemarks": "intactItemRemarks",
        "alwaysSendAllSnoozedProducts": True,
        "snoozeWhenOutOfStock": None,
        "averagePreparationTime": 15,
        "averageDeliveryTime": 15
        }
    },
    "paymentProfile": "",
    "brandId": "62fc44dc934376949a733247",
    "menuUrl": "",
    "status": 2,
    "name": "Uber Eats",
    "channel": 7,
    "anonymizeCustomer": False,
    "bufferOrders": False,
    "defaultPreparationTime": 15,
    "averageDeliveryTime": 15,
    "mockPOS": False,
    "logPOS": False,
    "application": "ROCKETSHIP",
    "APIKey": ""
    })
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjI1MzgxNDEsImV4cCI6MTY2MjYyNDU0MSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.NJSwR66OJS7MeiD8t485Cr4vOTLReDBGWgbKpFWcuOoCTTbP1_PmnclF1gaNZNn9whT_9CIZrFhRjtdkYbzrGF7lH6OI4JrvxNmywA6mlJQSgZ_erQJ4M1jBSIcpRi_VKjKqpBfthP3xDIAJtFV6Zd6A70uz6ftm6EuOu7sCp5VN4xq7q_lk9XRcZJ9wWsG3yFXj6l_WV3D3lyfu_ArRMhjTudR0QaptVjV3NMPcurx3ddMCf3Xhpx4xmqNBvQRl4XzQwPyMd0aHPcik1cO_0e5XoppHAZjfHxMSsvBw3zS8VbP4EWXN5oxhV_1sN5NXa9JcPJ3eC_jyoFJ7hBxo4w',
    'Content-Type': 'application/json'
    }

    # response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)



query = pcli.locations.list_all(q={"account" : "62fc44dc934376949a733248"})

for i in query:
    print(i.name , "--",i._id)