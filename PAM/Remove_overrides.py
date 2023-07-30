menu = "64193794d69958a5625b1534" 
account = "someAccontIdHere"


cp = pcli.channelProducts.list_all(q={"account" : account,"menu" : menu, "price" : {"$exists" : True}})



for c in cp:
    print(c.price)
    del c.price
    pcli.channelProducts.replace(c, c)

