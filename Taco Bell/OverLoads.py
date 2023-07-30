collins = "605335af9a090bd16d42350d"



query = pcli.products.list_all(q={ "account" : collins ,"location" : "605335ec9a090bd16d423ed6", "overloads" : {"$exists" : True}, "posValues.overloads" : {"$exists" : True}})

for prod in query:
    # pcli.products.update(prod,{
    #     "overloads" : [],
    #     "posValues.overloads" : []
    # })
    print(prod.overloads)
    print(prod.posValues.overloads)
    print("-------------")
    # if prod.overloads == [] and prod.posValues.overloads != []:
        
    #     pcli.products.update(prod,{"overloads": prod.posValues.overloads})
        # print(prod.overloads)
        # print(prod.posValues.overloads)
        # print( prod._id , prod.plu)
        # pcli.products.update(prod,{"overloads" : []})
   