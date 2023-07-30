#list of UUID from Oliver 
remove_uuid = [
"b3ab0467-3393-505d-a5da-5c789bf70041",
"2ea9d4d2-58a1-5e03-8d97-a1705f711315",
"04c6d9e1-3a94-5755-a331-75de359099f0",
"8149badc-403c-54d0-85e5-a68ac17975fe",
]


# step 1 get the channel link id
channelLink = pcli.channelLinks.list_all(q={"channelSettings.storeId" : {"$in" : remove_uuid}})
CLID = []
map_list = []
#step 2, create a list with the CL ID 
for cl in channelLink:
    print(cl._id)
    CLID.append(cl._id)
    mapping = cl._id + " *_* " + cl.channelSettings.storeId
    map_list.append(mapping)
map_list


# step 3 , call uber to close the stores 
import requests
for id in CLID:

    url = f"https://api.deliverect.com/disableChannelLink/{id}"
    print(url)

    payload = ""
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NTYzOTc4NjEsImV4cCI6MTY1NjQ4NDI2MSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.cFqYdHXbS7zV94IsO6gHWd7ucxfCGQy8Psf-XkI1SL052SF9voMUKecS5tMTym59PfAR8zYgLgaQPyaaK37wZp1ENHv9qWMWtGAZJpT0JXyIyNlVPYuFo_2qlZcZFGvFOcfZodS1sASbR8gE-7kUb_kjrnI6cUyeCmASBLjm9r1Tc5lVuL1j-pkekyq_yOoPAgiqLrc3WNvF1X_mV420paBCzL1yAz96bI8I5gEoKsYEBiSMgXvJASiKjUJ7Yg1mxGJJhecOn7dhuS5XLWAJCgcEW-K3m461pDotROQ4vwKOxWPJRPotK7JsEl65JNfVS1DPKP9WyE7VVddzE4eCRg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

#step 4 : patch the channel Link with an empty store ID.

for cl in channelLink:
    pcli.channelLinks.update(cl,{
        "channelSettings.storeId" : "removed"})