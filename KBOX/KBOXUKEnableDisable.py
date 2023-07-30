import requests

account = "6335c4b0aa8c958f74195c4a"
query = pcli.channelLinks.list_all(q={"account" : account , "channel" : 7})
for links in query:
    id = links._id
    activateUrl = f"https://api.deliverect.com/v2/channelLinks/{id}/activate"
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjkyNDQyOTIsImV4cCI6MTY2OTMzMDY5MiwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.ArEohDbRq4EKSV2Y1YBjiQvBXbahC3rBYF8zvXxtgNV7Ib4Bht5R40Y20mFVyvGtIjg0ISiuFs_LmeckDt8VNBy8v5dHP4ymrJHQUSel0Rz9ih9RHkY5oBRr5v-gnopjKEYAGBEQzD4ijMqSAd6EuL69VQsAF0jbxUttdoJnWsanswqKFgLPOuitIL0xVIOcpP6a1Fzu15qqsH2nsDaes0qb2nIWeYWPsftB-vSJ-NvPLXg4TR-lc2hUn5TohQmrQ1e4_ryHGU6vz9c23rTdTUlP2YNUAbFkbrQ3P5gKuvZo9GOOdKLrEVQelmM6txG6f_ju1QM5Zx4exmowGnE8ZA'
        }
    payload={}
    disableUrl = f"https://api.deliverect.com/disableChannelLink/{id}"
    #disable
    response = requests.request("POST", disableUrl, headers=headers, data=payload)
    print("Disabled: ",response.text)
    activeresponse = requests.request("POST", activateUrl, headers=headers, data=payload)
    print("activated: ", activeresponse.text )





uberquery = pcli.channelLinks.list_all(q={"account" : account, "channel": 7 , "channelSettings.storeId" : {"$exists" : True} , "APIKey" : ""})
for i in uberquery:
    print(i.name ,i._id)


uber = ["06cbe5db-05c0-4065-ab08-61b6375d4ebc",
"09a56215-e4fa-44cc-b770-c983267aa68f",
"0c599b4c-c519-44ef-95ac-1a8ab6efc29e",
"0e692004-ae8c-53a6-938e-d67e34aacd9b",
"1015378f-ffe2-466d-8315-42a79b08a05d",
"139b879a-9f71-51d1-b743-dd8acaa10b9e",
"14654b6e-cec2-45ea-b168-485ad833fe39",
"1c33a7e0-8107-4b6d-9f0b-53ef0dc94fa1",
"21729cc3-dd2d-4136-9fba-f0fa288b9b3a",
"2be551b2-e62a-4819-bdcf-9dd0c389ba75",
"39e038c2-78b8-42df-a58e-6eec30e981ef",
"3c2fb471-065d-41bb-ac80-b7562c1741e2",
"3d75609b-a2aa-5322-a52d-da6a64d88286",
"3e6e5078-6bfe-45bc-82cc-c16216e3da87",
"3fcd9fba-4685-4df3-9211-3da98d304d37",
"403fb36b-6f96-4fbc-a1e2-2c03c1847d49",
"40607f31-1716-486a-a170-5daaf09772dc",
"424ba8a3-ef16-58ff-9165-ba2a2061100c",
"458bcca1-3952-559d-9164-537ed7f1e0ed",
"4826c105-c1eb-41d0-8885-10ecff0ad711",
"4e6e2c85-0b58-4867-8a73-dcee315b81e1",
"5116da02-782c-5fae-96fd-11f5f300b66f",
"513dffb8-88d4-4297-b947-a07682c3643d",
"577b158d-f99e-42ab-bae5-2e9a05fce18e",
"5848c442-bd3d-4853-aa9e-e0fb9f4ab450",
"5f5eb3a5-0152-42b8-ab08-f05c45ae65a5",
"5f75f517-1b3d-586d-b1ea-4799cc291d5d",
"600854b8-77bf-5e1c-9f4b-137110a22ffb",
"61516cce-5d32-486d-9a94-d0a634f1dba1",
"648a5117-623f-5901-bbcf-2c85ed9ecc7e",
"66f0ac8a-62ef-49a7-af21-24958da37577",
"695443af-f819-4893-bb55-cd33be33fbb8",
"7012fc76-d243-5a18-81e8-9982a8913a2f",
"713f29b1-0bc3-5056-89c5-5ffbe6a318d3",
"7682fc6c-935c-4a5c-9099-733422585330",
"76a74611-79f0-5764-8e40-b435032c8885",
"77ae833b-dfbd-56eb-bd41-c530845d04ec",
"7c7aedbe-d521-4346-8038-9b8b3affae76",
"7ccc616b-59f1-4941-8507-c0d9c4bdfc5d",
"7e0c0ce3-adb6-5c3c-9c2c-e4ceb268a049",
"83fdea81-632a-4b9e-a097-f5ff80a24362",
"8db5c8b6-76af-4a07-9fc3-1ade274af763",
"90f56833-6b1a-4d4e-8e0e-60ca0f5b2382",
"93be7f9b-1e2e-47ef-bed1-f5e975478c3f",
"94a60d4a-9740-4c4c-a51c-f1f56d5626fe",
"990933be-bd58-46f3-8fb5-0c547fba3db5",
"9a1c0477-c9e7-51ea-bee6-f4dc6e61074f",
"9bb28f0e-2572-4d39-a089-021539607e38",
"a78f29bd-1245-49bc-a981-06ca14c181c7",
"a83d1099-1ff5-4cf5-ac9f-16edea27ecce",
"a87ef947-d173-4fed-a8e0-54c06c8b002c",
"a8f3b5fb-bf66-5c48-931a-451fe2ed21d9",
"ac6f7b91-11fe-5e13-a4e0-6d41d4adee93",
"ac87fb7b-2ead-45e9-872c-0d56ba63992d",
"af237dac-7465-4f50-b11e-3981cf456201",
"b18eb284-1475-5a3b-a552-7f0879c6cd10",
"b498e7a3-7607-5eef-9b83-a74686b34744",
"b4e55f79-3051-4e75-a569-7f310179ebbf",
"b7423b24-eab3-4acd-80d2-6ce664b85efb",
"b9e17a22-5836-4acd-a47f-001c5fe27477",
"c4b6bd23-c66f-44c6-a941-9e380e4d34a8",
"c5726ceb-731c-4a97-ac86-74e2314f0c1b",
"c58e6873-89da-5c68-81fe-6717d54130ac",
"c5d99b35-4c2a-4224-b9fe-78e8902fdfe3",
"c91e69dc-fd9b-59b7-b53c-7973f37c4bfe",
"c94b750a-21ba-4a9d-b8b0-9ff60e8777ba",
"cc91d698-6e6a-4bad-9187-c312d6d7f7ca",
"d2c20205-9448-5859-8599-774ef51fbf8c",
"d8e4d98e-3a4c-5144-9984-8936d9b79180",
"da383691-84f6-5ab2-bf64-85d2d933744a",
"dadac5f8-3ef8-521f-93a4-257a676c962b",
"dc556698-dd98-4b6c-bc1f-2d600f349d43",
"ea58915e-9a3e-4972-8a62-e01da982285a",
"eb140052-31b2-4b90-a95b-76f8c3d217ca",
"fb3f7654-c239-5b10-a97f-dc9d65376b76",]

for u in uber:
    uberquery = pcli.channelLinks.list_all(q={"channel": 7 , "channelSettings.storeId" : u })
    if len(uberquery) > 1:
        for cl in uberquery:
            print(f"UUID: {u} exists on 2 channelLinks.")
            print(f"exists in Account: {cl.account} in ChannelLink: {cl._id} ")
            print("----------------------------------------------------------------------")




for u in uber:
    uberquery = pcli.channelLinks.list_all(q={"channel": 7 , "channelSettings.storeId" : u })
    if len(uberquery) > 1:
        for cl in uberquery:
            if cl.account != "6335c4b0aa8c958f74195c4a":
                pcli.channelLinks.update(cl,{
                    "channelSettings.storeId" : "",
                    "APIKey": ""
                })