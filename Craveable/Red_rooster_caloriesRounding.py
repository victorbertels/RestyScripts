account = "5fe17b1effe9e99933f9f58a"


products = pcli.products.list_all(q={"account" :account})


for product in products:
    