ACCOUNT  = "63435e96e54f9c12e91c9745"

products = pcli.products.list_all(q={"account" : ACCOUNT, "posValues" :{"$exists" : True}})


for prod in products:
    try:
        subProdCount = len(prod.subProducts)
        posValuesCoiunt = len(prod.posValues.subProducts)
        # print(subProdCount,posValuesCoiunt , prod.plu)
        if posValuesCoiunt > subProdCount:
            print(prod.plu)
            pcli.products.update(prod,{
                "subProducts" : prod.posValues.subProducts
            })

    except:
        print("No Posvalues" , prod.plu)
    print(subProdCount,posValuesCoiunt)
    # if len(prod.subProducts) != len(prod.posValues.subProducts):
    #     print(prod.plu)



import requests

tkn = "here-be-your-token"

page = 1
while page < 600:
    print("PAGE", page)
    todo = requests.get(f'https://api.deliverect.com/products?where={{"account": "624f796288b904a46ab92175", "posValues.subProducts.0": {{"$exists": true}}, "subProducts.0": {{"$exists": false}}}}&max_results=500&page={page}', headers={"Authorization": f"Bearer {tkn}"})
    print(todo.json()["_meta"])

    for idx, p in enumerate(todo.json()['_items']):
        # Update the product.
        req = requests.patch(f"https://api.deliverect.com/products/{p['_id']}", json={"subProducts": p["posValues"]["subProducts"]}, headers={"Authorization": f"Bearer {tkn}", "If-Match": p['_etag']})
        print(idx, req, req.text)

    page += 1