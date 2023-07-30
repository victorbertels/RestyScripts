query = pcli.accounts.list_all(q={"featureFlags.showProductsV21":False})


for acc in query:
    id = acc._id
    name = acc.name
    locationCount = len(acc.get("locations",{}))
    type = acc.accountType
    Layout = acc.featureFlags.showProductsV21
    region = acc.region
    status = acc.get("status",{})


    print(f"{id},{name},{locationCount},{type}, {Layout} , {region}, {status}")



query2 = pcli.accounts.list_all(q={"featureFlags.combinedProductsPage":False})


for acc in query2:
    id = acc._id
    name = acc.name
    locationCount = len(acc.get("locations",{}))
    type = acc.accountType
    Layout = acc.featureFlags.combinedProductsPage
    region = acc.region
    status = acc.get("status",{})


    print(f"{id},{name},{locationCount},{type}, {Layout} , {region}, {status}")
