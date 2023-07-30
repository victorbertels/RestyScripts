import requests
import json



allAcc = ["5e7bbf7265013b00010cb6aa","5fe17b1effe9e99933f9f58a","615e8f1f4875a94524fa9947"]
locations = pcli.locations.list_all(q={"account" : {"$in" : allAcc}})


for location in locations :
    etag = location._etag
    url = f"https://api.deliverect.com/locations/{location._id}?propagate=all&override=true"
    payload = json.dumps({
    "posSettings": {
        "simphony": {
        "anonymizeCustomer": True
        }
    }
    })
    headers = {
    'If-Match': f'{etag}',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjY2NjQzMzMsImV4cCI6MTY2Njc1MDczMywiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.k6wekUZaO_vPjte19vWoe1pI9nlIqbd0H7lPQK5wH8M4H6Xll8VIIsz7cSYCdJycP4AdO4V8SlE9mbQEoeFL2xzGifWp14gorIozv2TYHvPNjJ4-fdjVgj6XbKATUNRLaw7cNk6aNIKrCO-V_o44RI8wovznsW-HNuA9pPYFTxvJG3PpiuPBGNNWlysOMNa6pmmZq-YuOIziCnSXpzprbR4mMGOq7PaCsbwIMPcXApGU7y9OA_mCjpdNgkA3SP0PfxTFwaUD3KExLXwBRMbt90jwzKC6kEfVswHyXvgIq7wRXigM_i7kW-8oybwPHmjG4MOHrAvPAQjOIO8M0Kc8UA',
    'Content-Type': 'application/json'
}

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.text)
