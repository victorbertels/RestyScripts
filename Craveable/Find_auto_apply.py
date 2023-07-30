ap = pcli.products.list_all(q={
    "account" : "615e8f1f4875a94524fa9947" , "autoApply" : {"$exists" : True}
})

for i in ap:
    print(i.plu)