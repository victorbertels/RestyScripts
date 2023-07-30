acc = "624f796288b904a46ab92175"
plusss = ["40338","40339","40341","40340","30093_2","30093_1","30091_2","40303","40308","30092_1","40246","30087_1","40309","30120_1","30120_0","40310","40311",]
query = pcli.productOverrides.list_all(q={"account" : acc ,"plu" :{"$in" : plusss}, "location" : {"$in" :["6268ce08e97401166b98cc83" , "6268ce08e97401166b98cc89"]}})




for override in query:
    print("-----------------")
    print("plu:  ",override.plu)
    print("price:  ",override.price)
    print("loc " , override.location)
    print("DELETED")
    print("-----------------")
    pcli.productOverrides.delete(override)

    



#look for the ones without locations

query = pcli.productOverrides.list_all(q={"account" : acc , "location": {"$exists" : False}})


for i in query:
    print(i)
    break



query = pcli.products.list_all(q={"account" : acc ,"price" : 1998})
