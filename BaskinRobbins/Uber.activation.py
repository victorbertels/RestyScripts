import requests
account  = "630c507964ffb8c1f3b8bb7b"

query = pcli.channelLinks.list_all(q={"account" : account , "channel" : 7})

for i in query:
    channelLink = i._id
        

    
    url = f"https://api.deliverect.com/activateChannelLink/{channelLink}"
    print(url)
    payload={}
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjczNDQxMzMsImV4cCI6MTY2NzQzMDUzMywiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.qNapjN38nIJqcWkwnyMZB5xHAh3zwU_SonQ7hYkhJIEUQKwIQmpSW-rSfE8_SqzgqhZjy_7uKDGMGNwjXsSFg78vo0jQ1R9bAmqozLWWPTNjQr4nLjoFXDkKq9Zm7hpGFc16tbS3VoBAM4feL4V-jpahVNGtZqAWsN7atRZb3uFB13qhaOPF-YhF83ht1lvh6FCUw3BITC43rtwpleRDTMvXEQfx1-Z_2GRvWy3OTPshH-mGgUSnEFG_HuzB7LYopbzvx_aff4IgHDr87LMERE7wx3J-DI5ackVn7XIMYkoRLnuJoh8fPCdj5kjsBCdK_7qe1KDXzMs2QkSyIg8qSQ'
}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

