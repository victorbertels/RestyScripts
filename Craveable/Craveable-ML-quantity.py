import json
import requests

url = "https://api.deliverect.com/jsonMenuPreview"
payload = json.dumps({
  "menus": [
    "630c051aa105853f898c5f07"
  ],
  "channelLink": "63fd6add08e9704f09b12960"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2ODU0MDI3OTMsImV4cCI6MTY4NTQ4OTE5MywiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.GaQPAlSqm7BtMaQbdrdPO9MutKq_HeaYSt0XSesiOjvfb-Dpt1jMDAtNbfHvMBZcD-axtBTZmwaTXUv5pXLqzfa8TN1e3z7VzrUzjshhgHpSyauTH0x8Vx3WVfy7i9gK6cRPl249Is78ip1I1kNLkz2g6Hcpg7ENKnE0XCrt6Ouza4cDT_3Gdw3p9COng6z_3yLAFm4FjSwBjGCg3yC8cnGlkqUGaw7IRZo--_Hyyn1S2CE9_YyRtP54BsSvx5GXg27qmb91tqhGEOnvUCOCmeD7FnR4aZ9K5hA1nkQ-rpjbolYxA8Fcse_10UoyhuUGg5kTeSAf6YVI2mtPBsQ6Qg',
  'Content-Type': 'application/json'
}

menulogJson = requests.request("POST", url, headers=headers, data=payload).json()
# print(menulogJson)

for menu in menulogJson["menus"]:
    categories = menu.get("categories")
    for category in categories:
        products = category.get("items")
        for product in products:
            modifiers = product.get("modifiers")
            for modifier in modifiers:
              # print(modifier)
              pick = modifier.get("pick", {})
              min = pick.get("range", {}).get("from", 0)
              exactly = pick.get("exactly", 0)
              options = len(modifier.get("options"))
              # print(f"{min}, {exactly} and {len(modifiers)}")
              if min > options:
                  print(f"{modifier['name']} has minimum {min} greater than {len(modifiers)}")
              if exactly > options:
                  print(f"{modifier['name']} has exactly {exactly} greater than {len(modifiers)}")
