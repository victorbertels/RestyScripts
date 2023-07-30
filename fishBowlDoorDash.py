
import requests
import json




url = "https://api.deliverect.com/channelLinks"
headers = {
  'If-Match': 'd49327efc877b6b9a1561fb3f53c13034d89c121',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODkzMTA5MTIsImV4cCI6MTY4OTM5NzMxMiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.l5INjZp_XKn5On3ijGeV6r08TwOjsNK_2Sum0QGaMNJsi0T__CERpY3Q6J34y1axmSzrDj2o4EaNwEq5EHW-HCDs_QBg29HQ5Sbfirq0G9KtiPC7kgxlJk0KwSPx1WXbln6mflCAlOgozC7pqQn9othLTH4B-zQswvLpWTcR1xrO_kwK8lhnNfNVy1OI35lJi-U6iPJxPGsOfs12cDu8alh7lX4-LGV_WkfNUo6ZLfIA-Fe7dztCM06ss1EAacMPe0T_7iabBV7IK-DPhDP_JG3EnfcD3EGoB07K2qrzjuc1v0RkExDLfvtOKfcSpzFKgsRiQx8qo_6MkXhkknkNRg'
}




account = "5eb08b2b87b1bf0001c3b292"
vicaccout = "647d1f8106cec41fc728af5f"

locs = pcli.locations.list_all(q={"account" : vicaccout})


for loc in locs:
   brandId = loc.subscriptions[0].brandId
   print(brandId)
   loc_id = loc._id
   squareId = loc.posSettings.square.locationId
   print(loc_id)
   payload =json.dumps( {
    "location": loc_id,
    "account": "5eb08b2b87b1bf0001c3b292",
    "posSystemId": 13,
    "taxExcl": False,
    "timezone": "Australia/Sydney",
    "fulfillmentEnabled": False,
    "channelSettings":
    {
        "useUpdateOrderItemsFlow": False,
        "useSetPrepTime": False,
        "insertPosOrderAfterDmaAccept": False,
        "roundTaxPerItem": False,
        "useDoorDashTaxAmount": False,
        "addDeliveryFeeToPaymentTotal": False,
        "autoAcceptOrderStatus": 20,
        "logChannelOperations": False,
        "sendRejectStatus": False,
        "sendProductTax": False,
        "isDoorDashCatalogCreated": False,
        "useCategoryAvailabilities": False,
        "sendImagesOnMenuPush": True,
        "sendCaloriesAsKJ": False,
        "coreFlatten": False,
        "storeUUID": "",
        "storeId": "",
        "provisioning": 0,
        "application": "PRODUCTION"
    },
    "posSettings":
    {
        "square":
        {
            "accessProfile": "_SquareProfile",
            "currency": "AUD",
            "bufferOrders": False,
            "logOps": True,
            "locationId": squareId,
            "anonymizeCustomer": False,
            "readonly": False,
            "sourceName": "",
            "cancelPlu": "",
            "orderNoteTemplate": "{channelName} {br}{orderNote}",
            "manageInventory": False,
            "useOverloads": True,
            "snoozeOnSync": False,
            "useVariants": False,
            "sortModifiers": 0,
            "sendDiscount": False,
            "sendDeliveryFee": False,
            "sendServiceCharge": False,
            "sendTip": False,
            "sendDeliveryFeeCondition": 0,
            "deliveryByChannelIsPickup": False,
            "ignoreUnknownOrderStatuses": False,
            "recalcPriceOverrides": False,
            "useShipmentFulfillmentType": False,
            "usePreparationTime": True,
            "overrideSource": "",
            "useSquareCatalogTaxes": False,
            "bagFeeChargeId": "",
            "separateSameProducts": False,
            "averagePreparationTime": 15,
            "averageDeliveryTime": 15,
            "dontSendCancel": False
        }
    },
    "paymentProfile": "online-ordering0",
    "brandId": brandId,
    "menuUrl": "",
    "status": 2,
    "name": "DoorDash",
    "channel": 12,
    "priceLevelSettings":
    {},
    "anonymizeCustomer": False,
    "bufferOrders": False,
    "defaultPreparationTime": 15,
    "averageDeliveryTime": 15,
    "mockPOS": False,
    "logPOS": True,
    "application": "PRODUCTION"
})
   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.text)







channelLinks ={"64aca4388badb4e28415d3a6": "25142066",
                "64aca42a5895e26670f81219": "25143191",
                "64aca42f0854b3d77624b8aa": "25142812",
                "64aca42d334ab6881dac09bf": "25143882",
                "64aca434540bd199503556bf": "25143202",
                "64aca44a8144ef06ca32d8f0": "25142983",
                "64aca451c54ef1ceba8ff2c7": "25142810",
                "64aca43c0854b3d77624b9dc": "25142985",
                "64aca42c6db06b23d8cad3e2": "25142807",
                "64aca4527e7c9f3c67f57bff": "25142061",
                "64aca4295895e26670f7fec2": "25143195",
                "64aca43287312bcb07714fdb": "25142073",
                "64aca4277434ef980390ff25": "25142065",
                "64aca42bac4f12dd1ee1b071": "25142067",
                "64aca43041288471cf27f2c3": "25142982",
                "64aca444c54ef1ceba8ff076": "25142808",
                "64aca43ef3e109884280654d": "25143883",
                "64aca44f6db06b23d8cadb99": "25142068",
                "64aca43a8144ef06ca32d54d": "25142984",
                "64aca4357434ef980391023b": "25142070",
                "64aca448b48d180e42e90d8e": "25143194",
                "64aca426b6414eabe6a0fd74": "25142059",
                "64aca443d95e46074a953adc": "25142809",
                "64aca437ac4f12dd1ee1b287": "25143891",
                "64aca4460854b3d77624be3b": "25142062",
                "64aca448ac4f12dd1ee1c641": "25143886",
                "64aca436c17215ed28be797e": "25143895",
                "64aca441ac4f12dd1ee1b99c": "25143196",
                "64aca44c5895e26670f81a12": "25143885",
                "64aca431b48d180e42e90a82": "25142060",
                "64aca429540bd199503554f1": "25142072",
                "64aca43987312bcb077150ed": "25142064",
                "64aca445297614b9823656ac": "25142805",
                "64aca450540bd19950355ba5": "25143199",
                "64aca43dc54ef1ceba8feec1": "25144054"}



account = "5eb08b2b87b1bf0001c3b292"
channel = 12
get_doordash = pcli.channelLinks.list_all(q={"account" : account , "channel" : channel})

for link in get_doordash:
   pcli.channelLinks.update(link,{
         "channelSettings": {
       "menuIds": [
      "62ce5090badaac62c7a1a74c"
    ]},  "status": 3
   })




account = "5eb08b2b87b1bf0001c3b292"
channel = 12
get_doordash = pcli.channelLinks.list_all(q={"account" : account , "channel" : channel})

for link in get_doordash:
   location = link.location
   squareId = link.posSettings.square.locationId
   get_location_id = pcli.locations.get(location).name
   print("location Name - ",get_location_id , "Square id - " ,squareId )









# for channel in channelLinks:
#    get_channel = pcli.channelLinks.get(channel)
#    for get in get_channel:
#       print(get._id)



account = "5eb08b2b87b1bf0001c3b292"
channel = 12
get_doordash = pcli.channelLinks.list_all(q={"account" : account , "channel" : channel})

for link in get_doordash:
    location = link.location
    get_location_id = pcli.locations.get(location).posSettings.square.locationId
    print(get_location_id)
    pcli.channelLinks.update(link,{
      "posSettings": {
    "square": {

      "locationId": get_location_id
    }}})
