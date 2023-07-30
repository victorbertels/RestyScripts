import datetime
from datetime import datetime, timedelta , date

import csv
account = "62fc44dc934376949a733248"

locations = pcli.locations.list_all(q={"account" : account , "_id" : {"$in" :["631e66ffab0801315bd439b8"]}})

dt = datetime.now()
dt_string = dt.strftime("%Y-%m-%d___%H:%M:%S")
query_date = date.today()- timedelta(days=1)




with open(f'/Users/victorbertels/Desktop/KBOX/UUID_EXPORT-{dt_string}.csv', 'w', newline='') as f:
    header = ['LocationName', 'ChannelLinkName', 'ChannelLink Id', 'UUID']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    for location in locations:
        name = location.name
        for clink in location.channelLinks:
            clName = pcli.channelLinks.get(clink)
            ordersAmount = pcli.orders.count(q={"account": account, "channelLink": clink ,"_created":{"$gt":f"{query_date}T00:00:00.000Z"}})
            if ordersAmount:
                get_status = pcli.orders.list_all(q={"account": account, "channelLink": clink ,"_created":{"$gt":f"{query_date}T00:00:00.000Z"}})
                for order in get_status:
                    orderStatus = order.status  
                    if orderStatus == 1:
                        orderAmount = len(order)
                        print(orderAmount)
                    print(orderStatus ,order.channelLink)

            else:
                print("no orders")
            
            

            # print(orderTotal)
            # for order in ordersAmount:
            #     status = order.status
            # writer.writerow({
            #     "LocationName" : name , "ChannelLinkName" : clName.name , "ChannelLink Id" : clink , "OrderAmount" : orderTotal  , "OrderStatus" : status , "orderDate" : query_date
            # })
            # print(f"LocationName : {name} , ChannelLinkName : {clName.name} , ChannelLink Id : {clink} , OrderAmount : {orderTotal}, OrderStatus : {status}")




