import requests
import json





ChickenTreat_products = pcli.products.list_all(q={"account" : "63290d3fdceae416df65c7e8" ,"location" : "63290d6ccb9d7fad3380c74d", "productType": 1 ,"calories" : {"$exists" : True}})

for product in ChickenTreat_products:

    plu = product.plu
    etag = product._etag
    KiloJoules = product.calories
    KiloJoulesToCalories = round(KiloJoules / 4.184 )
    # print("KiloJoules:",KiloJoules)
    # print(product.plu)
    # print("Calories ",KiloJoulesToCalories)
    # print(product.name)
    # print(product.calories)
    # print(product.plu)
    # print("------------------------------------------")
    url = f"https://api.deliverect.com/v3/products/63290d3fdceae416df65c7e8/{plu}"
    payload = json.dumps({
                            "calories": KiloJoulesToCalories
                            })
    headers = {
  'If-Match': 'fdsafdsa',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODU0ODkyMzIsImV4cCI6MTY4NTU3NTYzMiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.EtCl3of8-w5jOkewfBeRpQ05D1H1Pbeo794hmJ45Ki567amGWk4YhtjzJcVagfEJcBuOzU965zzD6e9Pdcee4UhXMTIOIPY2JGYSdSMJ8V96MNBvL4jsY30DeLXFv8oUb-IZ_G5KNBsp8VsUA2OXYz9jYxalqvHOA14o_5xgh43y4_U6JunSc2xqQLf8uSPr26bXVMRKIw0Ch2VjQe-Ws7V5nbs-xPCM0W7RZCX0Xq1Kt5I7HWbstrxlQoRThcuAmwi7az-tB9AtxTwbd35ZIOpJMgdGylkW4M-bfUYYWad1VKzF2dEm0uvAZfpT8ynBARz_Tf4kINgyr8tZjwhrnA'
}

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.status_code)

        
