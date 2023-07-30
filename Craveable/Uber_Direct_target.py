query = pcli.locations.list_all(q={  "region": "AUS",
})

CL = []
for i in query:
    try:
        if i.channelLinks:
            print(i.channelLinks)
            try:
                get_cl = pcli.channelLinks.list_all(q={"_id" : {"$in" : i.channelLinks}})
                for cl in get_cl:
                    if cl.channel == 30:
                        CL.append(cl.account)
                        print("oo found")
            except:
                print("no CL there")
    except:
        print("shit")


print(CL)

acc = pcli.accounts.list(q={"_id" : {"$in" : CL}})
for ac in acc:
    print(ac.name)


acc_query = pcli.accounts.list_all(q={  "region": "AUS",
})

CL2 =[]
for account in acc_query:
    try:
        if account.locations:
            try:
                get_locs = pcli.locations.list_all(q={"_id" : {"$in" : account.locations}})
                try:
                    for loc in get_locs.channelLinks:
                        get_cls = pcli.channelLinks.list_all(q={"_id" : {"$in" : loc}})
                        for cls in get_cls:
                            if cls.channel == 30:
                                CL2.append(cls.account)
                                print(cls._id)
                                print("--------------------------------------------------------")
                except:
                    print("shit")
            except:
                print("double shit")
    except:
        print("triple shit")

print(CL2)

