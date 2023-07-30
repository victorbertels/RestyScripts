CTaccount = "63290d3fdceae416df65c7e8"
OPaccount = "63435e96e54f9c12e91c9745"

products = pcli.products.list_all(q={"account": CTaccount , "autoApply" : {"$exists" : True}, })

Oproducts = pcli.products.list_all(q={"account": OPaccount , "autoApply" : {"$exists" : True}})


for AP in products:
    if AP.autoApply != []:
        print(AP.autoApply, AP.plu)
        pcli.products.update(AP,{
            "autoApply" : []
        })


for AP in Oproducts:
    if AP.autoApply != []:
        print(AP.autoApply, AP.plu)
        pcli.products.update(AP,{
            "autoApply" : []
        })
