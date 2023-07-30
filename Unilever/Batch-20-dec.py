import requests

uuids = ["b4b7c208-8191-542f-a699-525a977cb6d5",
"d37609d7-0aee-55e7-9c47-30adde116dd2",
"61dc40d4-b777-5aa1-aa05-5a0e48338b1d",
"d64cdd51-3082-51a7-80bd-759a8633307c",
"11189161-b4ad-5c94-b093-4907e4037c94",
"70094726-3b10-51e3-989b-f4f405a8df81",
"55ce8a85-366a-5438-b735-c775cc0d3f94",
"74c75535-0d5d-5fd4-a232-258aca592ba2",
"100d6fdc-f317-5cab-9251-dbb054e249ce",
"d550d81a-b340-5b6e-9144-0d90622af90f",
"562d0652-30ee-5208-8701-933927d7ddac",
"8ebe8ca8-f3a2-57f8-b309-2ca56333eae6",
"75c286d1-676c-5554-9e30-0e21299575cb",
"8b384eb7-383b-509c-afe2-4323812bb7d2",
"0a0cf984-cc2f-5fe8-9adf-f0202205c6c1",
"f6ceb774-af0c-5971-a263-d6e8f563c4f4",
"b4b7c208-8191-542f-a699-525a977cb6d5",
"d37609d7-0aee-55e7-9c47-30adde116dd2",
"93d8905e-96f8-55c4-a9ca-9fdc7e885ee9",
"1446c0f9-f12e-5baf-9ac5-f8f7d111ebbc",
"5eb0c314-4c07-5d0f-9d76-3691bea5d8ad",
"2dfc2245-e8c3-5da8-ab4d-5fceb6de29eb",
"4c2309ae-f56d-57cd-b4e4-489b28dd63e3",
"74e53241-71db-55d8-8f2e-db33dbe1f56f",
"6ef0fe0f-62ba-5c70-9711-6728fe874bfb",
"70003001-8fb7-5666-bb97-87b68635f63f",
"cf143a54-1727-5a9f-9cc8-a3cfc52adaf1",
"f6cb8e0e-b9d9-56d3-a867-58d863988b47",
"b8b7a97a-d41e-5f21-a730-503450265566",
"b55a777e-e34a-5171-852b-e71e25d4e3a2",
"b4cdfebc-ebf6-51e7-b38e-a4f77173ebce",
"16387733-b7f7-597e-85ee-ca1f1efb6bf9",
"a6b9f2f7-e956-5a77-81c7-5130577f286d",
"5f11eb8f-2e0d-535b-89e5-a85f5bbcce95",
"d77cf8ec-f0a7-517e-b8f1-d2643bd350b4",
"78b0c009-6819-5c9d-abdd-e6c63a3048e2",
"30c34978-3ae5-5810-b732-a3e679aad0e8",
"696acb2c-3344-5abb-a000-0fd971759de0",
"4afd44d0-fb76-5c21-aed7-ea9fa703b8ed",
"41695d02-72fe-51f4-b6c8-e45de50e1e91",
"35564146-444c-58a9-bdd1-ab00ea241804",
"4e96e756-fe4f-5b27-a8a9-2bdd4c790f24",
"bd7ad3a4-6e5a-5863-84cb-04a88a5cc14f",
"34bfa295-fafe-57f5-93f4-12f3424d0766",
"19025a88-34b5-5526-90dc-1d7f3606fbd4",
"b0df01c7-1a79-5965-ae11-787f2bdd63c6",
"b1deb3a6-5aba-50dc-955d-4da5dd949315",
"51aceb2e-4d07-55a7-a38a-a4129e8bf27c",
"4aa45963-65ff-5476-919d-368118093cc9",
"c9750b59-98a4-58d6-a64a-01d5ac57120d",
"9e00ecee-9833-56dc-8144-e4fd7798cbd9",
"a606f5cf-811e-57ab-8ed1-d22bc711ef7a",
"70546fae-b218-5ca4-88bd-4222d6330a9d",
"e55078d9-74de-5db1-a373-08dbabbdd689",]


query = pcli.channelLinks.list_all(q={"account" : "5d67c3f06f006f00012b83d1" , "APIKey" : {"$in" : uuids} })

for i in query:
    clid = i._id
    locationid = i.location
    apikey = i.APIKey
    url = f"https://api.deliverect.com/v2/channelLinks/{clid}/activate"
    payload={}
    headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmRlbGl2ZXJlY3QuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NzE0MjI0MzksImV4cCI6MTY3MTUwODgzOSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.FgoHel5nyzDV573tL-zkbeyknDd9z-E-5fHaOwh9BLK_hec07oAmaWd7fl6vgGZ6E66Ov4ECDftemH2mE-PoqQoW1NWcsakto7B5u7abkxJnTUPk4xmGpawdaxqvuHBSI3XSyxrwVl8StxbYStOQzhG7ibQUNkQ84-GcIZCC_WcZWEqxb3hMjJSYsBXvSF2bY-FqzM_oUMvlJtGt4fej1Xt5-GNaeiAxqw2xfmhgzkKxMCVvanz0WVA58E79aZQLPHf5ksnccjfNC9dbVLciE4Kf6z_0RTyK5TLnB2ZawLorKjfGPEaUKabpuA26GrOa48BIxlawYUX5gjatFFMiNQ'
}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    print(f"{apikey} - {clid} - {locationid}")






