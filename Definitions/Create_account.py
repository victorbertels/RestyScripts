import requests
import json
import time


#print('Enter your token:')
#token = str(input())
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjIzNjEwMzksImV4cCI6MTY2MjQ0NzQzOSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.YxIFgthic0OlqjPVzbJW0UySVmzGuM1iwILg4WgCmB6iN0ftXiSR177ZD0i_k4y71RSpmjPvXaKmVjjA1su-gwPmBW5jOum2x-RTAnDhwZMKNDp3aZtvsJcSmAwQH5dnhhHSj8TiL3pe2E9XjDZREMv0b3dPtbD83OxACNZhwqptwJ5Zf531b_x3MAqRLA7RvtnM7p-c86SJHY-9MOQMxZ6rqLOZyQndR2YKOvDkIXzMdYIptqfa_IZ61psjAvH4E9dTrjRa5ev34gUYPIR5QW_0UlCM1el26GvZ8AzNeEMiiTEm3vlS1LAARqy9D9pRDCqIVETJl5dOvChA4SzLuQ"
print("Whats the name of the new account: ")
inputname = str(input())
print("Paste your SubId")
subscription = str(input())
acc_url = "https://api.deliverect.com/accounts"
loc_url = "https://api.deliverect.com/locations"
cl_url = "https://api.deliverect.com/channelLinks" 
headers = {
    'Authorization': "Bearer " f"{token}",
    'Content-Type': 'application/json'
            }

acc_to_create = []
location_to_create = []

def _createAccount(name):
    payload = json.dumps({
    "name":name,
    "accountType":3,
    "status":"STATUS_TESTING",
    "posSystem":25,
    "currency":6,
    "storeTimezone":"Australia/Sydney",
    "whitelabel":"deliverect",
    "region":"AUS",
    "settings":{
        "taxExcl":False
    },
    "featureFlags":{
        "combinedProductsPage":True,
        "showProductsV21":False,
        "autoApply":False,
        "bottleDepositPrices":False,
        "allowLocationSelectionInProductsV2":False,
        "enableCalorieRanges":False,
        "showProductNutritionalInfo":False,
        "enablePartnerIntegrationPage":False,
        "enableLeadsDashboard":False,
        "enableLeadsDashboardTransactional":False,
        "enableOOOneClick":False,
        "enableOOEatIn":False,
        "enableNewOOOnboarding":False,
        "enableDMAProductSync":False,
        "enableDMAIntercom":False,
        "showPLUOnDMA":False,
        "showOldDMAOrders":False,
        "enableQCommerce":False,
        "printNumberOfItemsDMA":False,
        "injectPosOrdersWithoutDmaAccept":False,
        "enableSelfOnboarding":False,
        "enableSetupGuide":False,
        "salesChannels":False,
        "bagFeeMapping":False,
        "showReportsPage":False,
        "enableFinance":False,
        "enablePayments":False,
        "enableNewLayout":False,
        "enableNotificationSettings":False,
        "enableLocationTags":False,
        "enableWhatsAppIntegration":False,
        "enableCourierCheckIn":False,
        "menuLocationOverrides":False,
        "pullAvailabilities":False,
        "enableMenuAvailabilities":False,
        "menuLocationRestriction":False,
        "menuOptimization":False,
        "enableUnsnoozeAllProducts":False,
        "dashboardReviews":False,
        "enhanceOpeningHours":False
    },
    "deliverectVersion":"2.0"
           
        

            })
    response = requests.request("POST", acc_url, headers=headers, data=payload)
    if response.ok:
        jsonResponse = response.json()
        account_id = jsonResponse.get('_id')
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("----------------------------------------------")
        print(f"ACCOUNT : {name} HAS BEEN SUCCESFULLY BUILT")
        print(f"THIS IS YOUR ACCOUNT ID: {account_id}")
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("----------------------------------------------")
        acc_to_create.append(account_id)
    else:
        print("Incorrect: ",response)
        print("Refresh your token")


def _createLocation(locationName,accountId,subId):
    payload = json.dumps({
        "account": accountId,
        "name": str(locationName),
        "status": "TESTING",
        "subscriptions":
        [],
        "comment": "",
        "enableOutOfStock": False,
        "splitOrderItems": False,
        "enableWorkstations": False,
        "ignorePOSOrderStatuses": False,
        "posSystemId": 25,
        "address":
        {
            "remarks": "",
            "phoneNumber": "",
            "houseNumber": "",
            "street": "",
            "postalCode": "",
            "city": "",
            "restaurantName": ""
        },
        "contact":
        {
            "phoneNumber": "",
            "email": "",
            "firstName": "",
            "lastName": ""
        },
        "timezone": "Australia/Sydney",
        "taxExcl": False,
        "enablePickupScreen": False,
        "enablePickupScreenQR": False,
        "pickupScreenSubscriptionId": "",
        "posSettings":
        {
            "kounta":
            {
                "showOnline": False,
                "defaultServiceFeeTax": 0,
                "defaultDeliveryFeeTax": 0,
                "anonymizeCustomer": False,
                "completeWhenPaid": True,
                "passThruPrinting": False,
                "overrideNumberOfCustomers": 0,
                "sendDiscount": False,
                "sendDeliveryFee": False,
                "sendServiceCharge": False,
                "sendDeliveryFeeCondition": 0,
                "posOrdersAreAlwaysPaid": False,
                "sendTip": False,
                "sortModifiers": 0,
                "bufferOrders": False,
                "deliveryByChannelIsPickup": False,
                "ignoreUnknownOrderStatuses": False,
                "recalcPriceOverrides": False,
                "enableCourierUpdates": False,
                "readonly": False,
                "logOps": False
            }
        }
    })
    response = requests.request("POST", loc_url, headers=headers, data=payload)
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("----------------------------------------------")
    print(f"CREATING LOCATION.....")
    print("----------------------------------------------")
    print("----------------------------------------------")
    print("----------------------------------------------")
    if response.ok:
        jsonResponse = response.json()
        loc_id = jsonResponse['_id']
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("LOCATION SUCCESFULLY CREATES")
        print("this is your location Id", loc_id )
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("----------------------------------------------")
        location_to_create.append(loc_id)
        time.sleep(1)

        print("----------------------------------------------")
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("UPDATING THE SUBSCRIPTION ID")
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("----------------------------------------------")
        url = f"https://api.deliverect.com/locations/{loc_id}"
        getInfo = requests.request("GET", url, headers=headers, data=payload)
        getInfoResponse = getInfo.json()
        accIdList = []
        accountId = getInfoResponse.get("account")
        accIdList.append(accountId)
        etag = getInfoResponse.get("_etag")
        jsonSubs = getInfoResponse.get('subscriptions')
        brandId = str(jsonSubs)[14:-3]
        etagheaders = {
            'Authorization': "Bearer " f"{token}",
            'If-Match': f'{etag}',
            'Content-Type': 'application/json'
                    }
        correct_payload = json.dumps({
        "subscriptions":
        [
            {
                "brandId": f"{brandId}",
                "subscriptionId": f"{subId}"
            }
        ]
    }) 
        patchInfo = requests.request("PATCH", url, headers=etagheaders, data=correct_payload)
        if patchInfo.ok:
            #update partner account with new account ID
            #change the ID when going prod to 5e7b70272bb18e000197dedb
            partner_url = f"https://api.deliverect.com/accounts/5e7b70272bb18e000197dedb"
            partnerInfo = requests.request("GET", partner_url, headers=headers, data=payload)
            getPartnerResponse = partnerInfo.json()
            petag = getPartnerResponse.get("_etag")
            accounts = list(getPartnerResponse.get('accounts'))
            accounts.extend(accIdList)
            partnerPayload = json.dumps({"accounts" : accounts})
            partnerHeader = {
            'Authorization': "Bearer " f"{token}",
            'If-Match': f'{petag}',
            'Content-Type': 'application/json'
                    }
            print("waiting 2 seconds")
            time.sleep(2)
            patchPartnerInfo = requests.request("PATCH", partner_url, headers=partnerHeader, data=partnerPayload)
            patchresponse = patchPartnerInfo.json()
            if patchPartnerInfo.ok:
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("PARTNER ACCOUNT UPDATED")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("-------------Creating Channellink-------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                print("----------------------------------------------")
                #create channelLinks
                cl_payload = json.dumps({
            "location": f"{loc_id}",
            "account": f"{accountId}",
            "posSystemId": 25,
            "taxExcl": False,
            "timezone": "Australia/Sydney",
            "fulfillmentEnabled": False,
            "channelSettings":
            {
                "sendRejectStatus": False,
                "allowUpdateMenuPrepTime": False,
                "defaultTableId": ""
            },
            "posSettings":
            {
                "kounta":
                {
                    "showOnline": False,
                    "defaultServiceFeeTax": 0,
                    "defaultDeliveryFeeTax": 0,
                    "anonymizeCustomer": False,
                    "completeWhenPaid": True,
                    "passThruPrinting": False,
                    "overrideNumberOfCustomers": 0,
                    "sendDiscount": False,
                    "sendDeliveryFee": False,
                    "sendServiceCharge": False,
                    "sendDeliveryFeeCondition": 0,
                    "posOrdersAreAlwaysPaid": False,
                    "sendTip": False,
                    "sortModifiers": 0,
                    "bufferOrders": False,
                    "deliveryByChannelIsPickup": False,
                    "ignoreUnknownOrderStatuses": False,
                    "recalcPriceOverrides": False,
                    "enableCourierUpdates": False,
                    "readonly": False,
                    "logOps": False,
                    "discountPLU": "",
                    "deliveryPLU": "",
                    "serviceChargePLU": ""
                }
            },
            "paymentProfile": "",
            "brandId": f"{brandId}",
            "menuUrl": "",
            "status": 2,
            "name": "Test Channel",
            "channel": 1,
            "anonymizeCustomer": False,
            "bufferOrders": False,
            "mockPOS": False,
            "logPOS": False
        })
                createChannelLink = requests.request("POST", cl_url, headers=headers, data=cl_payload)
                CL = createChannelLink.json
                if createChannelLink.ok:
                    print("fiinished")
        else:
            print("==================KAPUT=======================")

    else:
        print("Incorrect: ",response)
        print("Refresh your token")



_createAccount(inputname)
just_the_id = str(acc_to_create)[2:-2]
_createLocation(inputname,just_the_id,subscription)
