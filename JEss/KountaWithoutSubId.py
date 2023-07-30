import requests

TOKEN = "PUT YOUR DELIVERCT TOKEN HERE"
HEADER = {"Authorization": f"Bearer {TOKEN}"}
pos = 25

updateCount = 0
for page in range(1, 1000):
    URL = f'https://api.deliverect.com/locations?where={{"posSystemId":{pos}}}&max_results=100&page={page}&sort=_id'
    req = requests.get(url=URL, headers=HEADER)
    if not req.ok:
            raise RuntimeError(f"Help: {req.text}")

    locations = req.json().get("_items")
    if not locations:
        print("Done!")
        print(f"Found {updateCount} thieves")

        break

    # Go over the products.
    for location in locations:
        # Store the overloads.
        status = location.get("status", [])
        id = location.get("_id", [])
        sub = location.get("subscriptions", [])
        if not sub and status != "SUSPENDED":
            # print(sub , status , id)
            print(f"LocationId: {id} with status {status} , has no subs {sub} and is stealing da money")
            updateCount += 1


