account = "5fe17b1effe9e99933f9f58a"

locations = pcli.locations.list_all(q={"account" : account})



for location in locations:
  for clink in location.channelLinks:
      ordersAmount = pcli.orders.count(q={"account": account, "channelLink": clink, "_created":{"$gt":"2022-05-14T00:00:00.000Z"}})
      if not ordersAmount:
          print(f"channel link id= {clink} had no orders in the last 6 months")
      else:
        print(f'channel link id= {clink}, had {ordersAmount} orders in the last 6 months')



account = "5fe17b1effe9e99933f9f58a"
channel = pcli.channelLinks.list_all(q={"account" : account, 'channel' : {"$in" : [12,2,7,26]}})
no_orders = []
has_orders = []
for clink in channel:
    ordersAmount = pcli.orders.count(q={"account": account,"channelLink": clink._id, "_created":{'$gte':"2021-12-01T00:00:00.000Z","$lt":"2021-12-31T00:00:00.000Z"}})
    if not ordersAmount:
        print(clink._id, clink.name)
        no_orders.append(clink._id)

    else:
        print(f"i got orders : {clink._id}")
        has_orders.append(clink._id)



locations = pcli.locations.list_all(q={"account" : account})




def _removePriceOverrides (menuId):
    get_menu = pcli.menus.get(menuId)
    for i in get_menu: 
        del i.deliveryTax




