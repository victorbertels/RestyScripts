import requests

TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODgwMTA2ODIsImV4cCI6MTY4ODA5NzA4MiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.AoISHCaS03GYCyVPUTilOpHCfyRjq-HMQFwI69T5H-gLjtJfJc3kmwVyZrqd-V8f1_1grwaXzcgQey9Rx9Tv2AjrInIqBzZ3W8RjwBBXCXHdQy-miUHAUezHUN8-9kI1SUFjFKVBwbcmajWgOpCICLkt0X7mGDw1XhC04QsonjL4f7IGbxKf4NmKNh0gZ-Q-Ol35GQWTQYBY2p-564ERlKlCvrg3CRD4aC2_IGKjsmKHOJN8JpPKOrKrTZA-eRn1QhvuomxUFMZYMIY7FOu29IYdwvJR9K8Dk5SqJXt32FQqi9unVoLa8cSK1pId4Qvxxu5_F8CGJO6TPiBXB1MpFw"
HEADER = {"Authorization": f"Bearer {TOKEN}"}
pos = 25
accounts = ["5e7bbf7265013b00010cb6aa", "615e8f1f4875a94524fa9947", "5fe17b1effe9e99933f9f58a"]
updateCount = 0

for page in range(1, 1000):
    URL = f'https://api.deliverect.com/locations?max_results=5000&where={{"account":{{"$in":["5e7bbf7265013b00010cb6aa", "615e8f1f4875a94524fa9947", "5fe17b1effe9e99933f9f58a"]}}}}&max_results=100&page={page}&sort=_id'
    
    req = requests.get(url=URL, headers=HEADER)
    if not req.ok:
        raise RuntimeError(f"Error: {req.text}")

    locations = req.json().get("_items")
    if not locations:
        print("Done!")
        print(f"Found {updateCount} thieves")
        break

    # Iterate over the locations.
    for location in locations:
        # Store the details.
        name = location.get("name", [])
        account = location.get("account", [])
        location_id = location.get("_id", [])
        status = location.get("status", [])
        identifier = location.get("_id", [])
        sub = location.get("subscriptions", [])
        
        if not sub and status not in ("SUSPENDED", "INACTIVE"):
              
            account_str = ",".join(map(str, account))
            identifier_str = ",".join(map(str, identifier))
            print(account_str)
            print(identifier_str)
        
            ordersurl = f'https://api.deliverect.com/orders?page=1&cursor=new&where={{"account":{{"$in":[{account_str}]}},"location":{{"$in":[{identifier_str}]}}}},"_created":{{"$gt":"2023-06-01T14:00:00.000Z","$lt":"2023-06-29T13:59:59.999Z"}},"sort":"_created","max_results":25,"useFastCount":true'
            orderreq = requests.get(url=ordersurl, headers=HEADER)      
            print(ordersurl)
            print(orderreq)
            if orderreq:
            # print(sub, status, identifier)
                print(f"LocationId: {identifier}, name: {name}, with status: {status}, has no subscriptions: {sub} and is stealing the money")
                updateCount += 1