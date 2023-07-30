modgroupplu = "44FF3QUC2X2GSOCMXVQIR4FG"

subProducts = []

subProducts = pcli.products.list_all(q={"plu" : modgroupplu , "account" :"5eb08b2b87b1bf0001c3b292","location" : "62ce4ed1ca26867c33eee605"})
query = pcli.channelProducts.list_all(q={"plu" : modgroupplu , "account" :"5eb08b2b87b1bf0001c3b292","menu" : "63cf62cff57775aa5b694f0d"})


for subProduct in subProducts:
    subs = subProduct.subProducts
    for sub in subs:
        getPLUs = pcli.products.list_all(q={'_id': sub})
        for plu in getPLUs:
            subProducts.append(plu.plu)
            print(plu.plu)

            print(subProducts)