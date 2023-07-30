query = pcli.locations.list_all(q={'timezone' : "Australia/Sydney" , "posSystemId" : 13})



for i in query:
    print(i.account)
    print(i.name)
    print("-----------------")