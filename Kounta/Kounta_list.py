query = pcli.accounts.list_all(q={"posSystem": 25})
acc = pcli.accounts.list_all(q={"_id" : "60dbaf617159694a572f3883"})

for kountas in query:
    pcli.accounts.update(kountas,{
        "featureFlags": {
            "enableNewLayout": True},
        "deliverectVersion": "2.0"

    })
    try:
        newLayout = kountas.featureFlags.enableNewLayout
        version = kountas.deliverectVersion
        if version != "2.0":
            print(kountas.name)

    except:
        print("dont hav that")
        

for kountas in acc:
    try:
        newLayout = kountas.featureFlags.enableNewLayout
        version = kountas.deliverectVersion
        if version != "2.0":
            print(kountas.name)

    except:
        print("dont hav that")