account = "615e8f1f4875a94524fa9947"

locs = pcli.locations.list_all(q={"account" : account })


for loc in locs: 
    # print(loc.name[-6:])
    if loc.name[-6:] == "CLOSED":
        pcli.locations.delete(loc)
        print(loc.name)