import requests
import json

token = ""
url = "https://api.deliverect.com/productAndCategories"

payload = json.dumps({
  "accountId": "624f796288b904a46ab92175",
  "locationId": "6268ce08e97401166b98ccd1",
  "products": [
    {
      "productType": 1,
      "plu": "PR03",
      "price": 900,
      "name": "Cheese Lovers Pizza",
      "posProductId": "INTERNAL-POS-ID-1",
      "posCategoryIds": "INTERNAL-POS-CAT-2",
      "imageUrl": "https://www.stockvault.net/data/2009/07/20/109569/preview16.jpg",
      "description": "Pizza made for cheese fanatics",
      "deliveryTax": 6000,
      "takeawayTax": 6000
    }
  ]
})
headers = {
  'Authorization': f'Bearer {token}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
