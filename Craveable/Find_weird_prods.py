allAcc = "63290d3fdceae416df65c7e8"

query = pcli.products.list_all(q={"account" : allAcc,"productType" : {"$in" : [3,4]}})
for i in query:
  _min = int(i.min)
  _max = int(i.max)
  amount_of_subProducts = len(i.subProducts)
  if _min > amount_of_subProducts:
    print(i.plu , i._id)