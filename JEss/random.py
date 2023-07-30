import requests


# response = requests.get("http://www.boredapi.com/api/activity?participants=1")
response = requests.get('https://api.github.com')

print(response)
