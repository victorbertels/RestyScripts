import requests
import json
account = "61df8c560706d58e1016f00d"
menu = "62eb2f8c5b9f185610b2d293"
category = "6392b2cf9102060a1c343c63"
location_ids = pcli.locations.list_all(q={"account" : account})
for ids in location_ids:
    id = ids._id
    print(id)
    payload =json.dumps([{
        "startTime":"06:00",
        "endTime":"20:00",
        "dayOfWeek":2,
        "location":f"{id}",
        "menu":menu,
        "account":"61df8c560706d58e1016f00d",
        "category":category
    },
    {
        "startTime":"06:00",
        "endTime":"20:00",
        "dayOfWeek":1,
        "location":f"{id}",
        "menu":menu,
        "account":"61df8c560706d58e1016f00d",
        "category":category
    },
    {
        "startTime":"06:00",
        "endTime":"20:00",
        "dayOfWeek":3,
        "location":f"{id}",
        "menu":menu,
        "account":"61df8c560706d58e1016f00d",
        "category":category
    },
    {
        "startTime":"06:00",
        "endTime":"20:00",
        "dayOfWeek":4,
        "location":f"{id}",
        "menu":menu,
        "account":"61df8c560706d58e1016f00d",
        "category":category
    },
    {
        "startTime":"06:00",
        "endTime":"20:00",
        "dayOfWeek":5,
        "location":f"{id}",
        "menu":menu,
        "account":"61df8c560706d58e1016f00d",
        "category":category
    },
    {
        "startTime":"06:00",
        "endTime":"20:00",
        "dayOfWeek":6,
        "location":f"{id}",
        "menu":menu,
        "account":"61df8c560706d58e1016f00d",
        "category":category
    },
    {
        "startTime":"06:00",
        "endTime":"20:00",
        "dayOfWeek":7,
        "location":f"{id}",
        "menu":menu,
        "account":"61df8c560706d58e1016f00d",
        "category":category
    }
    ])
    url = "https://api.deliverect.com/menuAvailabilities"
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NzA1NDgxODEsImV4cCI6MTY3MDYzNDU4MSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.NDHVzmZiCQyCtS7hV6_AgMR5gpietMWrtASGxbhkK5I7Jh0moHdO-GZtC6eSA17OkfjXpBtmNTzh-q9InYe6_q5ZJkqma49LiNMkKGk03h6D2D2JrU1MVE2cxSWJEY8TodpJWexvi1qx8hWpEO6gZ21qFnmubwz4E6ooDt0OJb9t-IuXD-VyTiahopqXPEBGA2AeKB48kCQAwaiaiuKk8SiukZ6YTEnSXqAhaUxL8RNjrt2xOD48Gfb5maZ4AjZtYlCSdTICNzmW8H1zkQ8y9cxtK6W5w2Bb0Sq72OrMjszkZBdGNWkr8xEzyBjmx_gmBmk-TxmyvDbuRyjoUHzTCw',
  'Content-Type': 'application/json'
}
    response = requests.request("POST", url, headers=headers, data=payload)


    print(response.text)
