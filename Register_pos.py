import requests
import json

url = "https://humpback.ordermatecentral.com/HumpBack/webservices/drect/v1/register"

payload = json.dumps({
  "accountId": "61e92784cd8c5150ce3c56e8",
  "locationId": "61e928470fd3096c884a0897",
  "externalLocationId": "2963"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
