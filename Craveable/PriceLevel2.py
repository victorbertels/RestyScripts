acc = "63290d3fdceae416df65c7e8"
loc = "638049d5fdf26d1b9e742e9f"


query = pcli.products.list_all(q={"account" : acc , "location" : loc})


for pro in query:
    try:
        if pro.priceLevels["2"]:
            pcli.products.update(pro,{
                "priceLevels": {
                   "1": pro.priceLevels["2"]
            }})
            print(pro.priceLevels["2"])
            
        # pricelevel2 = pro.priceLevels["2"]

    except:
        print(pro.plu,"no pricelevels")
