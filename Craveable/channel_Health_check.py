import requests

redRooster = "5fe17b1effe9e99933f9f58a"
oporto = "5e7bbf7265013b00010cb6aa"
supported_channels = [2,7,12]
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NTUyNDg2NzksImV4cCI6MTY1NTMzNTA3OSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.HrFZMKY39v-Q5oxJM3vv7qCWGKoEsJq-DU1tfwqJmb_UAycLI_emxMi6tTR88Zmy4OuCVqZI3QdOr7oKPwCMJhgtDkxuRzcQ9yIbUbI7vsn7R85D74gAW3KiyePY7WdFmb_Vwjl5Sbkws9pP1PCwPLrNh4C7de8d58PGFsy7kGnoTS_Mww4LNeaCLa3cXnfdzbNxJwSsECE5UWKFvY1RMgYh5cCRSCZxH0DFnfcaWvvzEv_Y_oKIWv9-Jqw2hIMS2T0A6742zubv9CxbYIUvWxjxv57u147ivgccau79suVpJMYzHvI22SSMyAc4TOrQMXR6wQ-bRUcNG2LVgYufsw"

redRooster_cl = pcli.channelLinks.list_all(q={"account" : redRooster, "channel": {"$in" : supported_channels} })
oporto_cl = pcli.channelLinks.list_all(q={"account" : oporto,"channel": {"$in" : supported_channels}})

redRooster_list = []
oporto_list = []

for red in redRooster_cl:
    CLID = red._id
    channel = red.channel
    redRooster_list.append(CLID)

for op in oporto_cl:
    opCLID = op._id
    channel = op.channel
    oporto_list.append(opCLID)

print(redRooster_list)
print(oporto_list)


for cl in redRooster_list:
    url = f"https://api.deliverect.com/channelLinks/{cl}/health"



for chan in oporto_list:
    url = f"https://api.deliverect.com/channelLinks/{chan}/health"
    payload={}
    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    print(f"channelLink : {chan}",response.text)
    
    if response.ok:
        jsonResponse = response.json()
        pos_integration = "Enabled" if jsonResponse.get("pos_integration_enabled") else "Disabled"
        order_release = "Enabled" if jsonResponse.get("order_release_enabled") else "Disabled"
        print(f"Order integration is {pos_integration} , Order Release is {order_release} for this {uuid}")
    
    
    else:
        print(response.text,"for UUID: ",uuid)
    



