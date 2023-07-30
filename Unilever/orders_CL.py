account = "5d67c3f06f006f00012b83d1"

locations = pcli.locations.list_all(q={"account" : account})



for location in locations:
  for clink in location.channelLinks:
      ordersAmount = pcli.orders.count(q={"account": account, "channelLink": clink, "_created":{"$gt":"2022-05-14T00:00:00.000Z"}})
      if not ordersAmount:
          print(f"channel link id= {clink} had no orders in the last 6 months")
      else:
        print(f'channel link id= {clink}, had {ordersAmount} orders in the last 6 months')



account = "5d67c3f06f006f00012b83d1"
channel = pcli.channelLinks.list_all(q={"account" : account, 'channel' : {"$in" : [2,7,12,26]}})
no_orders = []
has_orders = []
not_us = []
for clink in channel:
  if clink.name[-3:] == "NEW":
    ordersAmount = pcli.orders.count(q={"account": account, "channelLink": clink._id, "_created":{"$gt":"2022-05-22T00:00:00.000Z"}})
    if not ordersAmount:
      print("no Orders: ", clink._id , "channel: ", clink.channel)
      no_orders.append(clink._id)


    else:
      print("orders: ",ordersAmount , "CL:", clink._id)
      has_orders.append(clink._id)

  else:
    print(clink.name, "is not what we added")
    not_us.append(clink._id)


#get the info for no_orders.#
loc_ids = []
norders = pcli.channelLinks.list_all(q={"account" : account, "_id" : {"$in":no_orders}})
for no in norders:
  loc_ids.append(no.location)
  print(no.name ,"--", no.channel,"**", no.location)

locs = pcli.locations.list_all(q={"account" : account, "_id" : {"$in":loc_ids}})
for name in locs:
  print(name._id,name.name)


good_loc_ids = []
hasorders = pcli.channelLinks.list_all(q={"account" : account, "_id" : {"$in":has_orders}})
for no in has_orders:
  print(no.name ,"--", no.channel,"**", no.location)

locs = pcli.locations.list_all(q={"account" : account, "_id" : {"$in":good_loc_ids}})
for name in locs:
  print(name._id,name.name)


