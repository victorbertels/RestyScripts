account = "61df8c560706d58e1016f00d"
channel = pcli.channelLinks.list_all(q={"account" : account})
no_orders = []
has_orders = []
not_us = []
for clink in channel:
    ordersAmount = pcli.orders.count(q={"account": account, "channelLink": clink._id, "_created":{"$gt":"2022-07-05T00:00:00.000Z"}})
    if not ordersAmount:
      print("********--------********no Orders: ", clink._id , "channel: ", clink.channel,"********--------********")
      no_orders.append(clink.location)
    else:
      print("orders: ",ordersAmount , "CL:", clink._id)


locs = pcli.locations.list_all(q={"account" : account, "_id" : {"$in":no_orders}})
for name in locs:
  print(name._id,name.name)


good_loc_ids = []
hasorders = pcli.channelLinks.list_all(q={"account" : account, "_id" : {"$in":has_orders}})
for no in has_orders:
  print(no.name ,"--", no.channel,"**", no.location)

locs = pcli.locations.list_all(q={"account" : account, "_id" : {"$in":good_loc_ids}})
for name in locs:
  print(name._id,name.name)


