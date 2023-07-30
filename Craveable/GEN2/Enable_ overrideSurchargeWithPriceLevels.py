import requests

ACCOUNT = "63435e96e54f9c12e91c9745"
LOCATION = "641a44cc7ccad44aefcda1ec"
TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2Nzk0NDM3MDYsImV4cCI6MTY3OTUzMDEwNiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.iytsqUd8zqeE2Dw4Wi4quBwpGD8RKr0TeNkWgsm-wLB_9HSo2pYMYtH4Au07E0AD3tCydQQOVe16JS7mTlc_cp3vN5zQphkl6VVGfBmM6MvKdsHzgP3RIlfLKrp6uLgATbomn8_5a4qI9KCNPgmNbEudRu6nUpw073wRBw2_t_SS03FhmhxZdyQREVPywpucKZ5AbuO3s6S5LwTWfwGuEJNeliuAQaBLplZt9loukaFeqe2V5cHl4wSWkVRI4r6EZZ9fzLdXeFXogtS2CxC0mxWp46NSub3QFPcKbT7EjS-jwfTsMVTz0e8pcDpg8g0vB_diPXOg6JzTvvtSxXxlag"
HEADER = {"Authorization": f"Bearer {TOKEN}"}

updateCount = 0
for page in range(1, 1000):
    # Get 100 products (maximum is 500 but let's not kill the API).
    req = requests.get(f'https://api.deliverect.com/products?where={{"account": "{ACCOUNT}","location": "{LOCATION}","overloads": {{"$exists": true}}}}&max_results=100&page={page}&sort=_id', headers=HEADER)
    if not req.ok:
        print("broken")
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
            if overload.get("priceLevels"):
                print(overload.get("priceLevels"))
            # If the overload has priceLevels filled in, we should set overrideSurchargeWithPriceLevels to True
            if overload.get("priceLevels") and not overload.get("overrideSurchargeWithPriceLevels"):
                overload["overrideSurchargeWithPriceLevels"] = True
                modified = True
            # print(overload)
        # If we modified anything, store the changes on the product.
        if modified:
            print(f"Updated {product['_id']}")
            updateCount += 1
            # requests.patch(f"https://api.deliverect.com/products/{product['_id']}", json={"overloads": overloads}, headers={**HEADER, "If-Match": product['_etag']})

print(f"Updated {updateCount} products")




