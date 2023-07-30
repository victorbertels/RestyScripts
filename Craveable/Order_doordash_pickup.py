orders = pcli.orders.list_all(q={"account" : "5e7bbf7265013b00010cb6aa" , "location" : "60bf8f0d380a86ba6660afdc" ,"channel" : 12 ,"orderType" : 1 ,"_created" : {"$gt":"2022-06-20T00:00:00.000Z"} })



for i in orders: 
    print(i.courier)
    print(i.channelOrderDisplayId)
    print(i._created)
    print("--------")