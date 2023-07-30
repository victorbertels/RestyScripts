menupr = pcli.products.list_all(q={"account" : "60427d4bc05aa6daba9c5e6f"})

for products in menupr:
    name = products.name
    plu = products.get('plu')
    nameTranslation = products.get('nameTranslations')
    patchJson={}
    if name is None and nameTranslation is None:
        continue
    print(f"{name} ,{ nameTranslation}")
    if name is None and nameTranslation is not None and nameTranslation.get('en') and nameTranslation.get('en') != " ":
        patchJson["name"]=nameTranslation.get('en')
    if nameTranslation is not None and nameTranslation.get('en'):
        nameTranslation['en']=None
        patchJson["nameTranslations"]=nameTranslation
    print(patchJson)
    if patchJson:
        pcli.channelProducts.update(menupr , patchJson)