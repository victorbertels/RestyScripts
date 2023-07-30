account = "5d67c3f06f006f00012b83d1"
DoorDash_requested = ["624a790719a0d62ad62ec9c4",
"624a790819a0d62ad62eca33",
"624a790819a0d62ad62eca02",
"624a790719a0d62ad62ec978",
"624a790719a0d62ad62ec99d",
"624a790819a0d62ad62eca69",
"624a790719a0d62ad62ec97e",
"624a790819a0d62ad62ec9f4",
"624a790719a0d62ad62ec984",
"624a790719a0d62ad62ec9be",
"624a790819a0d62ad62eca81",
"624a790719a0d62ad62ec9af",
"624a790719a0d62ad62ec9b7",
"624a790819a0d62ad62eca15",
"624a790819a0d62ad62eca2d",
"624a790819a0d62ad62eca27",
"624a790719a0d62ad62ec98a",
"624a790819a0d62ad62eca7b",
"624a790819a0d62ad62eca99",
"624a790819a0d62ad62ecaa5",
"624a790819a0d62ad62ec9ee",
"624a790719a0d62ad62ec990",
"624a790819a0d62ad62eca8d",
"624a790819a0d62ad62eca45",
"624a790819a0d62ad62eca52",
"624a790819a0d62ad62eca75",
"624a790719a0d62ad62ec9a7",
"624a790819a0d62ad62eca87",
"624a790819a0d62ad62eca63",
"624a790819a0d62ad62eca6f",
"624a790819a0d62ad62eca5d",
"624a790819a0d62ad62eca0f",
"624a790819a0d62ad62eca09",
"624a790719a0d62ad62ec9ca",
"624a790719a0d62ad62ec9d0",
"624a790719a0d62ad62ec9d6",
"624a790819a0d62ad62ecaab",
"624a790719a0d62ad62ec996",
"624a790819a0d62ad62ec9fa",
"624a790819a0d62ad62eca39",
"624a790819a0d62ad62eca9f",
"624a790719a0d62ad62ec9dc",
"624a790719a0d62ad62ec9e2",
"624a790719a0d62ad62ec9e8",
"624a790819a0d62ad62eca4b",
"624a790819a0d62ad62eca93",
"624a790819a0d62ad62eca1b",
"624a790819a0d62ad62eca3f",
"624a790819a0d62ad62eca21",
]
channel = pcli.channelLinks.list_all(q={"account" : account,"_id" : {"$in" : DoorDash_requested}})
no_orders = []
has_orders = []
not_us = []
for clink in channel:
    ordersAmount = pcli.orders.count(q={"account": account, "channelLink": clink._id, "_created":{"$gt":"2022-05-22T00:00:00.000Z"}})
    if not ordersAmount:
      print("no Orders: ", clink._id , "channel: ", clink.channel)
    else:
      print("orders: ",ordersAmount , "CL:", clink._id)

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


