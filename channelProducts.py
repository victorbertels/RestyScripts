menu = "611621caafd91840c41b35c0"
account = "60f1607e857fdbecd63580ff"
plu = "40FjsJBObMIGhEs0Qnqy"

#find Channel Prods
#channelprods = pcli.channelProducts.list_all(q={"account" : account , "menu" : menu,'productType' : 1})


#get 1 CP
getDeliverect_ID = pcli.products.list_all(q={'account':account, 'plu' : plu})
channelprods = pcli.channelProducts.list_all(q={"account" : account , "menu" : menu,"deliverectProductId" : "60f165f5510fb903bf50a0d3"})

for i in channelprods:
    print(i)


