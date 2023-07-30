theCloud = pcli.locations.list_all(q={'account' :"6017e71bcb8a91b4944db5fe","posSettings.generic.ordersWebhookURL":{"$exists":True}})

for i in theCloud:
  if i.posSettings.generic.ordersWebhookURL != "https://dashboard.thecloud.ae/webhook/Deliverect/fetchOrder.php":
    pcli.locations.update(i,{
      "posSettings.generic.ordersWebhookURL" : "https://dashboard.thecloud.ae/webhook/Deliverect/fetchOrder.php"
    },override = 1, propagate = 'all'
    )

