acc = "5e7bbf7265013b00010cb6aa"


products = pcli.products.list_all(q={"account" : acc ,"location" : "5f109866f3494b8ce30aaa56", "calories" : {"$exists" : True}})

updateCount = 0
for prod in products:
    if prod.calories is not None:
        print(prod.calories)

        x = round(prod.calories)
        pcli.products.update(prod,{
            "calories" : x
        })
        updateCount += 1
        print(updateCount)
