import requests
import json
account_id='630c507964ffb8c1f3b8bb7b'
locations = pcli.locations.list_all(q={"account" : account_id})

for loc in locations:
    print(loc._id , "**--**" , loc.name)

location_list=[
"631dc62871c3a68d02022e86",
"630eaa649a14616b9c9d2c34",
"630eaa649a14616b9c9d2c2e",
"630eaa649a14616b9c9d2c0a",
"630eaa649a14616b9c9d2c04",
"630eaa649a14616b9c9d2bfe",
"630eaa649a14616b9c9d2bf8",
"630eaa649a14616b9c9d2bf2",
"630eaa649a14616b9c9d2bec",
"630eaa649a14616b9c9d2be6",
"630eaa649a14616b9c9d2be0",
"630eaa649a14616b9c9d2bda",
"630eaa649a14616b9c9d2bd4",
"630eaa649a14616b9c9d2bce",
"630eaa649a14616b9c9d2bc8",
"630eaa649a14616b9c9d2bc2",
"630eaa649a14616b9c9d2bbc",
"630eaa649a14616b9c9d2bb6",
"630eaa649a14616b9c9d2bb0",
"630eaa649a14616b9c9d2baa",
"630eaa649a14616b9c9d2ba4",
"630eaa649a14616b9c9d2b9e",
"630eaa649a14616b9c9d2b98",
"630eaa649a14616b9c9d2b92",
"630eaa649a14616b9c9d2b8c",
"630eaa649a14616b9c9d2b86",
"630eaa649a14616b9c9d2b80",
"630eaa649a14616b9c9d2b7a",
"630eaa649a14616b9c9d2b74",
"630eaa649a14616b9c9d2b6e",
"630eaa649a14616b9c9d2b68",
"630eaa649a14616b9c9d2b62",
"630eaa649a14616b9c9d2b5c",
"630eaa649a14616b9c9d2b56",
"630eaa649a14616b9c9d2b50",
"630eaa649a14616b9c9d2b4a",
"630eaa649a14616b9c9d2b44",
"630eaa649a14616b9c9d2b3e",
"630eaa649a14616b9c9d2b38",
"630eaa649a14616b9c9d2b2c",
"630eaa649a14616b9c9d2b26",
"630eaa649a14616b9c9d2b20",
"630eaa649a14616b9c9d2b1a",
"630eaa649a14616b9c9d2b14",
"630eaa649a14616b9c9d2b0e",
"630eaa649a14616b9c9d2b02",
"630eaa649a14616b9c9d2afc",
"630eaa649a14616b9c9d2af6",
"630eaa649a14616b9c9d2af0",
"630eaa649a14616b9c9d2aea",
"630eaa649a14616b9c9d2ae4",
"630eaa649a14616b9c9d2ade",
"630eaa649a14616b9c9d2ad8",
"630eaa649a14616b9c9d2ad2",
"630eaa649a14616b9c9d2acc",
"630eaa649a14616b9c9d2ac6",
"630eaa649a14616b9c9d2ac0",
"630eaa649a14616b9c9d2aba",
"630eaa649a14616b9c9d2ab4",
"630eaa649a14616b9c9d2aae",
"630eaa649a14616b9c9d2aa8",
"630eaa649a14616b9c9d2aa2",
"630eaa649a14616b9c9d2a9c",
"630eaa649a14616b9c9d2a96",
"630eaa649a14616b9c9d2a90",
"630eaa649a14616b9c9d2a8a",
"630eaa649a14616b9c9d2a84",]
location_list_2 = [

"630eaa649a14616b9c9d2a78",
"630eaa649a14616b9c9d2a72",
"630eaa649a14616b9c9d2a6c",
"630eaa649a14616b9c9d2a66",
"630eaa649a14616b9c9d2a60",
"630eaa649a14616b9c9d2a5a",
"630ea91a69bcd44f1f566847",
"630d5a46d4ac393ee3e4769a",
]



for loc in location_list_2:
    loc_name = pcli.locations.get(loc).name
    url = f"https://api.deliverect.com/v1/tunnel/630c507964ffb8c1f3b8bb7b/{loc}"
    payload={}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjYyMjU1ODcsImV4cCI6MTY2NjMxMTk4NywiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.TAO0J17KbqfYNyX6BAYxI5WRXL6liQeQBOg5js_vVf2yhZc4-tME-z5QENWeOCnGoT_5Y_Sb8HvnLF-nsA9p2UVA_6ewI94HrkaTU1i_XDgXsH2WJFg6ovmKyFjVMOYYDP_YNDIffOlkYcQIfJcGf0g9SXthBIRHuXAeK244IaeR4ERGCD11qau_1GWC98xEw90IMoUx9F_abAfIeGC7s-QqKym51q73IYFRp3otGHwUZmJfUxaZPT3b6F7ZntZU4SFvCosm7N2JBSW1Ki6N8X6Kyt-J1DOWi2oShSHuyayftOc2BiUfiCbP6rNUBqhhUNWRG4NUfEw6qxvt50TJXA'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jsonresponse = response.json()
    token = jsonresponse.get("token")
    location_name = loc_name
    location_id = jsonresponse.get("tunnel")["location-id"]
    url = jsonresponse.get("tunnel")["domain"]
    constructed_url = "https://" + str(url) + ".tunnel.deliverect.com/MDProxyWebService/MDProxyService.asmx?wsdl"
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print(location_name)
    print(location_id)
    print("token: ", token)
    print(constructed_url)

