account = "605335af9a090bd16d42350d"


productsWithOverLoads = pcli.products.list_all(q={"account" : account , "overloads" :{"$exists" : True}})

count = 0
for products in productsWithOverLoads:
    overLoads = products.get("overloads",[])
    modified = False
    for overload in overLoads:
        # print(overload)
        # overRideSurcharge = overload.get("overrideSurchargeWithPriceLevels",{})
        # print(overRideSurcharge)
        if overload.get("overrideSurchargeWithPriceLevels",[]):
            overload["overrideSurchargeWithPriceLevels"] = False
            modified = True

        # print(products.plu)
    if modified:
        count=+1
        pcli.products.update(products, {"overloads" : overLoads})
        print(overLoads)
        print(count)
print(f"Updated {count} products")


 # Go over the products.
    for product in products:
        # Store the overloads.
        overloads = product.get("overloads", [])

        # Go over the overloads.
        modified = False
        for overload in overloads:
            # If the overload has priceLevels filled in, we should set overrideSurchargeWithPriceLevels to True
            if overload.get("priceLevels") and not overload.get("overrideSurchargeWithPriceLevels"):
                overload["overrideSurchargeWithPriceLevels"] = True
                modified = True

        # If we modified anything, store the changes on the product.
        if modified:
            print(f"Updated {product['_id']}")
            updateCount += 1
            # requests.patch(f"https://api.deliverect.com/products/{product['_id']}", json={"overloads": overloads}, headers={**HEADER, "If-Match": product['_etag']})

print(f"Updated {updateCount} products")