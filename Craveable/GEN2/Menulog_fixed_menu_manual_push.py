import requests
import json

url = "https://api.flytplatform.com/menus"

payload = json.dumps({
})


headers = {
  'X-Flyt-API-Key': 'hdgskuPbIIkAKyLAaJyiSTQpQcVOxFtfVVmQc',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
