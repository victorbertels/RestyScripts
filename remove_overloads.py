pid = "60548d8440a98c8fca6a70af"

acc = "605335af9a090bd16d42350d"

query = pcli.products.list_all(q={ "account" : acc , "overloads" : {"$exists" : True}})

for prod in query:
    if prod.overloads != []:
        print(prod.overloads)
        print( prod._id , prod.plu)
        pcli.products.update(prod,{"overloads" : []})
   