account = "5d67c3f06f006f00012b83d1"


query = pcli.channelLinks.list_all(q={"account" : account , "name" : "DD Dessert Store"})

for i in query:
    print(i.location , "*-*",i._id)



account = "5d67c3f06f006f00012b83d1"


query = pcli.accounts.list_all(q={"posSystem" : {"$in" : [10005]}})

for i in query:
    print(i._id)