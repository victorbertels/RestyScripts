query = pcli.locations.list_all(q={
    "account" : "5d67c3f06f006f00012b83d1", "status" : "SUSPENDED"
})


for i in query: 
    status = i.status
    cl = i.channelLinks
    if status == "SUSPENDED":
        for c in cl:
            pcli.channelLinks.update(c,{
                "status" : 1
            })


 