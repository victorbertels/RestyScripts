ACCOUNT = "63435e96e54f9c12e91c9745"

products = pcli.products.list_all(q={"account" : ACCOUNT , "location" : "641a44cc7ccad44aefcda1ec" , "overloads" : {"$exists" : True}})


for product in products:
    overloads = product.get("overloads" , [])
    for x in overloads:
        # if x.get("priceLevels",{}):
        #     print(x.get("priceLevels"))
        if x.get("priceLevels",{}) and not x.get("overrideSurchargeWithPriceLevels"):
            x["overrideSurchargeWithPriceLevels"] = True
            print(x)


        