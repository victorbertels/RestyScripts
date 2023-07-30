import datetime
from datetime import datetime, timedelta , date

import csv
account = "62fc44dc934376949a733248"


dt = datetime.now()
dt_string = dt.strftime("%Y-%m-%d___%H:%M:%S")
query_date = date.today()- timedelta(days=1)


allOrders = pcli.orders.list_all(q={"account" : account ,"channel" : 7,"_created":{"$gt":f"{query_date}T00:00:00.000Z" }})



with open(f'/Users/victorbertels/Desktop/KBOX/KBOX-ORDERCOUNT-{dt_string}.csv', 'w', newline='') as f:
    header = ['LocationName', 'ChannelLinkName', 'ChannelLink Id', 'OrderAmount' , "OrderStatus" , "orderDate" ]
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    for order in allOrders:
        print(len(order))
        clink = order.channelLink
        location = order.location
        status = order.status
        print(clink, location,status)

        for clink in location.channelLinks:
            clName = pcli.channelLinks.get(clink)
            ordersAmount = pcli.orders.list_all(q={"account": account, "channelLink": clink})
            for i in ordersAmount:
                status = i.status
                if status == 1:
                    len(i)
                print(len(i))
            orderTotal = len(ordersAmount)
            for order in ordersAmount:
                status = order.status
            writer.writerow({
                "LocationName" : name , "ChannelLinkName" : clName.name , "ChannelLink Id" : clink , "OrderAmount" : orderTotal  , "OrderStatus" : status , "orderDate" : query_date
            })
            print(f"LocationName : {name} , ChannelLinkName : {clName.name} , ChannelLink Id : {clink} , OrderAmount : {orderTotal}, OrderStatus : {status}")




