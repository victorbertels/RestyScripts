query = pcli.orders.list_all(q={"account" : "62b00ab0c843643ddb6f1aca" , "_created":{'$gte':"2022-11-08T02:14:00.403000Z"}})


for order in query:
  orderId = order._id
  
  pcli.call(f'/v1/deliverect/generateEtag/operationReports/638577e8fc3802d7d6924c5a', 'POST')


