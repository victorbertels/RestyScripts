import requests
import json
posSystem = [
"-2",
"0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"10",
"12",
"13",
"14",
"15",
"16",
"17",
"18",
"19",
"20",
"21",
"22",
"23",
"25",
"27",
"28",
"29",
"30",
"31",
"32",
"33",
"34",
"35",
"37",
"38",
"39",
"40",
"41",
"42",
"44",
"45",
"46",
"47",
"48",
"49",
"50",
"51",
"52",
"53",
"54",
"55",
"57",
"58",
"9999",
"10000",
"10001",
"10003",
"10005",
"10006",
"10007",
"10008",
"10010",
"10011",
"10012",
"10013",
"10015",
"10016",
"10017",
"10018",
"10019",
"10020",
"10022",
"10023",
"10024",
"10025",
"10026",
"10028",
"10029",
"10031",
"10032",
"10033",
"10034",
"10035",
"10036",
"10037",
"10038",
"10039",
"10041",
"10042",
"10043",
"10045",
"10046",
"10049",
"10050",
"10051",
"10053",
"10054",
"10055",
"10056",
"10057",
"10058",
"10059",
"10060",
"10061",
"10062",
"10063",
"10064",
"10065",
"10066",
"10067",
"10068",
"10069",
"10070",
"10072",
"10073",
"10074",
"10075",
"10076",
"10077",
"10078",
"10079",
"10080",
"10081",
"10082",
"10083",
"10084",
"10085",
"10086",
"10087",
"10089",
"10091",
"10092",
"10093",
"10094",
"10095",
"10096",
"10097",
"10098",
"10099",
"10101",
"10103",
"10104",
"10105",
"10106",
"10107",
"10110",
"10111",
"10112",
"10114",
"10115",
"10117",
"10118",
"10120",
"10121",
"10122",
"10125",
"10126",
"10127",
"10129",
"10131",
"10132",
"10135",
"10138",
"10139",
"10140",
"10141",
"10142",
"10144",
"10146",
"10148",
"10164",
"10165",
"10166",
"10167",
"10168",
"10169",
"10174",
"10176",
"10177",
"10180",
"10182",
"10183",
"10185",
"10188",
"20000",
]
location_list = [

]
settings = []

#locationId = input("Whats the location ID: ")
for system in posSystem: 
    print(system)
    url = "https://api.deliverect.com//locations?where={\"posSystemId\" : f'{system}' }"
    print(url)
    payload = ""
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjI1MzgxNDEsImV4cCI6MTY2MjYyNDU0MSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.NJSwR66OJS7MeiD8t485Cr4vOTLReDBGWgbKpFWcuOoCTTbP1_PmnclF1gaNZNn9whT_9CIZrFhRjtdkYbzrGF7lH6OI4JrvxNmywA6mlJQSgZ_erQJ4M1jBSIcpRi_VKjKqpBfthP3xDIAJtFV6Zd6A70uz6ftm6EuOu7sCp5VN4xq7q_lk9XRcZJ9wWsG3yFXj6l_WV3D3lyfu_ArRMhjTudR0QaptVjV3NMPcurx3ddMCf3Xhpx4xmqNBvQRl4XzQwPyMd0aHPcik1cO_0e5XoppHAZjfHxMSsvBw3zS8VbP4EWXN5oxhV_1sN5NXa9JcPJ3eC_jyoFJ7hBxo4w'
    }
    locresponse = requests.request("GET", url, headers=headers, data=payload)
    print(locresponse.text)
    jsonresponse = locresponse.json()





for loc in location_list:
    url = f"https://api.deliverect.com//posSettings?location={loc}&loadOptions=False"

    payload = ""
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUWkVNakV5TVVZeVJqazJPRGs1TkRjMVF6QXpNMFE1UTBFek1UazNPRFZGTkVJeFF6YzFRZyJ9.eyJpc3MiOiJodHRwczovL2RlbGl2ZXJlY3QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzI5OTY3MjkyNTM2NDEwNjY0IiwiYXVkIjpbImh0dHBzOi8vYXBpLmRlbGl2ZXJlY3QuY29tIiwiaHR0cHM6Ly9kZWxpdmVyZWN0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2NjI1MzgxNDEsImV4cCI6MTY2MjYyNDU0MSwiYXpwIjoiZ214blpIVFV2R1RPOTdTZ0ttclJFN09iX2NCcmNhaTQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.NJSwR66OJS7MeiD8t485Cr4vOTLReDBGWgbKpFWcuOoCTTbP1_PmnclF1gaNZNn9whT_9CIZrFhRjtdkYbzrGF7lH6OI4JrvxNmywA6mlJQSgZ_erQJ4M1jBSIcpRi_VKjKqpBfthP3xDIAJtFV6Zd6A70uz6ftm6EuOu7sCp5VN4xq7q_lk9XRcZJ9wWsG3yFXj6l_WV3D3lyfu_ArRMhjTudR0QaptVjV3NMPcurx3ddMCf3Xhpx4xmqNBvQRl4XzQwPyMd0aHPcik1cO_0e5XoppHAZjfHxMSsvBw3zS8VbP4EWXN5oxhV_1sN5NXa9JcPJ3eC_jyoFJ7hBxo4w'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonresponse = response.json()


    f = open(f'newsettings.json' , "w+")
    for i in jsonresponse:
        try:

            settings.append({"ID" : i["id"],"name" : i["name"] , "info" : i["info"]})

        except:
            settings.append({"ID" : i["id"],"name" : i["name"] , "info" : "no info "})
    print(settings)
    f.write(str(settings))
    f.close()



query = pcli.accounts.list_all(q={"accountType"  :3})
posSystems = []
f = open("posSystems.txt" , "w+")
for i in query:
    posSystems.append(i.posSystem)


f.write(str(posSystems))



# f.write(str(settings))
# f.close()
# print(settings)


# try:
#     print(f'{person} is {ages[person]} years old.')
# except KeyError:
#     print(f"{person}'s age is unknown.")


# # def search(name, jsonresponse):
# #     return [element for element in jsonresponse if element['name'] == name]
# # json = dict(response.json())
# # print(json.id)
# # print(json)
# # settings.update({"ID" : json.id})
# # settings.update({"name" : json.name})
# # settings.update({"info" : json.info})

# # print(settings)

# # print(response.text)
