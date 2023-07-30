import requests
import json
page = 1

url = "


ACCOUNT = "63290d3fdceae416df65c7e8"
TOKEN = "HIER-EEN-TOKEN"
HEADER = {"Authorization": f"Bearer {TOKEN}"}

updateCount = 0
for page in range(1, 1000):
    # Get 100 products (maximum is 500 but let's not kill the API).
    req = requests.get(f'https://api.deliverect.com/products?where={{"account": "{ACCOUNT}", "overloads": {{"$exists": true}}}}&max_results=100&page={page}&sort=_id', headers=HEADER)
    req = requests.get(f'https://api.staging.deliverect.com/v2/search/products?page={page}&query=burrito&locations=[%2264782ce83e59daecb7885c66%22]&itemTypes=[1]&account=64782cd8e8b4ff62b5cc207e&&max_results=25',headers=HEADER
    if not req.ok:
        raise RuntimeError(f"Welp: {req.text}")

    products = req.json().get("_items")
    if not products:
        print("Done!")
        print(f"Updated {updateCount} products")
        exit(0)

    # Go over the products.
    for product in products:
        # Store the overloads.
        overloads = product.get("overloads", [])

        # Go over the overloads.
        modified = False
        for overload in overloads:
            # If the overload has priceLevels filled in, we should set overrideSurchargeWithPriceLevels to True
            if overload.get("priceLevels") and not overload.get("overrideSurchargeWithPriceLevels"):
                overload["overrideSurchargeWithPriceLevels"] = True
                modified = True

        # If we modified anything, store the changes on the product.
        if modified:
            print(f"Updated {product['_id']}")
            updateCount += 1
            # requests.patch(f"https://api.deliverect.com/products/{product['_id']}", json={"overloads": overloads}, headers={**HEADER, "If-Match": product['_etag']})

print(f"Updated {updateCount} products")