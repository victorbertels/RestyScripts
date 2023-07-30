unilevers = pcli.channelLinks.list_all(q={"account" : "619df81f91d30c8217b5c62e" , "channel" : 7})
ClId = []

for uni in unilevers:
    ClId.append(uni._id)

print(ClId)


import requests
import json


# Bulk activate CL's

for Cl in ClId:
    url = f"https://api.deliverect.com/activateChannelLink/{Cl}"
    print(url)
    payload = ""

    headers = {

    'Authorization': 'Bearer JA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAHQAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAApAAAABwAAAAEAAAAEAAAANGs9dffIe4h2RC8V9zsr8-AAAAAcNHMxswQhvME0M6xoiUZLb_gW_nibnWr2tyRHWLXEFL7Ql_mXCrmlUzsne0ulen_eHWyrXl7Jj3zBWvUrDeCb79OOjlwpuvscUHoleheAu4jw7wDVAiGJ84q1uvdorefPtvowtLtsNb0qddommv-v2A-Ye9HOf75EbCDpCGzAW4MAAAA-KBLneRZvcF492nMJAAAAGIwZDg1ODAzLTM4YTAtNDJiMy04MDZlLTdhNGNmOGUxOTZlZQ',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text,"is activated again" ,Cl)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Bulk deacticate CL
import requests
import json
# Bulk activate CL's

for Cl in ClId:
    url = f"https://api.deliverect.com/disableChannelLink/{Cl}"

    payload = ''
    headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NzgzNjUzODYsImV4cCI6MTY3ODQ1MTc4NiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.oJ582Iy81xP-fKRztVq8rboYglNtQt_hmiqCFWMMo3IUqI4MfN9WK-yk1HjLPyS8LHSNmOo3yRH43fdb9eBBSFDhYI4DimtQ9GtupGw9j0-7m3BR3PMpbG66CEVE1jYp1G1LhbaPj_K0YenxPTxQv4inQjX6XdhYzjcvAuDpVpahuLt72TOz53q0zGEQawS2C5QMWF-uP0-wfefaHHzsvhPGKs2rbvzbzKSlM6-6GdtDprOhvdB0tNpeHNSbpNH_6alBrwMKL4lj_1TyOjFRitBTutq5_6HZvYL7w8kwXcKWGaE3GQsvh32JCCfrX8cLZJ-Nt7xnJFQM8KnB2YTa0w'
}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text,"is deactivated for ", Cl)





Deactivate = ["5f5f7f02d529db4721a05dc9",
"5f5f7f02d529db4721a05dbc",
"5f5f7f0234b8aa5e5f7f1542",
"5f5f7f01d529db4721a05daf",
"5f5f7f01d529db4721a05da7",
"5f5f7f0134b8aa5e5f7f1537",
"5f5f7f0134b8aa5e5f7f152b",
"5f5f7f0034b8aa5e5f7f150a",
"5f5f7eff34b8aa5e5f7f14f7",
"5f5f7eff34b8aa5e5f7f14f0",
"5f4f52ceb86920ed9b7c465a",
"5f4d1c2347277ebd982550e1",
"5f4d1c2318f853cb77218187",
"5f4d1c2247277ebd982550ce",
"5f4d1c2218f853cb7721817a",
"5f4d1c2147277ebd982550ca",
"5f4d1c2147277ebd982550bf",
"5f4d1c2118f853cb7721816f",
"5f4d1c2118f853cb7721816b",
"5f4d1c2118f853cb77218167",
"5f4d1c2047277ebd982550bb",
"5f4d1c2047277ebd982550b7",
"5f4d1c2047277ebd982550b3",
"5f4d1c2018f853cb77218162",
"5f4d1c2018f853cb7721815b",
"5f4d1c1f18f853cb7721814b",
"5f4d1c1f18f853cb77218146",
"5f3a31895bdd8b1c59174dd1",
"5f3a3188fe898929a412a436",
"5f3a3188fe898929a412a42d",
"5f3a31885bdd8b1c59174dc0",
"5f382974fe898929a4f6bb7e",
"5f382974fe898929a4f6bb7a",
"5f382974fe898929a4f6bb75",
"5f382973fe898929a4f6bb71",
"5f382973fe898929a4f6bb6a",
"5f382973fe898929a4f6bb64",
"5f382973fe898929a4f6bb5e",
"5f3829735bdd8b1c59fb4d82",
"5f3829735bdd8b1c59fb4d7e",
"5f382972fe898929a4f6bb5a",
"5f382972fe898929a4f6bb56",
"5f382972fe898929a4f6bb51",
"5f382972fe898929a4f6bb46",
"5f3829715bdd8b1c59fb4d60",
"5f3829715bdd8b1c59fb4d5a",
"5f3829715bdd8b1c59fb4d56",
"5f22ab70d876b4b3247bf1c6",
"5f229fc94e7b2db33f9257a6",
"5f229fc94e7b2db33f9257a5",
"5f229fc94e7b2db33f9257a4",
"5f229fc94e7b2db33f9257a2",
"5f229fc94e7b2db33f9257a1",
"5f229fc94e7b2db33f9257a0",
"5f229fc94e7b2db33f92579f",
"5f229fc94e7b2db33f92579e",
"5f229fc94e7b2db33f92579d",
"5f229fc94e7b2db33f92579c",
"5f0f059b25a6f50e23500a94",
"5f0f059b25a6f50e23500a93",
"5f0f059b25a6f50e23500a92",
"5f0f059b25a6f50e23500a91",
"5f0f059b25a6f50e23500a90",
"5f0f059b25a6f50e23500a8b",
"5f0f059b25a6f50e23500a8a",
"5f0f059b25a6f50e23500a89",
"5f0f059b25a6f50e23500a88",
"5f0f059025a6f50e23500a56",
"5f0f059025a6f50e23500a53",
"5f0439b83bda34ca30cdb115",
"5f04398a3bda34ca30cdb0dd",
"5eff08467cf8fbaf56afeb0c",
"5eff08467cf8fbaf56afeb09",
"5eff08467cf8fbaf56afeb08",
"5eff08467cf8fbaf56afeb07",
"5eff08467cf8fbaf56afeb06",
"5eff08467cf8fbaf56afeb05",
"5eff08467cf8fbaf56afeb04",
"5eff08467cf8fbaf56afeb02",
"5eff08467cf8fbaf56afeb01",
"5eff08467cf8fbaf56afeb00",
"5eff08467cf8fbaf56afeaff",
"5eff08467cf8fbaf56afeafe",
"5ef5c061322c7b000134be67",
"5eedd82a66300f0001b3114b",
"5eedd82a66300f0001b3114a",
"5eedd82a66300f0001b31149",
"5eedd82a66300f0001b31148",
"5eedd82a66300f0001b31147",
"5eedd82a66300f0001b31146",
"5eedd82a66300f0001b31144",
"5eedd81666300f0001b31124",
"5eedd81666300f0001b31123",
"5eedd81666300f0001b31122",
"5eedd81666300f0001b31121",
"5eedd81666300f0001b31120",
"5eedd81666300f0001b3111f",
"5eedd81666300f0001b3111e",
"5eedd81666300f0001b3111d",
"5eedd81666300f0001b3111c",
"5ee1bd5ce4391a000100de0b",
"5ee1bd1d4cd837000157cd1c",
"5edf982b7de8d900015924b4",
"5ed7ef404ff28f00011d438e",
"5ed7ef404ff28f00011d438d",
"5ed7e3f3494c1b00018b4e41",
"5ed7e3f3494c1b00018b4e40",
"5ed7e3f3494c1b00018b4e3e",
"5ed7e3f3494c1b00018b4e38",
"5ed7e3f3494c1b00018b4e36",
"5ed7e3f3494c1b00018b4e34",
"5ed7e3f3494c1b00018b4e32",
"5ed7e3f3494c1b00018b4e31",
"5ed7e3f3494c1b00018b4e30",
"5ed7e3f3494c1b00018b4e2f",
"5ed7e3f3494c1b00018b4e2e",
"5ed7e3f3494c1b00018b4e2d",
"5ed7e3f3494c1b00018b4e2c",
"5ed7e3f3494c1b00018b4e2b",
"5ed7e3f3494c1b00018b4e2a",
"5ed7e3f3494c1b00018b4e29",
"5ed7e3f3494c1b00018b4e28",
"5ed7e3f3494c1b00018b4e27",
"5ed7e3f3494c1b00018b4e26",
"5ed7e3f3494c1b00018b4e25",
"5ed7e3f3494c1b00018b4e24",
"5dd29fd93081130001847266",
"5d94780e6feb730001aca03a",
"5d7653e5c7eee200014fd8f8",
"5d7653e5c7eee200014fd8bf",
"5d7653e5c7eee200014fd8a0",
"5d68f757fbdf5900019874c3",]


loc = pcli.channelLinks.list_all(q={
    "_id" : {"$in" : Deactivate}
})



for i in loc:
    UUID = i.channelSettings.storeId
    location = i.location
    location_name = pcli.locations.get(location)
    print(i._id ,"they have UUID:", UUID ,location_name.name)