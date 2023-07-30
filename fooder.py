acc = "61f16a85c10f898fd52ab03c"

locations = pcli.locations.list_all(q={"account" : acc})

for loc in locations:
    loc_id = loc._id
    get_orders = pcli.orders.count(q={"638d9d57b10e4571bb0ed487" : loc_id, "_created": {'$gte':"2022-02-21T09:34:29.554000Z","$lt": "2022-02-22T09:34:29.554000Z"}})
    print(loc_id , "**","name" , loc.name,"--" ,"total orders" ,get_orders)
