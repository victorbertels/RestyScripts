modifiers = pcli.products.list_all(q={"account" : "624f796288b904a46ab92175","location" : "6268cd87e8f846409201548a" ,"productType": 2 })


for mod in modifiers:
    price = mod.price
    if mod.name[0:3] == "No " and price != 0:
        print(mod.plu)
        print(price)
        print(mod.location)
        pcli.products.update(mod,{
            "price" : 0,
            "posValues":
                {
                    "price": price,
                    "imageUrl": None
                }
    })
    