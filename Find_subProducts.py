## Script to remove any lingering internal products not part of a mod group or bundle. 

# we get all the internal products from 1 account.
query = {'account' : '5f9147e1a94e333fef335737' , "isInternal": True}
internal_products = pcli.products.list_all(q=query)

# We get all the subProducts from Modifier group and bundle in 1 account
query2 = {'account' : '5f9147e1a94e333fef335737' , "isInternal": True , "productType": {"$in": [3, 4]}}
bundles_and_modG = pcli.products.list_all(q=query2)

subProds = bundles_and_modG.get('subProducts')
print(subProds)


for internals in internal_products:
    product_ids = internals.get('_id')
    #print(product_ids)
    print(subProds)


#bundle : B-ON-W1jf-2 -- 5f97f0e310875f2b2239cbc7
# modifier  : (305004#305006) -- 5f98417810875f2b22664d57


prods = pcli.products.list_all(q={"account" : "5f9147e1a94e333fef335737","subProducts": "6058d74850b4121695936cf8"})


parent_product_query = {'account' : '5f9147e1a94e333fef335737',  "subProducts": ["5fa0082254beb88ca42f9b7a"]}
internal_products = pcli.products.list_all(q=parent_product_query)

pcli.channelProducts.get('6058b3f850b4121695888e7f')

##
pcli.products.get('6058d754380fbf31451277e9')
subProducts: ['6058d754380fbf31451277e9', '6058d754380fbf31451277f4']


# B-EA-7Gk5-3