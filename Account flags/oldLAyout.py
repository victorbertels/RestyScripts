query = pcli.accounts.list_all(q={"featureFlags.enableNewLayout":False}})


for acc in query:
    id = acc._id
    name = acc.name
    locationCount = len(acc.get("locations",{}))
    type = acc.accountType
    Layout = acc.featureFlags.enableNewLayout
    region = acc.region
    status = acc.get("status",{})


    print(f"{id},{name},{locationCount},{type}, {Layout} , {region}, {status}")
