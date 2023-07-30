p = pcli.products.list_all(q={"account" :"63290d3fdceae416df65c7e8","location" :"636055a2cb9fccb436a3e76c" ,"overloads" : {"$exists" : True} })

p = pcli.products.list_all(q={"account" :"63435e96e54f9c12e91c9745","overloads" : {"$exists" : True} })

for x in p:
    overloads = x.overloads
    for load in overloads:
        if load.priceLevel:

    

            load.update({"overrideSurchargeWithPriceLevels": True, 
            })
            print("---------")
            print(load)
            break
        
pcli.products.update(p, {'overloads': p.overloads})