accounts = ["5fe17b1effe9e99933f9f58a","5e7bbf7265013b00010cb6aa"]



timezones = pcli.locations.list_all(q={"account" : {"$in" : accounts}})

for zone in timezones:
    loczone = zone.timezone
    # print(loczone)
    # print(zone.timezone)
    channelLinks = zone.channelLinks
    for channel in channelLinks:
        get_cl = pcli.channelLinks.get(channel)
        id = get_cl.get("_id")
        clZone = get_cl.get("timezone")
        # print(clZone)

        if loczone != clZone:
            print(f"I have found location: {zone._id} , with timezone {loczone} , where CL {id} , has timezone {clZone}")
            print(f"updating {id} , to timezone {loczone}")
            pcli.channelLinks.update(channel, {
                "timezone": loczone,
                 "posSettings": {
                    "simphony": {
                        "timeZone": loczone}}

        
            })
            # print(loczone)
            # print(get_cl)




import requests
import json

accounts = ["5fe17b1effe9e99933f9f58a","5e7bbf7265013b00010cb6aa"]



timezones = pcli.locations.list_all(q={"account" : {"$in" : accounts}})


for zone in timezones:
    etag = zone._etag
    headers = {
  'Content-Type': 'application/json',
  'If-Match' : zone._etag,
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTAxNTQyNjcsImV4cCI6MTY5MDI0MDY2NywiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.g6y9I3r9xVQh9Ge_STJPvMs2F-Lkp7sqyStUznqg64PJ1rejq07uWrGjouS0-gHKSTxmfoxqZEqq1ni6kKfjoBbyAzAhrFW5b9JnDby44az1yipNvgvoLndhErnLt_yN6NTJQ6hr2OIXtlb2Twibw9nJvKHbqFN_YaWagCuDeEPA_WDbq3om6xWZs0uTI-UokMJZSEmOQ80HFl_BAOoUvE3d4G_YdHtu8PC_oLkVSjPHffc-Jyqk2rUszgbzZhA0LDJ-REWabLre2Sleuc2i5aTtd0CbfgwFDVT6o0W1uP7JSlDWFpVIhEIriAIZ7oQ12HahPULBEFf4abfHzo7OOg'
}
    locationId = zone._id
    timezone = zone.timezone
    url = f"https://api.deliverect.com/locations/{locationId}?propagate=all&override=true"
    payload = json.dumps(
        {"timezone":timezone}
    )
    print(url)
    print(payload)
    response = requests.request("PATCH", url, headers=headers, data=payload)
    print(response.status_code)
    print(response)