acc = "637a26720128e9495824a1fd"


query = pcli.locations.list_all(q={"account" : acc})

for loc in query:
    pcli.locations.update(loc,{
          "posSystemId": 36

    })




clinks = pcli.channelLinks.list_all(q={"account" : acc})

for clink in clinks:
    print(clink.posSystemId)
    print(clink.posSystem)

    pcli.channelLinks.update(clink,{
        "posSystemId": 36,
        "posSystem": "NCR BSP",



})

