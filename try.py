

ids = {"posSettings" : {"simphony" : {
    "notPaidPaymentType": "1002"
}}}


prod = {'account' : '6054c1d5c0e70796115e1d3e',"location":"6054c2d972958764ec6a7fdc" , 'channel': 30}
settings = pcli.channelLinks.list_all(q=prod)
for setting in settings:
    pcli.channelLinks.update(setting , { "channel": 1})


CL = {'account':'5e81f14758168e0001d981d5','channel': 10005}
CLS = pcli.channelLinks.list_all(q=CL)
for c in CLS:
    pcli.channelLinks.update(c,{
    "channelSettings": {
            "menuUpdateURL": "https://api1.pret.com/v1/deliverect/updatemenu",
            "statusUpdateURL": "https://api1.pret.com/v1/deliverect/orderstatus",
            "busyModeURL": "https://api1.pret.com/v1/deliverect/busymode",
            "activateURL": "https://api1.pret.com/v1/deliverect/channelstatus",
            "disabledProductsURL": "https://api1.pret.com/v1/deliverect/productdisable",
            "snoozeUnsnoozeURL": "https://api1.pret.com/v1/deliverect/snoozestatus",
    }})


pcli.products.update(setting,{ 'location' : None})
      

query ={ "channelSettings":{"storeId" : "ba4ae2db-0db0-44f9-910f-9f521166d4bd"}}


links = pcli.channelLinks.list_all(q={"channelSettings":{"storeId" : "ee05a35d-59ba-47c7-9405-0aae866e6279"}})
links = pcli.channelLinks.list_all(q={"channel" : 7,"channelSettings":{"storeId" : "995d02f4-6888-41b3-b0c1-750d2bd3c7c8"}})

for link in links: 
  print(link._id,"-",link.name,"-", link.channel)
CLId = "60743028c34ceeee01c68ad"

Curb = {'account' : '5faab0ed16e4a65ad8092eaf'}
links = pcli.channelLinks.list_all(q=Curb)

for link in links:
    pcli.channelLinks.update(link,{
      "reportingEndpoints": [
    {
      "endpointType": 10,
      "endpoint": "https://5lax7zqe50.execute-api.eu-west-1.amazonaws.com/production/events/deliverect/orders",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 10,
      "endpoint": "https://5lax7zqe50.execute-api.eu-west-1.amazonaws.com/production",
      "statusTrigger": [
        25
      ],
      "endpointLevel": 1
    }
  ]}







        

queryLink = {'account' :'6054c1d5c0e70796115e1d3e','channel':2}

url = "http://62.181.248.138:3150/ResPOSApiWeb/ResPosApiWeb.asmx?wsdl"

links = pcli.channelLinks.get("608fd637b605f734b2f950f1")

for link in links:
    pcli.channelLinks.update(link,{
    "posSettings": {
      "res3700":{
        "serverEndpoint": url    }}})
    

query ={'account' : '603cd4daee5752f56df40f35'}
links = pcli.locations.list_all(q=query)

for link in links:
    print(link.name,link._id)
    pcli.locations.update(link,{
    "posSettings": {
    "generic": {
      "bufferOrders": True,
      "averagePreparationTime": 30
  }}})


    pcli.locations.list_all(locs)
    for loc in locs:
      print(loc.name)



new_query = {'account' :"5ea18193785c9b000177cc31" }
new_prods = pcli.products.list_all(q=new_query)
for newprod in new_prods:
  sublevel = newprod.pluProps
  print(sublevel)
  


acc = "624f796288b904a46ab92175"
locs = pcli.locations.list_all(q={"account" : acc})
channels =pcli.channelLinks.list_all(q={"account" : acc})
for loc in locs:
  pcli.locations.delete(loc)

for channel in channels:
    pcli.channelLinks.delete(channel)


for link in links:
  pcli.channelLinks.update(link,{
    "channel": 1,
})


query ={'account' :"6017e71bcb8a91b4944db5fe",'channel' : 7 }
links = pcli.channelLinks.list_all(q=query)

for link in links:
  loc = link.get('location')
  location_name = pcli.locations.get(loc)
  app = link.channelSettings.application
  if app != 'ROCKETSHIP':
    print('this is is:',app)
    pcli.channelLinks.update(link,{
      "channelSettings.application" : 'THECLOUDPOS'
    })
    print('new app set and it is',link.channelSettings.application)
  print(location_name.name,',', link.name,',', link._id)
  print("channelLink ID : ",link._id," - ","channelLink name : ",link.name)  
  print("for", link.channelSettings.storeId, "the application is set to :",link.channelSettings.application)
  
  

  #print(link.channelSettings)
  print("storeId: ",link.channelSettings.storeId)
  print('Username: ',link.channelSettings.username)
  print('Password: ',link.channelSettings.password)
  print("accesToken: ",link.channelSettings.accessToken)
  pcli.channelLinks.update(link,{
    "channelSettings":{"application": "PRODUCTION"}
    #"channelSettings.password" : "7a3144c7c0d0b87affdce47d7bd300ad9bf22e2fc711333d366b3d51148b86ef"
  })

from random import randint
products = pcli.products.list_all(q={'account' : "5fdcaa8d12d2c46bbc11bdfa",   "isInternal": True, 'productType':1})
for prod in products: 
  #print(prod.plu)
  plus = prod.get("plu")
  print(plus)
  if plus[0] == "#":
    print('i am wrong')
    new_number =randint(100000,9999999)
    new_plu = str(new_number) + plus
    print(new_plu)
    #pcli.products.update(prod , {"plu" : new_plu})
  else:
    print("do nothing")










query ={'account' :"5e81f14758168e0001d981d5"}
links = pcli.channelLinks.list_all(q=query)

for link in links:
  charges = link.get('channelSettings')
  charges_state=charges.sendServiceCharge
  pcli.channelLinks.update(link,{
    "sendServiceCharge" : charges_state
  })
  
  #print(charges_state)
  if charges_state == True:
    print(link._id , charges_state)
  
query ={'account' :"5e81f14758168e0001d981d5"}
links = pcli.channelLinks.list_all(q=query)
for link in links:
  charges = link.channelSettings
  print(charges)

  
  charges_state=charges.sendServiceCharge
  print(charges_state)


  pcli.channelLinks.update(link,{
    "sendServiceCharge" : charges_state
  })

query = {'account' : '60ab40438d6c3db989a48d2e'}
links = pcli.channelLinks.list_all(q=query)


for link in links:
  delpu = link.posSettings.lightspeed.discountPLU
  discount = "posSettings.lightspeed.discountPLU"
  channel = link.channel
  print(channel)
  if channel == 2:
    pcli.channelLinks.update(link,{
      "posSettings.lightspeed.discountPLU" : "OD13"
    })
  elif channel == 20:
    pcli.channelLinks.update(link,{
      "posSettings.lightspeed.discountPLU" : "OD11"
    })
  elif channel == 14:
    pcli.channelLinks.update(link,{
      "posSettings.lightspeed.discountPLU" : "OD12"
    })



  #print(delpu)
  if delpu == None:
    print(link._id , link.name)
    print(link.name)


  root_paid = link.posOrdersAreAlwaysPaid
  nested_paid = link.channelSettings.posOrdersAreAlwaysPaid
  #print(nested_paid)
  #print(paid)
  if root_paid == None and nested_paid is not None:
    print(link._id,link.name)


acc_id ="5e81f14758168e0001d981d5"
query = {'account':acc_id}
links = pcli.channelLinks.list_all(q=query)
for link in links:
  apikey = link.channelSettings.APIkey
  print(apikey)

  })
  url = link.channelSettings.accessToken

  print(url)
  if url is None:
    print(link._id)
  print(url)
  print(link._id)


prodid = ["606eb57b7983f15bd2de00a3",
"5fb278283afd63cc36f4690c",
"5fb278283afd63cc36f46941",
"5fb278283afd63cc36f468dc",
"5fb278283afd63cc36f46924",
"5fb278293afd63cc36f469bf",
"6058adad19c07f0ca7ce418d",
"60631938cb6e67187f07e0d6",
"60461bafe6cf8a19d2a88605",
]

for prod in products:
  pcli.products.get(prodid)
  print(prod)

product_loc = '5f0830509f26c0077d566597'

acc = "6017e71bcb8a91b4944db5fe"
query = {'account' : acc}
links = pcli.channelLinks.list_all(q=query)

for link in links:
  print(link.channelSettings.logChannelOperations)
  pcli.channelLinks.update(link,{

    "channelSettings.logChannelOperations" : True
  })
  if prod_loc == None:
    print(prod_loc)
    pcli.channelLinks.update(link,{
    "productLocation" : product_loc})

  print(prod_loc)
  pcli.locations.update(link,{
    "productLocation" : product_loc})

internal_quer = {'account' : "6037d4911d6ed071c4f321f4",  "isInternal": True}
internal_prods = pcli.products.list_all(q=internal_quer)


query = {'account' : "6037d4911d6ed071c4f321f4" , "plu" :{"$in" : ["DEAL-SOULBOWL-P-LE-mb1m-22",
"DEAL-SMASH-P-SM-1Uof-34",
"DEAL-SMASH-P-BA-orMa-35",
"DEAL-SMASH-P-BE-CRlt-36",
"DEAL-SMASH-P-KI-FNQu-37",
"DEAL-SMASH-P-SM-WE3Q-38",
"DEAL-ELBURROP-ME-gUvC-7",
"DEAL-ELBURRO-P-FL-F8IQ-8",
"DEAL-ELBURRO-P-ME-t4WR-9",
"DEAL-ELBURRO-P-FL-OyqF-10",
"DEAL-BAHGAWK-P-BA-YTfM-5",
"DEAL-BAHGAWK-P-TH-b6bB-145",
"DEAL-BAHGAWK-P-TH-AgUa-147",
"DEAL-BAHGAWK-P-TH-zjvH-2",
"DEAL-CANDIE-P-CA-xmRs-186",
"DEAL-MACKA-P-MA-TCP7-258",
"DEAL-MACKA-P-WI-aInj-259",
"DEAL-ITALIANSIN-P-TE-JvIP-281",
"DEAL-ITALIANSIN-P-TA-13uA-283",
"DEAL-ITALIANSIN-P-TA-QlZt-290",
"DEAL-WOKYOU-P-WO-6Xtg-294",
"SMOOTHIES-CURB-P-HO-vCDX-3",
"SLUSH-CURB-P-SL-zTxD-326",
"MILKSHAKES-CURB-P-MI-zoJo-327",
"JARRITOS-CURB-B-JA-Ino1-9",
"DIPS-CURB-P-DI-TTXu-11",
"MAIN-CURB-P-CA-mMSr-158",
"MAIN-CURB-P-OU-TdZx-341",
"MAIN-CURB-P-WA-losT-1",
"MAIN-CURB-P-SM-FE3h-1",
"MAIN-CURB-P-SM-qrNK-2",
"MAIN-CURB-P-BU-YOX3-352",
"MAIN-CURB-P-BO-zyFg-9",
"MAIN-CURB-P-CH-uRMK-354",
"MAIN-CURB-P-BU-8L6L-355",
"MAIN-CURB-P-KO-sPJi-359",
"MAIN-CURB-P-WH-pKSO-363",
"MAIN-CURB-P-RE-Vk5O-364",
"MAIN-CURB-P-OU-arFy-367",
"SIDE-ALL-P-TH-1a7r-2",
"TORTILLACHIPS-CURB-P-TO-Rld5-334",
"DRINKS-CURB-P-SO-wvpJ-330",
"DRINK-ALL-P-JU-upgm-324",]}}

prods = pcli.products.list_all(q=query)

for prod in prods:
  print(prod.name)
  pcli.products.update(prod,{
      "isInternal": True
  })



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


account ="6037d4911d6ed071c4f321f4"
brands = scli.channelLinks.list_all(q={"account" : account,})


for brand in brands:
  scli.channelLinks.update(brand,{
      "reportingEndpoints": [
    {
      "endpointType": 10,
      "endpoint": "https://frithiofs-super-domain.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://curb-food-backend-staging.herokuapp.com/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://andrei-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://carl-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://fabian-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://frithiof-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://gabriel-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://jonas-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://kristopher-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    }
  ]})
    








  print(brand.location)
  location = brand.location
  brand_name = brand.name
  channel = brand.channel
  loc_query = pcli.locations.get(location)
  loc_name = loc_query.name
  print(loc_name,"+" , brand_name,"$",channel)




patcheroo = {"channelSettings": {
    "sendDeliveryFee": False,
    "sendServiceCharge": False,
    "sendDiscount": False},
"sendDeliveryFee": False,
  "sendServiceCharge": False,
  "sendDiscount": False}
query = pcli.channelLinks.list_all(q={'account':'5eb292bf06cfd400019deff5'})

for q in query: 
  pcli.channelLinks.update(q,patcheroo)


query = pcli.accounts.list_all(q={'featureFlags.combinedProductsPage' : True})
for q in query:
  print(q.name)




query  = pcli.channelLinks.list_all(q={'account' : "5c18b7a7c6489f00011c7f29"})
for q in query: 
  loc_id = q.location
  channel = q.channel
  loc_name_query =pcli.locations.get(loc_id)
  if channel == 7:
    channel_name = "Uber"
    print(loc_name_query.name,"-", q.name)
    print(channel_name,"service charge",q.posSettings.lightspeed.serviceChargePLU)
    print(channel_name,"Delivery plu",q.posSettings.lightspeed.deliveryPLU)
    print(channel_name,"Discount plu",q.posSettings.lightspeed.discountPLU)

  elif channel == 2:
    channel_name = "Deliveroo"
    print(loc_name_query.name,"-", q.name)
    print(channel_name,"service charge",q.posSettings.lightspeed.serviceChargePLU)
    print(channel_name,"Delivery plu",q.posSettings.lightspeed.deliveryPLU)
    print(channel_name,"Discount plu",q.posSettings.lightspeed.discountPLU)

  elif channel == 1:
    channel_name = "Deliverect"
    print(loc_name_query.name,"-", q.name)
    print(channel_name,"service charge",q.posSettings.lightspeed.serviceChargePLU)
    print(channel_name,"Delivery plu",q.posSettings.lightspeed.deliveryPLU)
    print(channel_name,"Discount plu",q.posSettings.lightspeed.discountPLU)

  elif channel == 8:
    channel_name = "Takeaway"
    print(loc_name_query.name,"-", q.name)
    print(channel_name,"service charge",q.posSettings.lightspeed.serviceChargePLU)
    print(channel_name,"Delivery plu",q.posSettings.lightspeed.deliveryPLU)
    print(channel_name,"Discount plu",q.posSettings.lightspeed.discountPLU)









account ="603cd4daee5752f56df40f35"
brands = pcli.channelLinks.list_all(q={"account" : account,})


for brand in brands:
  pcli.channelLinks.update(brand,{
    "posSettings": {
    "generic":{
    "sendDeliveryFee": False,
"sendServiceCharge": False}}})



account ="60d36ce980a8ba0b96a872a2"
products = pcli.products.list_all(q={"account" : account,})


for prod in products:
  tax = prod.deliveryTax
  if tax ==9500:
    pcli.products.update(prod, {'deliveryTax' : 9500})

query = pcli.accounts.list_all(q={  "deliverectVersion": "2.0-menubuilder",})

for q in query:
  print(q.name)




query = scli.channelLinks.list_all(q={"account" : "6037d4911d6ed071c4f321f4"})


for q in query :
  scli.channelLinks.update(q, {
      "reportingEndpoints": [
    {
      "endpointType": 10,
      "endpoint": "https://frithiofs-super-domain.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://curb-food-backend-staging.herokuapp.com/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://andrei-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://carl-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://fabian-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://frithiof-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://gabriel-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://jonas-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://kristopher-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0
    },
    {
      "endpointType": 10,
      "endpoint": "https://deliverect-gateway-v7ig6n5lsq-lz.a.run.app",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 0

    }
  ]
  })


pam = pcli.channelLinks.list_all(q={'account' : "6054c1d5c0e70796115e1d3e",'channel' : 9})

for pret in pam:
  id = pret._id
  pcli.channelLinks.update(pret, {
"channelSettings": {
    "alcoholMenuEnabled": False,
    "useFlytV2": True,
    "sendRejectStatus": False,
    "menuEndpoint": "https://api.flytplatform.com/menus",
    "snoozeEndpoint": "https://api.flytplatform.com/item-availability",
    "APIkey": "hdgskmoiHUFRruAQgnYAdphaEhUZImgmSHmDU",
    "locReference": str(id),
    "posBusinessName": "peckwater-brands"
  }})




acc= "5eb08b2b87b1bf0001c3b292"
links = pcli.channelMenu.list_all(q={"account": acc})


for link in links: 
  channel = link.get('channel')
  print(channel)
  if channel == 2:
    pcli.channelLinks.update(link, {
      "name" : "Deliveroo"
    }),
  elif channel == 7:
    pcli.channelLinks.update(link, {
      "name" : "Uber Eats"
    }),
  elif channel == 12:
    pcli.channelLinks.update(link, {
      "name" : "Doordash"
    }),
  elif channel == 26:
    pcli.channelLinks.update(link, {
      "name" : "MenuLog"
    })


products = pcli.products.list_all(q={'account': '6017e71bcb8a91b4944db5fe'}, only='plu,price')
for prod in products:
  if isinstance(prod['price'], str):
    print(prod)
    pcli.products.update(prod, {'price': int(prod.price)})



account = '5ea18193785c9b000177cc31'


products  = pcli.products.list_all(q={"account" : account,"location" : "5eb00d1f49faf600019b501f",  "plu" : {"$in" : ["888911001-1","888911004-1"]}})#,"888911002-1","888911101-1","888911006-1","888911007-1","888911005-1","888911008-1","888912007-1","888912006-1","888912005-1"]}})
products  = pcli.products.get("5eb9570546bfea0001f4a36d")
products  = pcli.products.list_all(q={"account" : account,"location" : "5eb00d1f49faf600019b501f",  "plu" : {"$in" : ["888911001-1","888911004-1","888911002-1","888911101-1","888911006-1","888911007-1","888911005-1","888911008-1","888912007-1","888912006-1","888912005-1"]}})
products  = pcli.products.list_all(q={"account" : account,"location" : "5eb00d1f49faf600019b501f",  "_id" : {"$in" : ['5fa2c4666bda183c525b3702','5ef60054f48c1600019de9a1','5ef5fff5f48c1600019de297','60acad82fa66ac8d7cb312f9','60a39e5edd79d1392f7419d0','5ee0a18635e7540001e32781','5edf3e75ed382c000190be84','5ee0a06397d34c0001781ba2','5ef0c92dbd3077000122eeed','5ee0a0e397d34c00017835b0','5edf3c56f165b000015b15c1']}})
for prod in products:

  #patch parent:
  pcli.products.update(prod,{'isVariantGroup' : True})
  #get subprod
  subprod = prod.subProducts
  print(subprod)
  



query = pcli.products.list_all(q={'account' : '60b6084f52481a800f70f19c' ,})
  
for link in query:
  if link.name is None:
    DrectID = link.deliverectProductId
    name = pcli.products.get(DrectID)
    #print(name.name)
    if link.productType == 1:
      print(name.name , '-' , link.plu ,  'type : Product')
    elif link.productType == 2:
      print(name.name , '-' , link.plu,  'type : modifier')
    elif link.productType == 3:
      print(name.name , '-' , link.plu , 'type : modifier group')
  elif link.name is not None:
    if link.productType == 1:
      print(link.name , '-' , link.plu  , 'type : Product')
    elif link.productType == 2:
      print(link.name , '-' , link.plu , 'type : modifier')
    elif link.productType == 3:
      print(link.name , '-' , link.plu , 'type : modifier group')



for link in query:
    if link.productType == 1:
      print(link.name , '-' , link.plu  , 'type : Product')
    elif link.productType == 2:
      print(link.name , '-' , link.plu , 'type : modifier')
    elif link.productType == 3:
      print(link.name , '-' , link.plu , 'type : modifier group')




import csv
from random import randint

query = pcli.locations.list_all(q={'account' : '60647b6bc068c0e7998d9f45'})

for product in query:
  plu = product.plu
  print(plu)
  if plu[0] != "5" and plu[0] != '7':
    print(plu)
    new_number =randint(10,999999999)
    new_plu = str(new_number)
    print(new_plu)
    pcli.products.update(product , {"plu" : new_plu})



query = pcli.locations.list_all(q={"subscriptions":[{"subscriptionId" : "AzZcmFSE8BUs9Ens"}]})

for q in query:
  print(q.name)






prods = pcli.products.list_all(q={'account' : '624b8a2e4000050172829b53'})

for pr in prods:
  pcli.products.delete(pr)


account_id='60647b6bc068c0e7998d9f45'
location_list=[
"60c3454717b4207e7cc3c4f1",
"60c3454717b4207e7cc3c4f4",
"60c3454717b4207e7cc3c4f7",
"60c3454717b4207e7cc3c4fa",
"60c3454717b4207e7cc3c4fb",
"60c3454717b4207e7cc3c4fc",
"60c3454717b4207e7cc3c4fe",
"60c3454717b4207e7cc3c4ff",
"60c3454717b4207e7cc3c500",
"60c3454717b4207e7cc3c502",
"60c3454717b4207e7cc3c503",
"60c3454717b4207e7cc3c504",
"60c3454717b4207e7cc3c505",
"60c3454717b4207e7cc3c507",
"60c3454717b4207e7cc3c509",
"60c3454717b4207e7cc3c50a",
"60c3454717b4207e7cc3c50b",
"60c3454717b4207e7cc3c50d",
"60c3454717b4207e7cc3c50e",
"60c3454717b4207e7cc3c50f",
"60c3454717b4207e7cc3c510",
"60c3454717b4207e7cc3c511",
"60c3454717b4207e7cc3c512",
"60c3454717b4207e7cc3c513",
"60c3454717b4207e7cc3c517",
"60c3454717b4207e7cc3c518",
"60c3454717b4207e7cc3c519",
"60c3454717b4207e7cc3c51a",
"60c3454717b4207e7cc3c51b",
"60c3454717b4207e7cc3c51c",
"60c3454717b4207e7cc3c51d",
"60c3454717b4207e7cc3c51e",
"60c3454717b4207e7cc3c521",
]
# Unfortunately, Update location server URL only works for Simphony 😔
update_location_server_url=True
result=pcli.create_tunnel_tokens(account_id, location_list, update_location_server_url)

if result['errors'] != None:
    print('errors found')
    for err in result['errors']:
        print(err)

tokens=[]
for created in result['created']:
	tokens.append({
		"token": created['token'],
		"location-id": created['tunnel']['location-id']
	})

# At this point you can use the tokens variable as you which
# Examples:
#     - Access the token in position [0] with: tokens[0]['token']
#     - Access the location-id in position [2] with: tokens[2]['location-id']
#     - Write to a file
tokens


query = pcli.channelLinks.list_all(q={'account' : "5ea18193785c9b000177cc31"})

for q in query:
  channel = q.channel
  print(channel)
  if channel == 16:
    pcli.channelLinks.update(q,{
    "channelSettings": {
          "accessToken": "kBn6HKvZH1iBV0XlcoERWptbaE3W4U3cRocP5gtdKhU=",
          "storeId": "",
          "username": "max_swe_menu",
          "password": "4c390ff5b1b629c089dcc6beb6217bfaa2f276cb5f7944d041c11b9916f76e32",
          "application": "PRODUCTION",
          "defaultMenuLanguage": "sv",
          "sendRejectStatus": False,
          "logChannelOperations": False,
          "useWebhooks": True,
          "autoAcceptOrderStatus": 1
  }},)
  "productLocation": "5eb00d1f49faf600019b501f",


query = pcli.channelLinks.list_all(q={'account' : "5ee37f2b0fbe6c0001e1ad90"})


for q in query:
  loc = q.channel
  print(loc)
  if loc == 16:
    pcli.channelLinks.update(q,{
      'channelSettings.useProductionStatus' : True

})


query = pcli.products.list_all(q={'account' : "60f686ea7ce019a52122d711" , 'location' : "60f688f0eefc703ebff9689d"})


for p in query:
  pcli.products.update(p,{
    'location' : None
  })


query = pcli.products.list_all(q={"account" : "5f0c230b60daee722b586641" ,"location":"5f0c41929b689fce5c69aeda","plu" : {"$in":["888911011-1","888911001-1","888911002-1","888911018-1","888911004-1","888911005-1","888911006-1","888911016-1","888911008-1","888913004-1","888913003-1","888913008-1","888913002-1","888913001-1","888913005-1","888913006-1","888913010-1","888913009-1",]}})
#query = pcli.products.list_all(q={"account" : "5f0c230b60daee722b586641" ,"location":"5f0c41929b689fce5c69aeda","plu" : "888912005-1"})

#query = pcli.products.list_all(q={"account" : "5f0c230b60daee722b586641" ,"location":"5f0c41929b689fce5c69aeda","_id" : {"$in":["5f31aae7bfd9917b8f83fcfc","5f31bd7f0d962e60910b9087","5f310933c73bd5d9d7e418f2","5f310aabc73bd5d9d7e47b85","5f31afdb0d962e60910b1889","5f31aaaabfd9917b8f83fc87","5f31099ec324cbc85c421e44","5f31af830d962e60910b17a6","611a7dcd048ec9227ca268bd","5f31aa6b0d962e60910a5ce3","5f31abd2bfd9917b8f842da4","5f31b01ebfd9917b8f847bd0","607409d1b58db75161e6eee4","5f576af4367269989973c968","5f31aa0b0d962e60910a513e"]}})




query = pcli.products.list_all(q={"account" : "5ee37f2b0fbe6c0001e1ad90" ,"plu" : {"$in":["100-MSIDE","100-MSIDE-2st","100-MSIDE-4st","100-MSIDE-Choice1","100-MSIDE-Choice2","100-MSIDE-Choice3","100-MSIDE-Choice4","125-SIDEKIDS"]}})


for prod in query:
  pcli.products.update(prod,{
      "productType": 3,

  })

  print(prod.name)
  print(prod.plu)
  print(prod._id)
  



  pcli.products.update(prod,{
    "isVariantGroup": True
  })

  


  print(prod.name)
  print(prod.plu)
  pcli.products.update(prod,{
    "isVariant": True
  })




WOLT = pcli.channelLinks.list_all(q={'account' : '5ea18193785c9b000177cc31' , 'channel': 16})

for w in WOLT: 
  pcli.channelLinks.update(w,{
      "posSettings.simphony.averagePreparationTime" : 8 
  })



channelsnog = pcli.channelProducts.list_all(q={'account' : "60cca03cd6cc3ba04dd6e9e7"})
productsnog = pcli.products.list_all(q={'account' : "5e8301d1fe21e4000180c733"})

for p in productsnog:
  print("name:",p.name,",plu:", p.plu)


channelsnog = pcli.channelProducts.list_all(q={'account' : "5e8301d1fe21e4000180c733"})
channelsnog = pcli.channelProducts.list_all(q={'account' : "60cca03cd6cc3ba04dd6e9e7", 'productType':1})

for p in channelsnog:
  if p.deliveryTax == 25000:
    #pcli.channelProducts.update(p,{'deliveryTax':25000})
    print("menuprod:", p.name,",menuplu:",p.plu, "tax:", p.deliveryTax)
  channelID = p._id
  channelProd = p.plu
  channelName = p.name
  print(channelName,channelProd)
  if channelName == None:
    prodName = pcli.products.get(channelID)
    name = prodName

  print(channelName,channelProd,channelID, prodName)




#Poland :
query = pcli.products.list_all(q={"account" : "5f0c22c79b689fce5c633e4e" ,"location":"5f0c3cda9b689fce5c68e281","plu" : {"$in":["888911011-1","888911001-1","888911002-1","888911018-1","888911004-1","888911005-1","888911006-1","888911016-1","888911008-1","888913004-1","888913003-1","888913008-1","888913002-1","888913001-1","888913005-1","888913006-1","888913010-1","888913009-1",]}})





loc = pcli.locations.list_all(q={'posSystemId':9})
loc = pcli.accounts.list_all(q={'_id':{"$in": ["5f3a9a3c1d3f1ba68382d311","5f3a9a3c1d3f1ba68382d311","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","5fe17b1effe9e99933f9f58a","6090618aaa8ffc6e4bedc6e8","6090618aaa8ffc6e4bedc6e8","6090618aaa8ffc6e4bedc6e8","60af656a61e33cf240beafe0","60bf6cff095b2bdf54252dd3","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60c165d40e80459be0e05037","5f3a9a3c1d3f1ba68382d311","60fe9472d9297bd29051ef47","610d9a7f7c3891f17ab20a4b","610d9a7f7c3891f17ab20a4b","610d9a7f7c3891f17ab20a4b","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","60647b6bc068c0e7998d9f45","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","5e7bbf7265013b00010cb6aa","60421678cc07cb38ccb7f1e0"]}})
for l in loc:
  print(l.name, l._id)

loc = pcli.locations.list_all(q={'posSystemId':9})
for l in loc:
  if l.posSettings.simphony.unpaidPaymentType == None and l.posSettings.simphony.posOrdersAreAlwaysPaid is False:
    print(l.account,)
  
with open('bkuk_sync.json', 'w') as f:
    import json
    json.dump(loc, f) 




  locs = l.location
  UUID = l.channelSettings.storeId
  loca = pcli.locations.get(locs)
  print(loca.name,"(",l.name,")","--",UUID)


  print(l.imageUrl)

  name = 'The Jolly Miller - ' + l.name
  print(name)
  pcli.locations.update(l,{
    'name' : name
  })


WOLT = pcli.channelLinks.list_all(q={'account' : '5f0c22c79b689fce5c633e4e' , 'channel': 16})

for w in WOLT: 
  pcli.channelLinks.update(w,{
      "status": 1,
  })
accid = "5f3a9a3c1d3f1ba68382d311"
bastard = pcli.channelProducts.list_all(q={"account":accid,'menu':"60aeb4186ca1aead82ef9993"})

for i in bastard:
  vat = i.deliveryTax
  print(vat)
  if vat == 12000:
    pcli.channelProducts.update(i,{'deliveryTax' : 15000})




  hms_failed_2 = pcli.orders.list_all(q={'account':'5e9eef1bc766d30001c6294c','status': 120})
  hms = pcli.orders.get('5fa923753fd21b469436c76d')

  for i in hms_failed:
    print(i.statusHistory)



Sushiyama = pcli.channelLinks.list_all(q={'account' : '5f9147e1a94e333fef335737','productLocation': {'$exists':False}})

for i in Sushiyama:
  pcli.channelLinks.update(i,{
      "productLocation": "5f91499341dc4479c8785b23",

  })
  print(i.name,i._id,i.location)


]}})
for s in Sushiyama:
  print(s.name,s._id)



Sushiyama = pcli.locations.list_all(q={'account' : '5f0c22c79b689fce5c633e4e'})
for i in Sushiyama:
  pcli.locations.update(i,{
    'productLocation' : '5f0c3cda9b689fce5c68e281'})





{{

    "channelSettings":{
     "accessToken": "M8T-N7yq5z0QYw-gN7zzqDlmVxcqhoIL2t9Jr92Fjvw=",
    "useWebhooks": True,
    "useProductionStatus": True,
    "username": "sushicentralenab_menu",
    "password": "78e0aa97525f3af4f4f770325bc6349d8289d293f84a49be4022ae74ba14f244",
    "defaultMenuLanguage": "sv",
    "sendRejectStatus": False,
    "autoAcceptOrderStatus": 1,
    "application": "PRODUCTION"
  }})
  storeId = i.channelSettings.storeId
  print(storeId,i._id)


max = pcli.channelMenus.list_all(q={"_id":"614a0365ffa0ab2d854691eb"})

for i in max : 
  pcli.channelMenus.update(i,{
      "masterLocationId": "6128c91d181b9545891e3ddf",

  })
  print(i.name)
CurbfoodSweden = pcli.products.list_all(q={'account' : '60f686ea7ce019a52122d711','isInternal' : True})

for prod in CurbfoodSweden:
  subprod = prod.subProducts
  for subs in subprod:
    subpr = pcli.products.get(subs)
    if subpr.min == 0:
      print(prod.name,prod.plu,subpr.name, subpr.plu,subpr.min,subpr.max)





    no_subs.append(prod.plu)
    print(no_subs,prod.name,prod.productType)




loc_names =["116 - Gullmarsplan ",
"101 - Stockholm Centralstation",
"117 - Barkarbystaden",
"301 - Farsta",
"124 - Norrkoping - Kungsgatan",
"151 - Stenpiren",
"907 - Vasteras ICA Erikslund",
"141 - Molndal ",
"160 - Malmo Mobilia",
"112 - Marsta",
"201 - Soderhallarna",
"147 - Halmstad Stortorget",
"114 - Vasagatan",
"159 - Sundsvall Torggatan",
"104 - Vastermalm",
"158 - Goteborg Frolunda Torg",
"501 - Nykoping",
"401 - Karlstad Mitt i City",
"146 - Orebro Krämaren",
"155 – Lund Nova",
"142 - Akersberga",
"102 - PK-huse",
"138 - Tyreso",
"115 - Linkoping - Stora Torget",
"134 - Norrkoping Linden",
"136 - Jakobsberg",
"152 - Femman nedre",
"148 - Stockholm Gallerian",
"130 - Faltoversten",
"153 - Femman ovre",]


query = pcli.channelLinks.list_all(q={'channel' :28, 'account' : '60b5e9e8ad1101089dc7f2f9'})


for i in query:
  pcli.channelLinks.update(i,{
    'status' : 1
  })



  
  accId = i.account
  print(accId)
  accname = pcli.accounts.get(accId)
  print(accname.name)


query = pcli.channelLinks.list_all(q={'account' : '5f9147e1a94e333fef335737','channel':10011})


for i in query :
  print(i.name,i._id)




  print(i._id,i.name)
  print(i.name,i.plu)
  pcli.channelLinks.update(i,{
    'posSettings.simphony.orderNoteTemplate' : "{customerName},{orderNote}"})


servy = ["61682d7a39b8c778b01c9e2f",
"61682d8e957a575f7ad01025",
"61682dc739b8c778b01ca790",
"61682dd941e2dd38e72366a7",
"61682e1a957a575f7ad02c18",
"61682e2f97f21cd260e7dc89",
"61682e6b41e2dd38e724305a",
"61682e850ede8fa62a89b259",]

servy_locs =["6064f1d01ac8010890c31ce5",
"6064f1d01ac8010890c31bfd",
"6064f1d01ac8010890c31c0d",
"6064f1d01ac8010890c31cf5",
"6064f1d01ac8010890c31c17",
"6064f1d01ac8010890c31c15",
"6064f1d01ac8010890c31c41",
"6064f1d01ac8010890c31ca5",]


query  = pcli.channelLinks.list_all(q={'account' : '5fe17b1effe9e99933f9f58a' , "location" : {"$in":servy_locs} , 'channel' : 10040})

for i in query :
  location = i.location
  name = i.name
  loc_call = pcli.locations.get(location)
  print(loc_call.name,"-",name,"-",i._id)
  
  
  
  
  
  name = 'Servy - Dine In'
  pcli.channelLinks.update(i,{'name' :name })

LPQ={
"id":"6168326939b8c778b020bff2",
	"VmStoreId" : "40b6af78-58ca-449a-a242-cd60b87f5831",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/40b6af78-58ca-449a-a242-cd60b87f5831",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/40b6af78-58ca-449a-a242-cd60b87f5831",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/40b6af78-58ca-449a-a242-cd60b87f5831",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/40b6af78-58ca-449a-a242-cd60b87f5831"
},

"id":"6168326839b8c778b020bfd2",
	"VmStoreId" : "cbb5b5ae-8074-4ae9-a902-5adae3a8b220",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/cbb5b5ae-8074-4ae9-a902-5adae3a8b220",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/cbb5b5ae-8074-4ae9-a902-5adae3a8b220",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/cbb5b5ae-8074-4ae9-a902-5adae3a8b220",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/cbb5b5ae-8074-4ae9-a902-5adae3a8b220"
},

"id":"6168326a39b8c778b020c06e",
	"VmStoreId" : "f2f76349-3abf-4a62-a3fe-63f2d300fa8d",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/f2f76349-3abf-4a62-a3fe-63f2d300fa8d",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/f2f76349-3abf-4a62-a3fe-63f2d300fa8d",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/f2f76349-3abf-4a62-a3fe-63f2d300fa8d",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/f2f76349-3abf-4a62-a3fe-63f2d300fa8d"
},

"id":"6168326839b8c778b020bfca",
	"VmStoreId" : "3eadff82-d901-443a-a100-cdc0a0f3c981",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/3eadff82-d901-443a-a100-cdc0a0f3c981",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/3eadff82-d901-443a-a100-cdc0a0f3c981",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/3eadff82-d901-443a-a100-cdc0a0f3c981",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/3eadff82-d901-443a-a100-cdc0a0f3c981"
},

"id":"6168326939b8c778b020bfe2",
	"VmStoreId" : "f08554f5-786d-47e1-9a01-0b1cb67b6d69",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/f08554f5-786d-47e1-9a01-0b1cb67b6d69",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/f08554f5-786d-47e1-9a01-0b1cb67b6d69",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/f08554f5-786d-47e1-9a01-0b1cb67b6d69",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/f08554f5-786d-47e1-9a01-0b1cb67b6d69"
},

"id":"6168326939b8c778b020c051",
	"VmStoreId" : "296a46a4-38cf-418d-98d1-d47d2c6c9821",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/296a46a4-38cf-418d-98d1-d47d2c6c9821",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/296a46a4-38cf-418d-98d1-d47d2c6c9821",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/296a46a4-38cf-418d-98d1-d47d2c6c9821",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/296a46a4-38cf-418d-98d1-d47d2c6c9821"
},

"id":"6168326a39b8c778b020c07e",
	"VmStoreId" : "a86db014-b5ff-4bb9-b98d-df645d62bd68",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/a86db014-b5ff-4bb9-b98d-df645d62bd68",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/a86db014-b5ff-4bb9-b98d-df645d62bd68",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/a86db014-b5ff-4bb9-b98d-df645d62bd68",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/a86db014-b5ff-4bb9-b98d-df645d62bd68"
},

"id":"6168326939b8c778b020c049",
	"VmStoreId" : "2dc9d417-4557-4720-ba8a-554f48da0a3a",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/2dc9d417-4557-4720-ba8a-554f48da0a3a",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/2dc9d417-4557-4720-ba8a-554f48da0a3a",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/2dc9d417-4557-4720-ba8a-554f48da0a3a",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/2dc9d417-4557-4720-ba8a-554f48da0a3a"
},

"id":"6168326a39b8c778b020c076",
	"VmStoreId" : "19c25030-7e10-41a6-b74a-d52330e4b0e0",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/19c25030-7e10-41a6-b74a-d52330e4b0e0",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/19c25030-7e10-41a6-b74a-d52330e4b0e0",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/19c25030-7e10-41a6-b74a-d52330e4b0e0",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/19c25030-7e10-41a6-b74a-d52330e4b0e0"
},

"id":"6168326939b8c778b020bfea",
	"VmStoreId" : "667e6140-15fa-44ee-afa9-51e74f6d97a8",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/667e6140-15fa-44ee-afa9-51e74f6d97a8",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/667e6140-15fa-44ee-afa9-51e74f6d97a8",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/667e6140-15fa-44ee-afa9-51e74f6d97a8",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/667e6140-15fa-44ee-afa9-51e74f6d97a8"
},

"id":"6168326939b8c778b020c024",
	"VmStoreId" : "06991d3e-01cd-4791-9d46-fe37e98f4637",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/06991d3e-01cd-4791-9d46-fe37e98f4637",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/06991d3e-01cd-4791-9d46-fe37e98f4637",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/06991d3e-01cd-4791-9d46-fe37e98f4637",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/06991d3e-01cd-4791-9d46-fe37e98f4637"
},

"id":"6168326a39b8c778b020c086",
	"VmStoreId" : "a1c054d1-d8d9-47b7-a603-27cfa7646f65",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/a1c054d1-d8d9-47b7-a603-27cfa7646f65",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/a1c054d1-d8d9-47b7-a603-27cfa7646f65",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/a1c054d1-d8d9-47b7-a603-27cfa7646f65",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/a1c054d1-d8d9-47b7-a603-27cfa7646f65"
},

"id":"6168326a39b8c778b020c096",
	"VmStoreId" : "f6773101-05b6-4dc5-a5e0-11b53cb386ab",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/f6773101-05b6-4dc5-a5e0-11b53cb386ab",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/f6773101-05b6-4dc5-a5e0-11b53cb386ab",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/f6773101-05b6-4dc5-a5e0-11b53cb386ab",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/f6773101-05b6-4dc5-a5e0-11b53cb386ab"
},

"id":"6168326939b8c778b020c041",
	"VmStoreId" : "ac35876a-9656-4376-91af-5cfe4fc3815d",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/ac35876a-9656-4376-91af-5cfe4fc3815d",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/ac35876a-9656-4376-91af-5cfe4fc3815d",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/ac35876a-9656-4376-91af-5cfe4fc3815d",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/ac35876a-9656-4376-91af-5cfe4fc3815d"
},

"id":"6168326a39b8c778b020c08e",
	"VmStoreId" : "511c9b19-3934-43cd-8bb1-969ea7dfb053",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/511c9b19-3934-43cd-8bb1-969ea7dfb053",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/511c9b19-3934-43cd-8bb1-969ea7dfb053",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/511c9b19-3934-43cd-8bb1-969ea7dfb053",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/511c9b19-3934-43cd-8bb1-969ea7dfb053"
},

"id":"6168326a39b8c778b020c059",
	"VmStoreId" : "31b081d6-b3bd-4733-8386-e882d1e792fb",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/31b081d6-b3bd-4733-8386-e882d1e792fb",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/31b081d6-b3bd-4733-8386-e882d1e792fb",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/31b081d6-b3bd-4733-8386-e882d1e792fb",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/31b081d6-b3bd-4733-8386-e882d1e792fb"
},

"id":"6168326939b8c778b020c02d",
	"VmStoreId" : "171a5fb1-cd0a-4192-8c73-1c1591fbc0c9",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/171a5fb1-cd0a-4192-8c73-1c1591fbc0c9",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/171a5fb1-cd0a-4192-8c73-1c1591fbc0c9",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/171a5fb1-cd0a-4192-8c73-1c1591fbc0c9",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/171a5fb1-cd0a-4192-8c73-1c1591fbc0c9"
},

"id":"6168326a39b8c778b020c09e",
	"VmStoreId" : "aef26c3a-8d5c-4648-86ed-c3956d290065",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/aef26c3a-8d5c-4648-86ed-c3956d290065",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/aef26c3a-8d5c-4648-86ed-c3956d290065",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/aef26c3a-8d5c-4648-86ed-c3956d290065",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/aef26c3a-8d5c-4648-86ed-c3956d290065"
},

"id":"6168326939b8c778b020c039",
	"VmStoreId" : "9d627d23-5201-4a43-936e-4fdd57bbc65c",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/9d627d23-5201-4a43-936e-4fdd57bbc65c",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/9d627d23-5201-4a43-936e-4fdd57bbc65c",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/9d627d23-5201-4a43-936e-4fdd57bbc65c",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/9d627d23-5201-4a43-936e-4fdd57bbc65c"
},

"id":"6168326839b8c778b020bfc2",
	"VmStoreId" : "9f927315-0540-46ef-959a-cda687941e67",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/9f927315-0540-46ef-959a-cda687941e67",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/9f927315-0540-46ef-959a-cda687941e67",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/9f927315-0540-46ef-959a-cda687941e67",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/9f927315-0540-46ef-959a-cda687941e67"
},

"id":"6168326839b8c778b020bfda",
	"VmStoreId" : "165149a0-032d-4760-931e-12d5b19f0cb7",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/165149a0-032d-4760-931e-12d5b19f0cb7",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/165149a0-032d-4760-931e-12d5b19f0cb7",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/165149a0-032d-4760-931e-12d5b19f0cb7",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/165149a0-032d-4760-931e-12d5b19f0cb7"
},

"id":"6168326b39b8c778b020c0b0",
	"VmStoreId" : "b3bbd44b-95a7-45a1-b9c0-ca85f8d3dd2e",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/b3bbd44b-95a7-45a1-b9c0-ca85f8d3dd2e",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/b3bbd44b-95a7-45a1-b9c0-ca85f8d3dd2e",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/b3bbd44b-95a7-45a1-b9c0-ca85f8d3dd2e",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/b3bbd44b-95a7-45a1-b9c0-ca85f8d3dd2e"
},

"id":"6168326b39b8c778b020c0a6",  
	"VmStoreId" : "766348b6-6692-474e-83a8-c0f83767d26f",
	"pushWebhook" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/menu-push/766348b6-6692-474e-83a8-c0f83767d26f",
	"channelStatus" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/status-update/766348b6-6692-474e-83a8-c0f83767d26f",
	"producSnooze" : "https://epos2-multitenant.vmos-serverless.com/v1/deliverect/products-snooze/766348b6-6692-474e-83a8-c0f83767d26f",
	"busyMod" :"https://epos2-multitenant.vmos-serverless.com/v1/deliverect/channel/busy-mode/766348b6-6692-474e-83a8-c0f83767d26f"
},]
query = pcli.products.list_all(q={'account':'60f686ea7ce019a52122d711'})


for i in query:
  if i.location is not None:
    pcli.products.update(i,{'location' : None})






query = pcli.channelLinks.list_all(q={'account':'610bcd6a28ddc58c7a65346b','location':'61687fbdb555c03e49ac1c1f'})


for loc in query:
  print(loc.name,"*",loc._id)
  pcli.channelLinks.delete(loc)


query = pcli.channelProducts.list_all(q={'account' :'5f0c230b60daee722b586641' })




for i in query:
  tax = i.deliveryTax
  print(tax)
  pcli.channelProducts.update(i,{'deliveryTax' : 15000})

id=["61775fd49a5e65f0d6bb7285",
"61279257abc68f90d93e3430",
"6142be893a814a690944851e",
"6142c2b43a814a690947f629",
"615c6128d667304c4947866f",
"615c62e9cb2d010e8f22dcd4",
"615c6448d93736225bca8cfc",
"61628b217c5c62326dbe5c23",
"61628fd6759f9c673b7fc65a",
"616290d1693d73bf156ccced",
"616291ac693d73bf156d1e7d",
"616292334b260a6857c0ddfa",
"6162932e4b260a6857c15c4a",
"616293d6693d73bf156ea592",
"616294fd293d0eaf76a9e06d",
"6170fa16d6bd67ae5dcd0438",
"6170fa74785a41a4f352937a",
"6170ff40785a41a4f3561f73",
"61710053d6bd67ae5dcffb66",
"617100b2d6bd67ae5dd0172f",
"617101253da7db6d6166a13e",
"61710420bd4641072528ccc8",
"6171046e785a41a4f358dfc8",
"617104c03da7db6d6169130b",
"6171050dd6bd67ae5dd28121",
"61710555d6bd67ae5dd2964f",]


query= pcli.channelLinks.list_all(q={'account' : '60db01eadf9dac5d93029308'})

mod = pcli.products.list_all(q={'account' : '5e7bbf7265013b00010cb6aa',"_id":{'$in':id}})


for i in query:
  pcli.channelLinks.update(i,{
    "channelSettings": {
"sendRejectStatus": False
    }})


for i in query:
  print(i.plu)

for f in mod:
  print(f.name,f.isVariantGroup)



  subproduct_first = i.subProducts[0]
  print(subproduct_first)
  for sub in subproduct_first:
    groups = pcli.products.get(sub)
    for f in groups: 
      if f.isVariantGroup:
        print('tiwokr') 
    if i.isVariant :True and g.isVariantGroup: False
      print(f._id)











for i in query:
  pcli.channelLinks.update(i,{
"posSettings":{
    "simphony":{
        'usePLUForCharges': True,
        'deliveryPLU' : "999999985-8",
        "discountPLU": "1245",
        "serviceChargePLU": "123",


 }} })



query= pcli.channelLinks.list_all(q={'account':'5e7bbf7265013b00010cb6aa'})

for i in query:
  pcli.products.delete(i)


for i in query:
  acc_id = i._id
  print(acc_id)
  loc_object = pcli.channelLinks.get(location)



  channels = i.channel
  loc = i.location
  if channels == 26:
    loc_get=pcli.locations.get(loc)
    print(loc_get.name,"-",i.name,"*",i._id)


  print(i.channelSettings)



for i in query:
  channels = i.channel
  #print(channels)
  if channels != 1:
    print(channels)

for i in query:
  calo = i.calories
  if calo == None:
    print(i.name,i.plu)




preview = {
  "menus": ["617a6f5b7967db29aed701e6"],
  "channelLink": "617a6aa97967db29aed70084"
}
menu = scli.call('/jsonMenuPreview', 'POST', json=preview)
    

loc_licst=["60bf8ee6c7392025eb768e34",
"60bf8eed95d35389fab63a4e",
"60bf8ef3c7392025eb769259",
"60bf8ef5380a86ba6660a484",
"60bf8ef595d35389fab63af0",
"60bf8ef9095b2bdf54350687",
"60bf8f00380a86ba6660a898",
"60bf8f04380a86ba6660aa75",
"60bf8f0bde8028cd9bd74e7b",
"61242b34a46f17a699bc93bd",
"61242b34a46f17a699bc93ca",
"6064f1d01ac8010890c31bdf",
"6064f1d01ac8010890c31be2",
"6064f1d01ac8010890c31be6",
"6064f1d01ac8010890c31be8",
"6064f1d01ac8010890c31bf2",
"6064f1d01ac8010890c31c19",
"6064f1d01ac8010890c31c27",
"6064f1d01ac8010890c31c2b",
"6064f1d01ac8010890c31c3d",
"6064f1d01ac8010890c31c64",
"6064f1d01ac8010890c31c75",
"6064f1d01ac8010890c31c7f",
"6064f1d01ac8010890c31c87",
"6064f1d01ac8010890c31cd2",
"6064f1d01ac8010890c31ce3",
"6064f1d01ac8010890c31ce7",
"6064f1d01ac8010890c31cf4",
"60bf8ee1c7392025eb768487",
"6064f1d01ac8010890c31c10",
"6064f1d01ac8010890c31c54",]

query = pcli.locations.list_all(q={'_id':{"$in":loc_licst}})

for i in query:
  print(i.name)



#Enable KJ for all ROO's on OP and RR
acc_ids=["5e7bbf7265013b00010cb6aa","5fe17b1effe9e99933f9f58a"]
query = pcli.channelLinks.list_all(q={'account':{"$in":acc_ids},'channel':2})


for i in query:
  print(i.channelSettings.sendCaloriesAsKJ)
  pcli.channelLinks.update(i,{
      "channelSettings.sendCaloriesAsKJ": True
  })




query  = pcli.channelLinks.list_all(q={'account': '5f296ba95a56ccada1498fc0'})
locat  = pcli.locations.list_all(q={'account': '5f296ba95a56ccada1498fc0'})

for i in query:
  print(i.posSettings.simphony.checkIdTemplate)
  pcli.channelLinks.update(i,{
    "posSettings.simphony.checkIdTemplate" : "{shortChannelName}-{orderId}"
  })

for i in locat:
    print(i.posSettings.simphony.checkIdTemplate)
    pcli.locations.update(i,{
    "posSettings.simphony.checkIdTemplate" : "{shortChannelName}-{orderId}"
  })

loc_list= ["61889d9cc00e4414dbb3e5db","61889d8a3bb72ccb88a0f4a9","6180c6327e60e7c98fade2cd"]
query  = pcli.channelLinks.list_all(q={'account': '6180a9a377c3b88c472ac622','location':{"$in": loc_list},'channel' :7})
query  = pcli.products.list_all(q={'account': '6180a9a377c3b88c472ac622'})


for i in query:
  if i.deliveryTax == 1000:
    print(i.plu)




for i in query:
  pcli.channelLinks.update(i,{
    "status" : 1
  })


  name = i.name[7:13]
  print(name)
  if name == "Smoki":
    print(i.name)



query = pcli.channelLinks.list_all(q={'account':"60b5e9e8ad1101089dc7f2f9"})


for i in query:
  loc = i.location
  loc_name = pcli.locations.get(loc)
  print(loc_name.name,i._id,i.name,i.posSettings.res3700.serverEndpoint)
  if i.posSettings.res3700.serverEndpoint is None:
    print(i_id)


acc = pcli.accounts.get("604a5e84f840a784e19aa868", only='POSAccessProfiles')


maxpol=["618b73a620de3d2f4d6f2b0a",
"618b6fccc4dbbe160ae4b578",
"618b70a2c4dbbe160ae511ed",
"618b70a2c4dbbe160ae511ed",
"618b70a2c4dbbe160ae511ed",
"618b73a620de3d2f4d6f2b0a",
"618b6fccc4dbbe160ae4b578",
"618b73a620de3d2f4d6f2b0a",
"618b70a2c4dbbe160ae511ed",]

oporto = pcli.channelLinks.list_all(q={"account":"60647b6bc068c0e7998d9f45",'channel':16})

for i in oporto:
  loc_name = pcli.locations.get(i.location)
  print(loc_name.name,"-",i.channelSettings.accessToken,"-",i.channelSettings.storeId,"-",i.channelSettings.username,"-",i.channelSettings.password)





query = pcli.channelLinks.list_all(q={"account":"619df81f91d30c8217b5c62e"})


for i in query:
  channels = i.channel
  print(channels)
  if channels == 7:
    print('7 met 7')
    pcli.channelLinks.update(i,{
      "channelSettings": {
    "autoAcceptOrderStatus": 1,
    "orderNoteTemplate": "",
    "storeId": "",
    "application": "ROCKETSHIP"
  }

    }),
  elif channels == 26:
        print("26e")
        pcli.channelLinks.update(i,{

    "channelSettings": {
    "locReference": "",
    "posBusinessName": "",
    "APIkey": "",
    "menuEndpoint": "",
    "snoozeEndpoint": ""
  }}),
  elif channels == 12:
        print("12e")
        pcli.channelLinks.update(i,{

    "channelSettings": {
    "application": "PRODUCTION",
    "autoAcceptOrderStatus": 1
  }}),
  elif channels == 2:
            print("2e")
            pcli.channelLinks.update(i,{

    "channelSettings": {
    "brandId": "",
    "countryCode": "",
    "application": "PRODUCTION",
    "readonly": False,
    "storeId": "",
    "checkRemoteSnoozes": False,
    "sendRejectStatus": False,
    "logChannelOperations": False,
    "updatePrepStage": False,
    "isTabletLess": False
  }})




for i in query:
  pcli.channelLinks.delete(i)
  print(i.name)


query = pcli.locations.list_all(q={"account":"5c18b7a7c6489f00011c7f29"})


for i in query: 
  pcli.locations.update(i,{
      "status": "SUBSCRIBED"})








query = pcli.channelLinks.list_all(q={'location':"605240eb926a1fa5400bdc62"})
loc_query =pcli.products.list_all(q={'account':"619df81f91d30c8217b5c62e"})

for i in loc_query:
  print(i.plu)
  
  pcli.locations.update(i,{
      "account": "60ae6ffc929e610c1b5601c8"

  })

for i in query:
  pcli.channelLinks.update(i,{
      "account": "60ae6ffc929e610c1b5601c8",

  })

list_of_subs =['61894bb42c90eaec01e92eca', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93217', '61894bb32c90eaec01e92da4', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6c', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93217', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92da6', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e92eca', '61894bb42c90eaec01e93707', '61894bb42c90eaec01e93709', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93709', '61894696c5697028e03f70a5', '61894696c5697028e03f713b', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e22dab69709ffd01ea01d', '618e22e305a5037471b8f195', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894696c5697028e03f7139',
'61894bb42c90eaec01e93709', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432',
'61894bb32c90eaec01e92da4', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e92eca', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e92eca', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92b96',
'61894bb32c90eaec01e92da4', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6c', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e22dab69709ffd01ea01d', '618e22e305a5037471b8f195',
'61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '61894696c5697028e03f75d2', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2348a7b8322ea61e43f9',
'61894bb32c90eaec01e92df8', '618ee9aabbd781b9106686f4', '61894696c5697028e03f70a5', '61894696c5697028e03f713b', '618ee9dbd514c9047c3c9499', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92da4', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6c', '61894bb32c90eaec01e92da6', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '61894696c5697028e03f76a4', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93217', '61894bb32c90eaec01e92da4', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b6c', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93283', '61894bb32c90eaec01e92da4', '61894bb32c90eaec01e92b6e', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93217', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '61894696c5697028e03f75d2',
'61894bb42c90eaec01e93217', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894696c5697028e03f70a5', '61894696c5697028e03f713b', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93709', '61894bb42c90eaec01e92f32', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93707', '61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92da4', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894696c5697028e03f70a5', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894696c5697028e03f713b', '618e232db69709ffd01ed432',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894696c5697028e03f713d', '618e232db69709ffd01ed432',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '618f07038bdfd28ed54a94a2',
'618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24', '61894bb32c90eaec01e92da6',
'61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894696c5697028e03f70a5', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'618eecf7924dbdfe268186c4', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92bee', '61894696c5697028e03f70ad', '61894bb32c90eaec01e92db8',
'61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92da6', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e92eca', '61894bb42c90eaec01e93283', '61894bb32c90eaec01e92b6e', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e22e305a5037471b8f195',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93709', '61894bb32c90eaec01e92da4', '61894bb32c90eaec01e92b6c', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93709', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '61894696c5697028e03f75d2',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93709', '61894bb32c90eaec01e92da6', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233da7b8322ea61e42a4', '618e233605a5037471b94445', '618e2199b69709ffd01d9a24',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894696c5697028e03f713f',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894696c5697028e03f713b',
'61894bb42c90eaec01e93709', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432',
'61894bb32c90eaec01e92b96', '618e216eb69709ffd01d91c3',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b96', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e92f32', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e92eca', '61894bb42c90eaec01e93147', '61894bb32c90eaec01e92b6c', '61894bb32c90eaec01e92dbc', '618eecf7924dbdfe268186c4',
'61894bb42c90eaec01e92eca', '61894bb32c90eaec01e92da4', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6c', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93283', '61894bb32c90eaec01e92b6e', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '61894696c5697028e03f75d2',
'61894bb42c90eaec01e93283', '61894bb32c90eaec01e92b6e', '61894696c5697028e03f70a5', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e22e305a5037471b8f195',
'61894bb42c90eaec01e93283', '61894bb32c90eaec01e92da6', '61894bb32c90eaec01e92b6e', '618e232db69709ffd01ed432', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e92eca', '61894bb42c90eaec01e93217', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93217', '61894bb42c90eaec01e92f32', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6e', '618e232db69709ffd01ed432', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93709', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618eecf7924dbdfe268186c4',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '618f07038bdfd28ed54a94a2', '618e232db69709ffd01ed432',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '61894696c5697028e03f7139', '618e232db69709ffd01ed432',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894696c5697028e03f713d',
'61894bb42c90eaec01e93cb5', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894696c5697028e03f713f',
'618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24', '61894696c5697028e03f75d2',
'618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b6e', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4', '618e2199b69709ffd01d9a24', '61894696c5697028e03f76a4',
'61894bb32c90eaec01e92da4', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894696c5697028e03f75d2', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92da6', '618e233605a5037471b94445', '618e233da7b8322ea61e42a4',
'61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6a',
'618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93217', '61894bb42c90eaec01e9479d', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e2199b69709ffd01d9a24', '61894696c5697028e03f75d2',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93217', '61894bb42c90eaec01e9479d', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92da6', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e94959', '61894bb42c90eaec01e93707', '61894bb42c90eaec01e93217', '61894bb42c90eaec01e9479d', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e2199b69709ffd01d9a24', '618eecf7924dbdfe268186c4',
'61894bb32c90eaec01e92bee', '61894bb32c90eaec01e92b6a', '618e233da7b8322ea61e42a4',
'618e233da7b8322ea61e42a4',
'618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e93217', '61894bb42c90eaec01e93147', '61894bb42c90eaec01e94635', '61894bb42c90eaec01e93cb5', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894bb32c90eaec01e92dbc',
'61894bb42c90eaec01e93217', '61894bb42c90eaec01e93147', '61894bb42c90eaec01e93cb5', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894bb32c90eaec01e92dbc', '618f137e8bdfd28ed54ea6cd',
'61894bb42c90eaec01e93217', '61894bb42c90eaec01e93cb5', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b96', '61894696c5697028e03f70a5', '618e232db69709ffd01ed432', '61894bb32c90eaec01e92dbc', '618f137e8bdfd28ed54ea6cd',
'61894bb42c90eaec01e93707', '61894bb42c90eaec01e93217', '61894bb42c90eaec01e9479d', '61894bb32c90eaec01e92da4', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92dc2', '618e233605a5037471b94445', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e92eca', '61894bb42c90eaec01e93707', '61894bb42c90eaec01e93217', '61894bb42c90eaec01e9479d', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92df8', '61894bb32c90eaec01e92b6a', '61894bb32c90eaec01e92dc2', '618e22dab69709ffd01ea01d', '618e2199b69709ffd01d9a24',
'61894bb42c90eaec01e94959', '61894bb42c90eaec01e93707', '61894bb42c90eaec01e93217', '61894bb42c90eaec01e9479d', '61894bb32c90eaec01e92da4', '618eedd5adbbcd1e8ac7ff2f', '618e233605a5037471b94445', '618e2199b69709ffd01d9a24',
'618e233da7b8322ea61e42a4',
'618e233da7b8322ea61e42a4',
'618e233da7b8322ea61e42a4',
'61894bb42c90eaec01e94c0d', '618f24f98bdfd28ed558db3b', '61894bb42c90eaec01e94c0f', '61894bb42c90eaec01e94c11',
'61894bb42c90eaec01e94c0b', '61894bb42c90eaec01e94c0d', '61894bb42c90eaec01e94c0f', '61894bb42c90eaec01e94c11',
'61894bb42c90eaec01e94c0b', '61894bb42c90eaec01e94c0f', '61894bb42c90eaec01e94c11',
'61894bb42c90eaec01e93217', '61894bb42c90eaec01e93147', '61894bb42c90eaec01e93cb5', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894bb32c90eaec01e92dbc', '61894696c5697028e03f75d2',
'61894bb42c90eaec01e93217', '61894bb42c90eaec01e93cb5', '618eedd5adbbcd1e8ac7ff2f', '61894bb32c90eaec01e92b96', '618e232db69709ffd01ed432', '61894bb32c90eaec01e92dbc', '618f1459b81c6e6c7198adde',
'61894bb42c90eaec01e94c09', '61894bb42c90eaec01e94c0b', '61894bb42c90eaec01e94c0d', '61894bb42c90eaec01e94c0f', '61894bb42c90eaec01e94c11']

prodquery = pcli.products.list_all(q={'account':'6180a9a377c3b88c472ac622'})

subProds = pcli.products.list_all(q={'account':'6180a9a377c3b88c472ac622',"_id" :{"$in":list_of_subs}})

for i in prodquery:
  prodTypes = i.productType
  if prodTypes == 3 and i.name != 'Remove Toppings' and i.name[:3] == 'Add':
    print(i.plu,"***",i._id,i.name,i.plu)
    name = subProds.name
    pcli.products.update(subProds,{})
    print(subProdGet)


for i in subProds:
  name = i.name
  new_name = "- " + name
  print(new_name)
  pcli.products.update(i,{
    "name" : new_name
  })

for i in prodquery:
  name = i.name
  if name[:1] == "-":
    if i.price != 0:
      print(i.name,i.price)
      pcli.products.update(i,{
        "price" : 0
      })


menuacc = pcli.accounts.list_all(q={"posSystem": 25, "deliverectVersion": "2.0-productsync"})
for i in menuacc:
  print(i.name,"-", i._id)

prodacc = pcli.accounts.list_all(q={"posSystem": 25, "deliverectVersion": "2.0-productsync"})

for i in prodacc:
  print(i.name,"-", i._id)

query = pcli.channelLinks.list_all(q={'channel':45,'channelSettings.useFlytV2':True})

for i in query:

  print(i.account)
CL_IDS=["619e14cba19b81c87380e324",
"619e14cda19b81c87380e3cf",
"619e14cda19b81c87380e3bd",
"619e14cba19b81c87380e33e",
"619e14cba19b81c87380e34a",
"619e14cca19b81c87380e363",
"619e14cda19b81c87380e40b",
"619e14cca19b81c87380e3b7",
"619e14cca19b81c87380e36d",
"619e14cda19b81c87380e3dc",
"619e14cda19b81c87380e417",
"619e154891d30c8217c59377",
"619e14cca19b81c87380e3a5",
"619e14cba19b81c87380e344",
"619e14cca19b81c87380e37f",
"619e14cba19b81c87380e356",]


query = pcli.channelLinks.list_all(q={'_id':{"$in":CL_IDS}})
for i in query:
    pcli.channelLinks.update(i,{
    'status' : 3
  })


query = pcli.channelLinks.list_all(q={'location':"619dfd2dd087b8b491db96c4","channel" : 26})
for i in query:
    print(i.name ,"-", i._id)
for i in query:

  pcli.channelLinks.update(i,{
    'status' : 4
  })

    print(i.name ,"-", i._id)

  pcli.channelLinks.update(i,{
    'status' : 3
  })


for i in query:
  print(i.name ,"-", i._id)


query = pcli.channelLinks.list_all(q={'posSystemId':25,"posSettings.kounta.useDefaultPLU" : {'$exists':True}})



Secondquery = pcli.locations.list_all(q={'posSettings.kounta.site': 105686})

Secondquery = pcli.locations.list_all(q={'posSettings.kounta.site': 95165})
for i in Secondquery:
  print(i.name,'-',i._id)


prod = pcli.channelProducts.list_all(q={"account": "603fa3225de02e8e2fd835d5"})

for i in prod:
  if i.price is not None:
    print(i.name,i.price, i.plu)
  print(i.price)


locations_smoothr =["61a884c8bf34b8b17ad50ab2",
"61a892ac978241d75ebea322",
"61a89322bf34b8b17ade4d9b",
"61a892f1978241d75ebecaac",
"61a892bb0194a3db11616d8f",
"61a893060194a3db1161995d",
"61a89312978241d75ebed0c8",
"61a89283bf34b8b17add7d5d",]


query =pcli.channelLinks.list_all(q={'location':{"$in":locations_smoothr},'channel':10064})


for i in query:
  pcli.channelLinks.update(i,{
    "channelSettings": {
    "channelLocationId": "",
    "activateURL": "",
    "resizerFormat": "default",
    "menuUpdateURL": "",
    "snoozeUnsnoozeURL": "",
    "alwaysSendAllSnoozedProducts": True,
    "busyModeURL": "",
    "statusUpdateURL": "",
    "autoAcceptOrderStatus": 1,
    "updatePrepTimeURL": "",
    "sendTableInfoToNotes": True
  },
  })



query = pcli.channelLinks.list_all(q={'account':'5fd8d36c6ff7e123646081fa'})


for i in query:
  if i.tags == None:
    print(i.name," No TAG")
  else:
    print(i.tags)



query = pcli.channelLinks.list_all(q={  "posSystemId": 25,'posSettings.kounta.useDefaultPLU':{"$exists": False} })

for i in query:
  print(i.account)

query = pcli.channelLinks.list_all(q={  "posSystemId": 25,'posSettings.kounta.useDefaultPLU': False })

for i in query:
  print(i.account)

for i in query: 
  pcli.channelLinks.update(i,{
  "timezone": "Europe/Brussels"
  })


query = pcli.locations.list_all(q={'account' : "5f9147e1a94e333fef335737",'timezone':{"$exists": True} })

usDefault= ["5ef51a9f7f16110001130b8f",
"5f0cd65bc490c572b3881a17",
"5f073e0cb5f7d7974c23a9a2",
"5f17712e2ead84471a7293b2",
"5f3c8052319f989249be6d97",
"5f3c697c08306bccf930de10",
"5f4001988f239013598d5494",
"5f401c45b9a2dcbfeeca461e",
"5f3ffb758f239013598ca82e",
"5f4411936d21bb255d5c8eb9",
"5f329cb3da4d7405cf9f2194",
"5f3f3a834bb8f85e522617c1",
"5f3f35104bb8f85e52260229",
"5f4912e14c90f7ec7b2d4885",
"5f4ca821c249410801784677",
"5f4012518f239013598f786a",
"5f4718dea4ad25a5a7e16528",
"5f4cee0861db3bc6edfb6bca",
"5f4d19f747277ebd9824eab9",
"5f4cca82c24941080181a740",
"5f329ca486e925dab739d9fe",
"5f52264062fcfa91c7c0e0a0",
"5f33470836a82da8d5aa4113",
"5f5652ebd909a53bc5b7422f",
"5f5632c0881308ff0a19d05d",
"5f5806abafbd08f6463f56a5",
"5f4041608f23901359940d50",
"5f4cec9361db3bc6edfb1eb9",
"5f51a4dc62fcfa91c7a00d3f",
"5f562c0f881308ff0a180872",
"5f44bd3bf47efd3988452074",
"5f5a447bf77a1803c72d5f81",
"5f4ce69361db3bc6edf98572",
"5f5f302f2e0f167f9f1b1e05",
"5f4e0b1d6ca7dbc69f50fd27",
"5f4cf9ef47277ebd9820bcb4",
"5f33502d66f5ca3eca827cb1",
"5f580669afbd08f6463efef2",
"5f607f0d9e26dca61f722463",
"5f440f646d21bb255d5bb520",
"5f60848659bc3b69586d7fbe",
"5f58fbda4b38e801855ffaf8",
"5f580713afbd08f6463f56e4",
"5f5e88a12e0f167f9f0778bd",
"5f6772dc8564b770390e4793",
"5f694f7dafbc7aef85d3467e",
"5f44111c6d21bb255d5c8559",
"5f5fed479e26dca61f6bfbdc",
"5f65b8e918929cbe0322e2bc",
"5f6284770b1a1c7bf166e44f",
"5f329c6fda4d7405cf9f0880",
"5f6af5e81a99f79003ffc6bd",
"5f732e973e853bd15e3d0768",
"5f68549e18929cbe0369ae02",
"5f7358fe3e853bd15e44d270",
"5f600cd159bc3b695866a05f",
"5f4f9242b86920ed9b8b03ac",
"5f6865f118929cbe036faae4",
"5f5a38adf77a1803c72c040a",
"5f734d54afde9bb5a2228a35",
"5f6aff27756bc01d507b63a7",
"5f60d5804138ca9bb46cc0fc",
"5f68adfc8564b770392f2d38",
"5f8b939ed0f473f101c49613",
"5f915f922359ca4c7a9d996d",
"5f8ee40e662bdd01401fcbbf",
"5f88542c3a69161a09a4d605",
"5f8ee39f662bdd01401fbee4",
"5f9857a714d29aa87a81fe90",
"5f9c34c78139f0781c2532eb",
"5f92b3863151e20ff769448e",
"5f8efd46bc9dba624abb2f29",
"5f7587066af4be3bd5a1038e",
"5fa420a452ba7128991fe466",
"5fa4bf772241499949f92128",
"5f6cef3383d1e220308073ae",
"5fa30a072df16dcd43387ac1",
"5f91932c3151e20ff727c959",
"5f5e8d2d8882d7bfbb371fef",
"5f5a3dfef77a1803c72c8bbf",
"5fad4c21c09d7cddca35afac",
"5fb69215d2109556af626322",
"5fa5791e0e08314e12b27596",
"5fa2e5c02df16dcd432d82a6",
"5fa9cd04eed7184d3728e09f",
"5fb29338358459f9321e8313",
"5fbfa58aea0f52ea3c9abb43",
"5fc06bf3056ffe77e45ba2d9",
"5fc0f76f056ffe77e477d4dc",
"5fceb3234ac74d1a28f6f3e5",
"5fbdb2ed72f076189f771349",
"5fbfdd5dcb0e03775d86f83b",
"5fcddba865134fbd277bd624",
"5fc5519e51f97efb742e7b97",
"5fd9fec043c1689164600e64",
"5fd3549e0185dd726020538c",
"5fda1e17a8526afabc7b693a",
"5fb7b2a8fb032ac07dd7971b",
"5fbf874dcb0e03775d6a42da",
"5fe356b7c8a130e18de5b6dd",
"5fe45c3bc8a130e18d183eac",
"5fe4a60ce935f5886050bc9f",
"5fcf37994ac74d1a28037edd",
"5fa4076c50f6ac7edbe491d9",
"5fd0b63283721dcec978b99a",
"5fe25c4ce19977424b3b04c0",
"5ff2fbefc6cc4ade721feae0",
"5fa3dda350f6ac7edbc9a1ca",
"5f874630820d80dad15ac974",
"600063727ae5e599b51f82b8",
"60007caa7ae5e599b529ca09",
"60005ad3e50a267534a252cb",
"600fce9c2ee8979db5985c1a",
"600020fccf3ed079076ac212",
"60141dc2cb8a91b49475011d",
"6007ef04981bff6ae62139bb",
"5fdc115339ee500b6e1f69f3",
"60142ba0cb8a91b494799e0c",
"60083ad94a4d3fe6ae2827ff",
"6022b22ef94b069a09502253",
"60141f2dd721e04d5b3c7cfa",
"601d3cb16e61c14cb27374bf",
"60122178868225156f06e8bd",
"5ff75e18b93d80254b123f7d",
"5fca4e767b02b49b0db3fd42",
"60362caa93c6fa6221b0f6bc",
"602e79418a0a621797f5f684",
"603f93a9125a1713d7801b2f",
"5f4cf7f218f853cb771c65cf",
"6038af88ee5752f56d048ab6",
"6041e9a0d0714781e4eae77c",
"604744bb12f1e37275b7bc87",
"60391c334584f2384834ca7e",
"6048875a0f149f88b122d71a",
"60507233bd59121f2f31a01a",
"604fbe1feb5ed06357c05f53",
"603ce7693edf5280152641d0",
"6053c84dcf92e3f495777139",
"60535783bd83997a7ff16922",
"6050096c803ffcfa3210a047",
"60530ed60138df44c0a1b686",
"60303de7e7cdbef390b7082d",
"604a8afc1bd1c7abf5babe9a",
"603d10262ddd2a4b36dc8938",
"6065d150336b9cfbd6cc0203",
"6062dd6ed21dd975a4779fe2",
"603e579bae07f1a8cd9d499a",
"60754b25a7f18c64e1e74dc8",
"5fad4ad782f3d2194ea6d475",
"6079ea62b2b6a5f9568a0851",
"607513bca7f18c64e1c4576e",
"6086151903f484f0d3bb9256",
"5f561fefa1415ea86619d809",
"5f3c7cd408306bccf93152cd",
"608722290284cb01c897b95a",
"6086de59a00154d2b1447ac6",
"6092f7557141f4ffb85085ed",
"5ffe0701afdad9fbea28c559",
"608c7065251a2c7339e421c2",
"60956316c3bf7bfecdfcd138",
"6086bc883ce92ad361c7e19f",
"609981e92085a279f18b2dc3",
"6054e04f286fe433c69f5e66",
"608c71c9879f46c9e2e1e754",
"6086cd9f03f484f0d3042675",
"5f68638f18929cbe036f5ebf",
"60a42257e152714f0b8768c4",
"5fb7ce156b51edc72e8c7b6d",
"60b03128b4ed9d5764e72b22",
"5f6aa2e71a99f79003fc706f",
"60bd7cc0f14f0eab67d961e9",
"60aeef436ca1aead82f7f22e",
"60cc26f78cf3a422ea71ff53",
"606cbe7854febf08603433d7",
"60c976e2b351027d51201fc9",
"60d405e77c0d45fa1175c8b9",
"60be17b7f9caf8405f5f5632",
"60da04b9a8dcd90a5825f1c5",
"60d648b1616a4dd0c47cbdc4",
"60dbafb2f755c8aa67647a1c",
"60dd457db5ff7011f1ae175d",
"60dbafd07159694a572f5164",
"60d4059b813efb85d3f5e41f",
"60e63e560a9b943896edbb56",
"60e63fad4349beb0423d0d1a",
"60dbb00376ab8c00f35da653",
"60c299fae9fa4c05b739ac48",
"60ef0a1e633f0e12e87e4987",
"60e52983da0dedc1fee58ba4",
"60e640520a9b943896ee1185",
"60ec4545be305d859d90f74c",
"60536e432fd4f87d170039e6",
"60f076975c8c7676a850c689",
"60ec4731f0ec5ff173ea7d1f",
"60c29add17b4207e7c83d8db",
"60f076db510fb903bfff84d8",
"60dd448b6281a05c9cd70f49",
"61006a1ae0643af6fcd7324c",
"60ed95f767c6994ec4bde6b1",
"6101940c434bd2ed561b5100",
"610aec0128ddc58c7a25245d",
"6102f96ea171f0149d0ada3f",
"6107a8d5a171f0149da47f53",
"610069989397a129434a5bf6",
"60fb0c8bd9297bd290d4cc3b",
"60f860d3e4ebc25a73f5b1d7",
"611145f58766c76506535add",
"611196f98766c76506681058",
"5f35409849cff1a3090d6d44",
"611c2c76745942fa2b1b2fcf",
"611ed1cb47c121334d1abc7f",
"611d220861626d66758be235",
"6123e45437055df35c6a8810",
"6126abdcabc68f90d9e7c777",
"605e2dee6e7539c2b05478dd",
"6123e311df7df2c4a4b387e5",
"612fbfc0e0012d53be5fe31b",
"6123e4c9bdb85fbf99af8cee",
"610aebcf68f1d77b2ed2fd32",
"6123e3d4280a110242fe6544",
"5fb7e6dd6b51edc72e9bfe3e",
"611ed20547c121334d1ac175",
"6160b24a4b260a6857f7e087",
]

query = pcli.users.list_all(q={'account' : {"$in" : usDefault}})




acc = {  "posSystem": 32}
accounts = pcli.accounts.list_all(q=acc)
cl_loc= {'posSystemId':32}
locations = pcli.locations.list_all(q=cl_loc)
CL = pcli.channelLinks.list_all(q=cl_loc)



for i in accounts:
  print(i.name,"-*-", i._id)



for i in locations: 
  number_of_channelLinks = len(i.channelLinks)
  acc_name= pcli.accounts.get(i.account)
  print(acc_name.name)
  print('location :',i.name,)
  print(number_of_channelLinks,' channelLinks')
  print("---------------------------------------------")


apikey= 'hdgskEHMlbYYZGTBazgguurQOqrIlFkseDQuG'

prod = {'account' : '619df81f91d30c8217b5c62e','channel': 26}
settings = pcli.channelLinks.list_all(q=prod)

for i in settings:
  print(i.channelSettings.APIkey)
  pcli.channelLinks.update(i,{
    "channelSettings.APIkey" : apikey
  })


#Update master location slider on all CL's for Red Rooster : 5fe17b1effe9e99933f9f58a, masterloc : 5ff385cac6cc4ade72524c1a
RedRooster = pcli.channelLinks.list_all(q={'account' :"6176679f656206bdc6915540","productLocation":{"$exists":False}})
locRedRooster = pcli.locations.list_all(q={'account' :"619dd20d92c19e0d28373259"})

for i in locRedRooster:
  print(i.name)


for i in locRedRooster:
    pcli.locations.update(i,{
          "productLocation": "617667b3d5bcdb9a7a4a5fc8" 
    },propagate = 'all')


for i in RedRooster:
    pcli.channelLinks.update(i,{
          "productLocation": "617667b3d5bcdb9a7a4a5fc8" 
    },propagate = 'all')



oporto = pcli.channelLinks.list_all(q={'account' :"619df81f91d30c8217b5c62e",'channel' : 26})

for i in oporto:
  pcli.channelLinks.update(i,{
    "channelSettings.useFlytV2" : True
  })


new_wolt= ["61b1ea69db04f87928e594c6",
"61b1ea69db04f87928e594cc",
"61b1ea69db04f87928e594d2",
"61b1ea69db04f87928e594dc",
"61b1ea69db04f87928e594e4",
"61b1ea69db04f87928e594ee",
"61b1ea69db04f87928e594f5",
"61b1ea69db04f87928e594fd",
"61b1ea6adb04f87928e5950d",
"61b1ea69db04f87928e594c0",
"61b1ea6adb04f87928e59514",
"61b1ea6adb04f87928e5951c",
"61b1ea6adb04f87928e59522",
"61b1ea6adb04f87928e59528",
"61b1ea6adb04f87928e5953a",
"61b1ea6adb04f87928e59540",
"61b1ea6adb04f87928e59552",
"61b1ea6adb04f87928e5955e",
"61b1ea6adb04f87928e59567",
"61b1ea6adb04f87928e5956e",
"61b1ea6adb04f87928e59574",
"61b1ea6adb04f87928e5957c",
"61b1ea6adb04f87928e59584",
"61b1ea6adb04f87928e5958a",
"61b1ea6adb04f87928e59590",
"61b1ea6adb04f87928e59596",
"61b1ea69db04f87928e59505",
"61b1ea6adb04f87928e5952e",
"61b1ea6adb04f87928e59534",
"61b1ea6adb04f87928e59546",
"61b1ea6adb04f87928e5954c",
"61b1ea6adb04f87928e59558",]


unilever = pcli.channelLinks.list_all(q={'account' :"604602ce60938a8ae170f693","_id":{'$in':new_wolt}})
unilever = pcli.channelLinks.list_all(q={'account' :"604602ce60938a8ae170f693","posSettings.unilever.applicationName" :{"$exists":False}})

for i in unilever:
  print(i._id)


for i in unilever:
  pcli.channelLinks.update(i,{
      "name": "Lody Ice Cream NOW",
      "brandId": "604602ce60938a8ae170f692",
      "posSettings": {
        "unilever": {
            "applicationName": "POLAND",
            "currency": "PLN",
            "anonymizeCustomer": False,
            "logOps": True,
            "readonly": False,
            "tipPLU": "",
            "serviceChargePLU": "186418",
            "deliveryPLU": "186305",
            "discountPLU": "186308",
            "bufferOrders": False,
            "averagePreparationTime": 5,
            "sendDiscount": True,
            "sendDeliveryFee": True,
            "sendDeliveryFeeCondition": 0,
            "sendServiceCharge": True,
            "sendTip": False,
            "posOrdersAreAlwaysPaid": False
                   }
             },
             "channelSettings": {
                "accessToken": "zW8h8WJnqxkYKEQxgJ8HdGnoyyH6wp50d3N72tCHvqk=",
                "application": "PRODUCTION",
                "storeId": "5e1df46250e34eebdc17e3f9",
                "username": "unilever_poland",
                "password": "567212abf976c3276a75b949db0aa6e56a7838da42d84ba97c56af5d55fd4bd4",
                "defaultMenuLanguage": "pl",
                "sendRejectStatus": False,
                "useWebhooks": True,
                "autoAcceptOrderStatus": 1,
                "updateOpeningHours": True
            },
            "discountPLU": "186308",
            "deliveryPLU": "186305",
            "serviceChargePLU": "186418",
            "logPOS": True,
            "tags": [
              "Lody Ice Cream NOW"
              ]
            })


  


for i in unilever:
  pcli.channelLinks.update(i,{

"tags": [
    "Lody Ice Cream NOW"
  ]
  })




query = pcli.products.list_all(q={'account' :'607e744a32dba7c1c9c9e79f','location' : '607e7fb4875706cdb7dc036d'})




for i in query:
  pcli.products.update(i,{
    "nameTranslations": {
    "en": None
  }
    })



Availa = ["619f6f7de49ccab91bf31075",
"619f6f7de49ccab91bf31077",
"619f6f7de49ccab91bf3107a",
"619f6f7de49ccab91bf3107b",
"619f6f7de49ccab91bf31079",
"619f6f7de49ccab91bf31076",
"619f6f7de49ccab91bf31078",]



query = pcli.menuAvailabilities.list_all(q={'account' : '619df81f91d30c8217b5c62e'})

for i in query:
  startTime = i.startTime
  if startTime == "00:00":
    print(startTime)
    pcli.menuAvailabilities.update(i,{
      "startTime" : "00:01"
    })



acc = "6017e71bcb8a91b4944db5fe"
query = pcli.channelLinks.list_all(q={'account' : acc,'channel':10027})
  
for i in query:
  print(i.channelSettings.channelLocationId)
  print(i._id)
  pcli.channelLinks.update(i,{
    "reportingEndpoints": [
    {
      "endpointType": 10,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        2
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 10,
      "endpoint": "https://link1-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        2
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 10,
      "endpoint": "https://link2-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        2
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 10,
      "endpoint": "https://link3-curb-ngrok-123.ngrok.io/order",
      "statusTrigger": [
        2
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 10,
      "endpoint": "http://kms-prod-app-sweden-dot-curb-food-production.ew.r.appspot.com/order",
      "statusTrigger": [
        2
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        20
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        95
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        100
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        110
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        75
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        92
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        30
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        87
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        83
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        90
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        80
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        4
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        123
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        10
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        70
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        60
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        50
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        40
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        7
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        5
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        2
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        129
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        122
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        25
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://curb-food-python.herokuapp.com/api/deliverect",
      "statusTrigger": [
        3
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        20
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 10,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        2
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        90
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        95
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        100
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        110
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        75
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        92
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        30
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        87
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        83
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        80
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        4
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        123
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        10
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        1
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        60
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        70
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        121
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        130
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        50
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        40
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        5
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        6
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        129
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        122
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        25
      ],
      "endpointLevel": 1
    },
    {
      "endpointType": 20,
      "endpoint": "https://wire.cvrb.io/deliverect",
      "statusTrigger": [
        3
      ],
      "endpointLevel": 1
    }
  ]
  })
 



theCloud = pcli.locations.list_all(q={'account' :"6017e71bcb8a91b4944db5fe","posSettings.generic.ordersWebhookURL":{"$exists":True}})

for i in theCloud:
  if i.posSettings.generic.ordersWebhookURL != "https://dashboard.thecloud.ae/webhook/Deliverect/fetchOrder.php":
    pcli.locations.update(i,{
      "posSettings.generic.ordersWebhookURL" : "https://dashboard.thecloud.ae/webhook/Deliverect/fetchOrder.php"
    },override = 1, propagate = 'all'
    )


heCloud = pcli.products.list_all(q={'account' :"619df81f91d30c8217b5c62e", 'productType':3})

for i in heCloud:
  subProd = i.subProducts
  print(i.name, len(subProd),i.plu)



KountaRoles = pcli.channelLinks.list_all(q={'_id':{"$in":ActiveID}})

for i in KountaRoles:
  print(i.name,"*****",i.channel)


for i in KountaRoles:
  print(i.activeChannelLinkIds)
  pcli.users.update(i,{
    "roles": [
    1,
    850,
    851,
    875,
    900,
    950,
    1000,
    1001,
    1002,
    1003,
    1004,
    1005,
    1006,
    1007,
    1008,
    1009,
    1010,
    1011,
    1012,
    1013,
    1014,
    1015,
    1016,
    1017,
    1018,
    1019,
    1020,
    1021,
    1022,
    1023,
    1024,
    1500,
    2000,
    2500,
    3000,
    3500,
    4000,
    4500,
    4600,
    4700,
    5000,
    5500,
    6000,
    6001,
    6100,
    6500,
    6600,
    6650,
    6700,
    6750,
    6800,
    7000,
    7500,
    8000,
    8500,
    8510,
    8520,
    8525,
    8530,
    9000,
    9500,
    10000,
    10500,
    11000,
    11500,
    12000,
    12010,
    12020,
    12050,
    12100,
    12750,
    13000,
    13500,
    14500,
    14600,
    14610,
    14615,
    14620,
    14630,
    15500,
    16000,
    16600,
    16610,
    16620,
    16630,
    17000,
    17001,
    17500,
    17510,
    18000,
    18010,
    18550,
    18600,
    19000,
    19500,
    20000,
    20500,
    21000,
    21500,
    21550,
    22000,
    22100,
    22500,
    23000,
    23050,
    23100,
    23101,
    23150,
    23200,
    23220,
    23250,
    23300,
    23350,
    23500,
    24000,
    25500,
    25550,
    25560,
    27000,
    27500,
    28000,
    29000,
    32100,
    32200,
    32300,
    32400,
    32500,
    33000,
    33100,
    33200,
    33300,
    35000,
    36000,
    40000,
    60000
  ],
  "groups": [
    "5e8b51816243b500010da3b4",
    "61a864010194a3db113f83cf",
    "5e7b24e334c93a000186f53e",
    "5d4d5e3bf133a500012058c5",
    "607bd8c40592295035499cf3",
    "5f3102c5c324cbc85c41c979"
  ],
  })



menu = pcli.channelLinks.list_all(q={'account' : '6017e71bcb8a91b4944db5fe', 'channel' : 10027})

for i in menu:
  print(i._id,i.channelSettings.channelLocationId)

for i in menu:
  pcli.channelLinks.delete(i)
  print(i.name, i._id,i.account)
print(menu)




query = pcli.channelLinks.list_all(q={'account' :'6123587eb44397bec9b80594','channel' : 12})
query = pcli.channelLinks.list_all(q={'account' :'6123587eb44397bec9b80594','name' : 'Jolly Jaffles','channel' : 12})


for i in query:
  location = i.location
  location_name = pcli.locations.get(location)
  print(location_name.name)
  print(i.name)
  print(i._id)
  print("--------")
  


  query = pcli.channelProducts.list_all(q={'account' :'61a96a8452aaa78db208617c'})



query = pcli.channelLinks.list_all(q={'account' : "6017e71bcb8a91b4944db5fe",'channel': 10027})


for i in query:
  print(i.channelSettings.channelLocationId)




query = pcli.products.list_all(q={'account' : "624b8a2e4000050172829b53"})


for i in query:
  pcli.products.delete(i)




CP = pcli.locations.list_all(q={"account":'$61b846149e2f2bf216ad114f',"_deleted" : True})



locs = pcli.locations.list_all(q={"posSystemId": 25,'posSettings.kounta.logOps':False})




locs = pcli.locations.list_all(q={'account' : "6017e71bcb8a91b4944db5fe" ,"posSettings.generic.sendDiscount" : False })
unexist_locs = pcli.locations.list_all(q={'account' : "6017e71bcb8a91b4944db5fe" ,"posSettings.generic.sendDiscount" : {"$exists" :False }})
channels = pcli.channelLinks.list_all(q={'account' : "6017e71bcb8a91b4944db5fe" ,"posSettings.generic.sendDiscount" : False })
unexist_cL = pcli.channelLinks.list_all(q={'account' : "6017e71bcb8a91b4944db5fe" ,"posSettings.generic.sendDiscount" : {"$exists" :False }})

for i in locs:
    pcli.locations.update(i,{
        'posSettings.generic.sendDiscount' : True
    },propagate='all', override=1)

for i in noElocs:
    pcli.locations.update(i,{
        'posSettings.generic.sendDiscount' : True
    },propagate='all', override=1)


for i in channels:
    pcli.channelLinks.update(i,{
        'posSettings.generic.sendDiscount' : True
    })



CL_query = pcli.channelLinks.list_all(q={'channel' : 20})
for i in CL_query:
  loc = i.location
  acc = i.account
  print(i.name,"****location ID",loc,"+++++account ID",acc)  


loc_query = pcli.locations.list_all(q={'_id':{"$in":loc_list}})






query = pcli.products.list_all(q={'account' : '61e9296b386b0c45c4a955e7'})

for i in query:
  pcli.products.delete(i)



query = pcli.channelProducts.list_all(q={'account' : "611418a658d83d209f99552d",'price' : {"$exists" : True}})


for i in query:
  print(i.plu,i.name)
  pcli.channelProducts.update(i,{
     "$unset": { "price": i.price}})
    
 
  plu = i.plu
  menu = i.menu
  price = i.price
  print(price, plu, menu,i._id )




   
    
    
    
    'price' : Null
  })




query =pcli.products.list_all(q={"account":"6006b6f2ae1f4b2319d7bd6b","isInternal" : True,'location' : "6006b77885f103aa84d2b7c7"})
for i in query:
  pcli.products.update(i,{
    "location" : None
  })

query =pcli.channelLinks.list_all(q={'account' : '619df81f91d30c8217b5c62e','location' : {'$in':['619dfd12a19b81c873756c53' , '619dfd5a92c19e0d2852527f','619dfd6fd087b8b491dbd2f7']}})




for i in query:
  pcli.channelLinks.update(i,
  {
    'status' : 1
  })


prods = pcli.products.list_all(q={'account' : '61e9296b386b0c45c4a955e7','productType' : 2 , 'deliveryTax' : {"$exists" : False}}})
for prod in prods:
  pcli.products.update(prod,{
    "deliveryTax" : 10000,
    "takeawayTax" : 10000
    }
    )

for prod in prods:
  pcli.products.update(prod,{
    "deliveryTax" : 10000,
    "takeawayTax" : 10000
  })

for prod in prods: 
  deliveryTax = prod.deliveryTax
  takeawayTax = prod.takeawayTax
  if deliveryTax is None and takeawayTax is None:
    print(prod._id)




query = pcli.locations.get('60b94001590e77d60802db20')





query = pcli.channelLinks.list_all(q={"account": "5e7bbf7265013b00010cb6aa", "channel" : 26
})



for i in query:
  print(i._id)


accounts =['5f9a1e2b35017e32e4ae2aa1',
'5fd1a15b48171e7ef41b9110',
'5fdac9f9710e77485e54646f',
'603cac3b1d6ed071c4fb7fd7',
'611dbafc72e15844a8f3d553',
'612816e6abb7077b7a3ea0ac',
'612dc96a5c18b888da90b8d7',
'6131d492d640338a3f4207e6',
'6139a226dc560f1d5ef90a87',
'6146f57175dff07517a0f6d6',
'6149e653a2fb7481fea3097b',
'6151ce1fb7b27b9756ff881f',
'6154128dc000516d4cd63fbc',
'619383f0f6f5882d932dec96',
'619dd20d92c19e0d28373259',
'619dd706422408ab702fe240',
'61a96a8452aaa78db208617c',
'61b6ef9afe9ea76aceaeb64a',
'61b846149e2f2bf216ad114f',
'62049533247d0df1bad5ca8b',
'620ade781bbff2d378d5a5b6',
'621847af25710730c0aef1dd',]

users = pcli.users.list_all(q={'account':{"$in":accounts}})


for i in users:
  accountID = i.account
  getacc = pcli.accounts.get(accountID)
  print(i.name,'**',i.email,'--',getacc.name)

acc_ids=['604b552c1bd1c7abf5e95ee7',
'602ffa42548106e63696bc59',
'6047f6d19808bdc4c5df5318',
'5ebca01e94abfb0001213973',
'60210bb0322b1a696c18e1ba',
'602be09b7fa23ae2ba5c3b89',
'606ebe85eb39a5dce7a15421',
'607053111af0d0b959d355f8',
'5f51abbb62fcfa91c7a0212c',
'5f51abbb62fcfa91c7a0212c',
'60210bb0322b1a696c18e1ba',
'60210bb0322b1a696c18e1ba',
'6080a5ff40529c3f572e739a',
'60210bb0322b1a696c18e1ba',
'60210bb0322b1a696c18e1ba',
'60210bb0322b1a696c18e1ba',
'60210bb0322b1a696c18e1ba',
'60d35f2097d805fe6ec728b3',
'60210bb0322b1a696c18e1ba',
'60c0dbb0a62d3122c7d91ee7',
'60b103f2a6dc26688a3c4598',
'5f7f4a971e09d91042e1e5d2',
'60f065873d9c43fc99ce0c9d',
'609410e2ab08a18ecde153c2',
'60f97953978972c6bb269ab6',
'5ea876218b4c780001b1f133',
'60ad6f433d9342055d57effa',
'5ee3e2630fbe6c0001ebe0f9',
'5f3e77366b72c16c91c2d758',
'606df65aeb39a5dce77d6cff',
'606df65aeb39a5dce77d6cff',
'5c18f4dfc6489f00016af507',
'6013064f600ac8864cb9df4e',
'610d5afc6582ac0938493367',
'6026a77f37be0c47c16565c6',
'5f89c0ef2577cca832b9c24f',
'6009b3d759338338acaf79cf',
'603e9521baa104c113bb5faa',
'603664ad860f7694baed6a44',
'611d2c8c930aec1cbd40a8df',
'60febaf46df5c052eba6ddb1',
'61201bcd3dde73a718bd6e80',
'603664ad860f7694baed6a44',
'5fe403882bc043229d1bdddf',
'60b9282c92d89ac7f0a101c5',
'60b9282c92d89ac7f0a101c5',
'60b103f2a6dc26688a3c4598',
'5f04d3a45911ba641bbb07bc',
'60cce885efd803827e530ddb',
'5ede8e72ed382c00018b4740',
'60d093a6396ed6fdc48da627',
'60d093a6396ed6fdc48da627',
'60d093a6396ed6fdc48da627',
'5ebd65ed5eca4e0001fa4c47',
'5ebd65ed5eca4e0001fa4c47',
'61095ac868a8be6fbbb1c12e',
'5ebd65ed5eca4e0001fa4c47',
'5ebd65ed5eca4e0001fa4c47',
'5ebd65ed5eca4e0001fa4c47',
'5ebd65ed5eca4e0001fa4c47',
'60b9282c92d89ac7f0a101c5',
'60b9282c92d89ac7f0a101c5',
'60b9282c92d89ac7f0a101c5',
'60b9282c92d89ac7f0a101c5',
'60b9282c92d89ac7f0a101c5',
'61098249a0efa9512483429e',
'60b9282c92d89ac7f0a101c5',
'60b9282c92d89ac7f0a101c5',
'610bf2df32fffa686ad85ac7',
'61157dddb74535274671d1bc',
'612d255e4e7b589e9cd10ff0',
'612d1810f584c4cd22454813',
'60b538f4ad1101089d9dc96b',
'6130d9afd640338a3fed7309',
'613fc0fa8b2d81681113e698',
'613fc0fa8b2d81681113e698',
'613f8ad9285713fe2beed6ef',
'612f2484557e849872bd788f',
'60be469229d4b860c8ee9b1e',
'6130d9afd640338a3fed7309',
'5ebd65ed5eca4e0001fa4c47',
'610958e20f628d335a77372f',
'610958e20f628d335a77372f',
'603e45d3fb5383869f3cd0f5',
'603e45d3fb5383869f3cd0f5',
'603f47235de02e8e2fb70d39',
'606df65aeb39a5dce77d6cff',
'60940df10cc8d56b5c59e5b4',
'60940df10cc8d56b5c59e5b4',
'60940df10cc8d56b5c59e5b4',
'60940df10cc8d56b5c59e5b4',
'6064889f3dfd03964880673b',
'5fac44500e641f97697c70c4',
'5fac44500e641f97697c70c4',
'5fac44500e641f97697c70c4',
'5f36989867e72df85baacfe2',
'61547be95b5ce2ad08b88f84',
'5ed7c5404ff28f000118c0ef',
'5ed7c5404ff28f000118c0ef',
'5ed7c5404ff28f000118c0ef',
'5ed7c5404ff28f000118c0ef',
'5ed7c5404ff28f000118c0ef',
'5ed7c5404ff28f000118c0ef',
'615b05013fc22089c0580c8b',
'60636c9d3dfd03964825f054',
'60636c9d3dfd03964825f054',
'615b824db71b9313cc6a027c',
'610b1cbb32fffa686a9076f5',
'610b1cbb32fffa686a9076f5',
'610b1cbb32fffa686a9076f5',
'6124b152280a1102423d47f0',
'615c6dae9b5ab8325029764d',
'615c6dae9b5ab8325029764d',
'6154a5d2d80bd39fd19c466b',
'5f36989867e72df85baacfe2',
'5f36989867e72df85baacfe2',
'5f36989867e72df85baacfe2',
'5ff345f03060a7c44006c66d',
'607a165f44195f71e3ad58f4',
'601ad3c74d0444d2fc4d8dce',
'601ad3c74d0444d2fc4d8dce',
'5ed6906e861df500012a60be',
'616e2ac5051b73b3753bccac',
'60210bb0322b1a696c18e1ba',
'613f98cb91a291032698a821',
'614a5956ffa0ab2d85667803',
'614ca4df3099723526885ebe',
'614ca4df3099723526885ebe',
'6112d5b5b78b0a6e334e7d0c',
'5f7f4a971e09d91042e1e5d2',
'5fd8db5d8a1a50a53d88ac8d',
'61435bbcfb17935bee6f08fe',
'61732acbd5bcdb9a7ac3c7c7',
'6167d9a6957a575f7a9313a5',
'5f29827d5a56ccada14d12b1',
'617c228ba0eb4cda4c3bb074',
'6182dafa0505c718a30fd2e0',
'612d1810f584c4cd22454813',
'612d1810f584c4cd22454813',
'61201bcd3dde73a718bd6e80',
'6183e31de5003d182279b943',
'6183e31de5003d182279b943',
'615f00304875a9452450bb2c',
'618be84e4f5041f4228744ff',
'618ed7958bdfd28ed5346c6a',
'5e8763917142660001d68381',
'619d09eaa2695fda6be35954',
'5fa026168139f0781ce6b895',
'603664ad860f7694baed6a44',
'5f47d9eca4ad25a5a7fe0a3b',
'61a5301d3f1be12dbca1adc5',
'5f47d9eca4ad25a5a7fe0a3b',
'5f47d9eca4ad25a5a7fe0a3b',
'5f47d9eca4ad25a5a7fe0a3b',
'5f47d9eca4ad25a5a7fe0a3b',
'61ae76f0d119ef55204217de',
'60270187ea90b148ab14db4b',
'6182f37c795c386cf16d23f3',
'61782975a5e9ac645b609c72',
'61782975a5e9ac645b609c72',
'61af82bee68c7a3b78f6863f',
'603664ad860f7694baed6a44',
'5f36989867e72df85baacfe2',
'5fac44500e641f97697c70c4',
'616e2e35a256b18c641ab5a1',
'6193c92f6bcb9d462a4d3370',
'61ba3e1eb3eb0c86ebae1914',
'61af82bee68c7a3b78f6863f',
'61cb2e4da02017515cfa427b',
'6033f603ae930475e9e9ef2c',
'61858baf7f461fd95441fc4b',
'61afc0d6491c8b1ade3b231a',
'606caa4754febf08602ca6c8',
'60f19b9e95602456d99807cc',
'60f19b9e95602456d99807cc',
'5ebd65ed5eca4e0001fa4c47',
'5ebd65ed5eca4e0001fa4c47',
'5ebd65ed5eca4e0001fa4c47',
'6197d69b03ee3f39b0d59363',
'619f9993e49ccab91b08fff0',
'61e7663e78628a669f3b52ba',
'61af82bee68c7a3b78f6863f',
'61af82bee68c7a3b78f6863f',
'613f6d6c19ae64163f932504',
'61eb331f8d9a1d578a777735',
'61f2c654c2da0bec21bf0e03',
'61af855f54d24fdd87e082bd',
'61f07914fe23b2d519cb14aa',
'61f07914fe23b2d519cb14aa',
'61f07914fe23b2d519cb14aa',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'60be8baae6941a3c91ee246b',
'61f474975dc24ab36cd773b3',
'61f1ae5b3e4a2863239cd2ce',
'618be84e4f5041f4228744ff',
'61f2c654c2da0bec21bf0e03',
'5ebd65ed5eca4e0001fa4c47',
'5ebd65ed5eca4e0001fa4c47',
'5ebd65ed5eca4e0001fa4c47',
'61eebc45e3e2c25434255273',
'61f02562fe23b2d519a22530',
'603664ad860f7694baed6a44',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'5fb6cd38fb032ac07d8c5c24',
'61fd996fc89575706ee345f1',
'61af75539eedfaeadc5e6daf',
'5e8b58586243b500010ddc35',
'61f2fdd81223a0d22eef572d',
'61dcedf7454025d0a2be75ca',
'61dcedf7454025d0a2be75ca',
'61dcedf7454025d0a2be75ca',
'6124abc736699b621be89263',
'6080a5ff40529c3f572e739a',
'600f3bfc93b24624506b71ce',
'607996bc27c3ac2ac5b08183',
'60300078ebbf8dcfe1b7ada8',
'61f9cc2b2eebb52af8888087',
'61f7e59b5dc24ab36c0069c0',
'60636c9d3dfd03964825f054',
'61d32cdf8edc69688cb3afba',
'621ffdb0fc6918965b1dbef8',
'5ff8c9f6d8a08c97928a1c18',
'61d485dd682cce72f0bf825f',
'6216cddf33ff8bce06f1c9bd',
'62227358cddada6ffe70739b',
'60e71f5dc296131604356aef',
'607710b78a26b83d93438e89',
'610adc74e43b0ca8e3c2224c',
'5ee3e2630fbe6c0001ebe0f9',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'5e4a5daf1ff9de0001251e05',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'61017c1678e6ac91ecf20870',
'604a41b11bd1c7abf5a157b4',
'5f919e713151e20ff72d6501',
'60073c828320c413b22a2fe8',
'5f49549361db3bc6edaa6cbf',
'6009a446ea3c88902b5748ec',
'610adb56fe915e6733363492',
'615579092338c45a68a0b286',
'615579092338c45a68a0b286',
'610adb56fe915e6733363492',
'600256ec1f255c940ebf3685',
'600256ec1f255c940ebf3685',
'600256ec1f255c940ebf3685',
'611a78f47c2fbdcc767be2b4',
'60a689bfeed9aefb48a2629e',
'6143accdbda0048d0454f94c',
'60e5b7f39522f962ef6e74cb',
'5f68638f18929cbe036f5ebf',
'5f68638f18929cbe036f5ebf',
'60210bb0322b1a696c18e1ba',
'600256ec1f255c940ebf3685',
'613a381044ae174f376dc55a',
'5f68638f18929cbe036f5ebf',
'5f68638f18929cbe036f5ebf',
'5f68638f18929cbe036f5ebf',
'5f68638f18929cbe036f5ebf',
'5f68638f18929cbe036f5ebf',
'5f68638f18929cbe036f5ebf',
'610adb56fe915e6733363492',
'612d1810f584c4cd22454813',
'612d1810f584c4cd22454813',
'612d1810f584c4cd22454813',
'617bf5aa19fd133111a73a4b',
'610adb56fe915e6733363492',
'61d5da8f682cce72f0885498',
'610adb56fe915e6733363492',
'60b569ad8bd42753ab8bc08d',
'5d847f2b21c6b20001e19847',
'61ce4cf436c11eba52bfc48f',
'610adb56fe915e6733363492',
'61aff2a8ea8f6a9c895bdaed',
'5f44104df47efd39883777be',
'60999af96f98feba44feb716',
'61e2190dced805d54be29280',
'5ffe066f36d307eb88f926bc',
'5ffcbc2f4b5075d3d9692c18',
'61e82fa39dd11a1642d9ed34',
'60e5b7f39522f962ef6e74cb',
'61782975a5e9ac645b609c72',
'61782975a5e9ac645b609c72',
'61782975a5e9ac645b609c72',
'61782975a5e9ac645b609c72',]


for i in query:
  acc_list = []
  acc_id = i.account
  print(acc_id)
  new_acc_list = acc_id.append(acc_list)
  print(new_acc_list)


query = pcli.channelLinks.list_all(q={"channel" :13 })


query = pcli.accounts.list_all(q={'_id':{"$in" : acc_ids}})
for i in query:
  print(i.name)

query = pcli.products.list_all(q={'account' : '6215871001e5e6c08d5a46c1'})



for i in query:
  pcli.products.delete(i)
  




query = pcli.channelLinks.list_all(q={'account' : '5d67c3f06f006f00012b83d1', 'channel' :7 , 'name' : "Ben & Jerry's and Magnum Store - NEW" })
query = pcli.channelLinks.list_all(q={'account' : '5d67c3f06f006f00012b83d1', 'channel' :{'$in':[2,7,26,12]} , 'name' : "Ben & Jerry's and Magnum Store - NEW" })



for i in query:




for i in query:
    locationid = i.location
    locationName = pcli.locations.get(locationid)
    print(i.name,"---",i._id,'*_*',i.channel,'***',locationName.name)


query = pcli.locations.list_all(q={'posSystemId' : 10120})


for i in query:
  orderhook = i.posSettings.generic.ordersWebhookURL
  synctableURL = i.posSettings.generic.syncTablesURL
  syncFloor = i.posSettings.generic.syncFloorsURL
  syncProdFloor = i.posSettings.generic.syncProductsURL
  print(i.name , "account Name:" , i.account , orderhook , synctableURL, syncFloor , )




AUSaccount = pcli.accounts.list_all(q={'region' :"AUS", "locations" : {"$exists":True} })


for i in AUSaccount:
  locsCount = len( i.locations)
  pos = i.posSystem

  print(i.name,"*", locsCount,"-", pos)


prods = pcli.products.list_all(q={"account" :"61c44b67f89a492d3a26ed34" })


for prod in prods:
  pcli.products.update(prod,{
    "deliveryTax": 20000,
  "takeawayTax": 20000,
  })


porchetta = pcli.channelLinks.list_all(q={'location' : "6260a88fe66b1fad43fa3d08"})

for i in porchetta:
  pcli.channelLinks.update(i,{
     "posSettings": {
        "generic": {
            "syncProductsURL": "",
            "syncFloorsURL": "",
            "syncTablesURL": "",
            "ordersWebhookURL": "",
            "locationId": ""
        }
    }
  })

inactive = pcli.locations.list_all(q={
  'account' : "61e9296b386b0c45c4a955e7" , "status" :"TESTING"
})

for i in inactive:

  channellink = i.channelLinks
  get_channels = pcli.channelLinks.list_all(q={"_id" : {"$in" : channellink}})
  for channel in get_channels:
    pcli.channelLinks.delete(channel)
  pcli.locations.delete(i)
  
  print(channellink)
  print(i.name)



query = pcli.channelLinks.list_all(q={"channel" : 7 , "channelSettings":{"provisioning" : 2}})
squery = scli.channelLinks.list_all(q={"channel" : 7 , "channelSettings.provisioning" : 2})



for i in squery:
  print(i._id)




user_mail = pcli.users.list_all(q={"email" : "admin@popkins.com.au"})

for i in user_mail:
  print(i.account)



  squares = pcli.locations.list_all(q={'posSystemId' : 13, "posSettings.square.logOps" : True})


  for i in squares:
  
    print(i._id)




Account = "5d67c3f06f006f00012b83d1 "


unilever = pcli.channelLinks.list_all(q={'account' : "5d67c3f06f006f00012b83d1" , "channel" : 1, "status" :1 })

for  i in unilever:
  pcli.channelLinks.update(
    i,
    {
        "status": 3

    }
  )


  channel = i.channel
  if channel == 1:
    print(i.location)




Jolly = pcli.channelLinks.list_all(q={'account' : "6123587eb44397bec9b80594" , "channel" : 12,"channelSettings.sendImagesOnMenuPush" : True })

for i in Jolly:
  sendim = i.channelSettings.sendImagesOnMenuPush
  print(sendim)




query = pcli.products.list_all(q={
  'account' : "627872f3094a6f5022e07c73" ,   "productType": 2, "overloads" : {"$exists" : True}

})


for i in query:

  print(i.plu,"***",i.overloads)
  pcli.products.update(
    i,{"overloads" : []}
  )
  print(i.plu,"***",i.overloads)


unilevers = pcli.locations.list_all(q={"account" : "5d67c3f06f006f00012b83d1","openingHours" : {"$exists" : True}})

for opening in unilevers:
  print("ID: ",opening._id)
  print("Name: ",opening.name)
  print(opening.openingHours)
  print()
  print()




nohours  = pcli.locations.list_all(q={"account" : "5d67c3f06f006f00012b83d1","openingHours" : {"$exists" : False}})
for opening in nohours:
  print("ID: ",opening._id)
  print("Name: ",opening.name)
  print()
  print()
  print()




nohours  = pcli.channelLinks.list_all(q={"account" : "61e9296b386b0c45c4a955e7" , "channel" : 7,"channelSettings.storeId":{"$exists" : True} })

for no in nohours:
  print(no.channelSettings.storeId)
  print(no._id," - ", no.name)




nohours  = pcli.products.list_all(q={"account":"624a7e20e572ff89f1ded6a2","subProducts" : "62732b31a30b09df6c643f22"})

for no in nohours:
  print(no._id, no.plu)




nohours  = pcli.channelLinks.list_all(q={"channelSettings.storeId" : "2ecc4463-e652-5d88-96e8-a0dbafff5b7f"})

orders = pcli.orders.list_all(q={"_id" :{"$in" : ["62b26b0e8fbb722fbf6bff5f",
"62b26b0ef75f7730dc82bc6f",
"62b26b0ecb0415f4e3907043",
"62b26b0ec3bd80d91a4c70d7",
"62b26b0e09d5811cbe29738f",
"62b26b0e54991348776bfb4e",
"62b26b0e771742884982c19f",
"62b26b0e91c4ace6c3906864",
"62b26b0e2b3ad375684c65cd",
"62b26b0e57af7e4113296ded",
"62b26321e45a95c0064c5f89",
"62b25e5db7b6042d4582c3bb",]}})


for i in orders:
  pcli.orders.update(
    i,{
      "location" : "621c50ecd156fa94594409c5",
      "account" : "61a55a6092785806cae51b80",
      "channelLink" : "62b269435097d31f118adb7b"
    }
  )



links = pcli.channelLinks.list_all(q={"channelSettings":{"storeId" : "231f0332-9a74-438d-bbff-f1f416df43f4"}})


links = pcli.locations.list_all(q={"account" : "61f16a85c10f898fd52ab03c"})


for l in links:
  print(l.name)

prods = pcli.products.list_all(q={"account" : "62b91de8362f63f030fd4d28", "location" : "62b93a01fc80643888b6cde1", "productType":2})


for i in prods:
  print(i.name ,"**",i.plu)



prods = pcli.accounts.list_all(q={"_created" : {"$gt":"2022-06-01T00:00:00.000Z"}})

for i in prods:
  print(i.name)


prods = pcli.products.list_all(q={"_created" : {"$gt":"2022-06-01T00:00:00.000Z"}})


myUser = scli.users.list_all(q={"_id":"61976c145a6c137ce750671a"})

for i in myUser:
  scli.users.update(i,{
    "roles": [0, 10000]
  })




products = pcli.products.list_all(q={"account":"603773064e2eafa286b7b123"})


for i in products:
  if i.deliveryTax != 25000:
    print(i.name)
      pcli.products.update(i,{
          "deliveryTax": 25000,
      })


links = pcli.channelLinks.list_all(q={"channelSettings.storeId" : "9372f22b-1a2d-4b79-b695-1e2dda7f2d0e"})


myUser = scli.users.list_all(q={'_id':"62cd3477823ffb0da00e308f" })


for i in myUser:
  scli.users.update(i,{
      "roles": [ 0]

  })




CC =["628d93e4f6ebeb84272a6942",
"628d93e4f6ebeb84272a6943",
"628d93e4f6ebeb84272a6944",
"628d93e4f6ebeb84272a6945",
"628d93e4f6ebeb84272a6946",
"628d93e4f6ebeb84272a6947",
"628d93e4f6ebeb84272a6948",
"628d93e4f6ebeb84272a6949",
"628d93e4f6ebeb84272a694a",
"628d93e4f6ebeb84272a694b",
"628d93e4f6ebeb84272a694d",
"628d93e4f6ebeb84272a694e"
"628c525f791514df8f4ab9ae",
"628c525f791514df8f4ab9af",
"628c525f791514df8f4ab9b0",
"628c525f791514df8f4ab9b1",
"628c525f791514df8f4ab9b2",
"628c525f791514df8f4ab9b3",
"628c525f791514df8f4ab9b4",
"628c525f791514df8f4ab9b5",
"628c525f791514df8f4ab9b6",
"628c525f791514df8f4ab9b7",
"628c525f791514df8f4ab9b8",
"628c525f791514df8f4ab9b9",
"628c525f791514df8f4ab9ba",
"62cf8e00197fa016d8e19fb6" ]


CQ = pcli.channelCategories.list_all(q={'account' : "625e0c0916aa929c63e9c359" , "_id" : {"$in" :CC }})



for i in CQ:
  print(i.subProducts)





CC2=[
  "628b75f6791514df8fc339d6",
    "628b761b814d8e28fa51c3ea",
    "628b7645b58193d7deebe9e4",
    "628b7673e0b9b9507aa4dc07",
    "628b76ffb58193d7deec865b",
    "628b772369ec71342f6da02d",
    "628b774cf721a7b313c7940f",
    "628b7790e14dbac6849a4c4b",
    "628b779eae276b0ccb969adc",
    "628b77b6ae276b0ccb969f79",
    "628b7821791514df8fc4aa87",
    "628b7829b58193d7deed8f18",
    "62cf8d01995fa7a811fa47a4"
     "628c5be487e67b01c1840268",
    "628c5be487e67b01c1840269",
    "628c5be487e67b01c184026a",
    "628c5be487e67b01c184026b",
    "628c5be487e67b01c184026c",
    "628c5be487e67b01c184026d",
    "628c5be487e67b01c184026e",
    "628c5be487e67b01c184026f",
    "628c5be487e67b01c1840270",
    "628c5be487e67b01c1840271",
    "628c5be487e67b01c1840272",
    "628c5be487e67b01c1840273",
    "628c5be487e67b01c1840274",
    "62cf8ebcabcc76671657372c"
]

CQ2 = pcli.channelCategories.list_all(q={'account' : "625e0c0916aa929c63e9c359" , "_id" : {"$in" :CC2 }})



for i in CQ2:
  print(i.subProducts)




prod = https://api.deliverect.com/v2/locations/622531d396ff269550150a81/syncProducts


acc = "5eea0625f9fb8f000138f11a"
loc = "5eea06350a59d30001f857ba"

body = {
   "accountId":acc, 
   "locationId":loc,
   "products" : [
      {
         "plu":"victor",
         "name":"bertels",
         "price":0
      }
   ],
   "categories":[
      {
         "name": "Australia",
         "posCategoryId": "SATE"
      }
   ]
}
resp = pcli.call("/productAndCategories","POST",json=body)
print(resp)





query = pcli.channelLinks.list_all(q={"account" : "61df8c560706d58e1016f00d" , "channel" : 2})

for i in query:
  try:
    brandID = i.channelSettings.brandId
    print(brandID)

  except:
    print("nope" , i._id)



prods = pcli.products.list_all(q={"account" : })



bundles = pcli.products.list_all(q={"account" : "605335af9a090bd16d42350d" , "productType" : 4 , "name" : "Meal Size",})


for i in bundles:
  print(i.autoApply,i._id)
  subp = i.subProducts
  for sub in subp:
    subpPLU = pcli.products.get(sub)
    PLU = subpPLU.plu
    print(PLU)
  pcli.products.update(i,{
        "posValues": {
          "autoApply": None
        },
        "autoApply" : [
        {
          "plu": PLU
        }
      ],
      })

percentages = pcli.products.list_all(q={
  "account" : "" , 
  "deliveryTax" : 0
})




calc = pcli.channelLinks.list_all(q={"account" :"625e0c0916aa929c63e9c359"})

for i in calc:
  if i.posSettings.revel.recalcPriceOverrides : 
    pcli.channelLinks.update(i,{
      "posSettings" : { 
        "revel" : {
          "recalcPriceOverrides" : False
        }      }
    })




GYG= pcli.users.get("619c1ce56ed9f9597b7b9db0")

for i in GYG:

  pcli.users.update(i,{
"roles": [
    0
  ]}
)
  print(i.name)




products = pcli.products.list_all(q={
  "account" : "611418a658d83d209f99552d" , 'productType' : 1
})

for i in products : 
  if i.subProducts != []: 
    print(i.plu,"_____",i.subProducts)



acc = pcli.products.list_all(q={"_id" : "630c12730e6d215906660d40"})

for i in acc:

  pcli.products.update(i,{
    "price" : 1000
  })
 



subids = ["628c3b3fe0b9b9507a1d8742",
"61242b34a46f17a699bc93c8",
"628c3837ef588a2b8f32d0ae",
"6064f1d01ac8010890c31cf6",
"628c610b69ec71342ff7ea4f",
"628c4368e0b9b9507a210b4b",
"6064f1d01ac8010890c31bef",
"6064f1d01ac8010890c31bdb",
"6064f1d01ac8010890c31c8a",
"6064f1d01ac8010890c31ca5",
"62b1062e08c134692e851356",
"628c5ad4ef588a2b8f48fb21",
"628c630aef588a2b8f4f0980",
"628c6600814d8e28fade51e8",
"628c46c6e0b9b9507a221dd8",
"61242b34a46f17a699bc93ce",
"6064f1d01ac8010890c31cf4",
"6064f1d01ac8010890c31c5f",
"628c67a469ec71342ffc9c07",
"628c6ad5ae276b0ccb2b730b",
"628c412fef588a2b8f3617ce",
"628ade89a8a469672acc6692",
"6064f1d01ac8010890c31c31",
"6064f1d01ac8010890c31c6e",
"628c5d6cef588a2b8f4a3176",
"5ff385cac6cc4ade72524c1a",
"628c64a0ef588a2b8f4ff3e4",
"6064f1d01ac8010890c31bd3",
"6064f1d01ac8010890c31c5a",
"628c6588814d8e28fade16b3",
"628b21374409f7d54cdac324",
"62b8f8592b156b5d6e300ad8",
"6064f1d01ac8010890c31c05",
"628c41fb791514df8f40e453",
"6064f1d01ac8010890c31be8",
"628c697ae0b9b9507a3bfc51",
"6163ec37759f9c673b349ba5",
"628c69f1814d8e28fae0e10d",
"628c641c69ec71342ffa4fcf",
"6064f1d01ac8010890c31c6d",
"6064f1d01ac8010890c31c96",
"628c5c8469ec71342ff498bf",
"628c6b52791514df8f5b2de6",
"6064f1d01ac8010890c31c14",
"628c4082e0b9b9507a1fb30b",
"628c45c7b58193d7de65b4c7",
"6064f1d01ac8010890c31c82",
"628b1e8aef588a2b8f80fcba",
"628c6291ef588a2b8f4e92fa",
"628c6823ef588a2b8f529c1d",
"6064f1d01ac8010890c31c1e",
"628b1377814d8e28fa0b9d80",
"6064f1d01ac8010890c31c51",
"628c608a69ec71342ff798c1",
"628c6bcdae276b0ccb2bebe0",]

query = pcli.locations.list_all(q={
  "_id" : {"$in" : subids}
})


for i in query:
  try:

    print("--------------------------------------------------------------")
    print(i.subscriptions)
    print(i.name)
    print("--------------------------------------------------------------")

  except:
    print(i.name,"no sub id ")



query  = pcli.menuAvailabilities.list_all(q={"menu":"6229337b8b7452f13f81b4c3","account":"5fe17b1effe9e99933f9f58a"})



for i in query:
  location = i.location
  location_name = pcli.location.get(location).name
  get_availabilities = pcli.menuAvailabilities.list_all(q={"account" : "5fe17b1effe9e99933f9f58a" ,"menu" : "6229337b8b7452f13f81b4c3" ,"location" : location})
  f = open(f"{location_name}" , "w+")



newroo = pcli.channelLinks.list_all(q={"channel" : {"$in" : [2,50]},"_created": {'$gte':"2022-08-01T04:59:40.000000Z"}})

for i in newroo:
  print("-------------------------")
  print("account ID: ",i.account)
  print("name: ",i.name)
  print("Channel: ",i.channel)
  print("Creation Date: "i._created)




uber = pcli.channelLinks.list_all(q={"channelSettings.storeId" : "8d881ec7-81fa-59e6-993b-e891ad338b56" })

for i in uber:
  print(i._id)

CL = ["631e66ffab0801315bd43b68",
"631e66ffab0801315bd43b65",
"631e66ffab0801315bd43b64",
"631e66ffab0801315bd43b63",
"631e66ffab0801315bd43b62",
"631e66ffab0801315bd43b61",
"631e66ffab0801315bd43b60",
"631e66ffab0801315bd43b5f",
"631e66ffab0801315bd43b5e",
"631e66ffab0801315bd43b59",
"631e66ffab0801315bd43b54",
"631e66ffab0801315bd43b53",
"631e66ffab0801315bd43b4c",
"631e66ffab0801315bd43b4b",
"631e66ffab0801315bd43b4a",
"631e66ffab0801315bd43b49",
"631e66ffab0801315bd43b48",
"631e66ffab0801315bd43b47",
"631e66ffab0801315bd43b46",
"631e66ffab0801315bd43b45",
"631e66ffab0801315bd43b44",
"631e66ffab0801315bd43b43",
"631e66ffab0801315bd43b41",
"631e66ffab0801315bd43b40",
"631e66ffab0801315bd43b34",
"631e66ffab0801315bd43b33",
"631e66ffab0801315bd43b32",
"631e66ffab0801315bd43b31",
"631e66ffab0801315bd43b27",
"631e66ffab0801315bd43b26",
"631e66ffab0801315bd43b23",
"631e66ffab0801315bd43b22",
"631e66ffab0801315bd43b1d",
"631e66ffab0801315bd43b16",
"631e66ffab0801315bd43b15",
"631e66ffab0801315bd43afe",
"631e66ffab0801315bd43afd",
"631e66ffab0801315bd43afa",
"631e66ffab0801315bd43af9",
"631e66ffab0801315bd43af0",
"631e66ffab0801315bd43aed",
"631e66ffab0801315bd43aec",
"631e66ffab0801315bd43aeb",
"631e66ffab0801315bd43aea",
"631e66ffab0801315bd43ae9",
"631e66ffab0801315bd43ae8",
"631e66ffab0801315bd43ae7",
"631e66ffab0801315bd43ae6",
"631e66ffab0801315bd43ada",
"631e66ffab0801315bd43ad9",
"631e66ffab0801315bd43ad8",
"631e66ffab0801315bd43ad7",
"631e66ffab0801315bd43acf",
"631e66ffab0801315bd43ace",
"631e66ffab0801315bd43acd",
"631e66ffab0801315bd43acc",
"631e66ffab0801315bd43a95",
"631e66ffab0801315bd43a94",
"631e66ffab0801315bd43a91",
"631e66ffab0801315bd43a90",
"631e66ffab0801315bd43a80",
"631e66ffab0801315bd43a7f",
"631e66ffab0801315bd43a7e",
"631e66ffab0801315bd43a7d",
"631e66ffab0801315bd43a75",
"631e66ffab0801315bd43a74",
"631e66ffab0801315bd43a72",
"631e66ffab0801315bd43a71",
"631e66ffab0801315bd43a70",
"631e66ffab0801315bd43a66",
"631e66ffab0801315bd43a65",
"631e66ffab0801315bd43a64",
"631e66ffab0801315bd43a63",
"631e66ffab0801315bd43a53",
"631e66ffab0801315bd43a52",
"631e66ffab0801315bd43a51",
"631e66ffab0801315bd43a50",
"631e66ffab0801315bd43a4a",
"631e66ffab0801315bd43a49",]


quer = pcli.channelLinks.list_all(q={"_id" : {"$in" : CL}})

for i in quer:
  print(i.channelSettings.storeId)


import requests
import threading

acc = "62fc44dc934376949a733248"
UIDS = ["03beda5c-7110-58a5-ba4a-4475304598f3",
"14f78d18-66aa-41c0-a6b0-2f999d6d386a",
"8174be4e-1056-4897-9ff3-3802e29a1e6b",
"4737b6a7-62d6-5eaf-94c4-a9ff1950d6d0",
"158e8f55-db73-55f6-b7aa-f82b55c155d7",
"cb5fd2c8-c81e-439e-b366-81da460b28cd",
"54d67d33-d775-41c1-9a63-fafac3788b42",
"834f9968-b62f-4fb7-8632-41c425abb31a",
"439ef855-73fa-4dcb-b5f7-86d5c5738fab",
"f69a2bec-0616-55d0-ab09-723629ad5692",
"66705af1-55fc-5c6c-b13c-99068e4fe13f",
"67f7defa-b116-516d-a252-71141a8a27f4",
"a8eb958f-bcd2-5722-8be9-cf5236335366",
"80b84084-6ae3-5c73-a4e4-20987903af94",
"fcb63813-b431-5578-9932-5ede851bebe3",
"3aa346e0-da35-56cd-93fc-ffb10fdece8e",
"b83baf5a-1a93-5398-953f-bd8084e1dd69",
"941c7117-6745-5c9c-a626-931bf83b205e",
"89ad0d38-ec43-550d-b3b7-fdeefc21688d",
"2bb2cb4c-1232-547f-91a9-266287ef7dca",
"48baf95a-db97-5c50-9b24-14c97d358a60",
"ff19899a-b32e-5481-9611-2a8d168124f0",
"299425a5-520e-53bc-8a95-86d9157ae1fd",
"8f2c42d2-0ac9-5c4f-abfd-d49be11e2733",
"a8ed274d-6ca1-5039-bfcc-9818fb7bcc63",
"9ce32f45-4547-538c-ad90-f060b54bce8f",
"9a811c34-e0b7-5eb6-882a-c7ee0a328d91",
"f6a69a39-e6ff-518f-a6c0-ce1008e04af4",
"ebe85799-1ee7-5778-8017-a58943e83dd2",
"b5f1db05-962a-502d-a979-c1541ed89f79",
"e48f0a70-eea5-513d-a610-260679c358c8",
"ae6ad77d-6f08-5a03-80a1-747c472d46a9",
"1be3d799-46f1-5844-bd4c-03e313ed97f8",
"b9be847a-f097-4c1e-801f-17499b5f823c",
"fc23cca9-4d18-4b4d-9f1f-2409d1575b4d",
"72ef0ac4-f701-5e2a-a679-67e6600a7eb6",
"7857a1a8-e6b3-5300-801d-d610c7f2a1ba",
"c32d82e0-8715-5056-b2e9-b642453747e1",
"545d2ecc-0258-5462-aff7-e6cb5711b5af",
"3e2725d6-cbe8-5cd7-9160-85e8a2f5ebac",
"16b4a914-7c71-4c32-80d4-fd1906d4f6c0",
"05817b56-0813-414d-9cb9-d2e714b27200",
"653fce89-c7b1-5912-beba-c8bc711fb862",
"ba3962fa-e1fe-5d6e-be1e-226d6e189d5d",
"a10ddc8f-25a8-4867-8104-eb62049401bb",
"4b113bf4-6882-4e4e-a491-54e691a2a91d",
"3af7857e-79bb-4079-8af5-92b5c6eb977a",
"73c1079e-bf84-45df-bdab-1bb284c0a60b",
"1927e2af-4bdd-5626-a6e3-5f0445e28a86",
"708d3bd4-41bb-5d04-a980-61b2ee429204",
"6f564d3f-86db-5da8-a621-5a5291b7aa45",
"f5c8d844-ea6f-513c-9861-21de8043bdb1",
"bc91fdad-dab4-467f-992a-c43a0e66702e",
"04d9f5b7-c8a5-4f0e-8b04-7b861fbc10e2",
"c8ff0b1d-cd8c-5ab8-84e6-f1b8d1721713",
"02852d20-c73a-55aa-a78c-df12556a6e54",
"e4fccccd-ac3a-5c4b-a212-0082b75a61db",
"df6d232c-53ad-5848-8a1a-be3c45219bb8",
"597ca2f2-1748-5766-ad58-a29b6c180695",
"70b63374-20a4-51c4-a5b3-51210a99acd0",
"4b6ed42d-1cb1-58a1-9a5a-65bd9706b057",
"49f65de3-145d-592b-8f55-9dab38273680",
"178ee179-f46b-52fc-abaf-90b756e101b5",
"a29c2428-4b1e-5760-85c6-ab6ae93f0fed",
"2d99d9f8-8444-54cd-bd58-125844a274d7",
"cd74aeb1-ee9f-5e3c-9ea3-35061a66bb79",
"db05ebd2-c84b-5a8a-994c-aa42b4c638c0",
"0400196c-f6f3-5dd8-b79d-b402f7584484",
"70a747ce-106d-521c-b1e9-ffcc33e16f8c",
"d37f2b19-01f9-5c6e-8684-7e672528485a",
"4d2266c5-b9cd-5a13-b613-eb309b959859",
"42023c89-f383-5b00-8ffa-e4d64371c424",
"ebb0b9ab-4713-5a90-988e-4045a265d760",
"6c92ffa6-3a0a-4198-b840-39254a170823",
"833c0021-c82f-435c-8ff1-0023a437663e",
"191f1525-065a-4afa-b713-e5e16aa5675f",
"26029dfb-8ff0-482c-9120-f15d86b926dd",
"f735de02-3f4b-5ffe-8bcc-6032579bac9b",
"df96f773-64e8-54e2-a6ce-65e520280ca8",]

quer = pcli.locations.list_all(q={"account" : "62fc44dc934376949a733248"})

for i in quer:
  print(i._id, i.openingHours)
  CLID = i._id
  url = f"https://api.deliverect.com/activateChannelLink/{CLID}"
  print(url)
  payload={}
  headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjM1NDMxOTIsImV4cCI6MTY2MzYyOTU5MiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.eTlPqym8dGLn52PCrpzzXIiDgImM6YiJOOMMmcyCx5WJQBPzMhnz60SBvI-91o_qeh3u6ilHN5rWa5dfbzWyGMIWs7ooEU3OXNozbkhLp27W6qEUTBLVV2EdLJsQbEJMTQgPTgYaZz3salsCnNi43ZMXqBeIEmcqbzOOD0geJnMYrmKtcyLvsxhe-sBLMRGNT16oJcG52m2WM81eWOoh61RiBwYfNP_1wHIBWeuvtw-lkbeVcJGMVsUoJVVlLMplM3v0UVOCy6HyiWx9d_uRIQLZ2McszL7UwOEi-yT8GGUcrok7jfackz0CrD-L-BZkp_aqd9Un3v3G0GIucLKhlg'
}

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)




links = pcli.channelLinks.list_all(q={"channel": 7, "channelSettings.storeId" : {"$exists" : True}, "APIKey": ""})

for link in links:
  if len(link.channelSettings.storeId) == 36:
    pcli.channelLinks.update(link, {"APIKey": link.channelSettings.storeId})
  else:
    print("you must be an imposter")



query = pcli.channelLinks.list_all(q={"channel" : 7 , "channelSettings.pollPickupTime" : True})

for i in query: 
  print(i._id , i.name)



from datetime import datetime, timedelta , date

cl = "6148a053faf3ace530865eb1"
acc = "60647b6bc068c0e7998d9f45"
dt = datetime.now()
dt_string = dt.strftime("%Y-%m-%d___%H:%M:%S")
query_date = date.today()- timedelta(days= 7 )
print(query_date)

ordersAmount = pcli.orders.list_all(q={"account": acc, "channelLink": cl ,"_created":{"$gt":f"{query_date}T00:00:00.000Z"}})

pic = pcli.channelLinks.list_all(q={"account" : "5fdb87212e02409b97ccdb93" , "channel" : 12})

for p in pic:
  print(p.name)
  pcli.channelLinks.update(p,{
      "externalMenuIds": []

  })


quer = pcli.locations.list_all(q={"account" : "630c507964ffb8c1f3b8bb7b"})

for i in quer:
  print(i.name , "-*-", i.timezone)

acc = "633bc40c2e37bb3f82b1d2e9"

query = pcli.orders.list_all(q={"account" : acc})



for order in query:
    print(order.pos)
  pcli.orders.update(order,{
    "pos" : 13
  })


query = pcli.channelLinks.list_all(q={"channel" : 5,"account" : "62b91de8362f63f030fd4d28"})

for i in query:
  print(i.channelSettings.region)
  pcli.channelLinks.update(i,{
    "channelSettings.region": "AS",
  })


# pushmenu 

pcli.call("/pushmenus",method="POST", {"account":"62b00ab0c843643ddb6f1aca","menus":["634cc3bef58cb5ce4bd207b8"],"channelLinks":["62b26adeddff6f74a588633c"],"serverUrl":"https://api.deliverect.com"})

    opReportResult = cli.call(f"/v2/locations/{locationId}/syncProducts?previewSync=true", method="POST")



acc = "615e8f1f4875a94524fa9947"

query = pcli.locations.list_all(q={"timezone" :{"$in" : ["Australia/Adelaide",
"Australia/Brisbane",
"Australia/Broken_Hill",
"Australia/Darwin",
"Australia/Eucla",
"Australia/Hobart",
"Australia/Lindeman ",
"Australia/Lord_Howe",
"Australia/Melbourne",
"Australia/Perth",
"Asia/Singapore",
"Asia/Hong_Kong"

]
} })
acc_ids = []
for o in query:
  acc_ids.append(o.account)
acc_ids = list(dict.fromkeys(acc_ids))
print(acc_ids)






for i in query:
  _min = int(i.min)
  _max = int(i.max)
  amount_of_subProducts = len(i.subProducts)
  if _min > amount_of_subProducts:
    print(i.plu , i._id)


query = pcli.locations.list_all(q={"account" : "630c507964ffb8c1f3b8bb7b",  "status": "INACTIVE",})

for i in query:
  pcli.locations.update(i,{  "status": "SUBSCRIBED",


  })



query = pcli.channelLinks.list_all(q={"channel" : 30})

for i in query:
  try:

    print(i.menuUrl)
  except:
    print("NoMenu")
  
grab =["6369bba5abbadb183b2edcf6",
"6369bba13c46651cb89231ff",
"6369bb9f617bb74419a935e9",
"6369bb9160d8064901a93e3f",
"6369bb9098de34c64e7bcae0",
"6369bb8fa10e27d784375e54",]

panda = ["6369bb9d63d722feed2ed935",
"6369bb9b4dd3f21af7eaa650",
"6369bb9a617bb74419a9352b",
"6369bb8dc77af0b9a27cc51d",
"6369bb883ea227ed7e103ba9",]

roo = ["6369bb999bd8243e676f2a88",
"6369bb964dd3f21af7eaa59c",
"6369bb9372fb91c094626596",
"6369bb928a60d250f1e6f9f1",
"6369bb7263d722feed2ed823",
"6369bb7029d4f9d9d9923109",]

query = pcli.orders.list_all(q={"_id" : {"$in" : roo}})
query3 = pcli.orders.list_all(q={"_id" : {"$in" : panda}})

query2 = pcli.orders.list_all(q={"_id" : {"$in" : grab}})



for order in query:
  pcli.orders.update(order,{
    "channel" : 5
  })




for order in query2:
  pcli.orders.update(order,{
    "channel" : 19
  })


for order in query3:
  pcli.orders.update(order,{
    "channel" : 2
  })



query = pcli.orders.list_all(q={"account" : "62b00ab0c843643ddb6f1aca" , "_created":{'$gte':"2022-11-08T02:14:00.403000Z"}})


for order in query:
  orderId = order._id
  pcli.call(f'/v1/deliverect/generateEtag/orders/{orderId}', 'POST')





query = pcli.orders.list_all(q={"account" : "62b00ab0c843643ddb6f1aca" , "_created":{'$gte':"2022-11-08T02:14:00.403000Z"}})


for order in query:
  orderId = order._id
  print(orderId)

  
  pcli.call(f'/v1/deliverect/generateEtag/orders/{orderId}', 'POST')




query = pcli.products.list_all(q={"account" :"6335c4b0aa8c958f74195c4a"})


for i in query:

  try:  
    print(i.plu)
    print(i.overloads)

  except:
    print("shit")



my_list = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Carl'},
]

result = next(
  (item for item in my_list if item['name'] == 'Bob'),
  {}
)





acc = "6360ff35fa2020af0b52846c"
query = pcli.channelProducts.list(q={"account" : acc , "name" : ' '})


for i in query:
  del i.name
  print(i)
  
  pcli.channelProducts.replace(i,i)



  try:
    print(i.name)


  except:
    print("bs")




location = ["62a204f91c416ef7b1bd6de8",
"62a204f91c416ef7b1bd6e1e",
"62a204f91c416ef7b1bd6e43",
"62a204f91c416ef7b1bd6e55",
"62a204f91c416ef7b1bd6e5b",
"62a204f91c416ef7b1bd6e67",
"62a204f91c416ef7b1bd6e85",
"62a204f91c416ef7b1bd6e8b",
"62a204f91c416ef7b1bd6e97",
"62a204f91c416ef7b1bd6e9d",
"62a204f91c416ef7b1bd6ec1",
"62a204f91c416ef7b1bd6ecd",
"62a204f91c416ef7b1bd6ed3",
"62a204f91c416ef7b1bd6ed9",
"62a204f91c416ef7b1bd6eeb",
"62a204f91c416ef7b1bd6f1b",
"62d50a6e073da7f3b613b63e",
"62d50a6e073da7f3b613b65c",
"62d50a6e073da7f3b613b674",
"62d50a6e073da7f3b613b686",
"62d50a6e073da7f3b613b69e",
"62d50a6e073da7f3b613b6aa",
"62d50a6e073da7f3b613b6bc",
"62d50a6e073da7f3b613b6c2",
"62d50a6e073da7f3b613b6da",
"62d50a6e073da7f3b613b6f8",
"62d50a6e073da7f3b613b70a",
"62d50a6e073da7f3b613b710",
"62d50a6e073da7f3b613b728",
"62d50a6e073da7f3b613b72e",]


quer = pcli.locations.list_all(q={"_id" :{"$in" : location}})


for i in quer:
  print(i.name)



query = pcli.locations.list_all(q={"posSystemId": 10120})


query = pcli.accounts.list_all(q={"accountPlan": 200})

    
for i in query:
  print(i.name ,"-" ,i._id)




def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice: ")

num1 = float(input("Enter number: "))
num2 = float(input("Enter number 2: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid Input")




locs = [
"5ff385cac6cc4ade72524c1",
"635098271b8fcb81bd72c9b",
"632aa2e1143f055c05b31c1",
"636acb5b4ffc882d644a2e7",
"638049d5fdf26d1b9e742e9",
"63508a321b8fcb81bd6a093",
"638447308e5f6533e4fbb56",
"632a87490291dbe2d99fe99",
"638440253800d7c95f6a7b4",
"6163ec37759f9c673b349ba",
"6384443f6c18578686b2ea9",
"5f109866f3494b8ce30aaa5",
]

loc = ["63508a321b8fcb81bd6a0931"]

query = pcli.locations.list_all(q={"_id" : {"$in" : locs}})


subs = ["16CKQ3T7c8tzP2Z8c",
"16CKQ3T7c8u4f2Z8g",
"16CKQ3T7c8u8w2Z8k",
"16CKQ3T7c91oz2ZEg",
"16CKQ3T7c91tx2ZEk",
"16CKQ3T7c91z12ZEo",
"16CKQ3T7c923o2ZFN",
"16CKQ3T7c928X2ZFW",
"16CKQ3T7c92a52ZGn",
"16CKQ3T7c92Dh2ZFw",
"16CKQ3T7c92eZ2ZGr",
"16CKQ3T7c92I92ZG0",
"16CKQ3T7c92Mo2ZGa",
"16CKQ3T7c92o82ZHH",
"16CKQ3T7c92RA2ZGf",
"16CKQ3T7c92sQ2ZHU",
"16CKQ3T7c92Vd2ZGj",
"16CKQ3T7c92wt2ZHe",
"16CKQ3T7c931Z2ZI8",
"16CKQ3T7c93652ZIK",
"16CKQ3T7c93Ab2ZIj",
"16CKQ3T7c93F12ZJ7",
"16CKQ3T7c93JN2ZJH",
"16CKQ3T7c93Np2ZJU",
"16CKQ3T7c93SX2ZJj",
"16CKQ3T7c93X12ZK1",
"16CKT4TI4TqjvSkR",
"16CKT4TI4TqopSkV",
"16CKT4TI4TqtMSkZ",
"16CKT4TI4TvaNSuU",
"16CKT4TI4TvfBSuY",
"16CKT4TI4Tvk6Suc",
"16CKT4TI4TvoxSug",
"16CKT4TI4TvRHSuM",
"16CKT4TI4TvtnSuk",
"16CKT4TI4TvVnSuQ",
"16CKT4TI4TvyqSux",
"16CKT4TI4Tw3SSvM",
"16CKT4TI4Tw86SvQ",
"16CKT4TI4Twb3SxL",
"16CKT4TI4TwCiSvU",
"16CKT4TI4TwfqSxP",
"16CKT4TI4TwHJSvY",
"16CKT4TI4TwkbSxT",
"16CKT4TI4TwMCSwA",
"16CKT4TI4TwRLSx8",
"16CKT4TI4TwrLSxe",
"16CKT4TI4TwvaSxs",
"16CKT4TI4TwWVSxC",
"16CKT4TI4Tx00Sxw",
"16CKT4TI4Tx4hSy0",
"16CKT4TI4Tx9NSy4",
"16CKT4TI4TxDySy8",
"16CKT4TI4TxIjSyC",
"16CKT4TI4TxNSSyG",
"16CKT4TI4Ty0LT1P",
"16CKUKTLYgwIl1qxt",
"16CKUKTLYgwIl1qxt",
"16CKUKTLYgwNT1qy1",
"16CKUKTLYgwS71qy5",
"16CKUKTLYixwY1uaM",
"16CKUKTLYixwY1uaM",
"16CKUKTLYiy161uaQ",
"16CKUKTLYiy161uaQ",
"16CKUKTLYiy5g1uaU",
"16CKUKTLYiy5g1uaU",
"16CKUKTLYj87i1us2",
"16CKUKTLYj8aD1uwZ",
"16CKUKTLYj8C61us6",
"16CKUKTLYj8et1uwd",
"16CKUKTLYj8Gs1usZ",
"16CKUKTLYj8Gs1usZ",
"16CKUKTLYj8jS1uwi",
"16CKUKTLYj8LQ1uty",
"16CKUKTLYj8nr1uwm",
"16CKUKTLYj8Q01uwP",
"16CKUKTLYj8sX1uwq",
"16CKUKTLYj8Ug1uwV",
"16CKUKTLYj8x31uwu",
"16CKUKTLYj92J1uwy",
"16CKUKTLYj97M1ux8",
"16CKUKTLYj9Cu1uxd",
"16CKUKTLYj9dm1uyL",
"16CKUKTLYj9Ib1uy5",
"16CKUKTLYj9P51uy9",
"16CKUKTLYj9Tg1uyD",
"16CKUKTLYj9Ys1uyH",
"16CKUKTLYjB2i1v34",
"16CKUKTLYjB7F1v38",
"16CKUKTLYjC1T1v7n",
"16CKUKTLYjC5p1v7r",]

acc = pcli.locations.list_all(q={"subscriptions": [
    {

      "subscriptionId": "16CKQ3T7c93Ab2ZIj"
    }]})



query = pcli.channelMenus.list_all(q={"account" : "633d14f8ea170601672a3ff5"})

for i in query:
  pcli.products.delete(i)



query = pcli.accounts.list_all(q={"region": "AUS"})

for loc in query:
   
  try:
      locationCount = len(loc.locations)
      if locationCount > 10:
         print(loc.name, "--",locationCount)

  except:
      print("no locations" , loc._id , "__",loc.name)





all_products = pcli.products.list_all(q={"account" : "624f796288b904a46ab92175" , "posValues.subProducts" : {"$exists" : True}})

for prods in all_products:
   subProductCount = len(prods.subProducts)
   posValuesCount = len(prods.posValues.subProducts)
   if subProductCount != posValuesCount:
    print(prods._id , prods.plu , prods.location)
    print(prods.subProducts , prods.posValues.subProducts)




auery = pcli.products.list_all(q={"account" : "633d14f8ea170601672a3ff5" , "_id" :{"$in" : ["64066e55db8688af4c1c6917",
"64066e55db8688af4c1c6915",
"63f554e5a6dd593264e9576a",
"63f554e5a6dd593264e95768",
"63f554e5a6dd593264e95766",
"63f554e5a6dd593264e95762",
"63f554e5a6dd593264e95760",
"63f554e5a6dd593264e9575e",
"63f554e5a6dd593264e9575c",
"63f554e5a6dd593264e9575a",
"63f554e5a6dd593264e95756",
"63f554e5a6dd593264e95754",
"63f554e5a6dd593264e95750",
"63f554e5a6dd593264e9574e",
"63f554e5a6dd593264e9574a",
"63f554e5a6dd593264e95748",
"63f554e5a6dd593264e95744",
"63f554e5a6dd593264e95742",
"63f554e5a6dd593264e9573e",
"63f554e5a6dd593264e9573c",
"63f554e5a6dd593264e9573a",
"63f554e5a6dd593264e95738",
"63f554e5a6dd593264e95734",
"63f554e5a6dd593264e95732",
"63f554e5a6dd593264e9572e",
"63f554e5a6dd593264e9572c",
"63f554e5a6dd593264e95728",
"63f554e5a6dd593264e95726",
"63f554e5a6dd593264e95724",
"63f554e5a6dd593264e95722",
"63f554e5a6dd593264e95720",
"63f554e5a6dd593264e9571e",
"63f554e5a6dd593264e9571c",
"63f554e5a6dd593264e95714",
"63f554e5a6dd593264e95672",
"63f554e5a6dd593264e9566a",
"63f554e5a6dd593264e95644"]}})



for prod in auery:
   print(prod._id , "---" , prod.name)
   pcli.products.update(prod,{
      "subProducts": []
   })



query = pcli.productOverrides.list_all(q={"account" : "5fb3cf362088f9d8903147cb",    "price": {"$exists" : True}})

for over in query:
      
      print(over.price)
      pcli.productOverrides.update(over,
      {"&unset":{"price":0}})



query = pcli.locations.list_all(q={"account" : "641b935c38d5ab6b2ea3b8fc"})

for loc in query:
  channelLinks = loc.channelLinks
  for channel in channelLinks:
     pcli.channelLinks.delete(channel)

  pcli.locations.delete(loc)


acc= "5fe17b1effe9e99933f9f58a"

query = pcli.products.list_all(q={"account" : acc})




acc = "61f16a85c10f898fd52ab03c"

cls = pcli.channelLinks.list_all(q={"account" : acc})
for cl in cls:
    print(cl.status)
    if cl.status != 1:
      pcli.channelLinks.update(cl,{
                "status": 1,
          })
  
   

for loc in locs:
   pcli.locations.update(loc,{
        "status": "SUSPENDED",
   })
   cl = loc.get("channelLinks",{})
   print(cl)



    
   for c in cl:
      getCl = pcli.channelLinks.get(c)
      for x in getCl:
         pcli.channelLinks.update(x,{
              "status": 1,
         })
         \\

acc = "61df8c560706d58e1016f00d"


links = pcli.menuAvailabilities.list_all(q={"account" : "62b91de8362f63f030fd4d28", "menu" : "642cef9513dee05bd63701ae"})

for avail in links:
   print("day",avail.dayOfWeek)
   print(avail.startTime)
   print(avail.endTime)
   print(avail.category)
   print("------------------------")


for link in links:
  name = link.name
  if name == "Eats 2 U":
    pcli.channelLinks.update(link,{
       "tags": [
       "Eats 2 U"
  ]
    })
    break



  links = pcli.accounts.list_all(q={"region" : "EU"})

  for link in links:
     print(link.name,"-#-",link._created)
     print()
     


channellinks = pcli.channelLinks.list_all(q={"account" : "63898dcf94b0ea4b6fc56dfe"})

for channel in channellinks:
   pcli.channelLinks.update(channel , {
      "posSettings": {
    "simphony_gen2": {
        "orderTypeId": "1",
        "curbsideOrderTypeOverride": "1",
        "eatInOrderTypeOverride": "1",
        "pickupOrderTypeOverride": "1",
              "paidPaymentType": "300",
      "notPaidPaymentType": "101",
    }
}
   })



loc  = pcli.locations.list_all(q={"_id":"643481ae45627f3635aacc30"})
pcli.locations.update(loc, {"_deleted" : False})

print(loc.name)

loc  = pcli.locations.list(q={"_id": "643481ae45627f3635aacc30", "_deleted": True})
for l in loc:
   pcli.locations.update(l,{"_deleted" : False})


loc_list=["62a204f91c416ef7b1bd6e73",
"633bc0e42ef3c14e806ea0eb",
"62a204f91c416ef7b1bd6e18",
"62d50a6e073da7f3b613b896",
"63cf579c39f9df0f10ab0078",
"62a204f91c416ef7b1bd6e67",
"62a204f91c416ef7b1bd6f1b",
"62d50a6e073da7f3b613b674",
"62d50a6e073da7f3b613b8cc",
"62d50a6e073da7f3b613b8d8",
"62d50a6e073da7f3b613b8e4",
"62d50a6e073da7f3b613b8ea",
"62a204f91c416ef7b1bd6eb5",
"62d50a6e073da7f3b613b8f6",
"62d50a6e073da7f3b613b8fc",
"62d50a6e073da7f3b613b67a",
"62d50a6e073da7f3b613b686",
"62a204f91c416ef7b1bd6ec1",
"62a204f91c416ef7b1bd6e06",
"62a204f91c416ef7b1bd6e37",
"62a204f91c416ef7b1bd6ddb",
"62d50a6e073da7f3b613b6bc",
"62d50a6e073da7f3b613b6c8",
"62d50a6e073da7f3b613b6d4",
"62d50a6e073da7f3b613b6da",
"62d50a6e073da7f3b613b6e0",
"62d50a6e073da7f3b613b6f2",
"62a204f91c416ef7b1bd6de2",
"62d50a6e073da7f3b613b710",
"62a204f91c416ef7b1bd6de8",
"62a204f91c416ef7b1bd6e85",
"62a204f91c416ef7b1bd6f33",
"62a204f91c416ef7b1bd6e8b",
"62a204f91c416ef7b1bd6df4",
"62d50a6e073da7f3b613b73a",
"62a204f91c416ef7b1bd6e24",
"62d50a6e073da7f3b613b77c",
"62a204f91c416ef7b1bd6dee",
"62d50a6e073da7f3b613b788",
"62a204f91c416ef7b1bd6f03",
"62a204f91c416ef7b1bd6e43",
"62a204f91c416ef7b1bd6edf",
"62a204f91c416ef7b1bd6efd",
"62d50a6e073da7f3b613b7a6",
"62a204f91c416ef7b1bd6ea9",
"62d50a6e073da7f3b613b7b2",
"62d50a6e073da7f3b613b7b8",
"633bc0e42ef3c14e806ea0bb",
"62d50a6e073da7f3b613b7d6",
"62d50a6e073da7f3b613b7e8",
"62a204f91c416ef7b1bd6e61",
"62d50a6e073da7f3b613b800",
"62d50a6e073da7f3b613b812",
"62a204f91c416ef7b1bd6e4f",
"62a204f91c416ef7b1bd6ebb",
"62a204f91c416ef7b1bd6e3d",
"62a204f91c416ef7b1bd6e00",
"633bc0e42ef3c14e806ea091",
"62a204f91c416ef7b1bd6e55",
"62d50a6e073da7f3b613b884",
"62a204f91c416ef7b1bd6e0c",]

locations = pcli.locations.list_all(q={"_id" : {"$in" : loc_list}})


for loc in locations:
   print(loc._id)


Channellinks = pcli.channelLinks.list_all(q={"account" : "61df8c560706d58e1016f00d" , "name" : "Ben & Jerry's"})


for channel in Channellinks:
  pcli.channelLinks.update(channel,
                           {
                              "tags": [
    "Ben & Jerry's"
  ]
                           })


links = pcli.channelLinks.list_all(q={"account" : "61df8c560706d58e1016f00d" , "status" : 4})
for link in links:
   pcli.channelLinks.update(link,{"status" :3})


payload = {"posSettings": {
    "ncr": {
      "nameIsAlwaysOrderData": True
    }}}


locations = pcli.locations.list_all(q={"account" : "637ef6ed078f8677e5de1218"})

for loc in locations:
   links = loc.channelLinks
   pcli.locations.update(loc,payload)
   for link in links:
      pcli.channelLinks.update(link,payload)



pixless = pcli.channelLinks.list_all(q={ "posSystemId": 39,  "posSettings.pixelpoint.orderNotePLU": {"$exists" : True }})


for pix in pixless:
   print("-----------------")
   print(pix.posSettings.pixelpoint.orderNotePLU)
   print(pix._id)


products = pcli.products.list_all(q={"account" :"643df5e2e3c6dac1c8dc5165", "productType" : 3})


for prod in products:
   print(prod.name)
   print("Min: ",prod.min)
   print("max: ", prod.max)



accs = ["63fddb4ca15b7a8ba70bb7cc",
"63c48200499e86151d582cea",
"6363db4d9b5dd2d53531a1f1",
"62c299338fe96344852f62e1",
"626fec37e8603d8868905969",
"64621b8f1af2a7c72e6f0814",
"641b28a6f676bac419a4fa34",
"63ea441ce127227838600087",
"63d9cbe3301774db888211ca",
"63c560b79539b1041bfb2c6c",
"63898dcf94b0ea4b6fc56dfe",
"61e5b0c784dca26bed204421",]


get_acc = pcli.channelMenus.list_all(q={"enforcePullAvailabilities":{"$exists" : True}}})

for acc in get_acc:
   print(acc.name,"--" ,acc._id)



products = scli.products.list_all(q={"account" : "64782cd8e8b4ff62b5cc207e", "productType" : 1 })

"https://api.staging.deliverect.com/v2/search/products?page=2&query=burrito&locations=[%2264782ce83e59daecb7885c66%22]&itemTypes=[1]&account=64782cd8e8b4ff62b5cc207e&&max_results=25"



acoount = "62d8a6ff4e5b46aaaa755da0"

users = pcli.products.list_all(q={"account" : acoount})


for user in users: 
   pcli.products.delete(user)


account ="63abd7593662ec3abb11db6f"

products = pcli.products.list_all(q={"account" : account})



     print(product.plu,"--" , product.location)


      
   


account = "649237e6bf546cf5de940fac"

query = pcli.products.list_all(q={"account" : account })

count = 0
for i in query:
   if i.priceLevels:
      count += 1
      print(i.plu)
print(count)

   


hungryPanda = scli.channelLinks.list_all(q={"channel" : 7})


for panderrr in hungryPanda:
      print(panderrr.get("APIKey",{}))
      print(panderrr.channelSettings.application)
      print(panderrr._id)





import requests

account = "61df8c560706d58e1016f00d"


ubers = pcli.channelLinks.list_all(q={"account" : account,"channel" : 7})

for uber in ubers:
   deactivate = f"https://api.deliverect.com/disableChannelLink/{uber._id}"
   acticate = f"https://api.deliverect.com/v2/channelLinks/{uber._id}/activate"
   print(deactivate)
   print(acticate)
   payload = {}
   headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODgzNDAzNzEsImV4cCI6MTY4ODQyNjc3MSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.W6v-1Poo5t6UNOWYen7vJOt4p7pgW9ZWTHOV0zBhI1InrumeZdYwCJRkMkElcJv2a5g6HwlOjaVbQudsJN6fVt99RYZ6y2ixI5UimXmaTGaimoMpTNn9eqo9LWD4ZJPsRuWJUg0InOWjFABqnyN7U1jWwm-yiP8h1YxZO9mcZtLnNSq1EYmpyGP7QE3zyUxB1lZqzroI-9GDR3FmYADOPXL5SW_3A5MOogKJM90T7aH8zJwgQoDOT-Cf5Mnvq3-PRs2FE1BFr-Ie-vtXSMFkE2Hpw_Nlv6SelJ5Xjk81luZvfA7RCj-TGn4Hg6k5zXCn2u1uxUwPy2EEhyuT4Uw79A'
}
   response1 = requests.request("POST", acticate, headers=headers, data=payload)
   response = requests.request("POST", deactivate, headers=headers, data=payload)
   response2 = requests.request("POST", acticate, headers=headers, data=payload)
   print(response1.text)
   print(response.text)
   print(response2.text)




while True:
  import requests
  import json
  import random

  url = "https://zambrerodevapi.xchangefusion.com/api/v3/OnlineOrders"
  random_integer = random.randint(1, 1000000000)
  print(random_integer)
  payload = json.dumps({
    "id": None,
    "source": None,
    "saleName": f"{random_integer}",
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
    "onlineOrderType": 1,
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
    "orderTypeId": 8,
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




account = "61df8c560706d58e1016f00d"




plu = ["30038_0_1",
"30039_0_1",
"30040_0_1",
"30041_0_1",
"30044_0_1",
"30045_0_1",
"30046_0_1",
"30048_0_1",
"30049_0_1",
"30050_0_1",
"30056_0_1",
"30058_0_1",
"30066_0_1",
"30067_0_1",
"30069_0_1",
"30075_0_1",
"30081_0_1",
"30083_0_1",
"30086_0_1",
"30089_0_1",
"30090_0_1",
"30091_0_1",
"30093_0_1",]


products = pcli.products.list_all(q={"account" : "605335af9a090bd16d42350d" , "location" : "64a4e70c058452c90f0f3e46" , "plu" : {"$in" : plu}})


for prod in products:




account = "6438d52dcec9f35c2d499d9a"

products = pcli.products.list_all(q={"account" : account})



for prod in products:
   pcli.products.delete(prod)




channel = pcli.products.list_all(q={"account": "64be14a1be00bdf242742a14"})


for chane in channel:
   pcli.products.delete(chane)