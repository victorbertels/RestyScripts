import requests
import json

prodWCalories = pcli.products.list_all(q={"account" : "63290d3fdceae416df65c7e8" ,"location" : "63290d6ccb9d7fad3380c74d" ,"calories" : {"$exists" : True}})
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2Nzk5NTc1MzMsImV4cCI6MTY4MDA0MzkzMywiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.jVZkGIDSpjsdzryYEbSxaPCmX-6qvO4vb_MBnuG5CwEuGnVOXwCV1zgwDmWF1CGaNqaH8Ukrn9Ux6WDe6hbxR5nelZTrFx19199aO4WJlAWEmpiACN2cY4f92udCHjRUgiDexGUjWND__RTX_uNS4SY4YhN49vw2knxcqn5CwVTTYzV78lZ3C_69a8nxuO-k2GakJdNW7QGFLLe5OUXGdladIKTKOdBdc1DNnbyitNcu5dpNiWjfgtrkDFAQncpkvHbLOrDrWPATqG-qX-aCP4ihzYvE0jqDbkGB8XlKjCfKinKrJNFso09eykHrj9ZfLbx1hfeg_0sHVI3-HgwiTA"
for prod in prodWCalories:
    plu = prod.plu
    calories = prod.calories
    print(plu , calories)
    etag = prod._etag
    url = f"https://api.deliverect.com/v3/products/63290d3fdceae416df65c7e8/{plu}"
    payload = json.dumps({
            "kJ": calories
})  
    headers = {
  'If-Match': etag,
  'Authorization': f'Bearer {token}',
  'Content-Type': 'application/json'
}
    

    req = requests.request("PATCH", url, headers=headers, data=payload)
    print(payload)
    print(req)